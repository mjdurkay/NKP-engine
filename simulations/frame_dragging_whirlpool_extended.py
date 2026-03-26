import numpy as np

# ================================================================
# NKP Frame Dragging — Rotating Defect / Whirlpool Test (Extended)
# ================================================================

N = 128
L = 20.0
dx = L / N
dt = 0.004
c = 5.0
gamma = 0.4

x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)

sigma = 1.5
omega = 0.4   # rotation rate of the defect

rho = np.zeros((N, N))
rho_prev = np.zeros_like(rho)

num_particles = 16
radius = 4.0
angles = np.linspace(0, 2*np.pi, num_particles, endpoint=False)
particle_pos = np.stack([radius*np.cos(angles), radius*np.sin(angles)], axis=1)
particle_vel = np.zeros_like(particle_pos)

def rotating_defect(t):
    cx = 1.5 * np.cos(omega * t)
    cy = 1.5 * np.sin(omega * t)
    dx = X - cx
    dy = Y - cy
    return 2.0 * np.exp(-(dx**2 + dy**2) / (2*sigma**2))

def step_wave(rho, rho_prev, source):
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2
    return (2*rho - rho_prev +
            (c*dt)**2 * lap -
            gamma*dt*(rho - rho_prev) +
            dt**2 * source)

def interp(field, pos):
    xi = (pos[:,0] - x[0]) / dx
    yi = (pos[:,1] - x[0]) / dx
    i0 = np.floor(xi).astype(int)
    j0 = np.floor(yi).astype(int)
    i1 = np.clip(i0+1, 0, N-1)
    j1 = np.clip(j0+1, 0, N-1)
    i0 = np.clip(i0, 0, N-1)
    j0 = np.clip(j0, 0, N-1)
    sx = xi - i0
    sy = yi - j0
    f00 = field[j0, i0]
    f10 = field[j0, i1]
    f01 = field[j1, i0]
    f11 = field[j1, i1]
    return (1-sx)*(1-sy)*f00 + sx*(1-sy)*f10 + (1-sx)*sy*f01 + sx*sy*f11

print("Running NKP Frame Dragging Test...")

steps = 8000
sample_every = 40

initial_angles = np.arctan2(particle_pos[:,1], particle_pos[:,0])

for n in range(steps):
    t = n * dt
    src = rotating_defect(t)
    rho_next = step_wave(rho, rho_prev, src)
    rho_prev = rho
    rho = rho_next

    if n % sample_every == 0:
        phi = -rho
        gy, gx = np.gradient(phi, dx)
        ax = interp(gx, particle_pos)
        ay = interp(gy, particle_pos)
        accel = np.stack([ax, ay], axis=1)
        particle_vel += dt * accel * 4.0
        particle_pos += dt * particle_vel

final_angles = np.arctan2(particle_pos[:,1], particle_pos[:,0])
drift = np.degrees(np.mean(np.unwrap(final_angles) - np.unwrap(initial_angles)))

print("\nFrame Dragging Result:")
print(f"Mean azimuthal drift: {drift:.2f} degrees")
