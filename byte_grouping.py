import numpy as np
import time   


byte_arr = np.arange(2048*2048) #4 million elements

time_start = time.perf_counter()
arr_32bit = []
for i in range(0, len(byte_arr), 4):
    group = byte_arr[i:i+4] #group elements in four
    dummy = 0
    for j in range(4):
        dummy = dummy | (group[j]<<j*8) #combine 4 bytes into 32-bit 
    arr_32bit.append(dummy)

time_stop = time.perf_counter()
time_elapsed = time_stop - time_start

print("Time Passed (byte grouping): ", time_elapsed)
