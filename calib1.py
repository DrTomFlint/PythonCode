import scurve
import matplotlib.pyplot as plt
import numpy as np
import random

# parameters 
curves = 16
Km = 0.01
Kb = 0.25
cal0 = 25
cal1 = 50
print(f"{curves} Curves with Km = {Km} and Kb = {Kb}, cal at {cal0} and {cal1}")

# variables
m0=[1.0]*curves
b0=[0.0]*curves
y0=[0]*curves
y1=[0]*curves

# computed
mx=[0.0]*16
bx=[0.0]*16
y2=[0]*curves
y3=[0]*curves

for i in range(curves):
    m0[i]=m0[i]*random.gauss(1,Km)
    b0[i]=random.gauss(0,Kb)
    y0[i]=m0[i]*cal0+b0[i]
    y1[i]=m0[i]*cal1+b0[i]
    print(f"Curve {i} has slope {m0[i]:.3f}, intercept {b0[i]:.3f}, y0 {y0[i]:.3f}, y1 {y1[i]:.3f}")

    mx[i]=(y1[i]-y0[i])/(cal1-cal0)
    bx[i]=y0[i]-mx[i]*cal0
    print(f"    estimated slope {mx[i]:.3f}, intercept {bx[i]:.3f}")

    y2[i]=(y0[i] - bx[i])/mx[i]
    y3[i]=(y1[i] - bx[i])/mx[i]
    print(f"corrected y0 {y2[i]:.3f}, y1 {y3[i]:.3f}")
    print(" ")

# plot 
t = [cal0-10, cal1+10]
raw = []
fix = []
for i in range(curves):
    yraw0 = m0[i]*(cal0-10)+b0[i]
    yraw1 = m0[i]*(cal1-10)+b0[i]
    yfix0 = (yraw0 - bx[i])/mx[i]
    yfix1 = (yraw1 - bx[i])/mx[i]
    raw.append( [yraw0, yraw1] )
    fix.append( [yfix0, yfix1] )

plt.figure(figsize=(16,8),layout='constrained')

for i in range(curves):
    plt.plot(t,raw[i],'-r')
    plt.plot(t,fix[i],'-b')

plt.grid()
plt.show()




