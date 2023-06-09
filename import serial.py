import serial
import xlwt
from datetime import datetime

class SerialDataLogger:
    def __init__(self, port, speed):
        self.port = port
        self.speed = speed
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Data from Serial", cell_overwrite_ok=True)
        self.ws.write(0, 0, "Date Time")
        self.columns = ["Date Time"]
        self.number = 100
        self.row = 1

    def initialize_serial(self):
        # Create a serial connection
        self.ser = serial.Serial(self.port, self.speed)

    def read_serial_data(self):
        while self.number > 0:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().rstrip()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.ws.write(self.row, 0, timestamp)
                self.ws.write(self.row, 1, data)
                self.row += 1
                self.number -= 1

    def save_data_to_excel(self, filename):
        self.wb.save(filename)
        print("Data saved to Excel successfully!")

# Usage example
port = '/dev/ttyUSB0'  # Replace with your actual serial port
speed = 9600  # Replace with your desired baud rate

data_logger = SerialDataLogger(port, speed)
data_logger.initialize_serial()
data_logger.read_serial_data()
data_logger.save_data_to_excel("serial_data.xls")