# Our Main function
import yfinance as yf
import plotly.graph_objs as go
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth


def main():
    stock = yf.Ticker(st.text_input('Input Ticker Symbol: ', value='DARK.L', placeholder='Enter Ticker Symbol').upper())
    get_stocks(stock)
    st.header(f'{stock.info["longName"]}')
    draw_graph()

    # show streamlit sidebar
    st.sidebar.success("Select a demo above.")


@st.cache(show_spinner=True)
def get_stocks(stock):
    """
    This function gets the stock data for a given ticker
    """
    # Get the stock data
    data = stock.history(period="365d")
    data.to_csv('yahoo.csv')


def draw_graph():
    """
    This function draws a graph of the stock data
    """
    # Get the data
    data = pd.read_csv('yahoo.csv')

    # Create the graph
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title='<b>Graph the stock<b>')

    # Plot!
    st.plotly_chart(fig, use_container_width=True, width=800, height=600)


if __name__ == '__main__':
    main()