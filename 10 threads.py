import threading
import time
import concurrent.futures

# pierwotne, najstarszy sposób obsługi wątków

def wo():
    print("Start function")
    time.sleep(3)
    print(f"Done in 3")

#start = time.time()

#t1 = threading.Thread(target=wo)
#t2 = threading.Thread(target=wo)

#t1.start()
#t2.start()

#t1.join()
#t2.join()

#stop = time.time()
#print(f'Finished in {round(stop-start, 2)} sec')

################################################

# wątki z parametrami funkcji
#def woo2(secs):
    #print(f'Work for {secs} secons')
    #time.sleep(secs)
    #print(f'Done in {secs} seconds')

#start = time.time()

#threads = []
#for i in range(1, 6):
    #t = threading.Thread(target=woo2, args=[i])
    #t.start()
    #threads.append(t)

#for i in threads:
    #i.join()

#stop = time.time()
#print(f'Finished in {round(stop-start, 2)} sec')

######################################################
#wykorzystanie biblioteki concurency i context menagera
def woo3(secs):
    print(f'Work for {secs} secons')
    time.sleep(secs)
    return f'Done in {secs} seconds'

with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = executor.submit(woo3, 2)
    t2 = executor.submit(woo3, 3)

    print(t1.result())
    print(t2.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(1, 6)]
    results = [executor.submit(woo3, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(1, 6)]
    results = executor.map(woo3, secs)

    for result in results:
        print(result)