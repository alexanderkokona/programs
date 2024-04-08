def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    density_water = 998.2
    gravity = 9.80665
    return (density_water * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2
    pressure_loss = (-friction_factor * pipe_length * density_water * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2
    pressure_loss = (-0.04 * density_water * fluid_velocity ** 2 * quantity_fittings) / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_water = 998.2
    dynamic_viscosity = 0.0010016
    return (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    density_water = 998.2
    pressure_loss = (-k * density_water * fluid_velocity ** 2) / 2000
    return pressure_loss
