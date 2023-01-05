# Telco Churn Project


# Project Description

### Telco is a telecommunications company that provides a number of services to include phone and internet. There has been a number of customers who have churned from Telco. In this project, I will delve into the different features of Telco's data and hone in on possible reasons why customers have decided to churn. 


# Business Goals

* Uncover drivers that are causing Telco customers to churn
* Use machine learning algorythms with drivers to hone in on possible reasons for customer churn.
* Develop an understanding of possible reasons customers are churning.

# Initial Thoughts

### My initial hypothesis is that customers with month-to-month contracts churn at a higher rate than those with a one year or two year contract.

# The Plan

* Acquire data from Sequel Ace DB

* Prepare Data
    * Remove unnecessary data to reduce noise
        * drop duplicates
        * payment type id
        * internet service type id
        * contract type id
    * Create new columns utilizing existing data
        * contract type
        * payment type
        * tech support
        * online security

    * Create a train, validate, and test dataset with a split of about 56/24/20. 

* Explore Data and uncover drivers
    * Answer initial questions
        * Are customers with month-to-month contracts churning faster than those with 1yr/2yr contracts?
        * Does having add-on services affect churn rate?
            * online security
        * Does having multiple lines affect churn rate?
        * Does having dependents affect churn rate?

* Develop machine learning models
    * Utilize drivers in various machine learning models
    * Evaluate and refine models on train and validate data sets
    * Select best performing models
    * Use test data set on best models
    
        


# Data Dictionary

| Feature | Definition |
| :-- | :-- |
| churn | customer who has cancelled their services |
| churn_numeric | churn column encoded |
| contract type | type of contract. Month-to_month, One year, Two year|
| multiple lines | customers with more than one phone line |
| monthly charges | charges due at end of month bill cycle |
| total charges | total amount paid from first day of service |
| online security no internet | online security add-on service with no internet service |
| online security yes_internet | online securtiy add-on service with internet service |
| dependents_no | customers with no dependents |
| dependents_yes | customers with dependents |



# Steps to Reproduce

1. Clone this repo.
2. To acquire data, use your own env.py file to access MySql database and download data
3. Use functions in acquire.py to upload data
4. Use functions in prepare.py to clean and prep data.
5. Use same configurations for models.

# Conclusions

* About 3 of every 10 customers have churned.
* Customers with month-to-month contracts are more likely to churn
* Customers with online_security are less likely to churn
* Customers with multiple lines are less likely to churn.
* Customers that have dependents are less likely to churn.


# Recommendations

* To decrease chance of a customer churning, upsell the importance of having online-security.