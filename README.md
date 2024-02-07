# 02-Workflow Orchestration

In this module, I have learned about orchestration and Mage. 
Mage is a wonderful framework and organize. I am able to understand more detail about data engineer. 

What I have learned so far. 

1. How to get/download data from web source.
   In this part, I realized that I need to download dataset only for quarter 3, 2020 and the dataset are splitted by month.
   What I have done was I looped by month in URL. After that, I performed data concatenation.

   For data transformation, I already have experiences and I do not encounter any problems, for now.

3. How to export data to Postgres
   This is new to me. My previous skillset was only to save data into Excel. 


4. How to load data into a data lake (GCS )using an API (Mage)
   This is my most favorite part. Previously, we learned how to create a bucket in GCS with Terraform without load real data but this module helps me to get a better understanding of data lake.
   I have also learned how to save the data by partition in parquet format.

5. How to export data from GCS to BigQuery
   What I have learned are how to load all parquet data from partition folder in GCS (data lake) then export data to BigQuery (data warehouse).
