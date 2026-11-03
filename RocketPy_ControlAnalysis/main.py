from rocketpy import Flight
from rocketpy.simulation import FlightDataExporter
from config import get_environment, get_motor, build_rocket
from controller import airbrake_controller

# 1. Setup Rocket & Environment
env = get_environment()
motor = get_motor()
rocket = build_rocket(motor)

# 2. Attach Airbrakes
air_brakes = rocket.add_air_brakes(
    drag_coefficient_curve=lambda deployment, mach: deployment * 0.8,
    controller_function=airbrake_controller,
    sampling_rate=10,
    name="Active Brakes",
)

# 3. Execute Simulation (time_overshoot=False required for discrete sampling)
flight = Flight(
    rocket=rocket,
    environment=env,
    rail_length=5.2,
    inclination=85,
    heading=0,
    time_overshoot=False,
)

# 4. Save Telemetry
exporter = FlightDataExporter(flight)
exporter.export_data("controlled_flight.csv", time_step=0.1)

print(f"Simulation Complete. Apogee: {flight.apogee:.2f} m")
flight.plots.trajectory_3d()