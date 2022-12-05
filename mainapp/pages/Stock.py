import streamlit as st
import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt


stocks = st.text_input("Stocks", "META")
stocks = stocks.split()
stocks_data = yf.download(stocks, period="5d", interval="1m")
st.dataframe(stocks_data)
