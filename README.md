# 📊Streamlined Analysis and Management of YouTube Trending Data Using AWS

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![AWS](https://img.shields.io/badge/AWS-Data%20Engineering-orange)

---

## 📌 Overview
This project demonstrates a **cloud-based, scalable ETL pipeline** for ingesting, transforming, storing, and analyzing structured & semi-structured YouTube trending data. It focuses on **automated data workflows**, **efficient data processing**, and **interactive analytics dashboards**.

---

## 🎯Project Goals
1. **Data Ingestion:** Develop a robust mechanism to ingest data from multiple sources.
2. **ETL System:** Transform raw data into a structured format suitable for analysis.
3. **Data Lake:** Create a centralized repository on **Amazon S3** to store data from various sources.
4. **Scalability:** Ensure the system can scale efficiently as data volume increases.
5. **Cloud Integration:** Leverage AWS to handle extensive data processing that exceeds local computing capabilities.
6. **Reporting:** Visualize data via **Amazon QuickSight** dashboards and provide insights into key questions.

---

## 🛠️ AWS Services Used
| Service | Purpose |
|---------|---------|
| **AWS Command Line Interface (CLI)** | Manage AWS services through scripts and terminal commands |
| **Amazon S3** | Object storage service for raw, cleansed, and analytics datasets |
| **AWS Identity And Access Management (IAM)** | Enables Admin to manage and control access to AWS services and resources securely |
| **AWS Glue** | Serverless data integration service for ETL jobs |
| **AWS Lambda** | Computing service that allows to run code without creating or managing servers |
| **AWS Athena** | Interactive SQL queries on S3 data |
| **Amazon QuickSight** | Business intelligence dashboard |
| **AWS CloudWatch** | Monitoring and automation triggers |

---

## 🔄 Project Execution Flow
- **Step 1(Raw JSON to Cleansed Parquet Data Bucket):**
Extract JSON Raw Data: Use AWS CLI to copy Kaggle dataset downloaded on my local machine to AWS S3 bucket -> Cloudwatch Trigger (S3 object event) -> Run Transform Function to convert all JSON files to Parquet Format -> Transform Data And Load it -> Query Using Athena
- **Step 2(Raw CSV to Cleansed Parquet Data Bucket):**
Extract Regionwise CSV Raw Data: Use AWS CLI to copy Kaggle dataset downloaded on my local machine to AWS S3 bucket -> Create ETL(Extract, Transform,Load) job using AWS Glue Studio Script Editor -> Run PySpark code written for ETL job -> Transform Data from CSV to Parquet format And Load it -> Query Using Athena
- **Step 3(Analytics/Reporting Bucket):**
Create ETL(Extract, Transform,Load) job using AWS Glue Studio Visual ETL tool that joins two table-1(cleansed JSON to parquet file) and table-2(cleansed CSV to parquet file)  -> Load the resultant joined table in S3 bucket -> Query Using Athena
- **Step 4(Quicksight Analysis):**
Validate and establish Quicksight and Athena Connections -> Import Final Analystics Dataset from Athena to Quicksight -> Generate Dashboards to answer Business questions for better insights.

---

## 🏗 Architecture Diagram
![Architecture Diagram](https://github.com/panditpooja/youtube-data-etl-and-analysis-aws-project/blob/dev/architecture.JPG)

---

## Install Packages
```
import awswrangler
import pandas
import os
import boto3
```

---

## 🏆Achievements
- Transformed Youtube data into actionable insights using Python, deployed it on AWS Cloud.
- Streamlined Data Processing by 31.6% with Automated Data Ingestion from source to analytics-ready format using AWS CLI, CloudWatch, Lambda, S3, and Athena to create an efficient ETL pipeline, enhancing scalability and efficiency.
- Created insightful dashboards with Amazon QuickSight, facilitating trend analysis and improving decision-making, resulting in faster insights.

---

## 📊 Dataset
[Kaggle - YouTube Trending Data](https://www.kaggle.com/datasets/datasnaek/youtube-new)  
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

---

## ✍️ Author

**Pooja Pandit**  
Master’s Student in Information Science (Machine Learning)  
The University of Arizona  

[![GitHub](https://img.shields.io/badge/GitHub-panditpooja-black?logo=github)](https://github.com/panditpooja)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-pooja--pandit-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pooja-pandit-177978135/)  
