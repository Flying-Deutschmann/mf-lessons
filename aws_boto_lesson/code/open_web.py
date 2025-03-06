#! /usr/bin/env python3
# ^ Shebang, sepcifies the interpreter, allows for direct exuting without specifying interpreter

# Python modules imported through the package manager pip
import webbrowser
import pyautogui
import time

def open_edge_and_print_hello_world(user_name):
    """
    Function to open Microsoft Edge and type 'Hello World'
    """
    # Local variable, locally available to function
    web_address = 'https://www.bing.com'
    
    # Opens Microsoft Edge and loads a website
    webbrowser.get('windows-default').open(web_address)

    # You can adjust the sleep time if necessary to make sure the browser is loaded
    time.sleep(3)
    
    # This will type the text into the currently focused input field
    pyautogui.write(f'Hello, ')
    
    # Run page execution
    pyautogui.press('enter')
    
    # Returns an error code or other type, used in methods and functions
    return 0


# A conditional statement to verifiy script is called directly or imported as module
if __name__ == '__main__':
    # Global variable, globally available
    user_name = input('Please enter name: ')
    
    # Run the function
    open_edge_and_print_hello_world(user_name)
    
    # Print output to terminal
    print(f'Thank you ${user_name}')
