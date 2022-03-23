import time

start = time.time()
print("hello")
time.sleep(90)  
end = time.time()
print(time.strftime('%H:%M:%S', time.gmtime((end - start))))




