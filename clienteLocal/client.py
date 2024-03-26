#servidor local 192.168.10.2

# import RPi.GPIO as GPIO
import time
from pyModbusTCP.client import ModbusClient # pip install pyModbusTCP
import requests

# endereço do escravo para interfaceamento entre mestres (CLP)
clp2 = ModbusClient(host='192.168.10.41', port=502, unit_id=2, timeout=1000.0, auto_open=True, debug=True)

estado = 0

while True:
    res = requests.get('https://dedbc447-f684-4fe5-a9a6-b6ba0704b9d0-00-17llpgw1o4yb6.kirk.repl.co/')
    response = res.json()
    print(response)
    requestReplit = [response['right'],response['left'],response['up'],response['down'],response['garra']]

    clp2.write_multiple_coils(0, requestReplit) #escreve no primeiro registro coil da rede modbus 0001
    time.sleep(0.01)
    
# para iniciar com o pm2 no ubuntu
# pm2 start server.py --name server --interpreter python3