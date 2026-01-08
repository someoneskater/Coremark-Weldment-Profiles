"""
SolidWorks Weldment Profile Generator
Generates .sldlfp (SolidWorks Library Feature Part) files from profile data

This script uses the SolidWorks API to create weldment profile sketch files
based on the JSON profile data.

Requirements:
- SolidWorks must be installed
- Python for Windows (win32com library)
- Run on Windows with SolidWorks
"""

import json
import os
import sys
import math

try:
    import win32com.client
    import pythoncom
except ImportError:
    print("Warning: win32com not available. This script must run on Windows with SolidWorks installed.")
    print("Install with: pip install pywin32")

def connect_to_solidworks():
    """Connect to SolidWorks application"""
    try:
        pythoncom.CoInitialize()
        sw_app = win32com.client.Dispatch("SldWorks.Application")
        sw_app.Visible = True
        return sw_app
    except Exception as e:
        print(f"Error connecting to SolidWorks: {e}")
        print("Make sure SolidWorks is installed and registered.")
        return None

def create_angle_profile(sw_app, profile, output_dir):
    """Create L-shaped angle profile sketch"""
    try:
        # Create new part
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            print(f"Failed to create document for {profile['name']}")
            return False
        
        # Get dimensions
        leg_a = profile['dimensions']['leg_a']
        leg_b = profile['dimensions']['leg_b']
        thickness = profile['dimensions']['thickness']
        
        # Select Front plane for sketch
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        
        # Get sketch manager
        sketch_mgr = sw_model.SketchManager
        
        # Draw outer L-shape (counterclockwise from origin)
        # Outer corner at origin, extending in positive directions
        points_outer = [
            (0, 0),                    # Origin (inner corner)
            (leg_a, 0),                # Bottom right
            (leg_a, thickness),        # Up to horizontal leg
            (thickness, thickness),    # Left to vertical leg
            (thickness, leg_b),        # Up vertical leg
            (0, leg_b),                # Left to outer corner
            (0, 0)                     # Close shape
        ]
        
        # Create lines for L-shape
        for i in range(len(points_outer) - 1):
            x1, y1 = points_outer[i]
            x2, y2 = points_outer[i + 1]
            sketch_mgr.CreateLine(x1, y1, 0, x2, y2, 0)
        
        # Exit sketch
        sw_model.InsertSketch2(True)
        
        # Save as library feature part
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        # Set custom properties
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        # Save the file
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating angle profile {profile['name']}: {e}")
        return False

def create_tube_profile(sw_app, profile, output_dir):
    """Create rectangular or square tube profile sketch"""
    try:
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            return False
        
        width = profile['dimensions']['width']
        height = profile['dimensions']['height']
        thickness = profile['dimensions']['thickness']
        
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        sketch_mgr = sw_model.SketchManager
        
        # Draw outer rectangle centered at origin
        outer_w = width / 2
        outer_h = height / 2
        sketch_mgr.CreateCenterRectangle(0, 0, 0, outer_w, outer_h, 0)
        
        # Draw inner rectangle (offset by thickness)
        inner_w = (width - 2 * thickness) / 2
        inner_h = (height - 2 * thickness) / 2
        sketch_mgr.CreateCenterRectangle(0, 0, 0, inner_w, inner_h, 0)
        
        sw_model.InsertSketch2(True)
        
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating tube profile {profile['name']}: {e}")
        return False

def create_channel_profile(sw_app, profile, output_dir):
    """Create C-channel profile sketch"""
    try:
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            return False
        
        depth = profile['dimensions']['depth']
        width = profile['dimensions']['width']
        thickness = profile['dimensions']['thickness']
        
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        sketch_mgr = sw_model.SketchManager
        
        # Draw C-channel (centered on web)
        half_depth = depth / 2
        
        # Outer profile
        points = [
            (-width, -half_depth),
            (-width, half_depth),
            (-width + thickness, half_depth),
            (-width + thickness, -half_depth + thickness),
            (0, -half_depth + thickness),
            (0, -half_depth),
            (-width, -half_depth)
        ]
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            sketch_mgr.CreateLine(x1, y1, 0, x2, y2, 0)
        
        sw_model.InsertSketch2(True)
        
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating channel profile {profile['name']}: {e}")
        return False

def create_beam_profile(sw_app, profile, output_dir):
    """Create I-beam profile sketch"""
    try:
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            return False
        
        depth = profile['dimensions']['depth']
        flange_width = profile['dimensions']['flange_width']
        web_thick = profile['dimensions']['web_thickness']
        flange_thick = profile['dimensions']['flange_thickness']
        
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        sketch_mgr = sw_model.SketchManager
        
        # Draw I-beam (centered)
        half_depth = depth / 2
        half_flange = flange_width / 2
        half_web = web_thick / 2
        
        # Create I-shape
        points = [
            (-half_flange, -half_depth),
            (half_flange, -half_depth),
            (half_flange, -half_depth + flange_thick),
            (half_web, -half_depth + flange_thick),
            (half_web, half_depth - flange_thick),
            (half_flange, half_depth - flange_thick),
            (half_flange, half_depth),
            (-half_flange, half_depth),
            (-half_flange, half_depth - flange_thick),
            (-half_web, half_depth - flange_thick),
            (-half_web, -half_depth + flange_thick),
            (-half_flange, -half_depth + flange_thick),
            (-half_flange, -half_depth)
        ]
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            sketch_mgr.CreateLine(x1, y1, 0, x2, y2, 0)
        
        sw_model.InsertSketch2(True)
        
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating beam profile {profile['name']}: {e}")
        return False

