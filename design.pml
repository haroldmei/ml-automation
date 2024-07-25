@startuml

file raw_data
file prediction_result

rectangle curated_data

rectangle feature_store

rectangle train_data

rectangle prediction_data

rectangle model_store

file model_params

process model_training
process model_inference


raw_data ---> curated_data
curated_data ---> feature_store : feature engineering
feature_store ---> train_data
feature_store ---> prediction_data
train_data ...> train_data : tag the feature

train_data ---> model_params : tuning
train_data ---> model_store : training
model_store ...> model_store : tag the model


prediction_data ===> model_inference : to be predicted
model_store ===> model_inference : selected model

model_inference ---> prediction_result

@enduml