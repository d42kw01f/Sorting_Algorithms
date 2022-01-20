import pandas as pd
import streamlit as slit
import re
import random
from Sort_Algos import SortingAlgo


def page_introduction():
    slit.header('CSP2348 Data Structures')
    slit.title('- Implementation and Analysis -')
    slit.markdown('***')

    slit.header('About Me :wave:')
    slit.write('')
    slit.markdown(':point_right:   **Name: **Dakshitha Perera')
    slit.markdown(':point_right:   ** ECU ID: **10519381')
    slit.markdown(':point_right:   ** ECU EMAIL: **pdakshi@our.ecu.edu.au')
    slit.markdown('***')


def main_menu():
    # try:
    slit.header('Let\'s do a test, shall we: :seedling:')
    with slit.expander('Test an individual sorting algorithm'):
        the_array = choice_arr(0)
        slit.write(the_array)
        selecting_algorithms(the_array)

    with slit.expander('Test multiple sorting algorithms'):
        the_array = choice_arr(1)
        slit.write(the_array)
        running_all_algorithms(the_array)

    # except:
    #     slit.error('#### Opps looks like a some kind of bug here.')
    #     slit.markdown('#### :confounded:Could you please check the way you ran is right. Cuz it worked fine with my computer.')
    #     slit.markdown('![Bug Meme](https://gorilla.sc/wp-content/uploads/2021/05/Debugging-is-a-Science.png)')


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


def choice_arr(the_key):
    slit.markdown('***')
    arr_choice = slit.radio('What about the array',
                            ('I Will Enter a One', 'Generate Random a One'), key=the_key)
    if arr_choice == 'I Will Enter a One':
        collect_numbers = lambda x: [int(i) for i in re.split("[^0-9]", x) if i != ""]
        input_number = slit.text_input('Enter the comma separated array Ex: 1, 2, 3 ', key=the_key)
        the_arr = collect_numbers(input_number)
        return the_arr
    else:
        arr_elem = slit.number_input('How many elements should be in the array: ', min_value=1, max_value=1000, value=20,
                                     step=1)
        the_arr = [round(random.uniform(-1000000, 1000000)) for _ in range(arr_elem)]
        return the_arr


def main():
    page_introduction()
    main_menu()


if __name__ == '__main__':
    main()
