

import FreeSimpleGUI as sg
import main # Assuming main.py is in the same directory and contains the optimization logic


right_click_def = ['hi', ':)', 'test']

# Define the window's contents
layout_start = [[sg.Text('Distributor Order Optimizer'), sg.Radio('Option 1', 'RADIO1', default=True), sg.Radio('Option 2', 'RADIO1')],
          [sg.Multiline('Select an option \nTesting\n', size=(40,10), key='-MLINE-')],
          [sg.Button('Solve'), sg.Button('List'), sg.Button('Quit')]]


sg.theme('dark purple 6') #i also like dark green 1


# Create the window
window = sg.Window('Window Title', layout_start, right_click_menu=right_click_def)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Solve':
        solution = main.main()
        sg.popup(f"Solution: {solution[0]}\nProfit: ${round(solution[1],2)}")
        layout_start = [[sg.Text(solution), sg.Text(size=(15,1))],
            [sg.Button('Quit')]]

    if event == 'List':
        pass


# Finish up by removing from the screen
window.close()    