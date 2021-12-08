import tkinter as tk
import multifactorgui as mfg


username = ""
password = ""

# This while loop will check if the User's username fits all of the requirments given
# Including the right length of characters, if there is a letter in the username, 
# And if there is a number in the username.
while len(username)+ 1 < 8 or len(username) + 1 > 24:
    print(len(username))
