import streamlit as st
import yfinance as yf
from datetime import datetime


st.sidebar.subheader("Stock Searcher")
selected_stock = st.sidebar.text_input("Enter a valid stock name", "META")
button_clicked = st.sidebar.button("Enter")
if button_clicked:

    st.subheader("Stocks dataframe")
    stocks = selected_stock.split()
    stocks_data = yf.download(stocks, period="5d", interval="1m")
    st.dataframe(stocks_data)

    st.subheader("Daily Closing price for " + selected_stock)
    stock_data = yf.Ticker(selected_stock)
    stock_df = stock_data.history(period="1d", start="2022-01-01", end=None)
    st.line_chart(stock_df.Close)

    st.subheader("Closing price for " + selected_stock)

    date = datetime.today().strftime("%Y-%m-%d")

    stock_last_price = stock_data.history(period="1d", start=date, end=date)

    last_price = stock_last_price.Close

    if last_price.empty == True:
        st.error("No data available at the moment")
    else:
        st.info(last_price)

    st.subheader("""**Quarterly earnings** for """ + selected_stock)
    display_earnings = stock_data.quarterly_earnings
    if display_earnings.empty == True:
        st.write("No data available at the moment")
    else:
        st.line_chart(display_earnings)
        st.write(display_earnings)
