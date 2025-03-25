from data_manager import jsonData
import FreeSimpleGUI as sg
from handlers import get_date_popup, update_main_table, form_validation, reset_values_to_blank, collect_new_category
from layout import Layout


class Windows():

    def __init__(self, name, layout):
        self.layout = layout.layout
        self.name = name
        self.json_data = jsonData()
        self.window = sg.Window(self.name, self.layout)

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
                self.submit_movement(values)
            case '-AMOUNT-':
                self.restrict_new_info_amount(event, values, self.window)
            case '-OUTCOMEBUTTON-'| '-INCOMEBUTTON-':
                self.submit_new_category(values, event)
            case '-INCOME-'|'-OUTCOME-':
                self.update_category_option(event)
            case '-GETDATE-':
                get_date_popup(self.window)

    def open_new_window(self, event):
        new_window = self.create_window(event, event)
        new_window.run_window()
        update_main_table(self.window, self.json_data)

    def submit_movement(self, values):
        validated_data = form_validation(values)
        if validated_data:
            self.json_data.data[2].append(validated_data)
            self.json_data.upload_json()
            reset_values_to_blank(self.window)
            sg.popup('Movement submited')

    def restrict_new_info_amount(self, event, values, window):
        if not values[event].isdigit():
            window[event].update(values[event][:-1])

    def submit_new_category(self, values, event):
        list_index = 0
        if event == '-OUTCOMEBUTTON-':
            list_index = 0
        elif event == '-INCOMEBUTTON-':
            list_index = 1
        new_category = collect_new_category(values, self.window)
        if new_category:
            self.json_data.data[list_index].append(new_category)
            self.json_data.upload_json()
            sg.popup('Category submitet')

    def update_category_option(self, event):
        list_index = 0
        if event == '-INCOME-':
            list_index = 1
        elif event == '-OUTCOME-':
            list_index = 0
        self.window['-CATEGORY-'].update(values=self.json_data.data[list_index])

    def create_window(self, name, event):
        layout = Layout(event)
        new_window = Windows(name, layout)
        return new_window
