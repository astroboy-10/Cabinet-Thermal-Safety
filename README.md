# Cabinet Thermal Safety System

This project implements a multi-layer thermal safety system for an electrical enclosure using industrial components.

## Overview

The system ensures safe operation of a 400W enclosure heater using:

- Dual temperature controllers (control + safety)
- Mechanical thermal cut-out
- Contactor for power isolation

## System Architecture

- TC1 (RS 1241057) – Heating controller (NO)
- TC2 (RS 1241057) – Safety controller (NC)
- TS1 (RS 222-8229) – Thermal cut-out (70°C NC)
- KM1 (RS 277-8515) – Contactor (230V coil)
- H1 (RS 103-314) – Pfannenberg heater (400W)

## Components

| Component | Link |
|----------|------|
| Temperature Controller | https://uk.rs-online.com/web/p/temperature-controllers/1241057 |
| Thermal Cut-out | https://uk.rs-online.com/web/p/thermal-cutouts/2228229 |
| Contactor | https://uk.rs-online.com/web/p/contactors/2778515 |
| Heater | https://uk.rs-online.com/web/p/enclosure-heaters/0103314 |

## How It Works

1. TC1 controls heating (ON below 40°C)
2. TC2 acts as safety cutoff (OFF above 50°C)
3. TS1 provides hard cutoff at 70°C
4. KM1 isolates and switches heater power

## Safety Philosophy

- Fail-safe design using **NC safety devices**
- Redundant thermal protection
- Electrical isolation via contactor

## Documentation

- Full LaTeX report: `docs/thermal_safety_system.tex`
- Draw.io diagram: `diagrams/`
- Wiring and BOM: `hardware/`

## Future Improvements

- Add fan cooling system
- Add alarm/indicator LEDs
- Integrate PLC or microcontroller monitoring

## License
MIT License

Copyright (c) 2026 Gaurav

Permission is hereby granted, free of charge...
