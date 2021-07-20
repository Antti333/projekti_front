import requests

#kun haetaan mennyttä säätä, pitänee antaa paikkakunnan koordinaatit, ei nimeä, Kaisaniemi lat = 60.2, lon = 24.9

#timestamp halutusta pvm:stä ja kelloajasta

#muuttujat tähän

lat = 60.2
lon = 24.9
#city_name = "Kaisaniemi"
api_key = "e8b0924d5a0ce89fd664d80238a253c3"
timestamp = 1626480000



def get_weather(api_key, city):
    
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}&units=metric"

    response = requests.get(url).json()
    #print(response)
    temp = response['current']['temp']
    #print(temp)
    
    return temp

print(get_weather(api_key,city_name))

