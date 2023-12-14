import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col
import pandas as pd






# build models
def create_model():
    '''
    create model using statsmodels not in R style
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    '''
    pass

# predict values
def get_predictions(model):
    return model.fittedvalues


def extract_predictions(data, y, models):
   '''
     df_predicted = pd.DataFrame()
    df_predicted['y_true'] = data[y]
    for model in models['models'].keys():
        df_predicted[f'{model}'] = models['models'][model].fittedvalues
    return df_predicted
    '''


# sum-up results of range of models in one df 
def compare_models(models):
    summary_table = summary_col(models, float_format='%0.4f', stars=True)
    summary_df = pd.DataFrame(summary_table.tables[0])
    return summary_df


# save weights of specific model
def save_weights():
    pass


# penalty tips (lasso, ridge, elasticnet)
def penalty_tips():
    '''
    ?
    '''
    pass


# restore values for decomposition and share of kpi per factor
def make_decomposition(model):
    pass

