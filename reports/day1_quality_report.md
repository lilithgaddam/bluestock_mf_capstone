# Day 1 Data Quality Summary

## Overview

The objective of Day 1 was to establish the project environment, ingest the provided mutual fund datasets, and perform initial validation checks to ensure data readiness for further analysis.

## Dataset Ingestion

Successfully loaded all 10 mutual fund datasets into the project using the Pandas library. The datasets were stored in the raw data layer and verified for successful ingestion.

## Data Validation Activities

The following validation checks were performed on each dataset:

* Examined dataset dimensions using the `shape` attribute.
* Reviewed column data types using `dtypes`.
* Inspected sample records using `head()`.
* Confirmed successful loading of all CSV files.
* Identified dataset structure and key business attributes.

## Fund Master Analysis

Explored the fund master dataset to understand the available scheme metadata, including:

* AMFI Scheme Codes
* Fund Houses
* Fund Categories
* Sub-Categories
* Risk Categories
* Benchmark Information

This analysis provided a foundational understanding of the mutual fund universe available within the project.

## AMFI Code Validation

Performed validation between `fund_master.csv` and `nav_history.csv` to ensure consistency of AMFI scheme codes.

**Result:** Missing Codes = 0

All AMFI codes available in the fund master dataset were successfully found within the NAV history dataset, indicating strong referential consistency between the two data sources.

## Live NAV Data Integration

Integrated the mfapi.in API and successfully fetched NAV history data for the following mutual fund schemes:

* HDFC Top 100 Direct Growth
* SBI Bluechip Fund
* ICICI Prudential Bluechip Fund
* Nippon India Large Cap Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund

The retrieved data was stored in CSV format within the raw data layer for future processing and analysis.

## Conclusion

Day 1 objectives were successfully completed. The project environment was configured, datasets were ingested and validated, live NAV data was integrated, and AMFI code consistency checks were completed. The data is now prepared for the next phase involving data cleaning, transformation, and database design.
