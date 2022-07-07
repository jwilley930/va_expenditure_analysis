# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project: Examination of Expenditures for Veterans Affairs

### Overview

The U.S. Department of Veterans Affairs is an agency of the federal government that provides vital services to military veterans and their families. The largest of these services is by far providing pensions and disability benefits, along with medical care, to veterans who got sick or injured while serving.  The VA also provides educational and vocational benefits in the form of the GI Bill and career training, along with providing financial services such as home loans and insurance.  It also one of the federal government's largest expenses.  In 2021, VA expenditures totalled about `$`224 Billion, and in 2023 it is budgeted for just over `$`300 Billion, making up about 5% of federal spending.  

### Problem Statement

Analyze VA spending at both the state and county levels to see where resources are being used the most, and analyzing whether the impact of various population, economic, health, or education factors are influencing these expenditures

---

## Table of Contents

|Notebook & Content|Description|
|---|---|
|**README**|Overview, Problem Statement, Datasets, Data Dictionary, Analysis Overview, Conclusions| 
|**Data Gathering**|Data Loading, Cleaning, Merging, and EDA| 
|**Modeling**|Model Building and Testing| 
|**Presentation.pdf**|Presentation of Analysis|
|**Streamlit App**|Modify variables to predict changes in VA expenditures|


### Datasets

* [`county_df.csv`](../data/df18to21H.csv): Cleaned and merged data for county-level spending and demographics
* [`AGG_GDX_FY07-21.xlsx`](../data/census_20.csv): Merged data for state-level VA expenditures years 2007-2021
* [`state_health.csv`](../data/population.csv): Cleaned data for state-level health variables
* [`facilities.csv`](../data/df18to21_cleanedH.csv): List of VA facilities in each state


---

### Data Dictionary

**Cleaned County-Level Demographic and VA Spending Data for 2021**

|Feature|Type|Description|
|---|---|---|
|**county**|object|County| 
|**state**|object|State| 
|**total_exp**|float|Total VA Expenditures in $000s| 
|**medical_care_exp**|float|VA Medical Expenditures in $000s| 
|**edu_training_exp**|float|VA Education and Vocation Training Expenditures in $000s|
|**exp_per_vet**|float|VA Expenditure per Veteran in $000s|
|**county_pop**|float|Population|
|**vet_pop**|float|Veteran Population|
|**med_patients**|float|Unique VA Medical Patients|
|**state_va_fac**|float|Number of VA Facilities in State|
|**hs_grad_pct**|float|Percentage of Population with High School Diploma|
|**clg_grad_pct**|float|Percentage of Population with College Degree|
|**median_income**|float|Median Income in $|
|**poverty_pct**|float|Percentage of Population in Poverty|
|**unemployment_pct**|float|Unemployment Rate|
|**severe_housing_problems_pct**|float|Percentage of Households Living with Severe Housing Problem|
|**smokers_pct**|float|Percentage of Adults Who Smoke| 
|**obesity_pct**|float|Percentage of Adults Considered Obese| 
|**inactive_pct**|float|Percentage of Adults Who Are Not Physically Active| 
|**excess_alcohol_pct**|float|Percentage of Adults Who Report Excessive Alcohol Use| 
|**diabetes_pct**|float|Percentage of Adults with Diabetes|
|**food_insecure_pct**|float|Percentage of Households Without Sufficient Access to Food| 
|**age_under18_pct**|float|Percentage of Population Under 18 Years Old|
|**age_over65_pct**|float|Percentage of Population Over 65 Years Old|
|**rural_pct**|float|Percentage of Population Living in Rural Area|


---

## Data Analysis

Data pertaining to Veterans Affairs was obtained from the VA's open data portal.  County and state information regarding population, health, education, and other variables was obtained from the County Health Rankings and Roadmaps.  The data was cleaned and then merged together in the county_df dataframe.  Regression analyses were performed targetting total expenditures as well as isolated health and education expenditures

---

## Conclusions

For further study, there are many more variables that can be examined, in particular only a small subset health variables were used in the model.  Also, further measures could be taken to control for population differences.

