# Connecting LM75A to Raspberry PI

WARNING: Work in progress

Tested HW/SW:

* Raspberry PI version (from https://raspberry-projects.com/pi/pi-hardware/raspberry-pi-pcb-versions):
  - `B Model B Revision 2.0 (512MB)`
  - PCB Says: `Raspberry Pi (c)2011.12`

* OS: `Raspbian GNU/Linux 9.9 (stretch)`
  from http://director.downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-04-09/2019-04-08-raspbian-stretch-lite.zip

* [CJMCU-75 board][CJMCU-75] with [I2C LM75A Digital Temperature Sensor][LM75A].
  Please see https://github.com/hpaluch/i2c-cjmcu-75 for instruction on this board setup (you need to wire address pins A0,A1,A2 to VCC or GND to set
  LM75A I2C device address.

# Setup

Install these requirements (see https://www.instructables.com/id/Raspberry-Pi-I2C-Python/ for details):

```bash
sudo apt-get install i2c-tools python-smbus
```


Should not be needed: Add your non-privileged
user (typically `pi`) to `i2c` group
to have access to `/dev/i2c-1` device:

```bash
usermod -G i2c -a pi
```

If you are already logged as `pi` issue:
```bash
newgrp
```
To ensure that you are now member of `i2c` group.

Now you can try to detect LM75A I2C Device:
```bash
 i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Looks OK - device found at address `0x48`

Now you can run example python program:
```
./test-lm75a.py 1 0x48
   Expecting LM75 to have I2C slave address 0x48 on I2C BUS 1
   Raw=0x801a Raw_Swapped=0x1a80
   Temperature in Celsius=26
```

# Bugs

* The +/- 0.5 degree of Celsius precision is lost (currently
only whole degrees of Celsius are shown)


[LM75A]: http://www.ti.com/lit/ds/symlink/lm75a.pdf
[CJMCU-75]: https://www.amazon.de/gp/product/B01FQWN79W/
