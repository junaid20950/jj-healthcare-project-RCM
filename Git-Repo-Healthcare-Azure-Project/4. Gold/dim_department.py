# Databricks notebook source
# MAGIC
# MAGIC  %sql
# MAGIC  CREATE TABLE IF NOT EXISTS gold.dim_department
# MAGIC  (
# MAGIC  Dept_Id string,
# MAGIC  SRC_Dept_Id string,
# MAGIC  Name string,
# MAGIC  datasource string
# MAGIC  );
# MAGIC
# MAGIC
# MAGIC  truncate TABLE gold.dim_department;
# MAGIC
# MAGIC  insert into gold.dim_department
# MAGIC  select 
# MAGIC  distinct
# MAGIC  Dept_Id ,
# MAGIC  SRC_Dept_Id ,
# MAGIC  Name ,
# MAGIC  datasource 
# MAGIC   from silver.departments
# MAGIC   where is_quarantined=false;
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC --  select * from gold.dim_department;
# MAGIC
