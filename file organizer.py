import os
import shutil
import time

path = input("path - ")
days = input("days - ")

time.time()

if os.path.exists(path):
    os.remove(path)

else:
    shutil.rmtree(path)
