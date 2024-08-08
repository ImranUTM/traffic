def flow(speed=None, density=None, headway=None):
    if headway is not None:
        # Calculate flow using the inverse of headway
        return 1 / headway
    elif speed is not None and density is not None:
        # Calculate flow using speed and density
        return speed * density
    else:
        raise ValueError("Insufficient data provided. Provide either (speed and density) or (headway).")

# Example usage:

# Using speed and density
'''speed = int(input("v: "))  # speed in km/h
density = int(input("k: "))  # density in vehicles/km
flow1 = flow(speed=speed, density=density)
print(f"Traffic Flow (using speed and density): {flow1} vehicles/hour")'''

def density(speed=None, flow=None, spacing=None):
    if spacing is not None:
        # Calculate flow using the inverse of spacing
        return 1 / spacing
    elif speed is not None and flow is not None:
        # Calculate flow using speed and density
        return flow / speed
    else:
        raise ValueError("Insufficient data provided. Provide either (speed and density) or (headway).")
