# Connecting LM75A to Raspberry PI

How to connect popular LM75A Temperature sensor to
Raspberry PI using I2C.


![Raspberry PI and I2C LM75A](https://github.com/hpaluch/pi-lm75a/blob/master/assets/pi-lm75a.jpg?raw=true) 

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


Connect your Raspberry PI to CJMCU-75 board using this layout

```
           Rasp. Pi
             1 2
CJMCU-75    +---+       CJMCU-75
NC  --  3.3V|o o|5V  -- VCC
SDA --  SDA |o o|NC
SCL --  SCL |o o|GND -- GND
             ...
            other pins unused
```

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
Current temperature is 26.0 Celsius
Hysteresis temperature is 75.0 Celsius
Shutdown temperature is 80.0 Celsius
```

Here is I2C communication in Sigrok PulseView:

Getting current temperature (Pointer Register = 0x00):

![LM75A Get Temperature PulseView](https://github.com/hpaluch/pi-lm75a/blob/master/assets/lm75a-raspberry-get-temp.png?raw=true) 

NOTE 0x001a = 26 (degrees of Celsius)

Getting hysteresis temperature (Pointer Register = 0x02):

![LM75A Get Hysteresis PulseView](https://github.com/hpaluch/pi-lm75a/blob/master/assets/lm75a-raspberry-get-hysteresis.png?raw=true) 

NOTE: 0x004b = 75 (degrees of Celsius)

# Bugs

N/A

[LM75A]: http://www.ti.com/lit/ds/symlink/lm75a.pdf
[CJMCU-75]: https://www.amazon.de/gp/product/B01FQWN79W/

