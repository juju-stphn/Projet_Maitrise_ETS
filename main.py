import camera_movment
import calibrate_pics
import camera_pics
import reconstruction
import matplotlib.pyplot as plt


# Fonction pour fermer affichage plt apres 3 secondes
def close_event():
    plt.close() 

def main():
    # Demande hauteur et vitesse a utilisateur
    hauteur=camera_movment.getvalue_int("la hauteur")
    vitesse=camera_movment.getvalue_int("la vitesse")
    
    # Initialisation de la camera
    camera_pics.camera_settings()
    
    # Prise des images
    nbphoto = camera_movment.movment(hauteur, vitesse)

    # Calibration des images
    calibrate_pics.calibration(10)
    
    
    # Exécution des étapes de traitement des images
    depth_maps = reconstruction.calculate_depth_maps()

    
    # Déplacement entre chaque prise de photo 
    displacement = -7000
 
    
    # Fusionner les cartes de profondeur
    merged_depth_map = reconstruction.align_depth_maps(depth_maps, displacement)
    
    
    plt.imshow(merged_depth_map, 'gray')
    plt.show()
    
    # Affichage et sauvegarde de la reconstruction stereo pendant 3 secondes
    fig = plt.figure()
    timer = fig.canvas.new_timer(interval = 3000) #creating a timer object and setting an interval of 3000 milliseconds
    timer.add_callback(close_event)
    timer.start()
    plt.imshow(merged_depth_map, 'gray')
    plt.savefig(f'/home/pi/Projet/reconstruction.png')
    plt.show()

    
main()


