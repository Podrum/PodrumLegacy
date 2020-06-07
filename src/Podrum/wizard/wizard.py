"""
*  ____           _                      
* |  _ \ ___   __| |_ __ _   _ _ __ ___  
* | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
from ..wizard import parser
from ..lang import base
from ..utils import fs

license = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

logo = """
    ____           _                      
   |  _ \ ___   __| |_ __ _   _ _ __ ___  
   | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
   |  __/ (_) | (_| | |  | |_| | | | | | |
   |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
   """

#Lang, MOTD, max players, gamemode
options = []

isInWizard = True

text = "- "

def wizard(path):
    step = 0
    while step >= 0 and step < 6:
        if(step == 0):
            print(logo)
            print(">- Podrum - Wizard -<\n\n")
            print("Do you want to follow the setup? [y/n]:")
            userInput = input(text)
            if parser.checkYesNo(userInput) == True:
                step += 1
            elif parser.checkYesNo(userInput) == False:
                print("Skipping the setup wizard...")
                skipWizard(path)
                break
            elif parser.checkYesNo(userInput) == None:
                print("Please, write yes (y) or no (n).")
        if(step == 1):
            print("Please, select a language:")
            base.getLangFiles(path)
            userInput = input(text)
            if parser.checkIfLangExists(userInput) == True:
                options.append(userInput)
                print(base.get("langSelectedAsBase"))
                step += 1
            else:
                print("That language does not exists. Please, choose one from the list.")
        if(step == 2):
            print(license)
            print(base.get("acceptLicense"))
            userInput = input(text)
            if parser.checkYesNo(userInput) == True:
                step += 1
            elif parser.checkYesNo(userInput) == False:
                print(base.get("mustAcceptLicense"))
            elif parser.checkYesNo(userInput) == None:
                print(base.get("writeYesOrNo"))
        if(step == 3):
            print(base.get("writeMOTD"))
            userInput = input(text)
            if userInput != "":
                options.append(userInput)
                step += 1
        if(step == 4):
            print(base.get("writeMaxPlayers"))
            userInput = input(text)
            if userInput.isdigit():
                options.append(userInput)
                step += 1
        if(step == 5):
            print(base.get("writeGamemode"))
            userInput = input(text)
            if userInput.isdigit():
                if int(userInput) >= 0 and int(userInput) <= 3:
                    options.append(userInput)
                    print(base.get("wizardFinished"))
                    endWizard(path)
                    break

def skipWizard(path):
    fs.createServerConfigFromWizard(path, True, [])

def endWizard(path):
    fs.createServerConfigFromWizard(path, False, options)
