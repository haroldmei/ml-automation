@startuml
left to right direction

<style>
componentDiagram {
  BackGroundColor palegreen
  LineThickness 3
  LineColor red
  FontSize 20
}
document {
  BackGroundColor white
}
</style>

file raw_data
file predicted_labels
file observed_labels

rectangle curated_data

rectangle feature_store

rectangle labelled_data

rectangle unlabelled_data

rectangle model_store

file model_params

process model_tuning
process model_training
process model_inference
process model_performance_report


raw_data ---> curated_data
curated_data ---> feature_store : feature engineering
feature_store ---> labelled_data
feature_store ---> unlabelled_data
feature_store -[#blue,dotted,thickness=8]-> feature_store : tag the feature

labelled_data ===> model_tuning : holdup test data
model_tuning ---> model_params : parallel cross validation

labelled_data ===> model_training : full data
model_training ---> model_store : select param and train

model_store -[#blue,dotted,thickness=8]-> model_store : tag the model


unlabelled_data ===> model_inference : unlabelled data


model_inference ---> predicted_labels

predicted_labels ---> model_performance_report
observed_labels ---> model_performance_report

@enduml