from rocketpy import Environment, Rocket, SolidMotor

def get_environment():
    env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)
    env.set_date((2026, 11, 4, 12))
    env.set_atmospheric_model(type="standard_atmosphere")
    return env

def get_motor():
    return SolidMotor(
        thrust_source=1000,
        burn_time=3.0,
        grain_number=3,
        grain_density=1700,
        grain_outer_radius=0.035,
        grain_initial_inner_radius=0.015,
        grain_initial_height=0.12,
        grain_separation=0.005,
        grains_center_of_mass_position=0.25,
        center_of_dry_mass_position=0.25,
        nozzle_radius=0.015,
        throat_radius=0.0075,
        dry_mass=1.5,
        dry_inertia=(0.05, 0.05, 0.001),
        nozzle_position=0.0,
        coordinate_system_orientation="nozzle_to_combustion_chamber",
    )

def build_rocket(motor):
    rocket = Rocket(
        radius=0.04,
        mass=8.0,
        inertia=(0.15, 0.15, 0.005),
        power_off_drag=0.4,
        power_on_drag=0.4,
        center_of_mass_without_motor=0,
        coordinate_system_orientation="tail_to_nose",
    )
    rocket.add_motor(motor, position=-0.6)
    rocket.add_nose(length=0.4, kind="vonkarman", position=0.8)
    rocket.add_trapezoidal_fins(n=4, root_chord=0.15, tip_chord=0.05, span=0.10, position=-0.5)
    return rocket