def create_pipe_profile(sw_app, profile, output_dir):
    """Create round pipe profile sketch"""
    try:
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            return False
        
        outer_dia = profile['dimensions']['outer_diameter']
        thickness = profile['dimensions']['thickness']
        inner_dia = outer_dia - 2 * thickness
        
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        sketch_mgr = sw_model.SketchManager
        
        # Draw outer circle
        sketch_mgr.CreateCircleByRadius(0, 0, 0, outer_dia / 2)
        # Draw inner circle
        sketch_mgr.CreateCircleByRadius(0, 0, 0, inner_dia / 2)
        
        sw_model.InsertSketch2(True)
        
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating pipe profile {profile['name']}: {e}")
        return False

def create_flat_bar_profile(sw_app, profile, output_dir):
    """Create flat bar profile sketch"""
    try:
        sw_model = sw_app.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2024\\templates\\Part.prtdot", 0, 0, 0)
        if not sw_model:
            return False
        
        width = profile['dimensions']['width']
        thickness = profile['dimensions']['thickness']
        
        sw_model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        sw_model.InsertSketch2(True)
        sketch_mgr = sw_model.SketchManager
        
        # Draw rectangle centered at origin
        half_w = width / 2
        half_t = thickness / 2
        sketch_mgr.CreateCenterRectangle(0, 0, 0, half_w, half_t, 0)
        
        sw_model.InsertSketch2(True)
        
        filename = f"{profile['id']}_{profile['material'].replace(' ', '_')}.sldlfp"
        filepath = os.path.join(output_dir, filename)
        
        sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, profile['material'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, profile['name'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, profile['id'], 2)
        sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(profile['price_per_foot']), 2)
        
        errors = sw_model.SaveAs3(filepath, 0, 2)
        sw_app.CloseDoc(filepath)
        
        print(f"Created: {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating flat bar profile {profile['name']}: {e}")
        return False

def generate_profiles(json_file, output_dir, profile_types=None, max_profiles=None):
    """
    Generate SolidWorks library feature parts from JSON data
    
    Args:
        json_file: Path to profiles.json
        output_dir: Directory to save .sldlfp files
        profile_types: List of profile types to generate (None = all)
        max_profiles: Maximum number of profiles to generate (None = all)
    """
    # Load profile data
    print(f"Loading profile data from {json_file}...")
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    profiles = data['profiles']
    print(f"Loaded {len(profiles)} profiles")
    
    # Filter by type if specified
    if profile_types:
        profiles = [p for p in profiles if p['type'] in profile_types]
        print(f"Filtered to {len(profiles)} profiles of types: {profile_types}")
    
    # Limit number if specified
    if max_profiles:
        profiles = profiles[:max_profiles]
        print(f"Limited to {max_profiles} profiles")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    
    # Connect to SolidWorks
    print("\nConnecting to SolidWorks...")
    sw_app = connect_to_solidworks()
    if not sw_app:
        print("Failed to connect to SolidWorks. Exiting.")
        return
    
    print("Connected successfully!\n")
    
    # Generate profiles
    success_count = 0
    fail_count = 0
    
    profile_generators = {
        'angle': create_angle_profile,
        'tube': create_tube_profile,
        'channel': create_channel_profile,
        'beam': create_beam_profile,
        'pipe': create_pipe_profile,
        'flat_bar': create_flat_bar_profile
    }
    
    for i, profile in enumerate(profiles):
        print(f"\n[{i+1}/{len(profiles)}] Processing {profile['name']}...")
        
        profile_type = profile['type']
        generator_func = profile_generators.get(profile_type)
        
        if generator_func:
            try:
                if generator_func(sw_app, profile, output_dir):
                    success_count += 1
                else:
                    fail_count += 1
            except Exception as e:
                print(f"Error: {e}")
                fail_count += 1
        else:
            print(f"Unknown profile type: {profile_type}")
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"Generation complete!")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Total: {len(profiles)}")
    print(f"{'='*60}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate SolidWorks weldment profiles')
    parser.add_argument('--json', default='../data/profiles.json', help='Path to profiles.json')
    parser.add_argument('--output', default='../profiles', help='Output directory for .sldlfp files')
    parser.add_argument('--types', nargs='+', help='Profile types to generate (angle, tube, channel, beam, pipe, flat_bar)')
    parser.add_argument('--max', type=int, help='Maximum number of profiles to generate')
    
    args = parser.parse_args()
    
    generate_profiles(args.json, args.output, args.types, args.max)

if __name__ == "__main__":
    # Check if running on Windows
    if sys.platform != 'win32':
        print("Warning: This script is designed for Windows with SolidWorks installed.")
        print("It will not work on other platforms.")
    
    main()
