from main_classes import MoneyMovement, NewCategory
from json_data import JsonData
from layout import Layout, Window
import FreeSimpleGUI as sg

# --------------------Controlador de datos--------------------

class DataController:
    def __init__(self, data):
        self.data = data
        self.json_data = JsonData()
        self.json_data.load_file()

    # --------------------Métodos de validación y creación--------------------
    def validate_correct_input(self):
        values = [
            self.data['-EXPENSENAME-'], 
            self.data['-AMOUNT-'], 
            self.data['-CATEGORY-'], 
            self.data['-DATE-']
        ]
        for v in values:
            if v.strip() == '':
                return 'cells on blank'
            elif v == values[1]:
                self.data['-AMOUNT-'] = int(values[1])

    def create_movement(self):
        if self.validate_correct_input() != 'cells on blank':
            new_money_movement = MoneyMovement(
                self.data['-EXPENSENAME-'], 
                self.data['-AMOUNT-'], 
                self.data['-CATEGORY-'], 
                self.data['-DATE-']
            )
            return new_money_movement.to_dict()
        else:
            return 'cells on blank'

    def append_new_money_movement_to_json(self, new_money_movement):
        self.json_data.data['movements'].append(new_money_movement)
        self.json_data.upload_json()

    # --------------------Métodos de categorías--------------------
    def create_new_category(self, list_val):
        new_category = NewCategory(self.data['-NEWCATEGORY-'], list_val)
        return new_category.to_dict()
    
    def append_new_category_to_json(self, new_category):
        self.json_data.data[new_category["category"]].append(new_category["name"])
        self.json_data.upload_json()

    # --------------------Métodos de recuperación de datos--------------------
    def return_category(self, category):
        if category == '-INCOME-':
            return self.json_data.data['income category']
        elif category == '-OUTCOME-':
            return self.json_data.data['outcome category']
        
    def return_table_data(self):
        return self.json_data.data['movements']
    
    def return_movements_list(self):
        self.json_data.load_file()
        movements_data = self.return_table_data()
        return [
            [movement['reason'], movement['amount'], movement['category'], movement['date']]
            for movement in movements_data
        ]

#--------------------Controlador de ventanas--------------------

class WindowController:

    def __init__(self, window):
        self.window = window
        self.data_controller = DataController({})
        self.data = self.data_controller.return_movements_list()

    #--------------------Ejecución de ventanas--------------------
    def run_main_window(self):
        running = True
        while running:
            event, values = self.window.window.read()
            
            if event == sg.WIN_CLOSED:
                running = False
            else:
                self.handle_events_main_window(event, values)
        self.window.window.close()

    def run_secondary_window(self, window):
        running = True
        while running:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                running = False
            else:
                self.handle_secondary_window_events(event, values, window)
        window.close()

    #--------------------Creación de ventanas--------------------
    def create_new_window(self, name):
        new_window_layout = Layout(name)
        new_window = Window(name, new_window_layout.layout)
        return new_window

    #--------------------Manejo de eventos--------------------
    def handle_events_main_window(self, event, values):
        if not self.data_controller:
            self.data_controller = DataController(values)
        match event:
            case '-TABLE-':
                self.update_main_table()
            case '-ADDMOVEMENT-':
                add_movement_window = self.create_new_window('-ADDMOVEMENT-')
                self.run_secondary_window(add_movement_window.window)
                self.update_main_table()
            case '-ADDCATEGORY-':
                add_category_window = self.create_new_window('-ADDCATEGORY-')
                self.run_secondary_window(add_category_window.window)

    #--------------------Métodos de actualizacion--------------------
    def update_main_table(self):
        self.data = self.data_controller.return_movements_list()
        self.window.window['-TABLE-'].update(values=self.data)

    def update_category_list(self, window, event, category):
        updated_category = self.data_controller.return_category(category)
        window[event].update(values=updated_category)

    #--------------------Métodos de popup--------------------
    def warning_pop_up(self):
        return sg.popup('All fields must have a value.')

    def category_error_pop_up(self):
        return sg.popup('Cell in blank or already exists')

    #--------------------Método de validacion--------------------
    def validate_new_category(self, key):
        data = self.data_controller.data['-NEWCATEGORY-'].strip()
        category_list = self.data_controller.json_data.data[key]
        if data != '' and data not in category_list:
            return True
        else:
            self.category_error_pop_up()
            return False

    def create_full_movement(self, window):
        new_movement = self.data_controller.create_movement()
        if new_movement != 'cells on blank':
            self.data_controller.append_new_money_movement_to_json(new_movement)
            self.turn_cells_to_blank(window, '','-AMOUNT-', '-DATE-', '-EXPENSENAME-', '-CATEGORY-')
            self.create_submit_popup()
        else:
            self.warning_pop_up()

    def create_full_category(self, window, key):
        new_category = self.data_controller.create_new_category(key)
        is_valid = self.validate_new_category(key)
        if is_valid:
            self.data_controller.append_new_category_to_json(new_category)
            self.turn_cells_to_blank(window, '', '-NEWCATEGORY-')

    def create_submit_popup(self):
        return sg.popup('Movement submited succesfully')

    #--------------------Eventos de ventana secundaria--------------------
    def handle_secondary_window_events(self, event, values, window):
            self.data_controller = DataController(values)
            match event:
                case '-OUTCOME-':
                    self.update_category_list(window, '-CATEGORY-', '-OUTCOME-')
                case '-INCOME-':
                    self.update_category_list(window, '-CATEGORY-', '-INCOME-')
                case '-SUBMITMOVEMENT-':
                    self.create_full_movement(window)
                case '-INCOMEBUTTON-':
                    self.create_full_category(window, 'income category')
                case '-OUTCOMEBUTTON-':
                    self.create_full_category(window, 'outcome category')
                case '-AMOUNT-':
                    self.restrict_string_values_on_input(window, values, '-AMOUNT-')
                case '-GETDATE-':
                    self.get_date_popup(window)

    #--------------------Métodos auxiliares--------------------
    def get_date_popup(self, window):
        date = sg.popup_get_date(close_when_chosen=True, no_titlebar=True)
        if date:
            month, day, year = date
            formatted_date = f"{day}-{month}-{year}"
            window['-DATE-'].update(formatted_date)

    def restrict_string_values_on_input(self, window, values, event):
        if not values[event].isdigit():
            window[event].update(values[event][:-1])

    def turn_cells_to_blank(self, window, new_value, *args):
        for event in args:
            window[event].update(value= new_value)