
Clarify requirements
Define ML problem

# Data and feature
* Data sources: user generated vs system generated, cleanless of data, can the data source be trusted, do we need moderate data, etc
* Data storage: the DB used, or the file system 
* Data ETL: a framework / automation to stage clean and normalized data from various sources to data warehouse for downstream task consumption. (Data vaults store raw data as-is without applying business rules)
* Data types:
Strucutred: numerical(continuous vs discrete), categorical(ordinal, nominal)
Date: Year, Month, Week are good features
Time: Working hours / afterwork, morning/afternoon/evening, etc
Address: Area, postcode, state, etc
Names, credit number, phone, etc.

Unstructured: Video, audio, text, image

* Feature Engineering
Deal with NA/Inf: 
remove columns/rows with too many na/inf; which reduces usable data
fill with imputation/mean/medium, especially helpful in time series

Scaling
1. tree based models are normally not affected by data in different ranges
2. min-max: features scaled to range 0-1
3. z-score: features scaled to normal distribution, deal with outliers
4. log scaling: can make data less skewed

Discretization
convert continuous numerics to categorical

Categorical feature encoding
Integer: such as vote 1,2,3,4,5
One hot: 
Embedding: such as dirichlet embedding

Aggregate new features from historical feature
Labels as features and its historical aggregation - data leakage problem
Create features with Rank and rolling window

Feature importance, from Random Forest and Pearson correlation coefficient
Reduce data size - discretization


Video streaming system
Date source: user upload videos, stored in distributed fs, organised by metadata, do we need consider replicas,
the size of each video

Data collection, storage, fe, privacy/bias

Event recsys
Ad click prediction
Harmful content detection
Friend recsys
Jira sorting


Modelling
rule based baseline, simple models, complex models, ensembles
model input/output, model category, model parameters, 
linear regression, logistic regression, svm, nb
dt, rf
gbt
fm
nn

consider:
data size, training speed, hyperparams, continual training, computation, interpretability
interpretability: 

training:
split data, folds and cv, loss and eval, distributed training
hand labeling: expensive/slow, require domain knowledge, data privacy
natural labels

sampling: 
convenience sampling
snowball sampling
stratified sampling
reservoir sampling

overcome imbalance
over/under sampling
alter loss: class balanced loss, focal loss

distributed training
data parallelism
model parallelism

regularization: l1, l2, dropout, entropy regulation and cv

Adagrad (Adaptive Gradient Algorithm): use different learning rates for each parameter base on iteration
Adam: Adagrad + momentum



Evaluation
Serving
Misc: monitor, log, mlops

GCP, AutoML, VertexAI, Vision API, Speech2text API, NLP API
BigqueryML

VisionAPI 
* Text, landmark, logo, label detection
* object localization, crop hint, safe search, face detection
Not support
customer images, such as flower type classification, dog breed class, 

VAI: custom container, custom training
* upload data to bucket
* create notebook
* train models; (dump model to bucket)
* make custom container
* custom training setup with custom container, save model to bucket
* import model to model registry
* deploy model to endpoint



