import FreeSimpleGUI as sg
import json

# ------------------------ Main Window ------------------------
def create_main_window():
    button_one = sg.Button('Add movement', key='-ADDMOVEMENT-')
    button_two = sg.Button('Add category', key='-ADDCATEGORY-')
    
    table = sg.Table(   #Aqui deberia ser el destino de la informacion para la tabla
        '', 
        headings=['Expense', 'Amount', 'Category', 'Date'], 
        max_col_width=10, 
        key='-TABLE-'
    )

    button_column = sg.Column([[button_one], [button_two]])

    layout = [[sg.Text('Financial Management System')],[table, sg.vtop(button_column)]]

    window = sg.Window('Financial record', layout)
    run_window(window)

# ------------------------ Secondary Windows ------------------------
def create_secondary_window(name, layout):
    window = sg.Window(name, layout)
    run_window(window)

def create_money_movement_window():
    date_button = sg.Button('>', key='-GETDATE-')
    sumbit_button = sg.Button('Submit', key='-SUBMITMOVEMENT-', size=25)

    expense_column = sg.Column([
        [sg.Text('Expense name: ')],
        [sg.Input(key='-EXPENSENAME-', size=25)]
    ])
    
    amount_column = sg.Column([
        [sg.Text('Type the amount: ')],
        [sg.Input(key='-AMOUNT-', size=25)]
    ])

    category_column = sg.Column([
        [sg.Text('Select the category: ')],
        [sg.Combo('', s=25, enable_events=False, key='-CATEGORY-')]
    ])

    date_column = sg.Column([
        [sg.Text('Select the date: ')],
        [sg.Input(key='-DATE-', size=25, readonly=True), date_button]
    ])

    return [
        [expense_column, amount_column, category_column, date_column],
        [sg.Push(), sumbit_button, sg.Push()]
    ]

def create_add_category_window():
    submit_button = sg.Button('Submit category', size=25, key='-SUBMITCATEGORY-')
    
    add_category_column = sg.Column([
        [sg.Text('Type the new category: ')],
        [sg.Input('', size=30)],
        [submit_button]
    ])

    return [[add_category_column]]

# ------------------------ Functionalities ------------------------
def submit_money_movement():
    # Aquí debería agregarse la función para enviar la info a la tabla y JSON
    # También la verificación de si la categoría existe antes de enviarla
    sg.popup("Movement submitted")

def submit_category():
    # Aquí debería agregarse la función para enviar la categoría a la lista
    sg.popup('Category added')

def get_date_popup(window):
    date = sg.popup_get_date(close_when_chosen=True, no_titlebar=True)
    
    if date:
        month, day, year = date
        formatted_date = f"{day}-{month}-{year}"
        window['-DATE-'].update(formatted_date)

# ------------------------ Event Loop ------------------------
def run_window(window):
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == '-ADDMOVEMENT-':
            layout = create_money_movement_window()
            create_secondary_window('Add movement', layout)
        elif event == '-ADDCATEGORY-':
            layout = create_add_category_window()
            create_secondary_window('Add category', layout)
        elif event == '-GETDATE-':
            get_date_popup(window)
        elif event == '-SUBMITMOVEMENT-':
            submit_money_movement()
            break
        elif event == '-SUBMITCATEGORY-':
            submit_category()
            break

    window.close()

# ------------------------ JSON functions ------------------------
def load_file(path):
    with open(path) as jf:
        json_data = json.load(jf)




# ------------------------ Main Execution ------------------------
def main():
    path = 'C:/Users/jovan/Documents/GIT/semana17/financial_record.json'
    load_file(path)
    create_main_window()
    

if __name__ == "__main__":
    main()
