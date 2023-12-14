import statsmodels.api as sm
from statsmodels.tsa.seasonal import STL
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# find seasonality in data, decompose data

# decompose with stl

# decompose with prophet

# transformations

# find forms of time model - arima (autoarima)

# find forms of time model - sarima

# find forms of time model - sarimax

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
def make_stl(y):
    res_stl = STL(y).fit()
    df_timeseries = pd.DataFrame(y)
    df_timeseries['res_stl_resid'] = res_stl.resid
    df_timeseries['res_stl_trend'] = res_stl.trend
    df_timeseries['res_stl_seasonal'] = res_stl.seasonal
    return df_timeseries


# decompose data with prophet 
def decompose_prophet(df, target='y'):

    temp = pd.DataFrame({
        'y': df[target],
        'ds': df['date']
    })

    model = Prophet()
    model.fit(temp)
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig = model.plot_components(forecast)
    plt.show()



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


# smoothing with window (2-3-x)


# pacf - acf correlologramms



