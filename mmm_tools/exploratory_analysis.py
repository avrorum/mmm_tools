
# check distribution and normality of data vars

# check correlations

# find outliers


def print_data_info(df):
    # Data Summary
    print('Data Shape:', df.shape)
    print('\nData Types:')
    print(df.dtypes)

    # Missing Values Check
    print('\nMissing Values:')
    print(df.isnull().sum())

    # info about dataframe 
    print(df.info())

    # Statistical Summary
    print('\nStatistical Summary:')
    print(df.describe())

    # Adjusting the layout to accommodate all numerical columns
    num_columns = df.select_dtypes(include=['number']).shape[1]

    # Print correlations
    print(df.corr())
    print(sns.heatmap(df.corr()))


    rows = num_columns // 3 + (num_columns % 3 > 0)

    # Histograms for each numerical variable
    df.hist(bins=15, figsize=(15, rows * 5), layout=(rows, 3))
    plt.tight_layout()
    plt.show()


    # Box plots for each numerical variable
    df.plot(kind='box', subplots=True, layout=(rows, 3), figsize=(15, rows * 5), sharex=False, sharey=False)
    plt.tight_layout()
    plt.show()


