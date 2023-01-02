# Telco Churn Project


# Project Description

### Telco is a telecommunications company that provides a number of services to include phone and internet. There has been a number of customers who have churned from Telco. In this project, I will delve into the different features of Telco's data and hone in on possible reasons why customers have decided to churn. 


# Business Goals

* Uncover drivers that are causing Telco customers to churn
* Use machine learning algorythms with drivers to hone in on possible reasons for customer churn.
* Develop an understanding of possible reasons customers are churning.

# Initial Thoughts

### My initial hypothesis is that customers who are churning are customers who's monthly total bill are high and are on a month-to-month contract.

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
        * internet service type
        * payment type
        * tech support
        * online security
        * online backup
        * device protection
    * Create a train, validate, and test dataset with a split of about 56/24/20. 

* Explore Data and uncover drivers
    * Answer initial questions
        * Are customers with month-to-month contracts with monthly bills churning faster than those with 1yr/2yr contracts with similar bills?
            * Disregarding bill total, do month-to-month contracts churn at a higher rate than 1yr/2yr contracts?
            * Disregarding contract type, does having a higher bill affect churn rate?
        * Does having add-on services affect churn rate?
            * online security
            * online back-up
            * device protection
        * Does having multiple lines affect churn rate?
        * Does payment type affect churn rate?

* Develop machine learning models
    * Utilize drivers in various machine learning models
    * Evaluate and refine models on train and validate data sets
    * Select best performing models
    * Use test data set on best models
    
        


# Data Dictionary

| Feature | Definition |
|---------| ---------- |
| churn | customer who has cancelled their services |
| multiple lines | customers with more than one phone line |
| monthly charges | charges due at end of month bill cycle |
| total charges | total amount paid from first day of service |
| tech support no internet | add-on service with no internet service |
| tech support yes internet | add-on service with internet service |
| online security no internet | online security add-on service with no internet service |
| online security yes_internet | online securtiy add-on service with internet service |
| online backup no internet | online backup add-on service with no internet service |
| online backup yes internet | online backup add-on service with internet service  |
| device protection no internet | device protection add-on service with no internet service |
| device protection yes internet | device protection add-on service with internet service  |


# Steps to Reproduce


# Key Takeaways


# Recommendations