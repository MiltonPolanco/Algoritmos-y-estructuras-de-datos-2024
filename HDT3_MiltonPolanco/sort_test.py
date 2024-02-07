#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTOR: Milton Polanco - 23471
#   FECHA : 06/02/2024
#   DESCRIPCIÓN: Unit tests
#---------------------------------------------------------------------
import unittest

from gs import gnome_sort
from ms import mergeSort
from qs import quickSort
from rs import radixSort
from ss import selectionSort
from shs import shellSort
from hs import heapSort

class TestSorts(unittest.TestCase):
    def test_gnome_sort(self):
        self.assertEqual(gnome_sort([2,5,4,3,1]), [1,2,3,4,5])
    def test_merge_sort(self):
        self.assertEqual(mergeSort([2,5,4,3,1]), [1,2,3,4,5])
    def test_quick_sort(self):
        self.assertEqual(quickSort([2,5,4,3,1], 0, 4), [1,2,3,4,5])
    def test_radix_sort(self):
        self.assertEqual(radixSort([2,5,4,3,1]), [1,2,3,4,5])
    def test_selection_sort(self):
        self.assertEqual(selectionSort([2,5,4,3,1], 5), [1,2,3,4,5])
    def test_shell_sort(self):
        self.assertEqual(shellSort([2,5,4,3,1], 5), [1,2,3,4,5])
    def test_heap_sort(self):
        self.assertEqual(heapSort([2,5,4,3,1]), [1,2,3,4,5])

if __name__ == '_main_':
    unittest.main