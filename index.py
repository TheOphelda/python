import time
from rplidar import RPLidar

# Fonction de traitement des données lidar
def process_lidar_data(data):
    min_distance = float('inf')  # Distance minimale initiale
    for (_, angle, distance) in data:
        # Filtre les données dans l'intervalle de -90 à 90 degrés
        if -90 <= angle <= 90:
            # Fais quelque chose avec l'angle et la distance
            print(f"Angle: {angle}, Distance: {distance}")
            if distance < min_distance:
                min_distance = distance

    # Vérifie si la distance minimale est inférieure à la valeur seuil
    threshold_distance = 200  # Valeur seuil de distance (en centimètres)
    if min_distance < threshold_distance:
        print("Objet détecté !")

# Connexion au RPLidar
lidar = RPLidar('/dev/ttyUSB0')

# Acquisition des données lidar
try:
    # Démarre la rotation du lidar
    lidar.start_motor()

    # Attend quelques secondes pour que le lidar atteigne sa vitesse maximale
    time.sleep(2)

    # Lance l'acquisition des données
    lidar.connect()

    # Lit les données lidar en boucle
    for scan in lidar.iter_scans():
        process_lidar_data(scan)

except KeyboardInterrupt:
    print("Interruption par l'utilisateur")

# Arrête le lidar et ferme la connexion
lidar.stop_motor()
lidar.disconnect()


