import serial
import time
from datetime import datetime

# Envoi des commandes via la liaison serie
def command(ser, command):
    ser.write((command + '\n').encode('utf-8'))
    ser.flush()

# Attente du retour de imprimante pour continuer execution
def wait_for_ok(ser):
    while True:
        response = ser.readline().decode('utf-8').strip()
        print(response)
        if response == 'ok':
            break

# Ouverture de la connexion serie pour communiquer avec imprimante
def serial_open(port="/dev/ttyUSB0",baud=115200):
    ser= serial.Serial(port, baud, timeout=1)
    print(f"Connecté à l'imprimante sur le port {port} à {baud} bauds.")
    return ser

# Fermeture de la connexion serie
def serial_close(ser):
    time.sleep(2)
    ser.close()



