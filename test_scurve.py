import scurve
import matplotlib.pyplot as plt

# starting conditions
last = 1200

at0=100
ax0=0
av0=0
avmax0=2
aamax0=0.1

bt0=100
bx0=0
bv0=0
bvmax0=2
bamax0=0.05

# change list
dt=     [100,   500,    600,    800,    850,    900,    950]
datarg= [-100,  100,    0,      50,     -50,    50,     0]
davmax= [2,     2,      2,      2,      2,      2,      2]
daamax= [0.05,  0.05,   0.05,   0.05,   0.05,   0.05,   0.05]
dbtarg= [-100,  100,    0,      50,     -50,    50,     0]
dbvmax= [5,     5,      5,      5,      5,      5,      5]
dbamax= [0.01,  0.01,   0.01,   0.01,   0.01,   0.01,   0.01]

# instantiate two scurves
a=scurve.Scurve(at0,x0=ax0,v0=av0,vmax=avmax0,amax=aamax0)
b=scurve.Scurve(bt0,x0=bx0,v0=bv0,vmax=bvmax0,amax=bamax0)

# create lists for plotting
t=[0]
at=[at0]
ax=[ax0]
av=[av0]
avmax=[avmax0]
avmin=[-avmax0]
aamax=[aamax0]
bt=[bt0]
bx=[bx0]
bv=[bv0]
bvmax=[bvmax0]
bvmin=[-bvmax0]
bamax=[bamax0]

for i in range(1,last):
    
    # text to terminal
    print("step %2d,   A at %5.2f, delta is %5.2f, speed %5.2f,   B at %5.2f, delta is %5.2f, speed %5.2f" 
        % (i,          a.x,      a.delta,         a.v,            b.x,      b.delta,         b.v))
    
    # check for a change point
    if i in dt:
        k=dt.index(i)
        a.target=datarg[k]
        a.vmax=davmax[k]
        a.amax=daamax[k]
        b.target=dbtarg[k]
        b.vmax=dbvmax[k]
        b.amax=dbamax[k]
        print("step %2d, A targ %5.2f,  maxv %5.2f,  maxa %5.2f, B targ %5.2f, maxv %5.2f, maxa %5.2f "
              %( i,        a.target,         a.vmax,       a.amax,      b.target,          b.vmax,     b.amax ))
            
    # take 1 step
    a.step()
    b.step()

    # append data to plotting arrays
    t.append(i)
    at.append(a.target)
    ax.append(a.x)
    av.append(a.v)
    avmax.append(a.vmax)
    avmin.append(-a.vmax)
    aamax.append(a.amax)
    bt.append(b.target)
    bx.append(b.x)
    bv.append(b.v)
    bvmax.append(b.vmax)
    bvmin.append(-b.vmax)
    bamax.append(b.amax)

# plot 
plt.figure(figsize=(16,8),layout='constrained')
#plt.figure(layout='constrained')

plt.subplot(2,2,1)
plt.plot(t,at,'-b')
plt.plot(t,ax,'-r')
plt.title('A positions')
plt.xlabel('time')
plt.ylabel('position')
plt.grid()

plt.subplot(2,2,2)
plt.plot(t,bt,'-b')
plt.plot(t,bx,'-r')
plt.title('B positions')
plt.xlabel('time')
plt.ylabel('position')
plt.grid()

plt.subplot(2,2,3)
plt.plot(t,avmax,'-b',t,avmin,'-g')
plt.plot(t,av,'-r')
plt.title('A velocity')
plt.xlabel('time')
plt.ylabel('position')
plt.grid()

plt.subplot(2,2,4)
plt.plot(t,bvmax,'-b',t,bvmin,'-g')
plt.plot(t,bv,'-r')
plt.title('B velocity')
plt.xlabel('time')
plt.ylabel('position')
plt.grid()

plt.show()



