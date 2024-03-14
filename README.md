# Package Delivery Project

This program is designed to manage package delivery logistics for a delivery company. Here's a summary of its functionality:

1. Data Loading: Loads package data from a CSV file into a hash table for efficient retrieval and management.

2. Distance Calculation: Calculates the distance between addresses using a pre-loaded distance dataset.

3. Truck Initialization: Initializes three trucks with starting locations, capacities, and departure times.

4. Package Delivery: Iterates through each truck's package list, calculates the optimal delivery route based on distance, and updates package statuses and delivery times accordingly.

5. CLI Interface: Provides a command-line interface for users to check package statuses at specific times or overall package statuses, based on user input.

6. Dynamic Address Update: Updates the address of Package #9 based on the time of day, simulating a real-world scenario where package addresses may change.

7. Total Mileage Calculation: Calculates the total mileage covered by all trucks to deliver all packages.
