# ml-automation

## Summary
A Github based MLOps framework that strives to handle data solutions gracefully and takes care of following:

* Data privacy: strictly confine data within private cloud.
* Close source: if choose so, your source code stays within your organization.
* Flattened learning curve: Github is all you need for your data solution.
* Minimized operation cost: Maximize the utilization of existing IT resource and minimize the necessarity for new computing investiment.
* Minimalistic system design: No need for Argo/Airflow instances, neither any k8s clusters.

Apart from defining the components and workflows for productions of both machine learning modelling, inferencing workflows, this repositary also gives some examples to demonstrate how data teams can utilize Github's CI/CD automation for MLOps purposes.
Components supported:
* Data ingestion and ETL to BigQuery + Cloud Storage
* Feature engineering
* Machine learning modelling
* Parallel parameter search + cross validation
* Machine learning inference
* A/B testing
* Continuous training

Overview diagram:
![plot](./docs/overview.png)

## End to end automations for production

### Stock market prediction

#### AAPL crests & troughs prediction
![AAPL Crests and Troughs prediction](https://drive.google.com/uc?id=1t_bIRcFwMmc5US04fvc8CO0KkxE4DStz)

#### Backtest NASDAQ stocks
[Backtest NASDAQ stocks](https://docs.google.com/spreadsheets/d/1RZv5LuZ0fv8o-Xw0CaTOeEFDGK3OQd42yCVFn1bT-GY)

### Australia property listing data analysis

### Australia housing market prediction

### 