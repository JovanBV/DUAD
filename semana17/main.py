import FreeSimpleGUI as sg
from layout import Layout
from gui import Windows

def main():
    layout = Layout('Main')
    main_window = Windows('Main', layout)
    main_window.run_window()

if __name__ == "__main__":
    main()
