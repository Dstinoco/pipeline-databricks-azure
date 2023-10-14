# Databricks notebook source
df = spark.read.format("delta").load("/mnt/dados/bronze/dataset_imoveis")
display(df)

# COMMAND ----------

display(df.select('anuncio.*', 'anuncio.endereco.*'))

# COMMAND ----------

dados_df = df.select('anuncio.*', 'anuncio.endereco.*')

# COMMAND ----------

dados_df = dados_df.drop("caracteristicas", "endereco")
display(dados_df)

# COMMAND ----------

dados_df.write.format("delta").mode("overwrite").save("/mnt/dados/silver/dataset_imoveis")

# COMMAND ----------


