# Thermal Simulation

This simulation models the cabinet temperature using a lumped thermal system.

## Model

C dT/dt = P - k(T - Tamb)

## Features

- Heater control logic (TC1, TC2)
- Thermal cut-out safety
- Time evolution of cabinet temperature

## Run

```bash
python thermal_model.py
