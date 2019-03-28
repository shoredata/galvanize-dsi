import multiprocessing as mp
import time
import numpy as np
import sys

def quicksort(input_):
    if len(input_) < 2:
        return input_
    pivot = input_[0]
    less, more = [], []
    for i in input_[1:]:
        if i <= pivot:
            less.append(i)
        else:
            more.append(i)
    return quicksort(less) + [pivot] + quicksort(more)

def quicksort_parallel(input_, conn, pnum=8):
    if pnum <= 0 or len(input_) < 2:
        conn.send(quicksort(input_))
        conn.close()
        return

    pivot = input_[0]
    less, more = [], []
    for i in input_[1:]:
        if i <= pivot:
            less.append(i)
        else:
            more.append(i)

    # Pipe for the less subprocess
    pconnless, cconnless = mp.Pipe()
    # lessproc the quicksorts on the less list
    lessproc = mp.Process(target=quicksort_parallel, args=(less, cconnless, pnum-1))
    # Same for the more subprocess
    pconnmore, cconnmore = mp.Pipe()
    moreproc = mp.Process(target=quicksort_parallel, args=(more, cconnmore, pnum-1))
    # Start the processes
    lessproc.start()
    moreproc.start()
    #Send the result of the recursive step to the output of the pipe
    conn.send(pconnless.recv() + [pivot] + pconnmore.recv())
    conn.close()
    # Join the processes
    lessproc.join()
    moreproc.join()

def sort(input_, parallel=False):
    if parallel:
        pconn, cconn = mp.Pipe()
        p = mp.Process(target=quicksort_parallel, args=(input_, cconn, 8))
        p.start()
        result = pconn.recv()
        p.join()
        return result
    else:
        return quicksort(input_)

if __name__=="__main__":
    X = np.random.randint(2**7, size=200000)
    sys.setrecursionlimit(X.size*2)
    start = time.time()
    sort(X, False)
    print("Serial quicksort: ", time.time() - start)
    time.sleep(3)
    start = time.time()
    sort(X, True)
    print("Parallel quicksort ", time.time()-start)
