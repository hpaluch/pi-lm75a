#!/usr/bin/env python

# sys.argv
import sys
import smbus


def read_temp(bus_obj,i2c_addr):
    bus_obj.write_byte_data(i2c_addr,0,0)
    x = bus_obj.read_word_data(i2c_addr,0)
    # swap byte order
    x2 = (( x >> 8) & 0xff) + ( ( x << 8 ) & 0xff00)
    print("Raw=0x%x Raw_Swapped=0x%x" % (x,x2))
    print("Temperature in Celsius=%d" % (x2 >> 8,) )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s i2c_bus_number lm75_i2c_slave_address" % (sys.argv[0],))
        print("Example: %s 1 0x48" % (sys.argv[0],))
        sys.exit(1)

    i2c_bus  = int(sys.argv[1],0)
    i2c_addr = int(sys.argv[2],0)
    print("Expecting LM75 to have I2C slave address 0x%x on I2C BUS %u" % (i2c_addr,i2c_bus))

    bus = smbus.SMBus(i2c_bus)
    read_temp(bus,i2c_addr)


