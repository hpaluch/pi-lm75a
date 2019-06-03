#!/usr/bin/env python

# sys.argv
import sys
import smbus
import struct

def raw_temp_to_float(raw_temp):
    s=chr(raw_temp & 0xff) + chr( (raw_temp >> 8) & 0xff )
    # signed short, big-endian (I2C LM75A uses BE, this ARM uses LE)
    ss = struct.unpack(">h",s)
    ss0 = ss[0]
    # lowest 7-bits are unused (actually garbage) on LM75A
    # and we need to divide value by 2 (there is 0.5 precision)
    f = ( ss0 >> 7 ) * 0.5
    #print("ss=%d (0x%x)" % (ss0,ss0))
    #print("f=",f)
    return f


def read_temp(bus_obj,i2c_addr,temp_reg,descr):
    x = bus_obj.read_word_data(i2c_addr,temp_reg)
    #print("Raw=0x%x => float %.1f" % (x, raw_temp_to_float(x)))
    print("%s temperature is %.1f Celsius" % (descr,raw_temp_to_float(x)) )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s i2c_bus_number lm75_i2c_slave_address" % (sys.argv[0],))
        print("Example: %s 1 0x48" % (sys.argv[0],))
        sys.exit(1)

    i2c_bus  = int(sys.argv[1],0)
    i2c_addr = int(sys.argv[2],0)
    print("Expecting LM75 to have I2C slave address 0x%x on I2C BUS %u" % (i2c_addr,i2c_bus))

    bus = smbus.SMBus(i2c_bus)
    read_temp(bus, i2c_addr,0, "Current")
    read_temp(bus, i2c_addr,2, "Hysteresis")
    read_temp(bus, i2c_addr,3, "Shutdown")

