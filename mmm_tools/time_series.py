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
    df_timeseries['residuals'] = model.resid
    df_timeseries['trend'] = model.trend
    df_timeseries['seasonality'] = model.seasonal
    return df_timeseries


# todo

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


# transformations (exp smoothing)

# smoothing with window (2-3-x)

# pacf - acf correlologramms

# find forms of time model - arima (autoarima)

# find forms of time model - sarima

# find forms of time model - sarimax

