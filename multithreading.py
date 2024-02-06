# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:47:53 2024

@author: chillale sai krishna
"""

import threading
import subprocess
import time

# Define a function to run the first main file
def run_main1():
    start_time = time.time()
    result = subprocess.run(["python", "main_1.py"], capture_output=True, text=True)
    end_time = time.time()
    print("Result of main_1.py:")
    print(result.stdout)
    print(f"Time taken by main_1.py: {end_time - start_time} seconds, Start time {start_time}")

# Define a function to run the second main file
def run_main2():
    start_time = time.time()
    result = subprocess.run(["python", "main_2.py"], capture_output=True, text=True)
    end_time = time.time()
    print("Result of main_2.py:")
    print(result.stdout)
    print(f"Time taken by main_2.py: {end_time - start_time} seconds, Start time {start_time}")

# Create threads for each main file
thread1 = threading.Thread(target=run_main1)
thread2 = threading.Thread(target=run_main2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()



print("\n Both main files completed")


