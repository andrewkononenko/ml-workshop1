import pandas as pd


def get_init_dataset(dataset_path):
    '''
    read data to the dataframe
    :param dataset_path:
    :return: dataframe df
    '''
    return pd.read_csv(dataset_path)


def one_hot_encoding(df, list_columns):
    '''
     https://medium.com/@athif.shaffy/one-hot-encoding-of-text-b69124bef0a7
     http://queirozf.com/entries/one-hot-encoding-a-feature-on-a-pandas-dataframe-an-example
     http://www.insightsbot.com/python-one-hot-encoding-with-pandas-made-simple/
    '''

    for column in list_columns:
        encoded_columns = pd.get_dummies(df[column], prefix=column)
        df = pd.concat([df, encoded_columns], axis=1)
        df = df.drop(column, axis=1)

    return df

def read_and_prepare_df(dataset_path, hot_point_labels):

    df_raw = get_init_dataset(dataset_path)

    # Drop all rows with NULL cells
    df_raw_clean = df_raw.dropna()

    # Drop all rows with negative price
    df_raw_clean = df_raw_clean[(df_raw_clean['tx_price'] >= 0)]

    # Provide one hot encoding
    if len(hot_point_labels) > 0:
        df_raw_clean = one_hot_encoding(df_raw_clean, hot_point_labels)

    return df_raw_clean