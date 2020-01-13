import fakeSerial as serial
import threading

class Py2Arduino:
    
    def __init__(self):
        
        self.listening = True
        self.CLEAR = False
        self.serial = serial.Serial(data='')
        self.data = ''
        
        self.listener_thread = threading.Thread(target=self._listener)
        self.listener_thread.start()
        
    def _listener(self):
        while self.listening:
            data = self.serial.read()
            if data == '0':
                self.CLEAR = True
        
    def stop(self):
        self.listening = False
        self.listener_thread.join()
        
    def send_if_clear(self, data):
        if self.CLEAR:
            self.serial.send(data)
            return True
        return False
            
    def send_when_clear(self, data):
        self.wait_for_clear()
        self.serial.send(data)
        
    def wait_for_clear(self):
        while not self.CLEAR:
            pass
        
    