

import FreeSimpleGUI as sg
import main # Assuming main.py is in the same directory and contains the optimization logic
import data_parse

right_click_def = ['hi', ':)', 'test']
websites_data = data_parse.get_websites() #pulls current websites from data_parse file
websites_list = ''
for value in websites_data.values(): #pulls specifically the website urls 
    websites_list += f"{value}\n"

# Define the window's contents
layout_start = [[sg.Text('Distributor Order Optimizer')],
          [sg.Multiline(websites_list, size=(40,10), key='-MLINE-')],
          [sg.Button('Solve'), sg.Button('Add'), sg.Button('Remove'),sg.Button('Quit')]]


sg.theme('dark purple 6') #i also like dark green 1 #user can change theme later


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
        #I want to also add it so that when you hit solve it will 
        #ask the user if they want to filter specific products or categories
        #and then it will only show those products in the solution
        #maybe a popup with a checklist of categories/products?


    if event == 'List':
        pass


# Finish up by removing from the screen
window.close()    