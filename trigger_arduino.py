import serial

ser = serial.Serial("/dev/tty.usbmodem1411", 9600)
print "serial connection established"

response = False

while response == False:
  read = ser.read()
  if read == "1":
    print "communication with device established (" + read + ")"
    response = True
  else:
    print "connecting... (" + read + ")"

ser.write("1")
print "arduino command triggered"

ser.close()
print "connection closed"
