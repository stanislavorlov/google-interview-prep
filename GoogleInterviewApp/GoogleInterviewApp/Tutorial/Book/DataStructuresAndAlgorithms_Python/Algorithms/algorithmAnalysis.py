from time import time

start_time = time()

for i in range(0, 100000000):
    continue

stop_time = time()
elapsed = stop_time - start_time

print(elapsed)