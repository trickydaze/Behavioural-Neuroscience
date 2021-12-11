


import serial

arduino_port = "/dev/cu.Bluetooth-Incoming-Port" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="trial-data.csv"
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:")
file = open(fileName, "a")
print("Created file")

#display the data to the terminal
getData=str(ser.readline())
data=getData[0:][:-2]
print(data)

#add the data to the file
file = open(fileName, "a") #append the data to the file
file.write(data + "\\n") #write data with a newline

#close out the file
file.close()

