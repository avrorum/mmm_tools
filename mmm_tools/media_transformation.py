import pandas as pd
import numpy as np


def lag_data(df, columns_to_lag, shift=1):
    df_copy = df.copy()
    for col in columns_to_lag:
        name_new = f'{col}_lag_{shift}'
        df_copy[name_new] = df_copy[col].shift(shift)
    df_copy.dropna(inplace=True)
    return df_copy 


def adstock(series, decay_rate):
    """
    Apply adstock transformation to a series of advertising data.

    Parameters:
    series (pandas.Series): Series of advertising data (e.g., spend, impressions).
    decay_rate (float): Decay rate for adstock effect (between 0 and 1).

    Returns:
    pandas.Series: Transformed series with adstock applied.
    """
    adstocked = [series.iloc[0]]

    for i in range(1, len(series)):
        adstocked_value = series.iloc[i] + decay_rate * adstocked[i-1]
        adstocked.append(adstocked_value)

    return pd.Series(adstocked, index=series.index)


def adstock_media(df, media_vars, decay_rate=0.5):
    df_copy = df.copy()
    for col in media_vars:
        name_new = f'{col}_adst'
        df_copy[name_new] = adstock(df_copy[col], decay_rate)
    return df_copy


def saturation_hill_function(series, maximum, slope, inflection):
    return pd.Series(maximum * np.power(series, slope) / (inflection + np.power(series, slope)))


def estimate_saturation(df, media_vars, maximum, slope, inflection):
    df_copy = df.copy()
    for col in media_vars:
        name_new = f'{col}_satur'
        df_copy[name_new] = saturation_hill_function(df_copy[col], maximum, slope, inflection)
    return df_copy

