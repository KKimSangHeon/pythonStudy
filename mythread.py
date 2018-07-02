import threading
import time


class DemoThread(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            print(i)


t = DemoThread()
t.start()
t.join()