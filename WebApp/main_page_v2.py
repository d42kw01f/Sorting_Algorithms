import csv

import pandas as pd
import streamlit as slit
import re
import random
from Sort_Algos import SortingAlgo
import data_visualization
import run_algos


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
    try:
        slit.header('Let\'s do a test, shall we: :seedling:')
        with slit.expander('Test an individual sorting algorithm'):
            the_array = choice_arr(0)
            slit.write(the_array)
            run_algos.selecting_algorithms(the_array)

        with slit.expander('Test multiple sorting algorithms'):
            the_array = choice_arr(1)
            slit.write(the_array)
            multi_df = run_algos.running_all_algorithms(the_array)
            return multi_df

    except:
        slit.error('#### Opps looks like a some kind of bug here.')
        slit.markdown('#### :confounded:Could you please check the way you ran is right. Cuz it worked fine with my computer.')
        slit.markdown('![Bug Meme](https://gorilla.sc/wp-content/uploads/2021/05/Debugging-is-a-Science.png)')


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
        arr_elem = slit.number_input('How many elements should be in the array ', min_value=1, max_value=1000, value=20, step=1, key='multi-number')
        the_arr = [round(random.uniform(-10, 100)) for _ in range(arr_elem)]
        return the_arr


def main():
    page_introduction()
    main_menu()
    slit.markdown('***')
    data_visualization.data_head()


if __name__ == '__main__':
    main()
