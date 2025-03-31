from layout import Layout, Window
from controllers import WindowController

def main():
    main_layout = Layout('Main')
    main_window = Window('Main', main_layout.layout, finalize=True) 
    window_controler = WindowController(main_window)
    window_controler.run_main_window()

main()