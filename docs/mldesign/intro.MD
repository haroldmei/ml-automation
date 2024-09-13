# The framework

## Requirement clarification
* What are the business goals? (CTR, IncSales, etc)
Video recsys: improve user engagement

* Functional requirement
Video recommendation: user upvote/downvote/score
Jira ticket sorting: Per project or per company

* Data
Structured: Users, products, jira tickets, movies, events
Unstructured: movies, images
Data labelling available? Human labelling needed?

* Non functional requirement
Bulk/realtime serving, bulking cadency, realtime scalability/concurrency
number of users need to support, etc
Constraints: computing power, cloud based? on a device?
Support continuous training/deployment?
Performance: the latency of prediction, does accuracy have more priority than latency?

## Define ML task
### Define ML objective, specify input/output, choose model
Think about the following business objective, what are the corresponding ML objectives?
Doing prediction is not the goal, the goal is use this prediction to guide decisions and achieve these business objectives.
* increase event ticket sales - maximize the number of event registrations
I have some event ideas, how do i know each of them will end up with good sales? 

* improve user retention - maximize the time user spend browsing
* improve user engagement - maximize the time users spend watching videos
* sort jira ticket correctly - 
* increase user clicks - maximize CTR
* reduce insurance claim fraud - accurately predict fraudulent claims
* increate rate at which user grow friendship - maximize the number of formed connections

### Specify input and output
* harmful content detection, input: content (text, image, video); output: probability of being harmful
    multiple output usecase
* event recommendation system, input: user + event (text, image, video); output: probability of user registering the event, or
    input: user, output: softmax probabilities of user registering each event.

### Choose the right model category
Supervised: LGBM/Catboost/XGBoost/DL
Unsupervised: Kmeans clustering, KNN, EM, etc.
Reinforcement Learning: In long horizon 

Classification/Regression

What is a good ml object? how to compare different ml objectives?
Specify Input and Output from ML objectives? (User, Item, U-I interaction)
How to decide if we need more than one model?
How to decide if it should be regression or clasification?

## Data and feature
data engineering: etl, collecting, storing, retrieving and processing data
data source: who collect it, how clean, user generated or system generated, can the source be trusted? size of data? 
data storage: SQL, NoSQL(k-v, doc, graph, column based)
ETL: 

Data types: 
structured - numerical(continuous vs discrete), categorical(ordinal, nominal)
non-structured - video, audio, image, text, etc.

feature engineering: deal with NA, scale, discretization, categorical encoding (integer encoding, one-hot, embedding)
feature engineering extension: history aggregation, autoAE

*fe for unstructured data: image, audio, video
how to combine data of different types, such as texts, numbers, and images?
pii info, privacy, is anonymization needed? is data only available on your server?
bias of the data and ways to correct it?



Modelling
explore various model options and discuss pros and cons
LinearR, LogisticR, SVM, DT, RF, Factorization Machines (FM, in CF), GBM, LGBT
NN (CNN, RNN, Transformer, encoder-decoder, etc.)

different aspect of a model:
the amount of data
training speed
hyperparameters to choose
possibility of continual learning (checkpoint saves the context.)
compute requirement, more complex model means better performance but more computation(also may cause overfitting)



Evaluation
Serving
Monitor


