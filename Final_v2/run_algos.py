import streamlit as slit
import pandas as pd
from Sort_Algos import SortingAlgo


def unique_values(g):
    s = set()
    for x in g:
        if x in s:
            return False
        s.add(x)
    return True


def running_all_algorithms(arr):
    if slit.button('Sort the Array', key=2):
        slit.markdown('#### Results :see_no_evil:')
        slit.markdown('***')
        if not arr:
            slit.error('Looks like the array is empty')
            return
        unique_elem = unique_values(arr)
        if not unique_elem:
            slit.warning('WARNING: The Array includes some duplicate elements. Thus, No Counting Sort Algorithm !!!')
        multi_sort_algos = SortingAlgo(arr)
        result_list_select = multi_sort_algos.selection_sort()
        result_list_insert = multi_sort_algos.insertion_sort()
        result_list_merge = multi_sort_algos.merge_sort()
        result_list_quick = multi_sort_algos.quick_sort()
        result_list_bubble = multi_sort_algos.bubble_sort()
        result_list_optimal_bubble = multi_sort_algos.optimal_bubble_sort()
        if unique_elem == True:
            result_list_count = multi_sort_algos.count_sort()
        result_list_heap = multi_sort_algos.heap_sort()
        result_list_general_count = multi_sort_algos.general_count_sort()

        algos_time = []
        algos_comp = []
        arr_size = []

        algos_time.append(result_list_select[1])
        algos_time.append(result_list_insert[1])
        algos_time.append(result_list_merge[1])
        algos_time.append(result_list_quick[1])
        algos_time.append(result_list_bubble[1])
        algos_time.append(result_list_optimal_bubble[1])
        if unique_elem:
            algos_time.append(result_list_count[1])
        algos_time.append(result_list_general_count[1])
        algos_time.append(result_list_heap[1])

        algos_comp.append(result_list_select[0][1])
        algos_comp.append(result_list_insert[0][1])
        algos_comp.append(result_list_merge[0][1])
        algos_comp.append(result_list_quick[0][1])
        algos_comp.append(result_list_bubble[0][1])
        algos_comp.append(result_list_optimal_bubble[0][1])
        if unique_elem:
            algos_comp.append(result_list_count[0][1])
        algos_comp.append(result_list_general_count[0][1])
        algos_comp.append(result_list_heap[0][1])

        # Not really sure why this is needed. Asked for it. And did it. :|
        arr_size.append(len(result_list_select[0][0]))
        arr_size.append(len(result_list_insert[0][0]))
        arr_size.append(len(result_list_merge[0][0]))
        arr_size.append(len(result_list_quick[0][0]))
        arr_size.append(len(result_list_bubble[0][0]))
        arr_size.append(len(result_list_optimal_bubble[0][0]))
        if unique_elem:
            arr_size.append(len(result_list_count[0][0]))
        arr_size.append(len(result_list_general_count[0][0]))
        arr_size.append(len(result_list_heap[0][0]))

        if unique_elem:
            algos_names = ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal Bubble', 'Counting',
                           'General-Counting', 'Heap']
        else:
            algos_names = ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal Bubble',
                           'General-Counting', 'Heap']
        print(algos_names, arr_size, algos_time, algos_comp)
        multi_algos_df = pd.DataFrame(
            {'Algorithms': algos_names, 'Array Size': arr_size, 'Time': algos_time, 'Comparisons': algos_comp})
        multi_algos_df.to_csv('multi_algos_df.csv')
        if result_list_select[0][0] == result_list_insert[0][0] == result_list_merge[0][0] == result_list_quick[0][0] == result_list_bubble[0][0] == result_list_optimal_bubble[0][0]:
            slit.success('Everything went well')
            slit.table(multi_algos_df)
            slit.text('Sorted Array: ')
            slit.write(result_list_bubble[0][0])
        else:
            slit.error('Hmm! Something went wrong while sorting.')
            slit.write(result_list_select[0][0],result_list_insert[0][0],result_list_merge[0][0],result_list_quick[0][0],result_list_bubble[0][0],result_list_optimal_bubble[0][0])


def selecting_algorithms(arr):
    slit.markdown('***')
    selected_algo = slit.selectbox(
        'Select the Algorithm: ',
        ['Selection', 'Insertion', 'Merge', 'Quick', 'Bubble', 'Optimal-Bubble', 'Counting', 'General-Counting'])
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
            result_list = sort_alogs.quick_sort()
        elif selected_algo == 'Bubble':
            result_list = sort_alogs.bubble_sort()
        elif selected_algo == 'Optimal-Bubble':
            result_list = sort_alogs.optimal_bubble_sort()
        elif selected_algo == 'Counting':
            unique_elem = unique_values(arr)
            if not unique_elem:
                slit.warning(
                    'WARNING: The Array includes some duplicate elements. Thus, No Counting Sort Algorithm !!!')
                return
            result_list = sort_alogs.count_sort()
        elif selected_algo == 'General-Counting':
            result_list = sort_alogs.general_count_sort()

        col1, col2 = slit.columns(2)

        with col1:
            slit.markdown(':point_down: Number of Comparisons are: ')
            slit.write(result_list[0][1])
        with col2:
            slit.markdown(':point_down: Run Time of the Function: (ms)')
            slit.write(result_list[1])
        slit.text('Sorted Array: ')
        slit.write(result_list[0][0])
