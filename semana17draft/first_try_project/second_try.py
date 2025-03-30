import FreeSimpleGUI as sg
import json



def get_date_popup(window):
    date = sg.popup_get_date(close_when_chosen=True, no_titlebar=True)
    if date:
        month, day, year = date
        formatted_date = f"{day}-{month}-{year}"
        window['-DATE-'].update(formatted_date)



class jsonData():
    def __init__(self, path='C:/Users/jovan/Documents/GIT/semana17/financial_record.json'):
        self.path = path
        self.data = ''
        self.load_file()

    def load_file(self):
        with open(self.path) as jsf:
            self.data = json.load(jsf)

    def upload_json(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=4)
        self.load_file()


class Layout():
    def __init__(self, title):
        self.title = title
        self.layout = []
        self.json_data = jsonData()
        self.define_layout_type()

    def define_layout_type(self):
        if self.title == 'Main':
            button_one = sg.Button('Add movement', key='-ADDMOVEMENT-')
            button_two = sg.Button('Add category', key='-ADDCATEGORY-')
            table = sg.Table(
            values= self.json_data.data[2], 
            headings=['Expense', 'Amount', 'Category', 'Date'], 
            key='-TABLE-',
            auto_size_columns=True,
            enable_events=True
            )
            button_column = sg.Column([[button_one], [button_two]])
            self.layout = [[sg.Text('Financial Management System')],[table, sg.vtop(button_column)]]
        
        elif self.title == '-ADDMOVEMENT-':
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
                [sg.Combo('', size=25 ,readonly=True, key='-CATEGORY-')]
            ])
            date_column = sg.Column([
                [sg.Text('Select the date: ')],
                [sg.Input(key='-DATE-', size=(25,1), readonly=True ,disabled=False, do_not_clear=False), date_button]
            ])
            self.layout = [
                [sg.Push(),sg.Text('Enter your money movement'), sg.Push()],
                [checkbox_column, expense_column, amount_column, category_column, date_column],
                [sg.Push(), sumbit_button, sg.Push()]
            ]
        elif self.title == '-ADDCATEGORY-':
            outcome_radio = sg.Button('Outcome', key='-OUTCOMEBUTTON-', enable_events=True)
            income_radio = sg.Button('Income', key='-INCOMEBUTTON-', enable_events=True)
            add_category_column = sg.Column([
            [sg.Text('Type the new category: ')],
            [sg.Input('', size=30, key= '-NEWCATEGORY-', enable_events=True)],
            [outcome_radio, income_radio]
            ])
            self.layout = [[add_category_column]]
        else:
            raise ValueError('Layout type not supported')

class Windows():
    def __init__(self, name, layout):
        self.layout = layout.layout
        self.name = name
        self.data = jsonData()
        self.window = sg.Window(self.name, self.layout)

class WindowControler():
    def __init__(self):
        self.window = Windows()
        self.data_controler = DataControler()

    def run_window(self):
        running = True
        while running:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                running = False
            else:
                self.handle_event(event, values)
        self.window.close()

    def handle_event(self, event, values):
        match event:
            case '-ADDMOVEMENT-' | '-ADDCATEGORY-':
                self.open_new_window(event)
            case '-SUBMITMOVEMENT-':
                self.data_controler.form_validation(values)
                self.update_main_table(self.data_controler.submit_movement())
            case '-AMOUNT-':
                self.restrict_new_info_amount(event, values, self.window)
            case '-OUTCOMEBUTTON-'| '-INCOMEBUTTON-':
                self.data_manager.submit_new_category(values, event)
            case '-INCOME-'|'-OUTCOME-':
                self.update_category_option(event)
            case '-GETDATE-':
                get_date_popup(self.window)

    def create_window(self, name, event):
        layout = Layout(event)
        new_window = Windows(name, layout)
        return new_window

    def update_category_option(self, event):
        list_index = 0
        if event == '-INCOME-':
            list_index = 1
        elif event == '-OUTCOME-':
            list_index = 0
        self.window['-CATEGORY-'].update(values=self.json_data.data[list_index])

    def restrict_new_info_amount(self, event, values, window):
        if not values[event].isdigit():
            window[event].update(values[event][:-1])

    def open_new_window(self, event):
        new_window = self.create_window(event, event)
        new_window.run_window()

    def restrict_new_info_amout(self, event, values):
        if event and len(values[event]) and values[event][-1] not in ('0123456789'):
            self.window[event].update(values[event][:-1])

    def reset_values_to_blank(self):
        keys_to_update = ['-EXPENSENAME-', '-AMOUNT-', '-CATEGORY-', '-DATE-']
        for key in keys_to_update:
            self.window[key].update("")

    def update_main_table(self, data):
        data.load_file()
        self.window['-TABLE-'].update(values= data.data[2])


class DataControler():

    def __init__(self, values):
        self.values = values
        self.json_data = jsonData()

    def submit_movement(self, movement):
        if movement:
            self.json_data.load_file()
            self.json_data.data[2].append(movement)
            self.json_data.upload_json()

    def submit_new_category(self, event):
        new_category = self.collect_new_category(self.values)
        if event == '-OUTCOMEBUTTON-' and new_category != None:
            self.outcome_categorys.append(new_category)
        elif event == '-INCOMEBUTTON-' and new_category != None:
            self.outcome_categorys.append(new_category)
        if new_category:
            self.submit_to_json()

    def collect_new_category(self, values):
        if values['-NEWCATEGORY-'].strip() == '':
            raise ValueError('Category name cannot be empty')
        else:
            return values['-NEWCATEGORY-'].upper()

    def collect_money_movement(self, values):
        reason = values['-EXPENSENAME-'].upper()
        amount = values['-AMOUNT-']
        category = values['-CATEGORY-'].upper()
        date = values['-DATE-'].upper()
        return [reason, amount, category, date]

    def form_validation(self, values):
        data = self.collect_money_movement(values)
        if any(values.strip() == '' for values in data):
            raise ValueError('All fields must have a value.')
        else:
            self.json_data.data[2].append(data)
            self.json_data.upload_json()
            return data

class Movement():
    def __init__(self, data_tuple):
        self.reason, self.amount, self.category, self.date = data_tuple
        self.movement = [self.reason, self.amount, self.category, self.date]


def main():
    layout = Layout('Main')
    main_window = Windows('Main', layout)
    main_window.run_window()

if __name__ == "__main__":
    main()
