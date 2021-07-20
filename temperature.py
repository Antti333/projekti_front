import requests
import datetime

#


#kun haetaan mennyttä säätä, pitänee antaa paikkakunnan koordinaatit, ei nimeä, Kaisaniemi lat = 60.2, lon = 24.9

#timestamp halutusta pvm:stä ja kelloajasta

timestamp_generated = str(datetime.datetime(2021, 7, 15, 14, 00).timestamp()) #muutetaan str, jotta voidaan split() .0 poistamiseksi
timestamp_splitted = timestamp_generated.split(".") 
timestamp = timestamp_splitted[0] #valitaan haluttu eli listan 1.

#muuttujat tähän

lat = 60.2
lon = 24.9
api_key = "e8b0924d5a0ce89fd664d80238a253c3"

#testi timestamp devaukseen
#timestamp = 1626480000



def get_weather(timestamp):
    
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}&units=metric"

    response = requests.get(url).json()
    #print(response)
    temp = response['current']['temp']
    #print(temp)
    
    return temp

#testi tulostus 
#print(get_weather(timestamp))

