from uModBusSerial import uModBusSerial

modbus = uModBusSerial(
    uart_id=1,
    baudrate=19200,
    data_bits=8,
    stop_bits=1,
    parity=None,
    pins=[10, 9])

# 4 values from 0 for slave address 11
modbus.read_holding_registers(11, 0, 4, True)
