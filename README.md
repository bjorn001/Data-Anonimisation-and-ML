# K-Anonymity in practice Beyond Classifiers: How Generalisation and Suppression affect ML Performance

This repository contains the Python code for applying different _k_-anonymisation algorithms, i.e., Optimal Lattice Anonymization (OLA), Mondrian, Top-Down Greedy Anonymisation (TDG), k-NN Clustering-Based (CB) Anonymisation,  on datasets and measuring their effects on Machine Learning (ML) Classifiers and Regressors.

The repository is structured as follows:
1. Classification codebase
2. Regression codebase
3. Statistical testing code




How to run?

In order to install the necessary requirements either use `pipenv install` or `pip3 install -r requirements.txt`.
Then activate the virtual environment, e.g. with `pipenv shell`. This can also be done without the environment, but depends on dependencies. Therefore it is advised to first run it without downloading these requirements and dependencies

After installing, navigate to the folder ...\k-AnonML-main using cd in command prompt. After this, you call the several arguments below to initiate the code, depending on what privacy method and model combination you want to use. Each model uses a different command, such as 'log' for logistic regression. An example line of code to run logistic regression would be: "baseline_with_repetitions.py cahousing log mondrian"

The parameters, i.e., dataset, ML algorithm, _k_-anonymisation algorithm, and _k_ are defined via arguments as follows:

```txt
usage: baseline_with_repetitions.py [-h] [--start-k START_K] [--stop-k STOP_K] [--step-k STEP_K] [--debug] [--verbose] [{cmc,mgm,adult,cahousing}] [{log,nb, ada, lin,log,lasso,rf,knn,svm,xgb} ] {mondrian,ola,tdg,cb} ...

Anonymize data utilising different privacy methods and analyse the effects of the anonymization on the classification and regression performance

positional arguments:
  {cahousing}
                        the dataset used for anonymization
  {log,nb, ada, lin,log,lasso,rf,knn,svm,xgb}      machine learning classifier
  {mondrian,ola,tdg,cb}
    mondrian            mondrian anonyization algorithm
    ola                 ola anonyization algorithm
    tdg                 tdg anonyization algorithm
    cb                  cb anonyization algorithm

optional arguments:
  -h, --help            show this help message and exit
  --start-k START_K     initial value for k of k-anonymity
  --stop-k STOP_K       last value for k of k-anonymity
  --step-k STEP_K       step for increasing k of k-anonymity
  --debug, -d           enable debugging
  --verbose, -v
```


The _k_-anonymisation algorithms "_k_-NN Clustering-Based Anonymisation", "Mondrian" and "Top-Down Greedy Anonymisation" located in the folders `clustering_based`, `basic_mondrian` and `top_down_greedy` are based on the open-source implementation of [Qiyuan Gong](mailto:qiyuangong@gmail.com). The implementation of the classfiers rf, knn, svm and xgb and the ola anonymization algorithm are extended from the paper of Dam et al. (2021) called _k_-Anonymity in practice: How generalisation and suppression affect machine learning classifiers

Original implementations:

- [Clustering Based k-Anonymization](https://github.com/qiyuangong/Clustering_based_K_Anon)
- [Basic Mondrian](https://github.com/qiyuangong/Basic_Mondrian)
- [Top Down Greedy Anonymization](https://github.com/qiyuangong/Top_Down_Greedy_Anonymization)
- [k-Anonymity in Practice: How Generalisation and Suppression Affect Machine Learning Classifiers](https://github.com/fhstp/k-AnonML)

Notice that the extension used in our paper are the following modications:
- For regression:

  > median_house_value was moved to the target variable
  
  > Three new regressors were added: linear, lasso and ridge regression
  
  > New evaluation methods were implemented for regression: R2 score (and even MSE if useful)
  
  > writing of results was changed to allow for writing the different regression evaluation results
  
- For classification:

  > New classifiers were added: AdaBoostClassifier, Naive Bayes and Logistic Regression
  
- For both:

  > A non-anonymised score was printed and calculated



## Data
The repository contains following locations for data:

- `datasets`
  - contains all available datasets in separate folders
- `generalization/hierarchies`
  - contains the necessary defined generalization hierarchies per attribute and dataset, from the original paper of Dam et al. (2021)
- `results`
  - all computed results (anonymised datasets, ML performance, etc.) are stored inside a folder structure inside `results` for each experiment. 
- `paper-results`
  - Contains the results used for the paper itself

Author: Björn van Engelenburg     
Examined by: Jacco van Ossenbruggen and Dayana Spagnuelo

University: Vrije Universiteit Amsterdam
