
"""
Spyder Editor
This is a temporary script file.
"""
import time
import RPi.GPIO as IO
import matplotlib.pyplot as plt
IO.setmode(IO.BCM)
IO.setup(17, IO.IN)
IO.setup(27, IO.IN)
IO.setup(5, IO.OUT)
IO.setup(6, IO.OUT)
start = 0
pwm = IO.PWM(5, 1000)
pwm.start(start)
prev_loss = 0.
aloss = 0.

def get_phase(pin):
    t1 = time.time()
    count = 0
    state1 = IO.input(pin)
    state2 = state1
    while True:
        state2 = IO.input(pin)
        if state2 != state1:
            break
    t2 = time.time()
    return t2 - t1

def get_rpm(pin):
    i = 0
    time = 0
    while i != 14:
        time += get_phase(pin)
        i += 1
    return 60 / time
        

class PID:
    def __init__(self, P, I, D):
        self.P = P
        self.I = I
        self.D = D
    def control(self, loss, aloss, dloss):
        return self.P * loss + self.I * aloss + self.D * dloss

setpoint = 6000
speed = 0
i = 0
controller = PID(0.005, 0.007, 0.001)
while True:
    loss = setpoint - speed
    aloss += loss
    dloss = loss - prev_loss
    u = controller.control(loss, aloss, dloss)
    print(u)
    if u <= 0:
        u = 0
    if u >= 100:
        u = 100
    pwm.start(u)
    speed = get_rpm(27)
    prev_loss = loss
    i += 1
    plt.plot(i, speed, "ro")
