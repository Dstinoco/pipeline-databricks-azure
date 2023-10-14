# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "52d31c53-8dd4-4a41-9bc5-5cdc09406c8f",
          "fs.azure.account.oauth2.client.secret": "v7m8Q~8e3bhA.B0xNOCtME2s7TTaME63SoTbEauO",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/74f87453-2afd-4f90-8613-6cb4fbeafd47/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://imoveis@datalakecurso6998.dfs.core.windows.net/",
  mount_point = "/mnt/dados",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mkdirs('/mnt/dados')

# COMMAND ----------

display(dbutils.fs.ls('/mnt/dados'))

# COMMAND ----------


