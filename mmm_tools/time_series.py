import statsmodels.api as sm
from statsmodels.tsa.seasonal import STL
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# done

# find seasonality in data, decompose data

# build additive model naive
def decompose_additive(df, col='y', model='additive', period=PERIOD):
    result = sm.tsa.seasonal_decompose(df[col], model=model, period=period)
    result.plot()
    plt.show()


# build multiplicative model naive
def decompose_multiplicative(df, col='y', model='multiplicative', period=PERIOD):
    result = sm.tsa.seasonal_decompose(df[col], model=model, period=period)
    result.plot()
    plt.show()


# STL decomposition
def decompose_stl(y):
    model = STL(y).fit()
    df_timeseries = pd.DataFrame(y)
    df_timeseries['residuals_stl'] = model.resid
    df_timeseries['trend_stl'] = model.trend
    df_timeseries['seasonality_stl'] = model.seasonal
    return df_timeseries


# decompose data with prophet 
def decompose_prophet_basic(df, y, multi=False):
    '''
    df - full df with date in index
    y - target metric
    '''
    temp = df[[y]]
    temp.reset_index(inplace=True)
    temp.columns = ['ds', 'y']

    if multi:
        model = Prophet(seasonality_mode='multiplicative')
    
    else:
        model = Prophet(seasonality_mode='additive')
    
    model.fit(temp)
    future = model.make_future_dataframe(0)
    forecast = model.predict(future)

    df_prophet_extracted = forecast.copy()
    df_prophet_extracted.index = df_prophet_extracted['ds']

    return df_prophet_extracted


# check trend break
def check_trend_break(df, target='y'):
    '''
    Todo
    test Chow in y
    '''
    return


# inspect data for stationarity
def check_stationarity(df, target='y'):
    '''
    Todo
    test Dickey-Fuller in y
    plot ACF and PACF
    '''
    return


# transformation box-cox
def transform_box_cox(df, target='y'):
    '''
    Todo
    transform y with box-cox
    '''
    return


# transformations (exp smoothing)

# smoothing with window (2-3-x)

# pacf - acf correlologramms

# find forms of time model - arima (autoarima)

# find forms of time model - sarima

# find forms of time model - sarimax

