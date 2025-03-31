from json_data import JsonData
import FreeSimpleGUI as sg

#--------------------Controladores de interfaz--------------------
class Window:
    def __init__(self, name, window_layout, finalize=True):
        self.layout = window_layout
        self.name = name
        self.window = sg.Window(self.name, self.layout)

class Layout:
    def __init__(self, name):
        self.name = name
        self.layout = []
        self.json_data = JsonData() 
        self.json_data.load_file()
        self.define_layout()

    def define_layout(self):
        if self.name == 'Main':
            movements = self.json_data.data.get('movements', [])
            
            table_values = [
                [movement['reason'], movement['amount'], movement['category'], movement['date']] 
                for movement in movements
            ]
            
            table = sg.Table(
                values=table_values, 
                headings=['Expense', 'Amount', 'Category', 'Date'], 
                key='-TABLE-', 
                auto_size_columns=True, 
                enable_events=True
            )
            
            button_one = sg.Button('Add movement', key='-ADDMOVEMENT-')
            button_two = sg.Button('Add category', key='-ADDCATEGORY-')
            button_column = sg.Column([[button_one], [button_two]])
            self.layout = [[sg.Text('Financial Management System')],[table, sg.vtop(button_column)]]

        elif self.name == '-ADDMOVEMENT-':
            date_button = sg.Button('>', key='-GETDATE-')
            submit_button = sg.Button('Submit', key='-SUBMITMOVEMENT-', size=25)
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
                [sg.Combo('' ,size=(25,1) ,readonly=True, default_value='', key='-CATEGORY-')]
            ])
            
            date_column = sg.Column([
                [sg.Text('Select the date: ')],
                [sg.Input(key='-DATE-', size=(25,1), readonly=True, disabled=False, do_not_clear=False), date_button]
            ])
            
            self.layout = [
                [sg.Push(),sg.Text('Enter your money movement'), sg.Push()],
                [checkbox_column, expense_column, amount_column, category_column, date_column],
                [sg.Push(), submit_button, sg.Push()]
            ]
        
        elif self.name == '-ADDCATEGORY-':
            outcome_radio = sg.Button('Outcome', key='-OUTCOMEBUTTON-', enable_events=True)
            income_radio = sg.Button('Income', key='-INCOMEBUTTON-', enable_events=True)
            
            add_category_column = sg.Column([
                [sg.Text('Type the new category: ')],
                [sg.Input('', size=30, key='-NEWCATEGORY-', enable_events=True)],
                [outcome_radio, income_radio]
            ])
            
            self.layout = [[add_category_column]]
        else:
            raise ValueError('Layout type not supported')