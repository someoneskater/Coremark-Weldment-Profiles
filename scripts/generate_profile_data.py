"""
Generate comprehensive metal profile data for Coremark Metals library
Creates 734 profiles across different types and materials
"""
import json
import random

def generate_angle_profiles():
    """Generate L-shaped angle profiles"""
    profiles = []
    materials = ["Steel", "Aluminum", "Stainless Steel"]
    
    # Common angle sizes (leg x leg x thickness)
    sizes = [
        (1, 1, 0.125), (1, 1, 0.1875), (1.25, 1.25, 0.125), (1.25, 1.25, 0.1875),
        (1.5, 1.5, 0.125), (1.5, 1.5, 0.1875), (1.5, 1.5, 0.25),
        (2, 2, 0.125), (2, 2, 0.1875), (2, 2, 0.25), (2, 2, 0.3125),
        (2.5, 2.5, 0.1875), (2.5, 2.5, 0.25), (2.5, 2.5, 0.3125),
        (3, 3, 0.1875), (3, 3, 0.25), (3, 3, 0.3125), (3, 3, 0.375), (3, 3, 0.5),
        (4, 4, 0.25), (4, 4, 0.3125), (4, 4, 0.375), (4, 4, 0.5), (4, 4, 0.625),
        (5, 5, 0.3125), (5, 5, 0.375), (5, 5, 0.5), (5, 5, 0.625), (5, 5, 0.75),
        (6, 6, 0.375), (6, 6, 0.5), (6, 6, 0.625), (6, 6, 0.75), (6, 6, 0.875),
        (8, 8, 0.5), (8, 8, 0.625), (8, 8, 0.75), (8, 8, 0.875), (8, 8, 1.0)
    ]
    
    # Unequal angles
    unequal_sizes = [
        (2, 1.5, 0.1875), (2, 1.5, 0.25), (2.5, 2, 0.1875), (2.5, 2, 0.25),
        (3, 2, 0.1875), (3, 2, 0.25), (3, 2, 0.3125), (3.5, 2.5, 0.25),
        (4, 3, 0.25), (4, 3, 0.3125), (4, 3, 0.375), (5, 3, 0.3125),
        (5, 3.5, 0.375), (6, 4, 0.375), (6, 4, 0.5), (7, 4, 0.5),
        (8, 4, 0.5), (8, 6, 0.5), (8, 6, 0.625), (8, 6, 0.75)
    ]
    
    profile_id = 1
    for material in materials:
        for leg_a, leg_b, thickness in sizes:
            base_price = (leg_a + leg_b) * thickness * (1.5 if material == "Stainless Steel" else 1.2 if material == "Aluminum" else 1.0)
            profiles.append({
                "id": f"ANG-{profile_id:04d}",
                "type": "angle",
                "subtype": "equal" if leg_a == leg_b else "unequal",
                "material": material,
                "dimensions": {
                    "leg_a": leg_a,
                    "leg_b": leg_b,
                    "thickness": thickness
                },
                "name": f"Angle {leg_a}x{leg_b}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.5, 0.5), 2)
            })
            profile_id += 1
        
        for leg_a, leg_b, thickness in unequal_sizes:
            base_price = (leg_a + leg_b) * thickness * (1.5 if material == "Stainless Steel" else 1.2 if material == "Aluminum" else 1.0)
            profiles.append({
                "id": f"ANG-{profile_id:04d}",
                "type": "angle",
                "subtype": "unequal",
                "material": material,
                "dimensions": {
                    "leg_a": leg_a,
                    "leg_b": leg_b,
                    "thickness": thickness
                },
                "name": f"Angle {leg_a}x{leg_b}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.5, 0.5), 2)
            })
            profile_id += 1
    
    return profiles

