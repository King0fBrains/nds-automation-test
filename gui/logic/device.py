"""Device module to interact with PySerial
as it pertains to Arduino connections """
import time
import serial
import serial.tools
import serial.tools.list_ports


def list_ports() -> list[str]:
    """Same as the builtin serial.tools.list_ports but filters for
    COM and USB as to clutter the Linux dropdown view"""
    filters = ["USB", "COM"]
    port_names = []
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if any(f in p.description for f in filters):
            port_names.append(p.device)
    return port_names


class MCSerial:
    """Setup for a simple serial device"""
    def __init__(self, port, rate):
        self.port = port
        self.rate = rate
        self.default_rate = 9600

    def write_to_device(self, instruct: list[int]) -> None:
        """Writes the output string step by step to the device
        Initially, this function appeared to not work and send nothing
        to the devices. The flush method fixed the problem so it appears
        to be imperative in this functions execution"""

        try:
            with serial.Serial(bytesize=8,
                               baudrate=self.rate,
                               port=self.port) as ser:
                time.sleep(2)
                for i in instruct:
                    ins = f"{i}+"
                    ser.write(ins.encode(encoding='ascii'))
                ser.write("?".encode(encoding='ascii'))
                ser.flush()
        except serial.SerialException as e:
            raise e
