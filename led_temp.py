import os
import sys
import keyboard
import bluetooth
import requests

#mapeado
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def main():

	while True:
		r = requests.get('http://192.168.1.100/status/list.php?estado=now') 

		data = r.json()

		coreTemp = data[1]['coreTemp']

		#print(coreTemp)
		
		#100 brillos
		mapCoreTemp = _map(float(coreTemp),46,70,0,99)

		mapCoreTemp = _map(mapCoreTemp,0,99,0,255)

		#print(mapCoreTemp)

		#envio pwm red
		sock.send("R"+str(mapCoreTemp)+"A")
		#envio pwm green
		#sock.send("G0A")
		#envio pwm blue
		#sock.send("B0A")


if __name__ == '__main__':
	try:
		bd_addr = "20:16:02:30:81:19"
		port = 1
		sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		sock.connect((bd_addr, port))
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		sock.close()
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)


