# This file is executed on every boot (including wake-boot from deepsleep)
import os, machine
import gc
from ledmanager import LedManager
from constants import SSID, SSID_PASSWORD
import network, utime, machine

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSID_PASSWORD)
        while not sta_if.isconnected():
            print("Attempting to connect....")
            utime.sleep(1)
    print('Connected! Network config:', sta_if.ifconfig())

gc.collect()

print("Connecting to wifi..")
LedManager().red_mode()
connect()
LedManager().green_mode()