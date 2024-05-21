# Personal Project: Streamlined Analysis and Management of YouTube Trending Data Using AWS

## Overview
This project aims to securely manage, streamline, and analyze structured and semi-structured YouTube video data, focusing on video categories and trending metrics.

## Project Goals
1. **Data Ingestion:** Develop a robust mechanism to ingest data from multiple sources.
2. **ETL System:** Transform raw data into a structured format suitable for analysis.
3. **Data Lake:** Create a centralized repository to store data from various sources.
4. **Scalability:** Ensure the system can scale efficiently as data volume increases.
5. **Cloud Integration:** Leverage AWS to handle extensive data processing that exceeds local computing capabilities.
6. **Reporting:** Develop a dashboard to visualize data and provide insights into key questions.

## Services Utilized
1. **AWS CLI:** Command Line Interface for managing AWS services through scripts and terminal commands.
2. **Amazon S3:** Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
3. **AWS IAM:** AWS IAM is an dentity and access management which enables us to manage and control access to AWS services and resources securely.
4. **QuickSight:** Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
5. **AWS Glue:** A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
6. **AWS Lambda:** Lambda is a computing service that allows programmers to run code without creating or managing servers.
7. **AWS Athena:** Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

## Project Execution Flow
- **Step 1(Raw Data Bucket):**
Extract JSON Raw Data: Use AWS CLI to copy Kaggle dataset downloaded on my local machine to AWS S3 bucket -> Cloudwatch Trigger (S3 object event) -> Run Transform Function to convert all JSON files to Parquet Format -> Transform Data And Load it -> Query Using Athena
- **Step 2(Cleansed Data Bucket):**
Extract Regionwise CSV Raw Data: Use AWS CLI to copy Kaggle dataset downloaded on my local machine to AWS S3 bucket -> Create ETL(Extract, Transform,Load) job using AWS Glue Studio Script Editor -> Run PySpark code written for ETL job -> Transform Data from CSV to Parquet format And Load it -> Query Using Athena
- **Step 3(Analytics/Reporting Bucket):**
Create ETL(Extract, Transform,Load) job using AWS Glue Studio Visual ETL tool that joins two table-1(cleansed JSON to parquet file) and table-2(cleansed CSV to parquet file)  -> Load the resultant joined table in S3 bucket -> Query Using Athena
- **Step 4(Quicksight Analysis):**
Validate and establish Quicksight and Athena Connections -> Import Final Analystics Dataset from Athena to Quicksight -> Generate Dashboards to answer Business questions for better insights.

## Architecture Diagram
![Architecture Diagram](https://github.com/panditpooja/youtube-data-etl-and-analysis-aws-project/blob/dev/architecture.jpeg)

## Install Packages
```
import awswrangler
import pandas
import os
import boto3
```

## Achievements
- Transformed Youtube data into actionable insights using Python, deployed it on AWS Cloud.
- Streamlined Data Processing by 31.6% with Automated Data Ingestion from source to analytics-ready format using AWS CLI, CloudWatch, Lambda, S3, and Athena to create an efficient ETL pipeline, enhancing scalability and efficiency.
- Created insightful dashboards with Amazon QuickSight, facilitating trend analysis and improving decision-making, resulting in faster insights.

## Dataset Used
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.
[Kaggle Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)

