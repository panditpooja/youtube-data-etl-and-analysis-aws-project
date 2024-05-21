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
1. **Amazon S3:** Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. **AWS IAM:** AWS IAM is an dentity and access management which enables us to manage and control access to AWS services and resources securely.
3. **QuickSight:** Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. **AWS Glue:** A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. **AWS Lambda:** Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. **AWS Athena:** Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

## Dataset Used
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.
[Kaggle Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## Architecture Diagram
![Architecture Diagram](need to upload)



