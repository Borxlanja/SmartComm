# Simulation of a changing attribute so changes can be tracked and shown

import paho.mqtt.client as paho
import random
import time

def temperatura(raw_temp_bytes1,raw_temp_bytes2):

    raw_ambient_temp = int('0x' + raw_temp_bytes2 + raw_temp_bytes1,16)  # Choose ambient temperature (reverse bytes for little endian)
    ambient_temp_int = raw_ambient_temp >> 2 & 0x3FFF  # Shift right, based on from TI
    ambient_temp_celsius = float(ambient_temp_int) * 0.03125  # Convert to Celsius based on info from TI

    return ambient_temp_celsius

 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


bluetooth_adr = "B0:B4:48:D0:27:87"
tool = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
tool.expect('\[LE\]>')
print
"Preparing to connect. You might need to press the side button..."
tool.sendline('connect')
# test for success of connect
tool.sendline('char-write-cmd 0x24 01')
tool.expect('\[LE\]>')


client = paho.Client()
client.on_publish = on_publish
client.connect("130.206.112.29",1883)
client.loop_start()
temp = 15
while True:

    time.sleep(5)
    tool.sendline('char-read-hnd 0x21')
    tool.expect('descriptor: .*')
    rval = tool.after.split()
    temp = temperatura(rval[7], rval[6])
    temp= temp + random.randint(1,10) - 5
    print(temp)

    (rc, mid) = client.publish("/1234/Dev2975702/attrs/temperature", str(temp), qos=0)

