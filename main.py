# pip install streamlit yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go

# import library pandas
import pandas as pd

# Import library numpy
import numpy as np

# Import library matplotlib untuk visualisasi
import matplotlib.pyplot as plt

START = "2013-11-19"
END = "2023-05-19"

st.title('Tubes Visdat Daniar Abi')

stocks = ('BBCA.JK', 'BBNI.JK', 'BBRI.JK')
selected_stock = st.selectbox('Pilih dataset ', stocks)


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, END)
    data.reset_index(inplace=True)
    return data

if st.button("GO"):	
	data_load_state = st.text('Loading data...')
	data = load_data(selected_stock)
	data_load_state.text('Loading data... done!')
	st.subheader('Raw data')
	st.write(data.tail())

	# Plot raw data
	def plot_raw_data():
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
		fig.layout.update(title_text='Stock '+selected_stock, xaxis_rangeslider_visible=True)
		st.plotly_chart(fig)
		
	plot_raw_data()
