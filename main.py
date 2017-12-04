#!/usr/bin/python 
# -*- coding:utf-8 -*-

import serial
import time

ser = serial.Serial("/dev/ttyS0", 9600)

def sendToMCU(message):
    ser.write(message)
    ser.flushInput()
    time.sleep(0.1)

def recvHandle(buff):
    if buff == '@':
        print 'MCU Handshake'
    if buff == 'faketoken':
        print buff
        sendToMCU('RAPI0#')
        print 'Unlock Successful'
    else:
        print buff
        sendToMCU('RAPI1#')
        print 'Unlock Failed'
def main():
    while True:
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(count)
            recvHandle(recv)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()