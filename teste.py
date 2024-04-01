#servidor local 192.168.10.2

# import RPi.GPIO as GPIO
import time
from pyModbusTCP.client import ModbusClient # pip install pyModbusTCP
import requests

# endereço do escravo para interfaceamento entre mestres (CLP)
clp2 = ModbusClient(host='192.168.10.41', port=502, unit_id=2, timeout=1000.0, auto_open=True, debug=True)

estado = 0
right = 0
left = 0
up = 0
down = 0
garra = 0

while True:
    res = requests.get('https://eight-modbuscomservidorrender.onrender.com/')
    response = res.json()
    print(response)
    try:
        right = response['right']
        left = response['left']
        up = response['up']
        down = response['down']
    except:
        right = 0
        left = 0
        up = 0
        down = 0
    try:
        garra = response['garra']
    except:
        garra = garra
    requestReplit = [right, left, up, down, garra]

    clp2.write_multiple_coils(0, requestReplit) #escreve no primeiro registro coil da rede modbus 0001
    time.sleep(0.01)
    
# para iniciar com o pm2 no ubuntu
# pm2 start server.py --name server --interpreter python3