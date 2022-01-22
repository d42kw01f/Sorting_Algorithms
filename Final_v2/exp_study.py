import streamlit as slit
from Sort_Algos import SortingAlgo
import random
from pathlib import Path
import pandas as pd


def experimental_study():
    slit.header('Experimental Study: :seedling:')
    with slit.expander('Experimental Study'):
        if slit.button('Click here to Start Experiment', key='exp-sty-start'):
            num_elem_arr = [100, 200, 400, 800, 1000, 2000]
            for n in num_elem_arr:
                the_arr_exp = [round(random.uniform(-10, 100)) for _ in range(n)]
                slit.success(f'Randomly generated {n} size of an array')
                comp_df, time_df = running_all_algorithms_exp(the_arr_exp)

            slit.markdown('#### Results :see_no_evil:')
            slit.markdown('##### **Table 2:** number of comparisons for sorting algorithms')
            slit.table(comp_df)
            slit.markdown('##### **Table 3:** running time for sorting algorithms')
            slit.table(time_df)
            slit.warning('Please note that these are not average values')


def running_all_algorithms_exp(arr):
    exp_list_len = len(arr)
    print('***' * 20)
    if not arr:
        slit.error('Looks like the array is empty')
        return

    multi_sort_algos = SortingAlgo(arr)
    exp_study_select = multi_sort_algos.selection_sort()
    exp_study_insert = multi_sort_algos.insertion_sort()
    exp_study_merge = multi_sort_algos.merge_sort()
    exp_study_quick = multi_sort_algos.quick_sort()
    exp_study_bubble = multi_sort_algos.bubble_sort()
    exp_study_optimal_bubble = multi_sort_algos.optimal_bubble_sort()
    exp_study_heap = multi_sort_algos.heap_sort()
    exp_study_general_count = multi_sort_algos.general_count_sort()
    exp_csv = Path('exp_study_table_2.csv')
    exp_csv_1 = Path('exp_study_table_3.csv')

    if not exp_csv.is_file():
        exp_algo_names = ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal Bubble', 'General-Counting',
                          'Heap']
        exp_study_df = pd.DataFrame({'Algorithms': exp_algo_names})
        exp_study_df.to_csv(exp_csv)

    if not exp_csv_1.is_file():
        exp_algo_names = ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal Bubble', 'General-Counting',
                          'Heap']
        exp_study_df = pd.DataFrame({'Algorithms': exp_algo_names})
        exp_study_df.to_csv(exp_csv_1)

    exp_study_df = pd.read_csv('exp_study_table_2.csv', index_col=[0])
    exp_study_df_1 = pd.read_csv('exp_study_table_3.csv', index_col=[0])

    comparisons_epx = []
    run_time_epx = []
    comparisons_epx.append(exp_study_select[0][1])
    comparisons_epx.append(exp_study_insert[0][1])
    comparisons_epx.append(exp_study_merge[0][1])
    comparisons_epx.append(exp_study_quick[0][1])
    comparisons_epx.append(exp_study_bubble[0][1])
    comparisons_epx.append(exp_study_optimal_bubble[0][1])
    comparisons_epx.append(exp_study_general_count[0][1])
    comparisons_epx.append(exp_study_heap[0][1])

    run_time_epx.append(exp_study_select[1])
    run_time_epx.append(exp_study_insert[1])
    run_time_epx.append(exp_study_merge[1])
    run_time_epx.append(exp_study_quick[1])
    run_time_epx.append(exp_study_bubble[1])
    run_time_epx.append(exp_study_optimal_bubble[1])
    run_time_epx.append(exp_study_general_count[1])
    run_time_epx.append(exp_study_heap[1])

    if exp_list_len == 100:
        exp_study_df['n=100'] = comparisons_epx
        exp_study_df_1['n=100'] = run_time_epx

    elif exp_list_len == 200:
        exp_study_df['n=200'] = comparisons_epx
        exp_study_df_1['n=200'] = run_time_epx

    elif exp_list_len == 400:
        exp_study_df['n=400'] = comparisons_epx
        exp_study_df_1['n=400'] = run_time_epx

    elif exp_list_len == 800:
        exp_study_df['n=800'] = comparisons_epx
        exp_study_df_1['n=800'] = run_time_epx

    elif exp_list_len == 1000:
        exp_study_df['n=1000'] = comparisons_epx
        exp_study_df_1['n=1000'] = run_time_epx

    elif exp_list_len == 2000:
        exp_study_df['n=2000'] = comparisons_epx
        exp_study_df_1['n=2000'] = run_time_epx
    exp_study_df.to_csv(exp_csv)
    exp_study_df_1.to_csv(exp_csv_1)
    return exp_study_df, exp_study_df_1
