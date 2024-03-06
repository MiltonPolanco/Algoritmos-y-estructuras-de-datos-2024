import matplotlib.pyplot as plt
import numpy as np
import simpy
import random

t = []
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
        yield self.ram.get(memory_time)
        print(f'{self.env.now:.2f}: Process {name} obtains {instrucciones} units of memory. Memory at: {memory_time}')

        print('%s memory at %d' % (name, self.env.now))
        with self.cpu.request() as req:
            yield req
            print('%s starting to run at %s' % (name, self.env.now))
            yield self.env.timeout(CPU_SPEED)
            for i in range(instrucciones):
                print(f'    {self.env.now:.2f}: {name} ejecuta instrucción {i+1}')
                yield self.env.timeout(CPU_SPEED)

            print(f'    {self.env.now:.2f}: Proceso {name} finaliza su ejecución')
            yield self.ram.put(instrucciones)
            print(f'    {self.env.now:.2f}: Proceso {name} libera {instrucciones} unidades de memoria. Memoria en: {memory_time}')
        end_time = self.env.now
        t.append(end_time - start_time)

def generate(env, os):
    for i in range(NUM_PROCESS):
        required_memory = random.randint(1, 10)
        total_instructions = random.randint(1, 6)
        env.process(os.new(f'   Proceso {i}', total_instructions, required_memory))
        yield env.timeout(random.expovariate(1.0 / INTERVAL))

def grafica(average_time):
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(t)), t, color='blue', label='Duración por proceso')
    plt.axhline(y=average_time, color='r', linestyle='-', label=f'Tiempo Promedio = {average_time:.2f}')
    plt.xlabel('Cantidad de Proceso')
    plt.ylabel('Tiempo CPU')
    plt.title('Tiempo de Procesos en la CPU')
    plt.legend()
    plt.show()

def run():
    env = simpy.Environment()
    os = Simulation(env)
    ram = simpy.Container(env, init=100, capacity=100)
    env.process(generate(env,os))
    env.run(until = simulation_time)
    tiempo_respuesta_promedio = sum(t) / len(t)
    print(f'Tiempo de ejecución: {tiempo_respuesta_promedio:.2f}')
    average_time = np.mean(t)
    std_dev = np.std(t)
    print(f"Tiempo Promedio: {average_time:.2f}")
    print(f"Desviación Estándar: {std_dev:.2f}")
    grafica(average_time)

run()
