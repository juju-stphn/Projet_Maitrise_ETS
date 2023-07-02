import time 
import gcode_serial 
from classes import Range
import camera_pics


# Initialisation du mouvement de la camera
def movment(h,v):
    nb_pics = 9
    # Ouvrir la connexion série
    ser=gcode_serial.serial_open()

    # Réinitialisation imprimante
    print("Réinitialisation de l'imprimante...")
    gcode_serial.command(ser, 'M999')
    gcode_serial.wait_for_ok(ser)

    # Remise a zero de la position de la camera
    gcode_serial.command(ser,"G28 X0 Y0 Z0")
    gcode_serial.wait_for_ok(ser)

    # Deplacement de la camera a la hauteur voulue
    gcode_serial.command(ser,f"G00 X0 Y0 Z{h}")
    gcode_serial.wait_for_ok(ser)
    
    # Prise des photos a intervalle regulier a la vitesse souhaitee
    p = 20
    for i in (r:=Range(0,220,p)):
        print(i)
        gcode_serial.command(ser,f"G01 X{i} Y0 Z{h} F{v}")
        gcode_serial.wait_for_ok(ser)
        time.sleep(3)

        camera_pics.take_picture(nb_pics)
        nb_pics -= 1
    
    # Fermeture de la liaison serie
    gcode_serial.serial_close(ser)
    return nb_pics
    
# Demande des parametres utilateurs
def getvalue_int(prompt="la valeur"):
    while True:
        try:
           value= int(input(f"Entrez {prompt} voulu(e): "))
           return value

        except ValueError:
            print(f"{prompt.capitalize()} n'est pas bon(ne) entrez une valeur correcte")
            continue
    

