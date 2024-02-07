#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTOR: Milton Polanco - 23471
#   FECHA : 06/02/2024
#   DESCRIPCIÓN: Todos los sorts
#---------------------------------------------------------------------
import random
import time
import cProfile
import re
cProfile.run('re.compile("foo|bar")')
import sys
sys.setrecursionlimit(20000)

from gs import gnome_sort
from ms import mergeSort
from qs import quickSort
from rs import radixSort
from ss import selectionSort
from shs import shellSort
from hs import heapSort

while True:
    print("Selecciona: ")
    print("1. 10 elementos")
    print("2. 1495 elementos")
    print("3. 3000 elementos")
    print("4. 10 elementos en forma descendente")
    print("5. 1495 elementos en forma descendente")
    print("6. 3000 elementos en forma descendente")
    print("7. Detener")
    e = int(input("->: "))
    if e >= 1 and e <= 7:
            if e == 1:
                arr = [0]*10 
                for i in range(10): arr[i] = random.randrange(0, 10000)
            elif e == 2:
                arr = [0]*1495
                for i in range(1495): arr[i] = random.randrange(0, 10000)
            elif e == 3:
                arr = [0]*3000
                for i in range(3000): arr[i] = random.randrange(0, 10000)
            elif e == 4:
                arr = [0]*10
                for i in range(10): arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif e == 5:
                arr = [0]*1495
                for i in range(1495): arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif e == 6:
                arr = [0]*3000
                for i in range(3000): arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif e == 7:
                break

            with open('numeros.txt', 'w') as f:
                for item in arr:
                    f.write("%s\n" % item)
    else:
            print("Opción inválida")

    read_list = []
    with open('numeros.txt', 'r') as f:
            for line in f:
                read_list.append(int(line.strip()))

    print("Lista original: "+str(read_list)+"\n")
    
    s = time.perf_counter()
    gs = gnome_sort(read_list)
    e = time.perf_counter()
    print("  Gnome Sort: "+str(gs)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    ms = mergeSort(read_list)
    e = time.perf_counter()
    print("  Merge Sort: "+str(ms)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    qs = quickSort(read_list, 0, int(len(read_list)-1))
    e = time.perf_counter()
    print("  Quick Sort: "+str(qs)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    rs = radixSort(read_list)
    e = time.perf_counter()
    print("  Radix Sort: "+str(rs)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    ss = selectionSort(read_list, int(len(read_list)))
    e = time.perf_counter()
    print("  Selection Sort: "+str(ss)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    shs = shellSort(read_list, int(len(read_list)))
    e = time.perf_counter()
    print("  Shell Sort: "+str(shs)+"\n  Tiempo: "+str(e - s)+" s \n")

    s = time.perf_counter()
    hs = heapSort(read_list)
    e = time.perf_counter()
    print("  Heap Sort: "+str(hs)+"\n  Tiempo: "+str(e - s)+" s \n")