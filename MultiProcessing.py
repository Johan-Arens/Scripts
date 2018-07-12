#
#  Johan Arens
#  Cisco Systems
#  Jul 12 2018

import time
import multiprocessing
def worker(id):
    for number in range(10):
        print "looping number : " + str(number) + " - worker id : " + str(id)
        print "id "+ str(id) +" waits for " + str(id) + " sec"
        time.sleep(id/10)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(1000):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
