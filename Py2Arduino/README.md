# Py2Arduino over Serial

Anytime arduino is ready to receive, it send a CLEAR signal. A py thread continuosly watch for that signal, and update a global flag when received.
Before py can send data to arduino, arduino must have sent CLEAR signal.

Methods:
- Send if CLEAR
- Send when CLEAR
- Wait for CLEAR
- Is CLEAR