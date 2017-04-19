import requests


url = 'http://130.206.112.29:1026/v2/entities/sensor01/attrs/temperature/value'

headers = {"Fiware-Service":"icai29757","Fiware-ServicePath": "/environment"}

# call get service with headers and params
response = requests.get(url, headers=headers)
print "code:"+ str(response.status_code)
print "******************"
print "headers:"+ str(response.headers)
print "******************"
print "content:"+ str(response.text)


