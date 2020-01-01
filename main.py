#!/usr/bin/env python3
import .userInput.py as user
import .beam.py as beam 

mainMenu()

while True:
    if selection == 1:
        addLoad()
    elif selection == 2:
        addSup()
    elif selection == 3:
        compute()
        break
    else:
        print("Invalid selection")
        mainMenu()
