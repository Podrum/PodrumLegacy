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
import parser

text = None


def steps(step):
    if step == 0:
        return 'Do you want to follow the setup? [y/n]'


def wizard():
    step = 0
    while step >= 1:
        if step == 0:
            text = 'Do you want to follow the setup'
        userInput = input(text)
