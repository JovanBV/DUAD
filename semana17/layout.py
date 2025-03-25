import FreeSimpleGUI as sg
from data_manager import jsonData

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
