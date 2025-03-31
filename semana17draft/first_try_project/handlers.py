import FreeSimpleGUI as sg


def reset_values_to_blank(window):
    keys_to_update = ['-EXPENSENAME-', '-AMOUNT-', '-CATEGORY-', '-DATE-']
    for key in keys_to_update:
        window[key].update("")

def update_main_table(window, data):
    data.load_file()
    window['-TABLE-'].update(values= data.data[2])

def get_date_popup(window):
    date = sg.popup_get_date(close_when_chosen=True, no_titlebar=True)
    if date:
        month, day, year = date
        formatted_date = f"{day}-{month}-{year}"
        window['-DATE-'].update(formatted_date)

def collect_new_category(values, window):
    if values['-NEWCATEGORY-'].strip() == '':
        sg.popup('Category name cannot be empty')
        return None
    else:
        window['-NEWCATEGORY-'].update(value='')
        return values['-NEWCATEGORY-'].upper()

def collect_money_movement(values):
    reason = values['-EXPENSENAME-'].upper()
    amount = values['-AMOUNT-']
    category = values['-CATEGORY-'].upper()
    date = values['-DATE-'].upper()
    data = [reason, amount, category, date]
    return data

def form_validation(values):
    data = collect_money_movement(values)
    if any(values.strip() == '' for values in data) :
        sg.popup('All fields must have a value')
        return None
    else:
        amount = int(data[1] )
        data[1] = amount
    return data

def restrict_new_info_amout(event, values, window):
    if event and len(values[event]) and values[event][-1] not in ('0123456789'):
        window[event].update(values[event][:-1])