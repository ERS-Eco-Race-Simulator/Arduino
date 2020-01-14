import serial
import threading

class Py2Arduino:

    def __init__(self, port):

        self.listening = True
        self.CLEAR = False
        self.serial = serial.Serial(port=port)
        self.data = ''

        self.listener_thread = threading.Thread(target=self._listener)
        self.listener_thread.start()

    def _listener(self):
        while self.listening:
            data = self.serial.read()
            if data == b'0':
                self.CLEAR = True

    def stop(self):
        self.listening = False
        self.listener_thread.join()

    def write_if_clear(self, data):
        if self.CLEAR:
            self.serial.write(data)
            return True
        return False

    def write_when_clear(self, data):
        self.wait_for_clear()
        self.serial.write(data)

    def wait_for_clear(self):
        while not self.CLEAR:
            pass
