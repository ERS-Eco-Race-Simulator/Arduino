import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Py2Arduino'))

import Py2Arduino
p2a = Py2Arduino.Py2Arduino('/dev/ttyACM0')

running = True

while running:
    inp = input('[-1 to exit] > ')
    if inp == '-1':
        running = False
        p2a.stop()
    else:
        p2a.write_when_clear(str.encode(inp))
    
