# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS jj_hc_adb_ws.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS jj_hc_adb_ws.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# %sql
# truncate table  tt_hc_adb_ws.audit.load_logs 

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs

# COMMAND ----------

# MAGIC %sql
# MAGIC select coalesce(cast(max(loaddate) as date),'1900-01-01') as last_fetched_date from audit.load_logs where data_source='' and tablename=''
