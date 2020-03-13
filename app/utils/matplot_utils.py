import matplotlib.pyplot as plt


def plot_prices(list_df):
    for i in range(0, len(list_df)):
        plt.xlabel('price')
        plt.ylabel('sqft')
        plt.plot(list_df[i]['tx_price'], list_df[i]['sqft'])
        plt.show()