def generate_tube_profiles():
    """Generate rectangular and square tube profiles"""
    profiles = []
    materials = ["Steel", "Aluminum", "Stainless Steel"]
    
    # Square tubes (size x size x thickness)
    square_sizes = [
        (1, 1, 0.065), (1, 1, 0.083), (1, 1, 0.120), (1, 1, 0.188),
        (1.25, 1.25, 0.065), (1.25, 1.25, 0.083), (1.25, 1.25, 0.120),
        (1.5, 1.5, 0.065), (1.5, 1.5, 0.083), (1.5, 1.5, 0.120), (1.5, 1.5, 0.188),
        (2, 2, 0.065), (2, 2, 0.083), (2, 2, 0.120), (2, 2, 0.188), (2, 2, 0.250),
        (2.5, 2.5, 0.083), (2.5, 2.5, 0.120), (2.5, 2.5, 0.188), (2.5, 2.5, 0.250),
        (3, 3, 0.083), (3, 3, 0.120), (3, 3, 0.188), (3, 3, 0.250), (3, 3, 0.3125),
        (4, 4, 0.120), (4, 4, 0.188), (4, 4, 0.250), (4, 4, 0.3125), (4, 4, 0.375),
        (5, 5, 0.188), (5, 5, 0.250), (5, 5, 0.3125), (5, 5, 0.375), (5, 5, 0.500),
        (6, 6, 0.188), (6, 6, 0.250), (6, 6, 0.3125), (6, 6, 0.375), (6, 6, 0.500),
        (8, 8, 0.250), (8, 8, 0.3125), (8, 8, 0.375), (8, 8, 0.500), (8, 8, 0.625)
    ]
    
    # Rectangular tubes
    rect_sizes = [
        (2, 1, 0.083), (2, 1, 0.120), (2, 1, 0.188), (2, 1.5, 0.083), (2, 1.5, 0.120),
        (3, 1, 0.083), (3, 1.5, 0.083), (3, 2, 0.083), (3, 2, 0.120), (3, 2, 0.188),
        (4, 2, 0.083), (4, 2, 0.120), (4, 2, 0.188), (4, 2, 0.250), (4, 3, 0.120),
        (5, 2, 0.120), (5, 3, 0.120), (5, 3, 0.188), (5, 3, 0.250), (6, 2, 0.120),
        (6, 3, 0.120), (6, 3, 0.188), (6, 4, 0.120), (6, 4, 0.188), (6, 4, 0.250),
        (8, 2, 0.188), (8, 4, 0.188), (8, 4, 0.250), (8, 6, 0.188), (8, 6, 0.250)
    ]
    
    profile_id = 1
    for material in materials:
        for width, height, thickness in square_sizes:
            base_price = (width + height) * 2 * thickness * (1.5 if material == "Stainless Steel" else 1.2 if material == "Aluminum" else 1.0)
            profiles.append({
                "id": f"TUB-{profile_id:04d}",
                "type": "tube",
                "subtype": "square",
                "material": material,
                "dimensions": {
                    "width": width,
                    "height": height,
                    "thickness": thickness
                },
                "name": f"Square Tube {width}x{height}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.5, 1.0), 2)
            })
            profile_id += 1
        
        for width, height, thickness in rect_sizes:
            base_price = (width + height) * 2 * thickness * (1.5 if material == "Stainless Steel" else 1.2 if material == "Aluminum" else 1.0)
            profiles.append({
                "id": f"TUB-{profile_id:04d}",
                "type": "tube",
                "subtype": "rectangular",
                "material": material,
                "dimensions": {
                    "width": width,
                    "height": height,
                    "thickness": thickness
                },
                "name": f"Rectangular Tube {width}x{height}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.5, 1.0), 2)
            })
            profile_id += 1
    
    return profiles

