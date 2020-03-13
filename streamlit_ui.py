import streamlit as st
import altair as alt
from app.utils import df_utils
from app.utils.df_utils import get_init_dataset

init_df = get_init_dataset("./data/real_estate_data.csv")
init_df.dropna(inplace=True)


def one_hot_encoding(df, labels):
    # 2
    df_utils.check_and_fix_null(df)
    encoded_df = df_utils.one_hot_encoding(df, labels)
    return encoded_df


def show_data_frames():
    st.title("Welcome to ML workshop 1")
    labels = ["beds", "baths"]

    # if __name__ == "__main__":
    # 1 show dataset
    init_df = get_init_dataset("./data/real_estate_data.csv")
    st.dataframe(init_df)

    # 2 one_hot_encoding
    lables = []
    encoded_df = one_hot_encoding(init_df, labels)
    st.text("One hot encoded df:")
    st.dataframe(encoded_df)


def show_chart():
    # 3 show sqrfit and prices
    # df_sqft_price = encoded_df.filter(["sqft", "tx_price"])

    c = alt.Chart(init_df, width=700, height=400).mark_circle().encode(x='sqft', y='tx_price')
    st.write(c)


# UI
show_data_frames()
show_chart()

if __name__ == "__main__":
    show_data_frames()
    show_chart()
