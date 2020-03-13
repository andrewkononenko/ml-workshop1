import pandas as pd

from app.utils.df_utils import get_init_dataset, one_hot_encoding
from app.utils.matplot_utils import plot_prices


def sort_and_split(df, parts):
    '''
    Split to the 4 parts by 'tx_price' column
    :param df: preprocessed df
    :param parts: n parts for splitting
    :return: list of df
    '''

    df_sorted = df.sort_values('tx_price')
    arrays = pd.np.array_split(df_sorted, parts)
    return arrays


if __name__ == "__main__":
    # Read real_estate to the panda data frame
    dataset_path = "../../data/real_estate_data.csv"
    integer_labels = ["beds", "baths"]
    string_labels = ["property_type", "exterior_walls", "roof"]

    df_raw = get_init_dataset(dataset_path)

    # Drop all rows with NULL cells

    # Drop all rows with negative price

    # Provide one hot encoding

    df_encoded = ""
    plot_prices(sort_and_split(df_encoded, 2))
