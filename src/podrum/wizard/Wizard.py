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
from podrum.utils.Utils import Utils

class Wizard:
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

    @staticmethod
    def checkYesNo(value):
        if value.lower() == 'y' or value.lower() == 'yes':
            return True
        if value.lower() == 'n' or value.lower() == 'no':
            return False
        return

    @staticmethod
    def start():
        config = Utils.getDefaultConfig()
        step = 0
        while step >= 0:
            if step == 0:
                Base.printLanguages()
                userInput = input("> Please, select a language: ")
                if userInput in Base.languages:
                    config.config["language"] = userInput
                    print("- " + Base.getTranslation("langSelectedAsBase"))
                    step += 1
                else:
                    print("[!] That language does not exists. Please, choose one from the list.")
            elif step == 1:
                print(Wizard.podrumLicense)
                userInput = input("> " + Base.getTranslation("acceptLicense") + ": ")
                if Wizard.checkYesNo(userInput):
                    step += 1
                elif not Wizard.checkYesNo(userInput):
                    print(Base.getTranslation("mustAcceptLicense"))
                elif Wizard.checkYesNo(userInput) is None:
                    print(Base.getTranslation("writeYesOrNo"))
            elif step == 2:
                userInput = input("> " + Base.getTranslation("wizardSetup") + ": ")
                if Wizard.checkYesNo(userInput):
                    step += 1
                elif not Wizard.checkYesNo(userInput):
                    print("> " + Base.getTranslation("wizardSkipped"))
                    Wizard.isInWizard = False
                    config.save()
                    break
            elif step == 3:
                print(Wizard.podrumLogo)
                print(">- Podrum - Wizard -<\n\n")
                step += 1
            elif step == 4:
                userInput = input("[>] " + Base.getTranslation("writeServerPort") + " ")
                if userInput == "":
                    config.config["server-port"] = 19132
                    step += 1
                elif userInput.isdigit():
                    config.config["server-port"] = int(userInput)
                    step += 1
            elif step == 5:
                userInput = input("[>] " + Base.getTranslation("writeMOTD") + " ")
                if(userInput != ""):
                    config.config["motd"] = userInput
                    step += 1
            elif step == 6:
                userInput = input("[>] " + Base.getTranslation("writeGamemode") + " ")
                if userInput.isdigit():
                    if int(userInput) >= 0 and int(userInput) <= 3:
                        config.config["gamemode"] = int(userInput)
                        step += 1
            elif step == 7:
                userInput = input("[>] " + Base.getTranslation("writeMaxPlayers") + " ")
                if userInput.isdigit():
                    config.config["max-players"] = int(userInput)
                    step += 1
            elif step == 8:
                print(Base.getTranslation("wizardFinished"))
                Wizard.isInWizard = False
                config.save()
                break
                    
                    
                    
    
