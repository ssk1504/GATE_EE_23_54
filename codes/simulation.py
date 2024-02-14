import numpy as np
import matplotlib.pyplot as plt

# Load theoretical and practical data from text files
time_theoretical, voltage_theoretical = np.loadtxt('theoretical_data.txt', unpack=True)
time_practical, voltage_practical = np.loadtxt('practical_data.txt', unpack=True)

# Plot both theoretical and practical results on the same graph
plt.plot(time_theoretical * 1000, voltage_theoretical, label='Theoretical', color='blue')
plt.plot(time_practical * 1000, voltage_practical, label='Practical', color='red')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.legend()
plt.ylim(0, 20)  # Set the y-axis range from 0 to 20V
plt.grid(True)
plt.show()

