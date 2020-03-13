from app.utils.util_log import log

'''
https://www.datadriveninvestor.com/2019/11/20/the-math-in-ml-cosine-similarity/
https://neo4j.com/docs/graph-algorithms/current/labs-algorithms/cosine/
'''


def measure(df_encoded, df_raw, row_id):
    log.info('Start cosine similarity measurement')
    out_file_path = './cosine_similarity_report.csv'

    # Prepare 'ndarray' without column names.
    matrix = df_encoded.values
    # Vector for comparison
    vector_for_comparing = matrix[row_id: row_id + 1]
    # Calculate similarity

    # feature importance

    df_raw.to_csv(out_file_path)


if __name__ == "__main__":
    # Read real_estate to the panda data frame
    dataset_path = "../../data/real_estate_data.csv"
    integer_labels = ["beds", "baths"]
    string_labels = ["property_type", "exterior_walls", "roof"]

    # Drop all rows with NULL cells

    # Drop all rows with negative price

    # Provide one hot encoding

    # item for comparing

    apartment_id = 2
    measure(0, 0, apartment_id)
