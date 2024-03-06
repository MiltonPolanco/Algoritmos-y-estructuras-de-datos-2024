import numpy as np
import simpy
import random

t = []
simulation_time = 10000

RANDOM_SEED = 30
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
        with self.cpu.request() as req:
            yield req
            yield self.env.timeout(CPU_SPEED)
            for i in range(instrucciones):
                yield self.env.timeout(CPU_SPEED)
            yield self.ram.put(instrucciones)
        end_time = self.env.now
        t.append(end_time - start_time)

def generate(env, os):
    for i in range(NUM_PROCESS):
        required_memory = random.randint(1, 10)
        total_instructions = random.randint(1, 6)
        env.process(os.new(f'   Proceso {i}', total_instructions, required_memory))
        yield env.timeout(random.expovariate(1.0 / INTERVAL))

env = simpy.Environment()
os = Simulation(env)
ram = simpy.Container(env, init=100, capacity=100)
env.process(generate(env,os))
env.run(until = simulation_time)
tiempo_respuesta_promedio = sum(t) / len(t)
print(f'Tiempo de ejecución: {tiempo_respuesta_promedio:.2f}')