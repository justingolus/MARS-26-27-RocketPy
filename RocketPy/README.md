# FILE LAYOUT

### 25_26_MoS_Parameters
  - Stores the values that change from rocket to rocket and what can be edited in our simulations
  - Launch site, rail length/angle, mass properties, aero surface geometry, motor data, parachutes, drag data files, air-brake settings and IREC stability limits
  - All units SI, all positions measured from the nose tip toward the tail
  - Loads the input files: AeroTech_M2500T.eng, RASAeroII Cd Data.xlsx, airbrake_cd.xlsx

### Environment_IREC_Launch_Site
  - Builds the launch environment (env) at the IREC site in Midland, TX
  - Sets location, date and atmosphere using the values from 25_26_MoS_Parameters
  - ATMOSPHERE_MODEL switches between the GFS weather forecast and the no-wind standard atmosphere (required for IREC stability results, DTEG 10.2.3)

### M2500T
  - Defines the AeroTech M2500T solid motor (M2500T)
  - Thrust curve, case mass/inertia and grain geometry so RocketPy can track mass and CG changes during the burn
  - Swap this file to fly a different motor

### AFC_Controller
  - Defines the air-brake control law (controller_function)
  - Predicts apogee during the coast and commands brake deployment toward the 10,000 ft target
  - Kept separate so control laws can be changed or compared without touching the rocket file

### Method_of_Sections
  - Defines the rocket (rocket) and air brakes (air_brakes)
  - Airframe, nose cone, fins, boat tail, rail buttons, motor mounting, parachutes and AFC hardware
  - Uses the motor from M2500T and the controller from AFC_Controller

### Test_Flight_MoS
  - Runs every file above in order and flies the rocket
  - Prints burnout and apogee conditions, RocketPy's built-in plots, and the air-brake history
  - Exports all flight data to flight_data.csv
  - Plots stability (% of rocket length) against the IREC limits, and altitude with burnout, apogee and air-brake deployment

# This year (2026/27)
  - Create new parameter file for this years rocket
  - import CFD data
  - Create new control algorithm
  - 
# HOW TO RUN
  - Keep all notebooks and input files in the same folder
  - Edit values in the notebook they live in, save, then run Test_Flight_MoS from the top
  - Any notebook can also be opened on its own; it loads the files it depends on automatically
