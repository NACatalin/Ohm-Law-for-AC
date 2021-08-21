import numpy as np
from math import sin,pi
import matplotlib.pyplot as plt

#set  parameters of voltage
amplitude =float(input("Voltage amplitude:"))
frequency= float(input('Frequency:'))

#set  value of rezistor
resistance= float(input("Resistance value:"))

#Range time
nr_periods=float(input('The number of periods you want to see:'))
end_time=(nr_periods/frequency)*1000
time=np.linspace(0,end_time,1000)
values_of_voltage=list()
values_of_current=list()
values_of_power=list()


#Calcul of current
for i in time:
    voltage=amplitude*sin(2* pi*frequency*i)
    values_of_voltage.append(voltage)
    current=voltage/resistance
    values_of_current.append(current)


#plot current-time and voltage-time

plt.plot(time,values_of_voltage)
plt.plot(time,values_of_current)

plt.legend()
plt.show()



