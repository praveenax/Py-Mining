import time
def calc_time (func,a):
    start_time = time.time()
    func(a)
    print("--- %s seconds ---" % (time.time() - start_time))