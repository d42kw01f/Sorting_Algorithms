import streamlit as slit
import pandas as pd
from Sort_Algos import SortingAlgo


def running_all_algorithms(arr):
    if slit.button('Sort the Array', key=2):
        slit.markdown('#### Results :see_no_evil:')
        slit.markdown('***')
        if not arr:
            slit.error('Looks like the array is empty')
            return
        multi_sort_algos = SortingAlgo(arr)
        result_list_select = multi_sort_algos.selection_sort()
        result_list_insert = multi_sort_algos.insertion_sort()
        result_list_merge = multi_sort_algos.merge_sort()
        # result_list_quick = multi_sort_algos.quick_sort()
        result_list_bubble = multi_sort_algos.bubble_sort()
        result_list_optimal_bubble = multi_sort_algos.optimal_bubble_sort()
        result_list_general_count = multi_sort_algos.count_sort()
        print(result_list_general_count)
        result_list_heap = multi_sort_algos.heap_sort()
        # result_list_count = multi_sort_algos.count_general_sort()
        algos_time = []
        algos_comp = []
        algos_time.append(result_list_select[1])
        algos_time.append(result_list_insert[1])
        algos_time.append(result_list_merge[1])
        algos_time.append(result_list_bubble[1])
        algos_time.append(result_list_optimal_bubble[1])
        algos_time.append(result_list_general_count[1])
        algos_time.append(result_list_heap[1])

        algos_comp.append(result_list_select[0][1])
        algos_comp.append(result_list_insert[0][1])
        algos_comp.append(result_list_merge[0][1])
        algos_comp.append(result_list_bubble[0][1])
        algos_comp.append(result_list_optimal_bubble[0][1])
        algos_comp.append(result_list_general_count[0][1])
        algos_comp.append(result_list_heap[0][1])

        algos_names = ['Selection', 'Insertion', 'Merge', 'Bubble', 'Optimal Bubble', 'Count', 'Heap']
        multi_algos_df = pd.DataFrame({'Algorithms': algos_names, 'Time': algos_time, 'Comparisons': algos_comp})
        multi_algos_df.to_csv('multi_algos_df.csv')
        slit.table(multi_algos_df)


def selecting_algorithms(arr):
    slit.markdown('***')
    selected_algo = slit.selectbox(
        'Select the Algorithm: ',
        ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal Bubble', 'Counting'])
    slit.markdown('***')
    if slit.button('Sort the Array', key=3):
        slit.markdown('#### Results :see_no_evil:')
        slit.markdown('***')
        if not arr:
            slit.error('Looks like the array is empty')
            return
        sort_alogs = SortingAlgo(arr)
        if selected_algo == 'Selection':
            result_list = sort_alogs.selection_sort()
        elif selected_algo == 'Insertion':
            result_list = sort_alogs.insertion_sort()
        elif selected_algo == 'Merge':
            result_list = sort_alogs.merge_sort()
        elif selected_algo == 'Quick':
            slit.write('Still Under construction!!!')
        elif selected_algo == 'Bubble':
            result_list = sort_alogs.bubble_sort()
        elif selected_algo == 'Optimal Bubble':
            result_list = sort_alogs.optimal_bubble_sort()
        elif selected_algo == 'Counting':
            result_list = sort_alogs.count_sort()
        col1, col2 = slit.columns(2)

        with col1:
            slit.markdown(':point_down: Number of Comparisons are: ')
            slit.write(result_list[0][1])
        with col2:
            slit.markdown(':point_down: Run Time of the Function: (ms)')
            slit.write(result_list[1])
