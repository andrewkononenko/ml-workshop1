import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from app.utils.df_utils import read_and_prepare_df, get_init_dataset
from app.utils.util_log import log

'''
https://www.datadriveninvestor.com/2019/11/20/the-math-in-ml-cosine-similarity/
https://neo4j.com/docs/graph-algorithms/current/labs-algorithms/cosine/
'''


def measure(df_encoded, df_raw, row_id):
    log.info('Start cosine similarity measurement')
    out_file_path = './cosine_similarity_report_my.csv'

    # Prepare 'ndarray' without column names.
    matrix = df_encoded.values
    # Vector for comparison
    vector_for_comparing = matrix[row_id: row_id + 1]
    # Calculate similarity
    naive_simularity = cosine_similarity(df_encoded, vector_for_comparing)
    df_raw['cosin_simularity'] = naive_simularity
    df_raw = df_raw.sort_values(by=['cosin_simularity'], ascending=False)

    # feature importance
    #Have no idea even how to google it. Tried to google weights, but not sure that I've found correct thing

    df_raw.to_csv(out_file_path)


if __name__ == "__main__":
    # Read real_estate to the panda data frame
    dataset_path = "../../data/real_estate_data.csv"
    integer_labels = ["beds", "baths"]
    string_labels = ["property_type", "exterior_walls", "roof"]

    df_raw = get_init_dataset(dataset_path)

    # Drop all rows with NULL cellszx
    df_raw = df_raw.dropna()
    df_raw = df_raw[(df_raw['tx_price'] >= 0)]

    encoded_df = read_and_prepare_df(dataset_path, integer_labels + string_labels)

    # item for comparing

    apartment_id = 2
    measure(encoded_df, df_raw, apartment_id)
