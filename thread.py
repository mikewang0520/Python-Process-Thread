from threading import Thread
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    threads = []
    num_threads = 10

    # Create threads
    for i in range(num_threads):
        t = Thread(target = square_numbers)
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Join threads: wait for them to complete
    for t in threads:
        t.join()

    print('end main')