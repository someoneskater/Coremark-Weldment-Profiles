"""
Example usage of the SolidWorks Profile Generator

This example demonstrates how to generate a subset of profiles
or customize the generation process.
"""

from generate_profiles import SolidWorksProfileGenerator
import csv

def generate_sample_profiles():
    """Generate a small sample of profiles for testing."""
    
    # Initialize generator
    generator = SolidWorksProfileGenerator(
        output_base_dir="sample_profiles",
        template_path=None  # Use default template
    )
    
    # Connect to SolidWorks
    if not generator.connect_to_solidworks():
        print("Failed to connect to SolidWorks")
        return
    
    # Read all profiles
    with open('profiles_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        all_profiles = list(reader)
    
    # Filter to just a few samples for testing
    # Let's take 2 of each shape type
    sample_profiles = []
    shapes_count = {}
    
    for profile in all_profiles:
        shape = profile['Shape']
        if shapes_count.get(shape, 0) < 2:
            sample_profiles.append(profile)
            shapes_count[shape] = shapes_count.get(shape, 0) + 1
    
    print(f"Generating {len(sample_profiles)} sample profiles...")
    
    # Generate each sample profile
    success_count = 0
    for i, profile in enumerate(sample_profiles, 1):
        print(f"\n[{i}/{len(sample_profiles)}]", end=" ")
        if generator.generate_profile(profile):
            success_count += 1
    
    print(f"\n\nSample generation complete!")
    print(f"Success: {success_count}/{len(sample_profiles)}")


def generate_by_material(material):
    """Generate profiles for a specific material only."""
    
    generator = SolidWorksProfileGenerator(
        output_base_dir=f"{material.lower()}_profiles"
    )
    
    if not generator.connect_to_solidworks():
        return
    
    # Filter profiles by material
    with open('profiles_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        profiles = [p for p in reader if p['Material'] == material]
    
    print(f"Generating {len(profiles)} {material} profiles...")
    
    success = 0
    for i, profile in enumerate(profiles, 1):
        print(f"\n[{i}/{len(profiles)}]", end=" ")
        if generator.generate_profile(profile):
            success += 1
    
    print(f"\n\nGeneration complete! Success: {success}/{len(profiles)}")


def generate_by_shape(shape):
    """Generate profiles for a specific shape only."""
    
    generator = SolidWorksProfileGenerator(
        output_base_dir=f"{shape.replace(' ', '_').lower()}_profiles"
    )
    
    if not generator.connect_to_solidworks():
        return
    
    # Filter profiles by shape
    with open('profiles_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        profiles = [p for p in reader if p['Shape'] == shape]
    
    print(f"Generating {len(profiles)} {shape} profiles...")
    
    success = 0
    for i, profile in enumerate(profiles, 1):
        print(f"\n[{i}/{len(profiles)}]", end=" ")
        if generator.generate_profile(profile):
            success += 1
    
    print(f"\n\nGeneration complete! Success: {success}/{len(profiles)}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "sample":
            # Generate sample profiles for testing
            generate_sample_profiles()
        
        elif command == "material" and len(sys.argv) > 2:
            # Generate profiles for specific material
            # Example: python example_usage.py material Steel
            material = sys.argv[2]
            generate_by_material(material)
        
        elif command == "shape" and len(sys.argv) > 2:
            # Generate profiles for specific shape
            # Example: python example_usage.py shape "Square Tube"
            shape = sys.argv[2]
            generate_by_shape(shape)
        
        else:
            print("Usage:")
            print("  python example_usage.py sample")
            print("  python example_usage.py material <Steel|Aluminum|Stainless>")
            print("  python example_usage.py shape <Shape Name>")
    else:
        print("Usage:")
        print("  python example_usage.py sample")
        print("  python example_usage.py material <Steel|Aluminum|Stainless>")
        print("  python example_usage.py shape <Shape Name>")
