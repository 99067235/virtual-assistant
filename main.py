import json
import re
import cowsay
import os
with open('commands.json', 'r') as file:
    commands = json.load(file)

def giveninput(inputtext):
    splitted_input = splitforcommand(inputtext)
    command, params = checkforcommand(splitted_input)
    if command != '':
        condition = runcommand(command, stripquotesfromarray(params))
        if condition == True:
            print('Success')
        else:
            print(condition)

def runcommand(command, params):
    if command == '-say':
        try:
            if params[0] in cowsay.char_names:
                getattr(cowsay, params[0])(params[1])
                return True
            else:
                return 'That character isn\'t available yet.'
        except Exception:
            return 'An unexpected error uccurred.'
    else:
        return 'That command isn\'t available yet.'

def checkforcommand(splitted_input):
    command = ''
    params = []
    for word in splitted_input:
        if word.startswith('-'):
            command = word
        else:
            params.append(word)
    return command, params
def splitforcommand(inputtext):
    split_command = re.findall(r'(?:[^\s,"\']|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')+', inputtext)
    return split_command

def stripquotesfromarray(split_command):
    split_command = [word.strip("'\"") for word in split_command]
    return split_command

while True:
    giveninput(input())