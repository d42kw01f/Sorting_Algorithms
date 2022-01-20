import pandas as pd
import streamlit as slit
from pathlib import Path
import plotly.express as px


def data_head():
    slit.header('Data Visualization :deciduous_tree:')
    with slit.expander('Visualize on above multiple sorting algorithm dataframe'):
        csv_file = Path('multi_algos_df.csv')
        if not csv_file.is_file():
            slit.error('There is nothing to visualize')
            slit.markdown('Please use the multiple sorting algorithm function generate data.')
        multiple_df = pd.read_csv(csv_file)
        slit.markdown('### Num. of Comparisons made by Each Algorithms')
        multi_algo_pie_fig = px.pie(multiple_df, values='Comparisons', names='Algorithms')
        slit.write(multi_algo_pie_fig)
        slit.markdown('### Run Time That Each Algorithms Took')
        multi_algo_bar_fig = px.bar(multiple_df, x='Algorithms', y='Time')
        slit.write(multi_algo_bar_fig)
