import json
import http
import requests

    
def get_rates():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
  
       
    val = 'USD'
    print(type(data))
    a = data['Valute'][val]['CharCode']
    b = data['Valute'][val]['Value'] 
    
    message = b
    return message




   
          
        
    
       
