#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"



def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()



    print("People in space:", (sliceme['number']))
    print(sliceme['people'][0]['name'], "is on the", (sliceme['people'][0]['craft']))
    print(sliceme['people'][1]['name'], "is on the", (sliceme['people'][1]['craft']))
    print(sliceme['people'][2]['name'], "is on the", (sliceme['people'][2]['craft']))
    print(sliceme['people'][3]['name'], "is on the", (sliceme['people'][3]['craft']))
    print(sliceme['people'][4]['name'], "is on the", (sliceme['people'][4]['craft']))
    print(sliceme['people'][5]['name'], "is on the", (sliceme['people'][5]['craft']))
    print(sliceme['people'][6]['name'], "is on the", (sliceme['people'][6]['craft']))

main()