def generate_channel_profiles():
    """Generate C-channel profiles"""
    profiles = []
    materials = ["Steel", "Aluminum", "Stainless Steel"]
    
    # Standard channel sizes (depth x width x thickness)
    sizes = [
        (3, 1.5, 0.170), (3, 1.5, 0.258), (4, 1.75, 0.184), (4, 1.75, 0.321),
        (5, 2, 0.190), (5, 2, 0.325), (6, 2.25, 0.200), (6, 2.25, 0.314),
        (7, 2.5, 0.210), (7, 2.5, 0.419), (8, 2.75, 0.220), (8, 2.75, 0.487),
        (9, 3, 0.230), (9, 3, 0.413), (10, 3.25, 0.240), (10, 3.25, 0.526),
        (12, 3.5, 0.280), (12, 3.5, 0.510), (15, 4, 0.320), (15, 4, 0.650)
    ]
    
    profile_id = 1
    for material in materials:
        for depth, width, thickness in sizes:
            base_price = depth * width * thickness * (1.8 if material == "Stainless Steel" else 1.4 if material == "Aluminum" else 1.2)
            profiles.append({
                "id": f"CHN-{profile_id:04d}",
                "type": "channel",
                "subtype": "c_channel",
                "material": material,
                "dimensions": {
                    "depth": depth,
                    "width": width,
                    "thickness": thickness
                },
                "name": f"C-Channel {depth}x{width}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.5, 1.5), 2)
            })
            profile_id += 1
    
    return profiles

def generate_beam_profiles():
    """Generate I-beam profiles"""
    profiles = []
    materials = ["Steel", "Aluminum"]
    
    # I-beam sizes (depth x flange_width x web_thickness x flange_thickness)
    sizes = [
        (3, 2.5, 0.170, 0.260), (4, 2.66, 0.190, 0.293), (5, 3.0, 0.210, 0.326),
        (6, 3.33, 0.230, 0.359), (7, 3.66, 0.250, 0.392), (8, 4.0, 0.270, 0.425),
        (10, 4.66, 0.310, 0.491), (12, 5.0, 0.350, 0.557), (14, 6.0, 0.385, 0.623),
        (16, 7.0, 0.425, 0.689), (18, 7.5, 0.460, 0.755), (21, 8.0, 0.500, 0.821),
        (24, 9.0, 0.540, 0.887)
    ]
    
    profile_id = 1
    for material in materials:
        for depth, flange_width, web_thick, flange_thick in sizes:
            base_price = depth * flange_width * (web_thick + flange_thick) * (1.4 if material == "Aluminum" else 1.5)
            profiles.append({
                "id": f"BEM-{profile_id:04d}",
                "type": "beam",
                "subtype": "i_beam",
                "material": material,
                "dimensions": {
                    "depth": depth,
                    "flange_width": flange_width,
                    "web_thickness": web_thick,
                    "flange_thickness": flange_thick
                },
                "name": f"I-Beam {depth}x{flange_width} {material}",
                "price_per_foot": round(base_price + random.uniform(-1.0, 2.0), 2)
            })
            profile_id += 1
    
    return profiles

def generate_pipe_profiles():
    """Generate round pipe profiles"""
    profiles = []
    materials = ["Steel", "Aluminum", "Stainless Steel"]
    
    # Pipe sizes (outer_diameter x thickness)
    sizes = [
        (0.5, 0.065), (0.5, 0.109), (0.75, 0.065), (0.75, 0.113),
        (1, 0.065), (1, 0.109), (1, 0.133), (1.25, 0.065), (1.25, 0.109),
        (1.5, 0.065), (1.5, 0.109), (1.5, 0.145), (2, 0.065), (2, 0.109),
        (2, 0.154), (2.5, 0.083), (2.5, 0.120), (2.5, 0.188), (3, 0.083),
        (3, 0.120), (3, 0.216), (3.5, 0.083), (3.5, 0.120), (4, 0.083),
        (4, 0.120), (4, 0.226), (5, 0.109), (5, 0.134), (5, 0.258),
        (6, 0.109), (6, 0.134), (6, 0.280), (8, 0.148), (8, 0.250), (8, 0.322)
    ]
    
    profile_id = 1
    for material in materials:
        for diameter, thickness in sizes:
            base_price = diameter * thickness * 3.14159 * (1.6 if material == "Stainless Steel" else 1.3 if material == "Aluminum" else 1.1)
            profiles.append({
                "id": f"PIP-{profile_id:04d}",
                "type": "pipe",
                "subtype": "round",
                "material": material,
                "dimensions": {
                    "outer_diameter": diameter,
                    "thickness": thickness
                },
                "name": f"Round Pipe {diameter}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.3, 0.8), 2)
            })
            profile_id += 1
    
    return profiles

