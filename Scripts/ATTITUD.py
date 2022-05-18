#sensor_calc.py
import time
import numpy as np
import adafruit_bno055
import time
import os
import board
import busio


#board set up below needs to be updated
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)



#Activity 1: RPY based on accelerometer and magnetometer here is the problem
def roll_am(accelX,accelY,accelZ):
    #TODO
    return (180/np.pi) * np.arctan2(accelY, np.sqrt(accelX * accelX + accelZ * accelZ)) 

def pitch_am(accelX,accelY,accelZ):
    #TODO
    return (180/np.pi) * np.arctan2(accelX, np.sqrt(accelY * accelY + accelZ * accelZ))

def yaw_am(accelX,accelY,accelZ,magX,magY,magZ):
    pitch = pitch_am(accelX, accelY, accelZ)
    roll = roll_am(accelX, accelY, accelZ)
    mag_x = magX * np.cos(pitch) + magY * np.sin(roll) * np.sin(pitch) + magZ * np.cos(roll) * np.sin(pitch)
    mag_y = magY * np.cos(roll) - magZ * np.sin(roll)

    return (180/np.pi)*np.arctan2(-mag_y, mag_x)

#Activity 2: RPY based on gyroscope
def roll_gy(prev_angle, delT, gyro):
    #TODO
    return roll
def pitch_gy(prev_angle, delT, gyro):
    #TODO
    return pitch
def yaw_gy(prev_angle, delT, gyro):
    #TODO
    return yaw
def set_initial(mag_offset = [0,0,0]):
    #Sets the initial position for plotting and gyro calculations.
    print("Preparing to set initial angle. Please hold the IMU still.")
    time.sleep(3)
    print("Setting angle...")
    accelX, accelY, accelZ = sensor.acceleration #m/s^2
    magX, magY, magZ = sensor.magnetic #gauss
    #Calibrate magnetometer readings. Defaults to zero until you
    #write the code
    magX = magX - mag_offset[0]
    magY = magY - mag_offset[1]
    magZ = magZ - mag_offset[2]
    roll = roll_am(accelX, accelY,accelZ)
    pitch = pitch_am(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ)
    print("Initial angle set.")
    return [roll,pitch,yaw]

def calibrate_mag():
    offset = [0, 0, 0]
    maxMagX = -sys.maxint - 1
    maxMagZ = -sys.maxint - 1
    maxMagZ = -sys.maxint - 1
    minMagX = sys.maxint
    minMagY = sys.maxint
    minMagZ = sys.maxint
    
    
    print("Preparing to calibrate magnetometer. Please wave around.")
    #time.sleep(3)
    print("Calibrating...")
    t1 = time.time()
    while(time.time() - t1 < 3):
        magX, magY, magZ = sensor.magnetic
        print(magX)
        print(magY)
        print(magZ)
    
    print("Calibration complete.")
    return [0,0,0]

def calibrate_gyro():
    #TODO
    print("Preparing to calibrate gyroscope. Put down the board and do not touch it.")
    
    print("Calibrating...")
    #TODO
    print("Calibration complete.")
    return [0, 0, 0]
