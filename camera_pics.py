from time import sleep
import datetime 
from datetime import timedelta
from picamera import PiCamera
camera = PiCamera()

# Definition des parametres intrinseques de la camera
def camera_settings():
    camera.resolution = (800, 600)
    camera.framerate = 10
    camera.iso = 100
    #camera.start_preview()
    sleep(2) 

    camera.shutter_speed = camera.exposure_speed #exposure time
    camera.exposure_mode = 'off'

# Prise des images et sauvegarde dans un dossier
def take_picture(i):

    camera.capture(f'/home/pi/Projet/3.2.2/image_transfert{i}.png')
    

