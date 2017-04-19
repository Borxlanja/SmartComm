import requests
import json


#data = { "id": "prueba","type": "prueba_py","dato":  {"type": "text","value": "probando"}}

url = 'http://130.206.112.29:5050/iot/devices'

headers = {"Fiware-Service":"icai29757","Fiware-ServicePath": "/environment",
"Content-Type" : "application/json"}


data = {
    "devices": [ 
        { 
            "device_id": "Dev2975702", 
            "entity_name": "sensor01", 
            "entity_type": "temp_sensor", 
            "attributes": [ 
                  {  "name": "temperature", "type": "float" }
            ],
            "transport": "MQTT"
        }
    ]
}
# call get service with headers and params
response = requests.post(url,data=json.dumps(data), headers=headers)
print "code:"+ str(response.status_code)
print "******************"
print "headers:"+ str(response.headers)
print "******************"
print "content:"+ str(response.text)


