import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import math

with open("./settings.txt", "r") as settings_file:
    settings = [float(num) for num in settings_file.read().split("\n")]

data = np.loadtxt("./data.txt", dtype=int)

voltStep = settings[1]
timeStep = settings[0]

voltArr = data * voltStep
timeArr = np.arange(0, len(data)) * timeStep

voltMax     = np.max(voltArr)
voltMaxInd = np.argmax(voltArr)
timeMax     = np.max(timeArr)
timeMaxInd = np.argmax(timeArr)

figure, axes = plt.subplots(figsize = (16, 9), dpi = 400)

axes.set_xlabel("Время, с", fontsize = 14)
axes.set_ylabel("Напряжение, В", fontsize = 14)
axes.set_title("Зарядка-разрядка RC-цепи", fontsize = 18)

chargeLine   , = axes.plot(timeArr[0:voltMaxInd:], voltArr[0:voltMaxInd:], color = 'green')
dischargeLine, = axes.plot(timeArr[voltMaxInd::], voltArr[voltMaxInd::], color = 'red')

chargeLine.set_label("Зарядка")
dischargeLine.set_label("Разрядка")
axes.legend(prop={"size":16})

x_limits = (0.0, math.ceil(timeMax))
y_limits = (0.0, 3.5)
axes.set(xlim = x_limits, ylim = y_limits)

axes.xaxis.set_minor_locator(MultipleLocator(0.5))
axes.yaxis.set_minor_locator(MultipleLocator(0.25))

axes.xaxis.set_major_locator(MultipleLocator(1))
axes.yaxis.set_major_locator(MultipleLocator(0.5))

axes.grid(color = "black", which = "both", linestyle = ':', linewidth = 0.3)

chargeTime    = timeArr[voltMaxInd] - timeArr[0]
dischargeTime = timeArr[-1] - timeArr[voltMaxInd]

axes.scatter(timeArr[voltMaxInd], voltMax, color='blue')
axes.text(x = timeArr[voltMaxInd] - 0.5, y = voltMax + 0.25, s = ("Точка максимума"), color = 'blue', fontsize = 14)

axes.text(x = (chargeTime/2-0.8), y = voltMax/2, s = ("Время зарядки: " + str(round(chargeTime, 2)) + " s"), color = 'green', fontsize = 14)
axes.text(x = (chargeTime+dischargeTime/2-0.8), y = voltMax/2, s = ("Время разрядки: " + str(round(dischargeTime, 2)) + " s"), color = 'red', fontsize = 14)

figure.savefig("picture.svg")