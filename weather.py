import requests 
import time
import sys
from pynput.keyboard import Listener

def on_press(key):
    if key == 'q':
        print("q pressed. Exiting the loop...")
        return False

while True:
    where = input("Where to select (or type 'exit' to quit): ")
    
    if where.lower() == "exit":
        print("Exiting the program...")
        break

    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=c1573dd9175247c6b04162027240905&q={where}&aqi=yes')

    if response.status_code == 200:
        print("Query successful")
        one_minute = 10
        while True:
            with Listener(on_press=on_press) as listener:
                weather = response.json()['current']['temp_c']
                print(where,": ",weather)
                time.sleep(one_minute)
    else:
        print("Query failed. Please check your input and try again.")
