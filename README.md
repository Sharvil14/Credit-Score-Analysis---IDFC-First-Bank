# Credit Card Behavior Score Analysis

## Project Overview

This project aims to predict credit card behavior scores, such as the likelihood of default, using machine learning. Here, I utilized a dataset of credit card users and applied a series of data science techniques to build a robust predictive model. These techniques include data cleaning, feature engineering, feature selection, handling class imbalance, model training, and evaluation.

## Key Features

* **Data Preprocessing:** Cleans the data by handling missing values, converting data types, and engineering new features from existing ones.
* **Feature Selection:** Selects important features using L1-based feature selection with LightGBM and correlation analysis.
* **Class Imbalance Handling:** Addresses class imbalance in the target variable (`bad_flag`) using the SMOTE technique.
* **Model Training:** Trains various machine learning models, including LightGBM, Random Forest, Gradient Boosting, and Logistic Regression, and evaluates their performance.
* **Hyperparameter Tuning:** Optimizes the LightGBM model's hyperparameters using RandomizedSearchCV for improved accuracy.
* **Ensemble Modeling:** Combines predictions from multiple models to potentially enhance prediction accuracy.
* **Model Evaluation:** Employs metrics like AUC-ROC, classification report, and confusion matrix to evaluate model performance.
* **Model Persistence:** Saves the trained model as a pickle file (`credit_risk_model.pkl`) for future use.

## Dataset

The project utilizes two datasets:

* `Dev_data_to_be_shared_mini.csv`: The training dataset.
* `validation_data_to_be_shared_mini.csv`: The validation dataset.

## Files

* `Dev_data_to_be_shared_mini.csv`: Training dataset.
* `validation_data_to_be_shared_mini.csv`: Validation dataset.
* `predictions.csv`: Predictions on validation data from the best model.
* `credit_risk_model.pkl`: Saved model file.


## Results

The project achieved an AUC-ROC score of [0.7548] on the validation set using the [LightGBM] model.

## Instructions

To run this analysis:

1. Clone this repository to the coding environment.
2. Upload the required datasets (`Dev_data_to_be_shared_mini.csv`, `validation_data_to_be_shared_mini.csv`) to your Colab environment.
3. Run all cells in the `notebook.ipynb` notebook.

## Further Development

* Further refine the feature engineering and selection process.
* Explore other model types and ensemble methods.
* Implement more advanced error analysis techniques.
* Deploy the model as a web service for real-time predictions.

## Author

[Sharvil Acharya]

## Acknowledgements

* [Scikit-Learn]
