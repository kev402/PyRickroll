# Puedes cambiar el nombre del archivo a algo más serio para que sea más convincente y no hayan sospechas de la broma.

import subprocess as sp
import time

print("Bienvenido a la actualización de tu consola")
solicitud = input("Desea actualizar su consola? (s/n): ").strip().lower()
if solicitud == "s":
    time.sleep(3)
    print("Descargando colores...")
    time.sleep(3)
    print("Aplicando color...")
    time.sleep(3)
    sp.run("color a", shell=True)
    time.sleep(3)
    print("Aplicando nuevo banner...")
    time.sleep(3)
    print("CAÍSTE... XD")
    time.sleep(2)
    sp.run(["curl", "ascii.live/rick"])

else:
    print("Lastima, ahora a tu sabrás las consecuencias...")
    sp.run("color a", shell=True)
    time.sleep(3)
    sp.run(["curl", "ascii.live/rick"])
