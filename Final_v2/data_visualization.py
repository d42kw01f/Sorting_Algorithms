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
        slit.markdown('### Num. of Comparisons made by Each Algorithm')
        multi_algo_pie_fig = px.pie(multiple_df, values='Comparisons', names='Algorithms')
        slit.write(multi_algo_pie_fig)
        slit.markdown('### Run Time That Each Algorithm Took')
        multi_algo_bar_fig = px.bar(multiple_df, x='Algorithms', y='Time')
        slit.write(multi_algo_bar_fig)

    with slit.expander('Visualize on experimental study data'):
        csv_exp_file_0 = Path('exp_study_table_2.csv')
        csv_exp_file_1 = Path('exp_study_table_3.csv')
        if not csv_exp_file_0.is_file() or not csv_exp_file_1.is_file():
            slit.error('There is nothing to visualize')
            slit.markdown('Please use the multiple sorting algorithm function generate data.')
            return
        exp_df_0 = pd.read_csv(csv_exp_file_0, index_col=[0])
        exp_df_1 = pd.read_csv(csv_exp_file_1, index_col=[0])
        fig_exp_0 = px.bar(exp_df_0, x='Algorithms', y=exp_df_0.columns)
        fig_exp_1 = px.line(exp_df_1, x='Algorithms', y=exp_df_0.columns)
        slit.markdown('### Number of comparisons for sorting arrays')
        slit.write(fig_exp_0)
        slit.markdown('### Running time for sorting array size of n')
        slit.write(fig_exp_1)
