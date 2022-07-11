# Statistical results combinations ML models and anonymization algorithm

This folder contains the statistical results of the combination ML model with a specific anonymization algorithm. An example could be linear regression anonymized by 
the CB algorithm (lin_CB) compared against lasso regression using mondrian (lasso_mondrian). The statistical tests were performed using Mann-Whitney u tests.

This is done in a Jupyter Notebook where it can be chosen to filter out only the results higher than p=5. To acquire all p values higher than 5, remove the hashtag from 'display(p_larger_5)'. For all the results at once, simply run the code as it came delivered (display(p_value_df)). 


