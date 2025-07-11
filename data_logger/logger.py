# Python script to read serial data and log to CSV
import serial, csv, time
ser = serial.Serial('/dev/ttyUSB0', 115200)
with open('data_log.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    while True:
        line = ser.readline().decode().strip()
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        values = line.split(',')
        writer.writerow([ts] + values)