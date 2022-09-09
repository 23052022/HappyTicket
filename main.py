import time
import threading
import multiprocessing

def happy_ticket(limit1, limit2):
    numbers = list()
    for itm in range(limit1, limit2):
        b1 = f'{itm:06}'
        if int(b1[0]+b1[1]+b1[2] == b1[3]+b1[4]+b1[5]):
            numbers.append(b1)
    return numbers

def run_happy_ticket():
    start = time.time()
    happy_ticket(1, 1000000)
    end = time.time()
    print(end - start)


def run_happy_ticket_thread():
    start = time.time()
    a1 = threading.Thread(target=happy_ticket, args=(1, 500000, ))
    a2 = threading.Thread(target=happy_ticket, args=(500000, 1000000, ))
    a1.start()
    a2.start()
    a1.join()
    a2.join()
    end = time.time()
    print(end - start)


def run_process():
    start = time.time()
    p1 = multiprocessing.Process(target=happy_ticket, args=(1, 500000, ))
    p2 = multiprocessing.Process(target=happy_ticket, args=(500000, 1000000, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run_happy_ticket()
    run_happy_ticket_thread()
    run_process()
