#include <stdio.h>
#include <math.h>

#define MAX_DATA_POINTS 50000

// Define the theoretical voltage function
double theoretical_voltage_function(double t) {
    return 5 + (sin(1000*t - (M_PI/4) - 5) * exp(-1000*t));
}

// Function to calculate the derivative of voltage across the capacitor
double derivative(double voltage, double time, double V0, double R, double C) {
    return (V0 - voltage) / (R * C);
}

int main() {
    double time_theoretical[MAX_DATA_POINTS];
    double voltage_theoretical[MAX_DATA_POINTS];
    double voltage_practical[MAX_DATA_POINTS];
    double time_practical[MAX_DATA_POINTS];

    double C = 100e-6;  // Capacitance (F)
    double R = 10;      // Resistance (ohm)
    double V0 = 5;      // Voltage of the battery (V)
    double initial_voltage = 7.07 * sin(M_PI/4);  // Initial voltage across the capacitor (V)
    double delta_t = 0.0001;  // Time step (s)
    double total_time = 0.005; // Total simulation time (s)

    // Generate time values for theoretical and practical simulations
    int num_points = total_time / delta_t;
    for (int i = 0; i < num_points; i++) {
        time_theoretical[i] = i * delta_t;
        time_practical[i] = i * delta_t;
    }

    // Calculate corresponding theoretical voltage values
    for (int i = 0; i < num_points; i++) {
        voltage_theoretical[i] = theoretical_voltage_function(time_theoretical[i]);
    }

    // Euler method to solve the practical differential equation
    voltage_practical[0] = initial_voltage; // Set initial condition for practical simulation
    for (int i = 1; i < num_points; i++) {
        double voltage_derivative = derivative(voltage_practical[i-1], time_practical[i-1], V0, R, C);
        voltage_practical[i] = voltage_practical[i-1] + voltage_derivative * delta_t;
    }

    // Write theoretical data to text file
    FILE *theoretical_file = fopen("theoretical_data.txt", "w");
    if (!theoretical_file) {
        printf("Error opening theoretical_data.txt for writing.\n");
        return 1;
    }
    for (int i = 0; i < num_points; i++) {
        fprintf(theoretical_file, "%lf %lf\n", time_theoretical[i], voltage_theoretical[i]);
    }
    fclose(theoretical_file);

    // Write practical data to text file
    FILE *practical_file = fopen("practical_data.txt", "w");
    if (!practical_file) {
        printf("Error opening practical_data.txt for writing.\n");
        return 1;
    }
    for (int i = 0; i < num_points; i++) {
        fprintf(practical_file, "%lf %lf\n", time_practical[i], voltage_practical[i]);
    }
    fclose(practical_file);

    printf("Data has been written to theoretical_data.txt and practical_data.txt successfully.\n");

    return 0;
}

