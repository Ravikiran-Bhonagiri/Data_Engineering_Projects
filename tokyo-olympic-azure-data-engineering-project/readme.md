
# Olympic Data Analytics - Azure End-to-End Data Engineering Project

---

## **Project Overview**

This project demonstrates a complete end-to-end data engineering workflow for analyzing Olympic data using Microsoft Azure services. The workflow includes data ingestion, transformation, storage, and analytics. It serves as a practical guide to mastering Azure's cloud-based data engineering tools, including Azure Data Factory, Azure Data Lake Storage, Azure Databricks, and Azure Synapse Analytics.

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Project Workflow](#project-workflow)
3. [Tools and Services Used](#tools-and-services-used)
4. [Setup and Prerequisites](#setup-and-prerequisites)
5. [Step-by-Step Implementation](#step-by-step-implementation)
    - [1. Data Ingestion](#1-data-ingestion)
    - [2. Data Transformation](#2-data-transformation)
    - [3. Data Storage](#3-data-storage)
    - [4. Analytics and Insights](#4-analytics-and-insights)
6. [Key Features](#key-features)
7. [Learning Outcomes](#learning-outcomes)
8. [Next Steps](#next-steps)
9. [Contributors](#contributors)
10. [License](#license)

---

## **Introduction**

The Olympic Data Analytics project is designed to teach cloud-based data engineering workflows. The project involves:
- Extracting Olympic data from an API.
- Transforming and cleaning the data using Apache Spark.
- Storing both raw and processed data in Azure Data Lake Storage.
- Running SQL queries for data analysis using Azure Synapse Analytics.

This project is ideal for beginners and intermediate users who want hands-on experience with Azure's data engineering tools.

---

## **Project Workflow**

The project workflow consists of the following steps:
1. **Data Ingestion**: Extract data from an API and store it in Azure Data Lake (raw data).
2. **Data Transformation**: Use Apache Spark in Azure Databricks to clean and transform the data.
3. **Data Storage**: Save transformed data back into Azure Data Lake (processed data).
4. **Analytics**: Query the transformed data using Azure Synapse Analytics and derive insights.

---

## **Tools and Services Used**

### 1. **Azure Data Factory**
   - Used to create a pipeline for data ingestion from APIs or external sources.
   - Provides an intuitive interface for data extraction and orchestration.

### 2. **Azure Data Lake Storage (Gen2)**
   - Stores raw and processed data in hierarchical structures.

### 3. **Azure Databricks**
   - An Apache Spark-based analytics platform for performing data transformations.

### 4. **Azure Synapse Analytics**
   - Enables running SQL queries and performing analytics on the processed data.

### 5. **GitHub**
   - Source of data files used in the project.

### 6. **Apache Spark**
   - Framework for distributed data processing and transformations.

---

## **Setup and Prerequisites**

### **Prerequisites**
- An active Azure account (Free Trial available with $200 credits).
- Basic understanding of Python, SQL, and Apache Spark.
- Installed Python environment (e.g., Anaconda or standalone Python).

### **Setup**
1. **Azure Account Creation**:
   - Go to [Azure Portal](https://portal.azure.com) and create a free account.
2. **Resource Group**:
   - Create a Resource Group for organizing all Azure services used in this project.
3. **Azure Data Lake and Data Factory**:
   - Set up Azure Data Lake Gen2 and Data Factory for storing and ingesting data.

---

## **Step-by-Step Implementation**

### **1. Data Ingestion**
- Use Azure Data Factory to extract raw data from the provided API or GitHub repository.
- Configure the data pipeline with HTTP source connectors and specify the target as Azure Data Lake.

### **2. Data Transformation**
- Mount Azure Data Lake in Azure Databricks.
- Use Apache Spark to:
  - Perform schema inference.
  - Rename columns and transform data types.
  - Partition the data for better storage and query efficiency.

### **3. Data Storage**
- Store both raw and transformed data in Azure Data Lake Storage.
- Organize data in hierarchical structures for easier navigation.

### **4. Analytics and Insights**
- Load transformed data into Azure Synapse Analytics.
- Perform SQL-based data analysis to derive insights, such as:
  - Average number of entries by gender for each discipline.
  - Total medal counts by country.

---

## **Key Features**

- **Automated Data Pipeline**: Efficiently extract, transform, and load (ETL) data.
- **Distributed Processing**: Utilize Apache Spark for high-performance data transformation.
- **Cloud Storage**: Manage raw and processed data securely in Azure Data Lake.
- **SQL Analytics**: Derive actionable insights using Azure Synapse Analytics.

---

## **Learning Outcomes**

By completing this project, you will learn:
- How to build an end-to-end data engineering pipeline on Azure.
- Practical usage of Apache Spark for data transformation.
- SQL analytics in a cloud environment.
- Best practices for working with Azure's Data Engineering tools.

---

## **Next Steps**

- Explore advanced transformations using Apache Spark.
- Integrate machine learning models for predictive analytics.
- Enhance security and networking configurations on Azure.
- Experiment with real-time analytics using Azure Stream Analytics.

---

## **Contributors**

- **Project Author**: Ravikiran Bhonagiri

---
