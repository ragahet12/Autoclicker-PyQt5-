import threading
import time

from pynput.mouse import Button, Controller

mouse = Controller()


class clicker(threading.Thread):

    def __init__(self, name='clicker'):
        self.delay = 1
        self.running_on = False
        threading.Thread.__init__(self, name=name)
        threading.Thread.start(self)

    def start_clicking(self, delay_):
        self.running_on = True
        self.delay = delay_

    def stop_clicking(self):
        self.running_on = False

    def run(self):
        while True:
            while self.running_on:
                mouse.click(Button.left)
                time.sleep(self.delay)
            time.sleep(0.1)
