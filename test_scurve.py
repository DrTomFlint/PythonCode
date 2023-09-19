import scurve

a=scurve.Scurve(100,x0=0,v0=0,vmax=5,amax=1,)
b=scurve.Scurve(100,x0=50,v0=0,vmax=5,amax=1)

print("step %2d,   A at %5.2f, delta is %5.2f, speed %5.2f,   B at %5.2f, delta is %5.2f, speed %5.2f" 
        % (0,          a.x,      a.delta,         a.v,            b.x,      b.delta,         b.v))

for i in range(39):
    a.step()
    b.step()
    print("step %2d,   A at %5.2f, delta is %5.2f, speed %5.2f,   B at %5.2f, delta is %5.2f, speed %5.2f" 
          % (i+1,          a.x,      a.delta,         a.v,            b.x,      b.delta,         b.v))

