# Puedes cambiar el nombre del archivo a algo más serio para que sea más convicente y no hayan sospechas de la broma.

import os
import time

print("Bienvenido a la actualización de tu consola")
solicitud = input("Desea actualizar su consola? (s/n): ")
if solicitud == "S" or solicitud == "s":
    time.sleep(3)
    print("Descargando colores...")
    time.sleep(3)
    print("Aplicando color...")
    time.sleep(3)
    os.system("color a")
    time.sleep(3)
    print("Aplicando nuevo banner...")
    time.sleep(3)
    print("CAÍSTE... XD")
    time.sleep(2)
    os.system("curl ascii.live/rick")

else:
    print("Lastima, ahora a tu sabrás las consecuencias...")
    os.system("color a")
    time.sleep(3)
    os.system("curl ascii.live/rick")