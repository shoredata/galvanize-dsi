# Real Estate Case Study

## Introduction

This case study is an opportunity to apply skills that you have learned this week.

### Learning Objectives

 1. Write Python code to read and write CSV data files using file handles and the `csv` module.

 2. Implement the first three steps of the [Cross-Industry Standard Process for Data Mining](https://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining) (CRISP-DM) on a large, real-world, data set.

### CRISP-DM

There are six steps in CRISP-DM. Today, we'll focus on the first three:

#### CRISP-DM Step 1: Business/Problem Understanding

Define the business/problem objectives that motivate the project.

Key Questions:

* What is the problem or research question that we want to address?
* What does success look like?

#### CRISP-DM Step 2: Data Understanding

Identify data sources that may be available to answer the business question.

Key Questions:

* What data sources are available to answer the question?
* What is the size of the data?
    * Is it small enough to fit on one computer?
    * Can it be loaded into memory?
* What are the general domain concepts covered by the data source?
    * Can the domain concepts be meaningfully broken down into sub-concepts?
    * Are all these domain concepts meaningful to the problem being solved?
    * Are there any important domain concepts missing from the data at hand?
* How were the data generated?
* Are there data quality issues that need to be addressed?

#### CRISP-DM Step 3: Data Preparation

Implement an automated and repeatable process to prepare raw data for analysis.

Key Questions:

* What final data format would be most useful for modeling or analysis?
* Would an unfamiliar third party be able to use my code and documentation to repeat my data preparation process?

Think of your data preparation process as a *pipeline* that receives raw data and outputs transformed data. **Never make changes to the original data set**.


## Part 1: Business Understanding

You are a real estate investor interested in entering the Seattle housing market. You want to use publicly available data to develop a better understanding of Seattle real estate trends.

### Step 1.1: Identify Questions

?

### Step 1.2: What does success look like?

?

## Part 2: Data Understanding

You know that a great deal of real estate data is maintained by county tax assessment departments.

### Step 2.1: Download Data

Visit the [Assessments Data Download](http://info.kingcounty.gov/assessor/DataDownload/default.aspx) site and download data files that may be relevant to your analysis. These files may be of interest.

* Real Property Sales
* Real Property Appraisal History
* Parcel
* Commercial Building
* Residential Building
* Vacant Lot
* Real Property Account

Each file is accompanied by a metadata document. Download the metadata files as well.

* What is the unique ID number that identifies each parcel of land?
* What file(s) contain street addresses?
* What are the different ways that you can assign a value to a property using this data?
* Map out any other domain concepts covered by this data that may be important to you as a real estate investor.

### Step 2.2: Organize files

 * Move these files from your Downloads directory to the `data` directory in your case study repo.
 * Unzip each of the compressed data files. (Use the `unzip` command.)
 * Add each file to your `.gitignore` file to ensure that you won't accidentally commit them to your `git` history. (Files over 100 megabytes are too large to track with Git.)

## Part 3: Data Preparation

Build a pipeline that uses the data files that you've downloaded to create useful summary data that answers the questions identified in Part 1.
