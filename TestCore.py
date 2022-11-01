class TestCore:
  def __init__(self, dataframe: DataFrame):
    self.dataframe = dataframe.withColumn('_test_result', F.array().cast(T.ArrayType(T.MapType(T.StringType(), T.StringType()))))
    
  def check(self, test_name, condition, check_type='passive'):
    self.dataframe = self.dataframe.withColumn('_test_result', F.when(~condition, F.concat(F.col('_test_result'), F.array(F.create_map(F.lit(test_name), F.lit("FAILED"))))).otherwise(F.col('_test_result')))
    if check_type == 'critical':
      assert self.dataframe.filter(F.col('_test_result').cast('string').contains(test_name)).count() == 0, f"""Critical data quality failure on unit test: {test_name}, with condition: {condition}"""
    return self
        
  def check_duplicates(self, columns, check_type='passive'):
    w = Window.partitionBy(columns).rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
    return self.check('check_duplicates', (F.count(columns[0]).over(w) == 1), check_type)
  
  def validate(self):
    return [self.dataframe.filter(F.size('_test_result') == 0).drop('_test_result'), self.dataframe.filter(F.size('_test_result') > 0)]
