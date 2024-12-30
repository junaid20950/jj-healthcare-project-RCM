# Databricks notebook source
# MAGIC %sql
# MAGIC select count(*) from silver.claims;.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table jj_hc_adb_ws.silver.claims;
# MAGIC truncate table jj_hc_adb_ws.silver.cptcodes;
# MAGIC truncate table jj_hc_adb_ws.silver.departments;
# MAGIC truncate table jj_hc_adb_ws.silver.encounters;
# MAGIC truncate table jj_hc_adb_ws.silver.icd_codes;
# MAGIC truncate table jj_hc_adb_ws.silver.npi_extract;
# MAGIC truncate table jj_hc_adb_ws.silver.patients;
# MAGIC truncate table jj_hc_adb_ws.silver.providers;
# MAGIC truncate table jj_hc_adb_ws.silver.transactions;
# MAGIC
# MAGIC --Gold
# MAGIC
# MAGIC truncate table jj_hc_adb_ws.gold.dim_cpt_code;
# MAGIC truncate table jj_hc_adb_ws.gold.dim_department;
# MAGIC truncate table jj_hc_adb_ws.gold.dim_icd;
# MAGIC truncate table jj_hc_adb_ws.gold.dim_npi;
# MAGIC truncate table jj_hc_adb_ws.gold.dim_patient;
# MAGIC truncate table jj_hc_adb_ws.gold.dim_provider;
# MAGIC truncate table jj_hc_adb_ws.gold.fact_transactions;
# MAGIC
# MAGIC --audit
# MAGIC truncate table jj_hc_adb_ws.audit.load_logs;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.claims UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.cptcodes UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.departments UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.encounters UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.icd_codes UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.npi_extract UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.patients UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.providers UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.silver.transactions UNION ALL 
# MAGIC
# MAGIC --Gold
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_cpt_code UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_department UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_icd UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_npi UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_patient UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.dim_provider UNION ALL 
# MAGIC select count(*) FROM jj_hc_adb_ws.gold.fact_transactions UNION ALL 
# MAGIC
# MAGIC --audit
# MAGIC select count(*) FROM jj_hc_adb_ws.audit.load_logs;