def generate_flat_bar_profiles():
    """Generate flat bar profiles"""
    profiles = []
    materials = ["Steel", "Aluminum", "Stainless Steel"]
    
    # Flat bar sizes (width x thickness)
    sizes = [
        (0.5, 0.125), (0.5, 0.25), (0.75, 0.125), (0.75, 0.1875), (0.75, 0.25),
        (1, 0.125), (1, 0.1875), (1, 0.25), (1, 0.375), (1.25, 0.125), (1.25, 0.25),
        (1.5, 0.125), (1.5, 0.1875), (1.5, 0.25), (1.5, 0.375), (1.5, 0.5),
        (2, 0.125), (2, 0.1875), (2, 0.25), (2, 0.375), (2, 0.5),
        (2.5, 0.25), (2.5, 0.375), (2.5, 0.5), (3, 0.1875), (3, 0.25),
        (3, 0.375), (3, 0.5), (3, 0.625), (4, 0.25), (4, 0.375),
        (4, 0.5), (4, 0.625), (4, 0.75), (5, 0.25), (5, 0.375),
        (5, 0.5), (5, 0.625), (5, 0.75), (6, 0.375), (6, 0.5),
        (6, 0.625), (6, 0.75), (6, 1.0), (8, 0.5), (8, 0.75), (8, 1.0)
    ]
    
    profile_id = 1
    for material in materials:
        for width, thickness in sizes:
            base_price = width * thickness * (1.4 if material == "Stainless Steel" else 1.1 if material == "Aluminum" else 0.9)
            profiles.append({
                "id": f"BAR-{profile_id:04d}",
                "type": "flat_bar",
                "subtype": "flat",
                "material": material,
                "dimensions": {
                    "width": width,
                    "thickness": thickness
                },
                "name": f"Flat Bar {width}x{thickness} {material}",
                "price_per_foot": round(base_price + random.uniform(-0.2, 0.5), 2)
            })
            profile_id += 1
    
    return profiles

def main():
    """Generate all profile data and save to JSON"""
    print("Generating metal profile data...")
    
    all_profiles = []
    
    print("Generating angles...")
    angles = generate_angle_profiles()
    all_profiles.extend(angles)
    print(f"  Generated {len(angles)} angle profiles")
    
    print("Generating tubes...")
    tubes = generate_tube_profiles()
    all_profiles.extend(tubes)
    print(f"  Generated {len(tubes)} tube profiles")
    
    print("Generating channels...")
    channels = generate_channel_profiles()
    all_profiles.extend(channels)
    print(f"  Generated {len(channels)} channel profiles")
    
    print("Generating beams...")
    beams = generate_beam_profiles()
    all_profiles.extend(beams)
    print(f"  Generated {len(beams)} beam profiles")
    
    print("Generating pipes...")
    pipes = generate_pipe_profiles()
    all_profiles.extend(pipes)
    print(f"  Generated {len(pipes)} pipe profiles")
    
    print("Generating flat bars...")
    flat_bars = generate_flat_bar_profiles()
    all_profiles.extend(flat_bars)
    print(f"  Generated {len(flat_bars)} flat bar profiles")
    
    print(f"\nTotal profiles generated: {len(all_profiles)}")
    
    # Create the final data structure
    data = {
        "metadata": {
            "version": "1.0",
            "description": "Coremark Metals Structural Profile Library",
            "profile_count": len(all_profiles),
            "materials": ["Steel", "Aluminum", "Stainless Steel"],
            "units": "inches",
            "price_unit": "USD per foot",
            "profile_types": {
                "angles": len(angles),
                "tubes": len(tubes),
                "channels": len(channels),
                "beams": len(beams),
                "pipes": len(pipes),
                "flat_bars": len(flat_bars)
            }
        },
        "profiles": all_profiles
    }
    
    # Save to JSON file
    output_file = "../data/profiles.json"
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nProfile data saved to {output_file}")

if __name__ == "__main__":
    main()
