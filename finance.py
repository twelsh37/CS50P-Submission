# Our Main function
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go


def main():
    stock = yf.Ticker(input('Input Ticker Symbol: ').upper())
    get_stocks(stock)
    draw_graph()

def get_stocks(stock):
    """
    This function gets the stock data for a given ticker
    :param ticker: The ticker to get the data for
    :return: A dataframe of the stock data
    """
    # Get the stock data
    data = stock.history(period="1000d")
    data.to_csv('yahoo.csv')

def draw_graph():
    """
    This function draws a graph of the stock data
    :param data: The data to draw the graph for
    :return: None
    """
    # Get the data
    data = pd.read_csv('yahoo.csv')

    # Create the graph
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.show()

if __name__ == '__main__':
    main()