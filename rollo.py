from stepper import stepperMotor
from machine import Pin, PWM

class Rollo:
    def __init__(self, stepperPins,openingSteps, servoPin, servoOpenAngle=65, servoCloseAngle=100):
        self.rolloStepper = stepperMotor(stepperPins[0], stepperPins[1], stepperPins[2])
        self.openingSteps = openingSteps
        self.servoAngles = servoAngles
        self.Servo = PWM(Pin(servoPin), freq=50, duty=77)
        self.ServoOpenAngle = servoOpenAngle
        self.servoCloseAngle = servoCloseAngle
    def openBlind(self):
        # enable Servo
        self.Servo.duty(self.ServoOpenAngle)
        self.rolloStepper.doSteps(self.openingSteps)
        self.Servo.duty(self.servoCloseAngle)
        #disableServo
    def closeblind(self):
        # enable Servo
        self.Servo.duty(self.ServoOpenAngle)
        self.rolloStepper.doSteps(self.openingSteps)
        self.Servo.duty(self.ServoOpenAngle)
        # disable Servo
