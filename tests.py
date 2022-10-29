import os
import time
import random
import psutil

from functions.bitonic_sort import bitonic_sort
from functions.brick_sort import brick_sort
from functions.bubble_sort import bubble_sort#0.109s
from functions.bucket_sort import bucket_sort
from functions.cocktail_sort import cocktail_sort
from functions.comb_sort import comb_sort
from functions.gnome_sort import gnome_sort#0.123s
from functions.heap_sort import heap_sort
from functions.insertion_sort import insertion_sort
from functions.merge_sort import merge_sort
from functions.pancake_sort import pancake_sort
from functions.pigeonhole_sort import pigeonhole_sort
from functions.quick_sort import quick_sort
from functions.radix_sort import radix_sort
from functions.selection_sort import selection_sort
from functions.shell_sort import shell_sort
from functions.smooth_sort import smooth_sort
from functions.strand_sort import strand_sort


def main():
    list = []
    for i in range(1000):
        list.append(random.randint(0, 100))

    start = time.time()
    pid = os.getpid()
    python_process = psutil.Process(pid)
    # -------------- Function start --------------
    result = bubble_sort(list)
    # -------------- Function stop --------------
    memoryUse = python_process.memory_info()[0]/1000000  # memory use in MB
    end = time.time()

    print("Time: " + str(round(end - start, 3)) + "s")
    print("Memory: " + str(round(memoryUse, 3)) + "MB")

if __name__ == "__main__":
    main()