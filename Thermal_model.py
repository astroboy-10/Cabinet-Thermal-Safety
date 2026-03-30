import numpy as np
import matplotlib.pyplot as plt

# Parameters
P = 400  # Heater power (W)
C = 5000  # Thermal capacitance (J/K)
k = 8     # Heat loss coefficient (W/K)
T_ambient = 20  # Ambient temp (°C)

# Controller setpoints
T_on = 40   # TC1 ON
T_off = 50  # TC2 OFF
T_cut = 70  # Thermal cut-out

# Simulation
dt = 1
t_max = 2000
time = np.arange(0, t_max, dt)

T = np.zeros_like(time)
T[0] = 20

heater_on = False

for i in range(1, len(time)):
    # Control logic
    if T[i-1] < T_on:
        heater_on = True
    if T[i-1] > T_off:
        heater_on = False
    if T[i-1] > T_cut:
        heater_on = False

    power = P if heater_on else 0

    # Thermal equation
    dTdt = (power - k * (T[i-1] - T_ambient)) / C
    T[i] = T[i-1] + dTdt * dt

# Plot
plt.figure()
plt.plot(time, T)
plt.axhline(T_on, linestyle='--', label='TC1 ON (40°C)')
plt.axhline(T_off, linestyle='--', label='TC2 OFF (50°C)')
plt.axhline(T_cut, linestyle='--', label='Cut-out (70°C)')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title("Cabinet Thermal Response")
plt.grid()

plt.savefig("results/temperature_vs_time.png")
plt.show()
