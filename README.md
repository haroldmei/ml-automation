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


## Stock market prediction

### Feature importaince
![plot](./docs/s5-mod-lgbm/models/models-0-1-1/target_1_lgbm_importance.png)

### Cross Validation Evaluation per symbol

|symbol|f1           |auc  |tpr    |fpr    |p-total|n-total|tp |fp |tp/fp               |
|------|-------------|-----|-------|-------|-------|-------|---|---|--------------------|
|AAPL  |0.0833|0.7386|0.666|0.189  |3      |227    |2  |43 |0.0465 |
|ABBV  |0.1025|0.7584|0.666|0.149  |3      |227    |2  |34 |0.0588 |
|ABT   |0.1142|0.9320|1.0  |0.135  |2      |228    |2  |31 |0.0645 |
|ACN   |0.0833|0.6570|0.5  |0.185  |4      |226    |2  |42 |0.0476 |
|ADBE  |0.125 |0.7111|0.6  |0.177  |5      |225    |3  |40 |0.075  |
|AIG   |0.1052|0.9254|1.0  |0.149  |2      |228    |2  |34 |0.0588 |
|AMD   |0.1818|0.9203|1.0  |0.159  |4      |226    |4  |36 |0.1111 |
|AMGN  |0.2285|0.9402|1.0  |0.119  |4      |226    |4  |27 |0.1481 |
|AMT   |0.1428|0.9473|1.0  |0.105  |2      |228    |2  |24 |0.0833 |
|AMZN  |0.12  |0.7798|0.75 |0.190  |4      |226    |3  |43 |0.0697 |
|AVGO  |0.1111|0.9298|1.0  |0.140  |2      |228    |2  |32 |0.0625 |
|AXP   |0.16  |0.9539|1.0  |0.092  |2      |228    |2  |21 |0.0952 |
|BA    |0.2105|0.9336|1.0  |0.132  |4      |226    |4  |30 |0.1333 |
|BAC   |0.2580|0.9491|1.0  |0.101  |4      |226    |4  |23 |0.1739 |
|BK    |0.1052|0.6792 |0.5 |0.141  |4      |226    |2  |32 |0.0625 |
|BKNG  |0.1428|0.9207 |1.0 |0.158  |3      |227    |3  |36 |0.0833 |
|BLK   |0.2222|0.9222|1.0  |0.155  |5      |225    |5  |35 |0.1428 |
|BMY   |0.6666|0.9933|1.0  |0.013  |3      |227    |3  |3  |1.0    |


### AAPL crests & troughs prediction
![AAPL Crests and Troughs prediction](https://drive.google.com/uc?id=1t_bIRcFwMmc5US04fvc8CO0KkxE4DStz)

### Backtest NASDAQ stocks
[Backtest NASDAQ stocks](https://docs.google.com/spreadsheets/d/1RZv5LuZ0fv8o-Xw0CaTOeEFDGK3OQd42yCVFn1bT-GY)

## Australia property listing data analysis

## Australia housing market prediction

## 