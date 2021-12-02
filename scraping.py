#!/usr/python3.9.5

#pip install requests  #For Install requests Library

#https://github.com/m3hr44n

import requests

url = input('Enter the Webpage to Grab Source from ==> : ')

html_output_name = input('Name For Html File ==> : ')

req = requests.get( url , 'html.parser')

with open('html_output_name', 'a',encoding='utf-8') as file:    

    file.write(req.text + '\n')

    file.close()



         
        
