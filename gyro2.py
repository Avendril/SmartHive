import time
import smbus
import math

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

while True:
        def read_byte(reg):
                return bus.read_byte_data(address, reg)

        def read_word(reg):
                h = bus.read_byte_data(address, reg)
                l = bus.read_byte_data(address, reg+1)
                value = (h << 8) + l
                return value

        def read_word_2c(reg):
                val = read_word(reg)
                if (val >= 0x8000):
                        return -((65535 - val) + 1)
                else:
                        return val

        def dist(a,b):
                return math.sqrt((a*a)+(b*b))

        def get_y_rotation(x,y,z):
                radians = math.atan2(x, dist(y,z))
                return -math.degrees(radians)

        def get_x_rotation(x,y,z):
                radians = math.atan2(y, dist(x,z))
                return math.degrees(radians)

        bus = smbus.SMBus(1)
        address = 0x68

        bus.write_byte_data(address, power_mgmt_1, 0)

        print "----------------------------------------------------------------------"
        print "Angle of the Hive"

        Acceleration_x_axis = read_word_2c(0x3b)
        Acceleration_y_axis = read_word_2c(0x3d)
        Acceleration_z_axis = read_word_2c(0x3f)

        Acceleration_x_axis_scaling = Acceleration_x_axis / 16384.0
        Acceleration_y_axis_scaling = Acceleration_y_axis / 16384.0
        Acceleration_z_axis_scaling = Acceleration_z_axis / 16384.0

        Ac_x = Acceleration_x_axis_scaling * 100
        Ac_y = Acceleration_y_axis_scaling * 100
        Ac_z = Acceleration_z_axis_scaling * 100

        print "Angle at x axis: ", Ac_x#Acceleration_x_axis_scaling
        print "Angle at y axis: ", Ac_y#Acceleration_y_axis_scaling
        print "Angle at z axis: ", Ac_z#Acceleration_z_axis_scaling

        time.sleep(5)


