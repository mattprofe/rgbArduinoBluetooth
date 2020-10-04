#creado para cambiar el color de la tira de leds
#conectada a ardunio y controlado por bluetooth
import bluetooth

#id bluetooth
bd_addr = "00:00:00:00:00:00"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

#envio pwm red
sock.send("R0A")
#envio pwm green
sock.send("G0A")
#envio pwm blue
sock.send("B0A")

#cierro conexion
sock.close()
