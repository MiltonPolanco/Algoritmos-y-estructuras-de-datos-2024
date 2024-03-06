############################################################
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# DEPARTAMENTO DE INGENIERÍA
# ALGORITMOS Y ESTRUCTURA DE DATOS - CC2016
# AUTOR:Milton Giovanni Polanco Serrano - 23471
# DESCRIPCIÓN: Simulaciones con Simpy
# FECHA DE ENTREGA: Martes 05 de marzo del año 2024
############################################################
import matplotlib.pyplot as plt
import numpy as np
import simpy
import random

out_time = [] #Lista para tiempos de salida
simulation_time = 10000

RANDOM_SEED = 42
NUM_PROCESS = 150
INTERVAL = 10
RAM_CAPACITY = 100
CPU_CAPACITY = 2
CPU_SPEED = 1

random.seed(RANDOM_SEED)

class Simulation:
    def __init__(self, env):
        self.ram = simpy.Container(env, init=RAM_CAPACITY , capacity=RAM_CAPACITY )
        self.cpu = simpy.Resource(env, capacity=CPU_CAPACITY)
        self.env = env
    
    def new(self, name, instrucciones, memory_time):
        start_time = self.env.now
        yield self.ram.get(memory_time) #se consume 1 unidad de memoria por instrucción
        print(f'{self.env.now:.2f}: Process {name} obtains {instrucciones} units of memory. Memory at: {memory_time}')

        print('%s memory at %d' % (name, self.env.now))
        with self.cpu.request() as req:
            yield req
            print('%s starting to run at %s' % (name, self.env.now)) # Asignación de RAM
            yield self.env.timeout(CPU_SPEED)
            for i in range(instrucciones): # Simulación de ejecución
                print(f'    {self.env.now:.2f}: {name} ejecuta instrucción {i+1}') # Momento de ejecución
                yield self.env.timeout(CPU_SPEED)  # Instrucción en 1 unidad de tiempo

            print(f'    {self.env.now:.2f}: Proceso {name} finaliza su ejecución')
            yield self.ram.put(instrucciones) # Se liberan las unidades de memoria utilizadas
            print(f'    {self.env.now:.2f}: Proceso {name} libera {instrucciones} unidades de memoria. Memoria en: {memory_time}')
        end_time = self.env.now  # Tiempo de finalización
        out_time.append(end_time - start_time)  # Duración del proceso

def generate(env, os):
    for i in range(NUM_PROCESS):
        required_memory = random.randint(1, 10)
        total_instructions = random.randint(1, 6)
        env.process(os.new(f'   Proceso {i}', total_instructions, required_memory))
        yield env.timeout(random.expovariate(1.0 / INTERVAL))

def grafica(average_time):
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(out_time)), out_time, color='red', label='Duración por proceso')
    plt.axhline(y=average_time, color='black', linestyle='-', label=f'Tiempo Promedio = {average_time:.2f}')
    plt.xlabel('Cantidad de Proceso')
    plt.ylabel('Tiempo CPU')
    plt.title('Tiempo de Procesos en la CPU')
    plt.legend()
    plt.show()

def run(): #Ejecución
    env = simpy.Environment()
    os = Simulation(env)
    ram = simpy.Container(env, init=100, capacity=100)
    env.process(generate(env,os))
    env.run(until = simulation_time)

    # Tiempo de respuesta promedio
    tiempo_respuesta_promedio = sum(out_time) / len(out_time)
    print(f'Tiempo de ejecución: {tiempo_respuesta_promedio:.2f}')
    average_time = np.mean(out_time)
    std_dev = np.std(out_time)
    print(f"Tiempo Promedio: {average_time:.2f}")
    print(f"Desviación Estándar: {std_dev:.2f}")
    grafica(average_time)

run()
