import FreeSimpleGUI as sg
import json

# ------------------------ Main Window ------------------------
def create_main_window():
    button_one = sg.Button('Add movement', key='-ADDMOVEMENT-')
    button_two = sg.Button('Add category', key='-ADDCATEGORY-')
    
    data = load_file()

    table = sg.Table(
        values=data[2], 
        headings=['Expense', 'Amount', 'Category', 'Date'], 
        key='-TABLE-',
        auto_size_columns=True,
        enable_events=True
    )

    button_column = sg.Column([[button_one], [button_two]])
    layout = [[sg.Text('Financial Management System')],[table, sg.vtop(button_column)]]
    window = sg.Window('Financial record', layout)
    return window
# ------------------------ Secondary Windows ------------------------
def create_secondary_window(name, layout):
    window = sg.Window(name, layout)
    run_window(window)



def create_add_movement_window():
    date_button = sg.Button('>', key='-GETDATE-')
    sumbit_button = sg.Button('Submit', key='-SUBMITMOVEMENT-', size=25)

    income_radio = sg.Radio('Income', key='-INCOME-', group_id=1, enable_events=True)
    outcome_radio = sg.Radio('Outcome', key='-OUTCOME-', group_id=1, enable_events=True)

    checkbox_column = sg.Column([
        [income_radio],
        [outcome_radio]
    ])

    expense_column = sg.Column([
        [sg.Text('Reason: ')],
        [sg.Input(key='-EXPENSENAME-', size=25)]
    ])
    
    amount_column = sg.Column([
        [sg.Text('Type the amount: ')],
        [sg.Input(key='-AMOUNT-', size=25, enable_events=True)]
    ])

    category_column = sg.Column([
        [sg.Text('Select the category: ')],
        [sg.Combo('', size=25 ,readonly=True, bind_return_key=True, expand_x=True, key='-CATEGORY-')]
    ])

    date_column = sg.Column([
        [sg.Text('Select the date: ')],
        [sg.Input(key='-DATE-', size=(25,1), readonly=True ,disabled=False, do_not_clear=False), date_button]
    ])

    return [
        [sg.Push(),sg.Text('Enter your money movement'), sg.Push()],
        [checkbox_column, expense_column, amount_column, category_column, date_column],
        [sg.Push(), sumbit_button, sg.Push()]
    ]


def validate_int_input(window, event, values):
    if event and len(values[event]) and values[event][-1] not in ('0123456789'):
        window[event].update(values[event][:-1])


def update_category_list_for_money_movement(event, window):
    current_data = load_file()
    if event == '-INCOME-':
        window['-CATEGORY-'].update(values = current_data[1])
    elif event == '-OUTCOME-':
        window['-CATEGORY-'].update(values = current_data[0])


def create_add_category_window():
    outcome_radio = sg.Radio('Outcome', group_id=2, key='-OUTCOMERADIO-', enable_events=True)
    income_radio = sg.Radio('Income', group_id=2, key='-INCOMERADIO-', enable_events=True)
    add_category_column = sg.Column([
        [sg.Text('Type the new category: ')],
        [sg.Input('', size=30, key= '-NEWCATEGORY-', enable_events=True)],
        [outcome_radio, income_radio]
    ])
    return [[add_category_column]]

# ------------------------ Functionalities ------------------------
def submit_money_movement(values):
    data = load_file()

    new_movement = collect_money_movement(values)

    if '' in new_movement:
        sg.popup('All cells must have a value to be submited')
    else:
        new_movement[1] = int(new_movement[1])
        data[2].append(new_movement)
        upload_json(data)
        sg.popup("Movement submitted")


def update_main_table(window):
    updated_data = load_file()
    window['-TABLE-'].update(values=updated_data[2])


def collect_money_movement(values):
    reason = values['-EXPENSENAME-'].upper()
    amount = values['-AMOUNT-']
    category = values['-CATEGORY-'].upper()
    date = values['-DATE-'].upper()
    data = [reason, amount, category, date]
    return data


def submit_category(values, location, window):
    new_categorie = values['-NEWCATEGORY-'].upper()
    data = load_file()
    if new_categorie == '':
        reset_radio_values(window)
        sg.popup('Type category before selecting Outcome or Income')
    else:
        if new_categorie not in data[location]:
            upload_new_category(new_categorie, location, window)
        else:
            sg.popup('That category already exists')


def reset_radio_values(window):
    window['-INCOMERADIO-'].update(value=False)
    window['-OUTCOMERADIO-'].update(value=False)

def upload_new_category(new_categorie, location, window=None):
    data = load_file()
    data[location].append(new_categorie.upper())
    upload_json(data)
    if new_categorie != '':
        window['-NEWCATEGORY-'].update(value = '')
        reset_radio_values(window)
        sg.popup(f'Category uploaded')


def get_date_popup(window):
    date = sg.popup_get_date(close_when_chosen=True, no_titlebar=True)
    if date:
        month, day, year = date
        formatted_date = f"{day}-{month}-{year}"
        window['-DATE-'].update(formatted_date)


# ------------------------ Event Loop ------------------------
# podria ser que ocupe un run window por ventana


def run_window(window):
    running = True
    while running:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            running = False
        elif event == '-ADDMOVEMENT-':
            layout = create_add_movement_window()
            create_secondary_window('Add movement', layout)
            update_main_table(window)
        elif event == '-ADDCATEGORY-':
            layout = create_add_category_window()
            create_secondary_window('Add category', layout)
        elif event == '-GETDATE-':
            get_date_popup(window)
        elif event == '-SUBMITMOVEMENT-':
            submit_money_movement(values)
            break
        elif event in ['-INCOME-', '-OUTCOME-']:
            update_category_list_for_money_movement(event, window)
        elif event == '-OUTCOMERADIO-':
            submit_category(values, 0, window)
        elif event == '-INCOMERADIO-':
            submit_category(values, 1, window)
        elif event == '-AMOUNT-':
            validate_int_input(window, event, values)
    window.close()

# ------------------------ JSON functions ------------------------
def load_file():
    path = 'C:/Users/jovan/Documents/GIT/semana17/financial_record.json'
    with open(path) as jf:
        json_data = json.load(jf)
    return json_data

def upload_json(data):
    path = 'C:/Users/jovan/Documents/GIT/semana17/financial_record.json'
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

# ------------------------ Main Execution ------------------------
def main():
    load_file()
    main_window = create_main_window()
    run_window(main_window)

if __name__ == "__main__":
    main()
