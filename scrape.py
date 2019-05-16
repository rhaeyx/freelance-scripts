import pyautogui as pygui
import time
import pyperclip
import re
from datetime import datetime

# These phrase or words should be in the search
constants = '"@gmail.com" "tx"'

# Filename
filename = input('Enter a file name:')

business = ['orthodontist']
cities = ['Fort Worth', 'Arlington', 'Corpus Christi', 'Plano', 'Laredo', 'Lubbock', 'Garland', 'Irving', 'Amarillo', 'Grand Prairie', 'Brownsville', 'McKinney', 'Frisco', 'Pasadena', 'Mesquite', 'Killeen', 'McAllen', 'Carrollton', 'Midland', 'Waco', 'Denton', 'Abilene', 'Odessa', 'Beaumont', 'Round Rock',
          'The Woodlands', 'Richardson', 'Pearland', 'College Station', 'Wichita Falls', 'Lewisville', 'Tyler', 'San Angelo', 'League City', 'Allen', 'Sugar Land', 'Edinburg', 'Mission', 'Longview', 'Bryan', 'Pharr', 'Baytown', 'Missouri City', 'Temple', 'Flower Mound', 'New Braunfels', 'North Richland Hills', 'Conroe', 'Victoria', 'Cedar Park', 'Harlingen', 'Atascocita', 'Mansfield', 'Georgetown', 'San Marcos', 'Rowlett', 'Pflugerville', 'Port Arthur', 'Spring', 'Euless', 'DeSoto', 'Grapevine', 'Galveston']

def query(q):
    pygui.hotkey('ctrl','l')
    pygui.typewrite(q)
    pygui.typewrite('\n')

def take_data():
    pygui.hotkey('ctrl', 'a')
    pygui.hotkey('ctrl', 'c')
    data = pyperclip.paste()
    email_regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    emails = re.findall(email_regex, data)
    print(len(emails), 'emails found.') 
    with open(filename, 'a') as f:
        for email in emails:
            f.write(email + '\n')

def page_loaded():
    try:
        pygui.locateOnScreen('google.png') 
        return True
    except:           
        return False

input("Enter to start...")
print("Starting in 3 secs...")
time.sleep(3)

with open(filename, 'w') as f:
    f.write(constants + '\n')

for b in business:
    for city in cities:
        q = f"{city} {b} {constants}"
        print(q)
        query(q)
        time.sleep(3)
        if not page_loaded():
            input("Enter to continue...\nSolve the captcha...")
            time.sleep(2)
        take_data()
        time.sleep(3)
