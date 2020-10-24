"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.lang.Base import Base
from podrum.utils.ServerFS import ServerFS
from podrum.wizard.Parser import Parser

class Wizard:
    
    options = []
    isInWizard = True
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
        while step >= 0:
            if(step == 0):
                Base.Base.getLangFiles()
                userInput = input("> Please, select a language: ")
                if Parser.checkIfLangExists(userInput) == True:
                    Wizard.options.append(userInput)
                    print("- " + Base.Base.get("langSelectedAsBase"))
                    step += 1
                else:
                    print("[!] That language does not exists. Please, choose one from the list.")
            elif(step == 1):
                print(Wizard.podrumLicense)
                userInput = input("> " + Base.Base.get("acceptLicense") + ": ")
                if Parser.checkYesNo(userInput) == True:
                    step += 1
                elif Parser.checkYesNo(userInput) == False:
                    print(Base.Base.get("mustAcceptLicense"))
                elif Parser.checkYesNo(userInput) == None:
                    print(Base.Base.get("writeYesOrNo"))
            elif(step == 2):
                userInput = input("> " + Base.Base.get("wizardSetup") + ": ")
                if Parser.checkYesNo(userInput) == True:
                    step += 1
                elif Parser.checkYesNo(userInput) == False:
                    print("> " + Base.Base.get("wizardSkipped"))
                    Wizard.skipWizard(path)
                    break
            elif(step == 3):
                print(Wizard.podrumLogo)
                print(">- Podrum - Wizard -<\n\n")
                step += 1
            elif(step == 4):
                userInput = input("[>] " + Base.Base.get("writeServerPort") + " ")
                if userInput == "":
                    Wizard.options.append("19132")
                    step += 1
                elif userInput.isdigit():
                    Wizard.options.append(userInput)
                    step += 1
            elif(step == 5):
                userInput = input("[>] " + Base.Base.get("writeMOTD") + " ")
                if(userInput != ""):
                    Wizard.options.append(userInput)
                    step += 1
            elif(step == 6):
                userInput = input("[>] " + Base.Base.get("writeGamemode") + " ")
                if userInput.isdigit():
                    if int(userInput) >= 0 and int(userInput) <= 3:
                        Wizard.options.append(userInput)
                        step += 1
            elif(step == 7):
                userInput = input("[>] " + Base.Base.get("writeMaxPlayers") + " ")
                if userInput.isdigit():
                    Wizard.options.append(userInput)
                    step += 1
            elif(step == 8):
                print(Base.Base.get("wizardFinished"))
                Wizard.endWizard(path)
                break
                        
    def skipWizard(path, isTravisBuild = False):
        if isTravisBuild == True: Wizard.options.append("en")
        ServerFS.createServerConfigFromWizard(path, True, Wizard.options)
        
    def endWizard(path):
        ServerFS.createServerConfigFromWizard(path, False, Wizard.options)
                    
                    
                    
    
