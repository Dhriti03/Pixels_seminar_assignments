import serial
import xlwt
from datetime import datetime

port = '/dev/tty57'
#port = '/dev/ttyUSB0'  # Replace with your actual serial port
speed = 9600  # Replace with your desired baud rate
duration = 60  # Duration of data collection in seconds

wb = xlwt.Workbook()
ws = wb.add_sheet("Data from Sensor", cell_overwrite_ok=True)
ws.write(0, 0, "Timestamp")
ws.write(0, 1, "Sensor Data")
row = 1

ser = serial.Serial(port, speed)

start_time = datetime.now()
end_time = start_time + timedelta(seconds=duration)

while datetime.now() < end_time:
    if ser.in_waiting > 0:
        data = ser.readline().decode().rstrip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ws.write(row, 0, timestamp)
        ws.write(row, 1, data)
        row += 1

filename = "sensor_data.xls"
wb.save(filename)
print("Data saved to Excel successfully!")
