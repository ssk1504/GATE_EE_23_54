import os
import numpy as np
import matplotlib.pyplot as plt

# Define the NGSpice netlist
ngspice_netlist = """
*Title: case(ii) transient analysis

r 1 2 10
V1 1 0 DC 5V
C1 2 0 100u IC=SIN(159*time - PI/4)
.tran 0.002ms 4ms
.control
run
set color0=white
plot v(2)
.endc
.end
"""

# Write the netlist to a file
with open("transient_analysis.cir", "w") as file:
    file.write(ngspice_netlist)

# Run NGSpice simulation
command = "ngspice -b transient_analysis.cir"
output = os.popen(command).read()

# Parse the output to extract time and voltage values
time_values = []
voltage_values = []
for line in output.split("\n"):
    if line.strip() and not line.startswith("No"):
        data = line.split()
        if len(data) >= 2:
            try:
                time_values.append(float(data[0]))
                voltage_values.append(float(data[1]))
            except ValueError:
                pass

# Convert time to milliseconds
time_values = np.array(time_values) * 1000  # Convert to milliseconds

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(time_values, voltage_values)
plt.title("Transient Analysis")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.tight_layout()

# Find index corresponding to x = 1.57 ms
x_target = 1.57
index = np.abs(time_values - x_target).argmin()
y_value = voltage_values[index]

# Print the value of y at x = 1.57 ms
print(f"Voltage at x = {x_target} ms: {y_value} V")

# Check if y = 5 at x = 1.57 ms
if np.isclose(y_value, 5):
    print("Simulation verified")

plt.show()

