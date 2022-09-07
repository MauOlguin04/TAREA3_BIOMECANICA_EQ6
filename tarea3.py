# TAREA NO. 3 (CÁLCULO Y GRAFICO DE PI)
# BIOMECANICA JUEVES N4-N6, EQUIPO 6
#Luis Carlos Gómez Espinoza
#Cesar Mauricio Alvarez Olguín
#Fátima Montserrat Zarazúa Uribe
#Arturo Mariscal Picon
#Gabriel López Escobar
#Francisco Emiliano Moreno De Alba
from multiprocessing import Pool
from random import randint
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

width = 10000
heigth = width
radio = width

npuntos = 0
ndentro = 0
radio2 = radio*radio
replicas = 250
promediopi = []

if __name__ == '__main__':
        with Pool(6) as p:
            inicio = time.time()
            for j in range(replicas):
                    for i in range(1,100000):
                        t_0 = time.time()
                        x = randint(0,width)
                        y = randint(0,width)
                        npuntos += 1
                        if x*x + y*y <= radio2:
                            ndentro += 1
                        pi = ndentro * 4 /npuntos
                        promediopi.append(pi)
                        t_1 = time.time()
                        t_f = t_1 - t_0
                        t_m = t_f * 1000000
                    print(statistics.mean(promediopi))
                    print("tiempo: {}µs.".format(t_m)) 
            final = time.time()
            delta = final - inicio 
            minutos = delta/60
            print("tiempo: {}s.".format(delta))   
            print("tiempo: {}minutos.".format(minutos))   

v=[0,1000000,0,3.8]
plt.plot(promediopi,"b--")
plt.xlabel('Tiempo en microsegundos (µs)')
plt.ylabel('Valores de pi')
plt.title('Tarea #3 Equipo #6 Biomecánica Jueves N3 - N6')
plt.axis(v)
plt.grid()
plt.show()