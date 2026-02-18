import dlt

@dlt.table
def transformed():
  return spark.range(100)