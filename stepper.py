from machine import Pin
from time import sleep_us
from time import sleep

class stepperMotor:
    def __init__(self, dirPin, stepPin, enablePin):
        self.dirPin = Pin(dirPin, Pin.OUT)
        self.stepPin = Pin(stepPin, Pin.OUT)
        self.enablePin = Pin(enablePin, Pin.OUT, Pin.PULL_UP)
    def doSteps (self, steps):
        if steps:
            print("Start Stepping")
            self.enablePin.value(1)
            if steps > 0:
                self.dirPin.value(1)
            for step in range(0, abs(steps)):
                print(step)
                self.stepPin.value(1)
                sleep_us(2)
                self.stepPin.value(0)
                sleep_us(1000)
            self.enablePin.value(0)
            self.dirPin.value(0)
            return
