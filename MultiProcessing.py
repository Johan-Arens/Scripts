import time
import multiprocessing
def worker(id):
    for number in range(10):
      print "looping number : " + str(number) + " - worker id : " + str(id)
      if id == 5:
        print "id 5 is slower"
        time.sleep(3)
      else:
        time.sleep(0.1)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(6):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
