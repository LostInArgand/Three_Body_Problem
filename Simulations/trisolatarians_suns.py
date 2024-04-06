from vpython import *

sun1 = sphere(pos=vector(0,0,0), radius=6.9634e8, color=color.yellow, make_trail=True, trail_type='points', interval=10, retain=50)
sun1.mass = 1.989e30
sun1.p = vector(0, 0, -1e4) * sun1.mass

sun2 = sphere(pos=vector(1e11,0,0), radius=6.9634e8, color=color.red, make_trail=True, trail_type='points', interval=10, retain=50)
sun2.mass = 1.989e30

sun2.p = -sun1.p

G = 6.67e-11
dt = 1e4
while(True):
    rate(200)
    r = sun1.pos - sun2.pos
    F = G * sun1.mass * sun2.mass * r.hat / mag(r)**2
    sun1.p = sun1.p + F*dt
    sun2.p = sun2.p - F*dt
    sun1.pos = sun1.pos + (sun1.p/sun1.mass) * dt
    sun2.pos = sun2.pos + (sun2.p/sun2.mass) * dt
