import numpy as np
import matplotlib.pyplot as plt

# Define the theoretical voltage function
def theoretical_voltage_function(t):
    return 5 + (np.sin(1000*t - (np.pi/4) - 5) * np.exp(-1000*t))

# Constants for practical simulation
C = 100e-6  # Capacitance (F)
R = 10  # Resistance (ohm)
V0 = 5  # Voltage of the battery (V)
initial_voltage = 7.07 * np.sin(np.pi/4)  # Initial voltage across the capacitor (V)
delta_t = 0.0001  # Time step (s)
total_time = 0.005  # Total simulation time (s)

# Function to calculate the derivative of voltage across the capacitor
def derivative(voltage, time):
    return (V0 - voltage) / (R * C)

# Generate time values for theoretical and practical simulations
time_theoretical = np.arange(0, 0.005, 0.0001)
time_practical = np.arange(0, total_time, delta_t)

# Calculate corresponding theoretical and practical voltage values
voltage_theoretical = theoretical_voltage_function(time_theoretical)
voltage_practical = np.zeros_like(time_theoretical)
voltage_practical[0] = initial_voltage  # Set initial condition for practical simulation

# Euler method to solve the practical differential equation
for i in range(1, len(time_theoretical)):
    voltage_derivative = derivative(voltage_practical[i-1], time_theoretical[i-1])
    voltage_practical[i] = voltage_practical[i-1] + voltage_derivative * 0.0001

# Plot both theoretical and practical results on the same graph
plt.plot(time_theoretical * 1000, voltage_theoretical, label='Theoretical', color='blue')
plt.plot(time_theoretical * 1000, voltage_practical, label='Practical', color='red')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.legend()
plt.ylim(0, 20)  # Set the y-axis range from 0 to 25V
plt.grid(True)
plt.show()

