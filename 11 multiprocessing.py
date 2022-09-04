import multiprocessing
import time
import concurrent.futures

def woo():
    print("Working for 1 second")
    time.sleep(1)
    print("Done in 1 second")

def woo2(seconds):
    print(f"Working for {seconds} second")
    time.sleep(seconds)
    print(f"Done in {seconds} second")

def woo3(seconds):
    print(f"Working for {seconds} second")
    time.sleep(seconds)
    return f"Done in {seconds} second"

def main():
  #  start = time.time()
  #  p1 = multiprocessing.Process(target=woo)
  #  p2 = multiprocessing.Process(target=woo)
  #
  #  p1.start()
  #  p2.start()
  #
  #  p1.join()
  #  p2.join()
  #
  # stop = time.time()
  # print(f'Stoped in {round(stop-start, 2)} seconds')

###################################################
    # processes = []
    # for i in range(1, 6):
    #     p = multiprocessing.Process(target=woo2, args=[i])
    #     p.start()
    #     processes.append(p)
    #
    # for i in processes:
    #     i.join()

###################################################
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = [executor.submit(woo3, i) for i in range(1, 6)]
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

###################################################
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [i for i in range(1, 6)]
        results = executor.map(woo3, secs)

        for result in results:
            print(result)

if __name__ == "__main__":
    main()