import dlt

@dlt.table(
    name=${val}
)
def a():
    return spark.range(10)
