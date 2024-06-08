from serial import Serial
import threading
class SerialManager:

    def __init__(self, port="COM4", baudrate=9600):
        print("SerialManager started")
        self.conn = Serial(port, baudrate)
        def read_write_thread(self):
            while True:
                # Read data from serial connection
                data = self.conn.readline().decode().strip()
                if data:
                    print("    Serial: received data:", data)
                
                # Write data to serial connection
                # Example: self.conn.write(b"Hello, World!")
                
        # Create and start the read/write thread
        thread = threading.Thread(target=read_write_thread, args=(self,))
        thread.start()
    
    def set_opening(self, opening: int):
        print("    Serial: invio apertura messaggio apertura ", opening)
        self.conn.write(str(opening).encode())
        