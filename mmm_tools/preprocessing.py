import pandas as pd

# done
def read_data_w_days(file_path):
    '''
    File with data has necessary fields:
        date - in format %d.%m.%Y 
    '''
    df = pd.read_csv(file_path, index_col='date')
    df['date'] = pd.to_datetime(df.index)
    df['date'] = pd.to_datetime(df.index, format='%d.%m.%Y')
    df.set_index('date', inplace=True)
    return df


def make_df(file_path):
    df = pd.read_csv(file_path, index_col='date', sep=';')
    df['date'] = pd.to_datetime(df.index)
    df.set_index('date', inplace=True)
    df.head()
    return df


def replace_spaces_in_strings(df):
    for col in df.columns:
        if df[col].dtype == 'O':
            df[col] = df[col].str.replace(' ', '').astype('float64')
        if df[col].dtype == 'int64':
            df[col] = df[col].astype('float64')


def scale_series(series, scale=1):
    scaled = series * (1 / scale)
    return scaled


def scale_df(df, thsnds_col=None, mlns_col=None):
    if thsnds_col is not None:
        for col in df[thsnds_col]:
            df[col] = df[col].apply(scale_series, scale=1_000)
    if mlns_col is not None:
        for col in df[mlns_col]:
            df[col] = df[col].apply(scale_series, scale=1_000_000)


def resample_weeks(df, weeks_boundaries='W-SUN', label='left'):
    df_copy = df.resample(weeks_boundaries, label, loffset=pd.DateOffset(days=1)).sum()
    df_copy.reset_index(inplace=True)
    df_copy.set_index('date', inplace=True)
    return df_copy


def log_data(df, cols_to_log):
    ''' 
    transform to escape inf or nans: log1p is log(x + 1)
    revert to original data: np.expm1
    '''
    df_copy = df.copy()
    for col in cols_to_log:
        new_name = f'{col}_log'
        df_copy[new_name] = np.log1p(df[col])
    return df_copy


def exponent_data(df, cols_to_exponent):
    ''' 
    revert to original data: np.expm1
    '''
    df_copy = df.copy()
    for col in cols_to_exponent:
        new_name = f'{col}_exp'
        df_copy[new_name] = np.expm1(df[col])
    return df_copy


# FLOW
# done:
# load data file
# inspect_data: find nans
# data types checking 
# date into index
# resample days to weeks if needed 
# scale data (to mls/ thsnds/ etc)
# log data (X and y) or some of them


# todo:

# data type changing (fill with 0 or means or medians)
def change_types():
    '''
    
    '''
    pass



# handling nans (delete or replace)
def handle_nans(series):
    '''
    drop or fill nans
    '''
    pass


# create index for price if needed
def create_index(series):
    '''
    Create index for price changes with basis == 100
    '''
    pass


# normalization-standartization /  max-min 
def normalize_data():
    '''
    
    '''
    pass

