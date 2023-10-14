# Databricks notebook source
dbutils.fs.ls("/mnt/dados/inbound")

# COMMAND ----------

path = "/mnt/dados/inbound/dados_brutos_imoveis.json"
dados_df = spark.read.json(path)

# COMMAND ----------

display(dados_df)

# COMMAND ----------

dados_df = dados_df.drop("imagens", "usuario")
display(dados_df)

# COMMAND ----------

# MAGIC %md
# MAGIC #criando coluna de identificação

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

dados_df = dados_df.withColumn("id", col("anuncio.id"))
display(dados_df)

# COMMAND ----------

dados_df.write.format("delta").mode('Overwrite').save("/mnt/dados/bronze/dataset_imoveis")

# COMMAND ----------


