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
from podrum.lang import Base
from podrum.utils.ServerFS import ServerFS
from podrum.wizard.Parser import Parser

class Wizard:
    
    options = []
    isInWizard = True
    text = '- '
    podrumLogo = """
            ____           _                      
           |  _ \ ___   __| |_ __ _   _ _ __ ___  
           | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
           |  __/ (_) | (_| | |  | |_| | | | | | |
           |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
    """
    podrumLicense = """
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at
        
        http://www.apache.org/licenses/LICENSE-2.0
        
        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
    """

    def startWizard(path):
        step = 0
        while step >= 0 and step < 6:
            if(step == 0):
                print(Wizard.podrumLogo)
                print(">- Podrum - Wizard -<\n\n")
                print("Do you want to follow the setup? [y/n]:")
                userInput = input(Wizard.text)
                if Parser.checkYesNo(userInput) == True:
                    step += 1
                elif Parser.checkYesNo(userInput) == False:
                    print("Skipping the setup wizard...")
                    Wizard.skipWizard(path)
                    break
                elif Parser.checkYesNo(userInput) == None:
                    print("Please, write yes (y) or no (n).")
            if(step == 1):
                print("Please, select a language:")
                Base.Base.getLangFiles(path)
                userInput = input(Wizard.text)
                if Parser.checkIfLangExists(userInput) == True:
                    Wizard.options.append(userInput)
                    print(Base.Base.get("langSelectedAsBase"))
                    step += 1
                else:
                    print("That language does not exists. Please, choose one from the list.")
            if(step == 2):
                print(Wizard.podrumLicense)
                print(Base.Base.get("acceptLicense"))
                userInput = input(Wizard.text)
                if Parser.checkYesNo(userInput) == True:
                    step += 1
                elif Parser.checkYesNo(userInput) == False:
                    print(Base.Base.get("mustAcceptLicense"))
                elif Parser.checkYesNo(userInput) == None:
                    print(Base.Base.get("writeYesOrNo"))
            if(step == 3):
                print(Base.Base.get("writeMOTD"))
                userInput = input(Wizard.text)
                if userInput != "":
                    Wizard.options.append(userInput)
                    step += 1
            if(step == 4):
                print(Base.Base.get("writeMaxPlayers"))
                userInput = input(Wizard.text)
                if userInput.isdigit():
                    Wizard.options.append(userInput)
                    step += 1
            if(step == 5):
                print(Base.Base.get("writeGamemode"))
                userInput = input(Wizard.text)
                if userInput.isdigit():
                    if int(userInput) >= 0 and int(userInput) <= 3:
                        Wizard.options.append(userInput)
                        print(Base.Base.get("wizardFinished"))
                        Wizard.endWizard(path)
                        break
                        
    def skipWizard(path):
        ServerFS.createServerConfigFromWizard(path, True, [])
        
    def endWizard(path):
        ServerFS.createServerConfigFromWizard(path, False, Wizard.options)
                    
                    
                    
    
