"""
SolidWorks Weldment Profile Generator

This script generates .sldlfp (SolidWorks Library Feature Part) files for weldment profiles
using the SolidWorks API through win32com.client. It reads profile data from profiles_data.csv
and creates sketch geometry with custom properties for each profile.

Requirements:
- SolidWorks must be installed and accessible via COM
- Python packages: pywin32

Usage:
    python generate_profiles.py [--output-dir OUTPUT_DIR] [--template TEMPLATE]
"""

import win32com.client
import pythoncom
import os
import sys
import csv
import argparse
import time
from pathlib import Path


class SolidWorksProfileGenerator:
    """Generate SolidWorks weldment profile (.sldlfp) files."""
    
    def __init__(self, output_base_dir="weldment_profiles", template_path=None):
        """
        Initialize the SolidWorks profile generator.
        
        Args:
            output_base_dir: Base directory for output files
            template_path: Path to SolidWorks part template (optional)
        """
        self.output_base_dir = Path(output_base_dir)
        self.template_path = template_path
        self.sw_app = None
        self.sw_model = None
        
    def connect_to_solidworks(self):
        """Connect to SolidWorks application via COM."""
        try:
            print("Connecting to SolidWorks...")
            self.sw_app = win32com.client.Dispatch("SldWorks.Application")
            self.sw_app.Visible = True
            print(f"Connected to SolidWorks {self.sw_app.RevisionNumber()}")
            return True
        except Exception as e:
            print(f"Error connecting to SolidWorks: {e}")
            print("Please ensure SolidWorks is installed and not already running.")
            return False
    
    def create_new_part(self):
        """Create a new SolidWorks part document."""
        try:
            # Use template if provided, otherwise use default
            if self.template_path and os.path.exists(self.template_path):
                template = self.template_path
            else:
                # Try to find default part template
                template = ""
            
            # Create new document
            # Arguments: template, paper_size, width, height
            self.sw_model = self.sw_app.NewDocument(template, 0, 0, 0)
            
            if self.sw_model is None:
                # If that failed, try getting a new part from the default template
                self.sw_model = self.sw_app.NewPart()
            
            return self.sw_model is not None
        except Exception as e:
            print(f"Error creating new part: {e}")
            return False
    
    def select_plane(self, plane_name="Front Plane"):
        """Select a plane for sketching."""
        try:
            # Get the active document
            doc = self.sw_app.ActiveDoc
            if doc is None:
                return False
            
            # Select the plane
            boolstatus = doc.Extension.SelectByID2(
                plane_name, "PLANE", 0, 0, 0, False, 0, None, 0
            )
            return boolstatus
        except Exception as e:
            print(f"Error selecting plane: {e}")
            return False
    
    def create_angle_profile(self, width, height, thickness):
        """
        Create an angle (L-shape) profile sketch.
        
        Args:
            width: Width of horizontal leg (inches)
            height: Height of vertical leg (inches)
            thickness: Thickness of material (inches)
        """
        try:
            doc = self.sw_app.ActiveDoc
            sketch_mgr = doc.SketchManager
            
            # Start sketch
            sketch_mgr.InsertSketch(True)
            
            # Convert inches to meters for SolidWorks (SolidWorks uses meters internally)
            w = width * 0.0254
            h = height * 0.0254
            t = thickness * 0.0254
            
            # Draw outer profile (L-shape)
            # Starting from origin, going clockwise
            sketch_mgr.CreateLine(0, 0, 0, w, 0, 0)  # Bottom horizontal
            sketch_mgr.CreateLine(w, 0, 0, w, t, 0)  # Right vertical (short)
            sketch_mgr.CreateLine(w, t, 0, t, t, 0)  # Top horizontal (short)
            sketch_mgr.CreateLine(t, t, 0, t, h, 0)  # Left vertical (tall)
            sketch_mgr.CreateLine(t, h, 0, 0, h, 0)  # Top horizontal (full width)
            sketch_mgr.CreateLine(0, h, 0, 0, 0, 0)  # Left vertical back to origin
            
            # Exit sketch
            sketch_mgr.InsertSketch(True)
            
            return True
        except Exception as e:
            print(f"Error creating angle profile: {e}")
            return False
    
    def create_channel_profile(self, height, width, web_thickness, flange_thickness):
        """
        Create a channel (C-shape) profile sketch.
        
        Args:
            height: Height of channel (inches)
            width: Width of flanges (inches)
            web_thickness: Thickness of web (inches)
            flange_thickness: Thickness of flanges (inches)
        """
        try:
            doc = self.sw_app.ActiveDoc
            sketch_mgr = doc.SketchManager
            
            sketch_mgr.InsertSketch(True)
            
            # Convert to meters
            h = height * 0.0254
            w = width * 0.0254
            wt = web_thickness * 0.0254
            ft = flange_thickness * 0.0254
            
            # Draw C-shape starting from origin
            sketch_mgr.CreateLine(0, 0, 0, w, 0, 0)  # Bottom flange
            sketch_mgr.CreateLine(w, 0, 0, w, ft, 0)  # Bottom flange inner
            sketch_mgr.CreateLine(w, ft, 0, wt, ft, 0)  # Bottom inner horizontal
            sketch_mgr.CreateLine(wt, ft, 0, wt, h - ft, 0)  # Web inner
            sketch_mgr.CreateLine(wt, h - ft, 0, w, h - ft, 0)  # Top inner horizontal
            sketch_mgr.CreateLine(w, h - ft, 0, w, h, 0)  # Top flange inner
            sketch_mgr.CreateLine(w, h, 0, 0, h, 0)  # Top flange
            sketch_mgr.CreateLine(0, h, 0, 0, 0, 0)  # Web outer back to origin
            
            sketch_mgr.InsertSketch(True)
            return True
        except Exception as e:
            print(f"Error creating channel profile: {e}")
            return False
    
    def create_square_tube_profile(self, width, height, wall_thickness):
        """
        Create a square/rectangular tube profile sketch.
        
        Args:
            width: Outer width (inches)
            height: Outer height (inches)
            wall_thickness: Wall thickness (inches)
        """
        try:
            doc = self.sw_app.ActiveDoc
            sketch_mgr = doc.SketchManager
            
            sketch_mgr.InsertSketch(True)
            
            # Convert to meters
            w = width * 0.0254
            h = height * 0.0254
            t = wall_thickness * 0.0254
            
            # Draw outer rectangle (centered at origin)
            x1 = -w / 2
            y1 = -h / 2
            x2 = w / 2
            y2 = h / 2
            
            # Outer rectangle
            sketch_mgr.CreateLine(x1, y1, 0, x2, y1, 0)  # Bottom
            sketch_mgr.CreateLine(x2, y1, 0, x2, y2, 0)  # Right
            sketch_mgr.CreateLine(x2, y2, 0, x1, y2, 0)  # Top
            sketch_mgr.CreateLine(x1, y2, 0, x1, y1, 0)  # Left
            
            # Inner rectangle (offset by wall thickness)
            xi1 = x1 + t
            yi1 = y1 + t
            xi2 = x2 - t
            yi2 = y2 - t
            
            sketch_mgr.CreateLine(xi1, yi1, 0, xi2, yi1, 0)  # Bottom
            sketch_mgr.CreateLine(xi2, yi1, 0, xi2, yi2, 0)  # Right
            sketch_mgr.CreateLine(xi2, yi2, 0, xi1, yi2, 0)  # Top
            sketch_mgr.CreateLine(xi1, yi2, 0, xi1, yi1, 0)  # Left
            
            sketch_mgr.InsertSketch(True)
            return True
        except Exception as e:
            print(f"Error creating square tube profile: {e}")
            return False
    
    def create_round_tube_profile(self, outer_diameter, inner_diameter):
        """
        Create a round tube profile sketch.
        
        Args:
            outer_diameter: Outer diameter (inches)
            inner_diameter: Inner diameter (inches)
        """
        try:
            doc = self.sw_app.ActiveDoc
            sketch_mgr = doc.SketchManager
            
            sketch_mgr.InsertSketch(True)
            
            # Convert to meters
            od = outer_diameter * 0.0254
            id_val = inner_diameter * 0.0254
            
            # Draw outer circle centered at origin
            sketch_mgr.CreateCircleByRadius(0, 0, 0, od / 2)
            
            # Draw inner circle
            sketch_mgr.CreateCircleByRadius(0, 0, 0, id_val / 2)
            
            sketch_mgr.InsertSketch(True)
            return True
        except Exception as e:
            print(f"Error creating round tube profile: {e}")
            return False
    
    def create_flat_bar_profile(self, width, thickness):
        """
        Create a flat bar (rectangular solid) profile sketch.
        
        Args:
            width: Width of bar (inches)
            thickness: Thickness of bar (inches)
        """
        try:
            doc = self.sw_app.ActiveDoc
            sketch_mgr = doc.SketchManager
            
            sketch_mgr.InsertSketch(True)
            
            # Convert to meters
            w = width * 0.0254
            t = thickness * 0.0254
            
            # Draw rectangle centered at origin
            x1 = -w / 2
            y1 = -t / 2
            x2 = w / 2
            y2 = t / 2
            
            sketch_mgr.CreateLine(x1, y1, 0, x2, y1, 0)  # Bottom
            sketch_mgr.CreateLine(x2, y1, 0, x2, y2, 0)  # Right
            sketch_mgr.CreateLine(x2, y2, 0, x1, y2, 0)  # Top
            sketch_mgr.CreateLine(x1, y2, 0, x1, y1, 0)  # Left
            
            sketch_mgr.InsertSketch(True)
            return True
        except Exception as e:
            print(f"Error creating flat bar profile: {e}")
            return False
    
    def add_custom_properties(self, properties):
        """
        Add custom properties to the part.
        
        Args:
            properties: Dictionary of property name/value pairs
        """
        try:
            doc = self.sw_app.ActiveDoc
            if doc is None:
                return False
            
            # Get custom property manager
            custom_prop_mgr = doc.Extension.CustomPropertyManager("")
            
            # Add each property
            for name, value in properties.items():
                # Property types: 30 = Text
                custom_prop_mgr.Add3(name, 30, str(value), 2)
            
            return True
        except Exception as e:
            print(f"Error adding custom properties: {e}")
            return False
    
    def save_as_sldlfp(self, output_path):
        """
        Save the current part as a .sldlfp file.
        
        Args:
            output_path: Full path where to save the file
        """
        try:
            doc = self.sw_app.ActiveDoc
            if doc is None:
                return False
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save as Library Feature Part
            # SaveAs3 arguments:
            #   FileName: output path
            #   SaveOptions: 0 = default save options
            #   Flags: 2 = silent mode (no prompts)
            errors = 0
            warnings = 0
            result = doc.SaveAs3(output_path, 0, 2)
            
            if result:
                print(f"  Saved: {output_path}")
                return True
            else:
                print(f"  Failed to save: {output_path}")
                return False
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def close_document(self):
        """Close the current document without saving."""
        try:
            if self.sw_app and self.sw_app.ActiveDoc:
                self.sw_app.CloseDoc(self.sw_app.ActiveDoc.GetTitle())
        except Exception as e:
            print(f"Error closing document: {e}")
    
    def generate_profile(self, profile_data):
        """
        Generate a single weldment profile.
        
        Args:
            profile_data: Dictionary containing profile specifications
        """
        material = profile_data['Material']
        shape = profile_data['Shape']
        size = profile_data['Size']
        
        print(f"\nGenerating: {material} {shape} {size}")
        
        # Create new part
        if not self.create_new_part():
            print("  Failed to create new part")
            return False
        
        # Select front plane for sketching
        if not self.select_plane("Front Plane"):
            print("  Failed to select plane")
            self.close_document()
            return False
        
        # Create appropriate sketch based on shape
        success = False
        try:
            if shape == "Angle":
                width = float(profile_data['Width'])
                height = float(profile_data['Height'])
                thickness = float(profile_data['Thickness'])
                success = self.create_angle_profile(width, height, thickness)
                
            elif shape == "Channel":
                height = float(profile_data['Height'])
                width = float(profile_data['Width'])
                web_thickness = float(profile_data['Web_Thickness'])
                flange_thickness = float(profile_data['Flange_Thickness'])
                success = self.create_channel_profile(height, width, web_thickness, flange_thickness)
                
            elif shape in ["Square Tube", "Rectangular Tube"]:
                width = float(profile_data['Width'])
                height = float(profile_data['Height'])
                wall_thickness = float(profile_data['Wall_Thickness'])
                success = self.create_square_tube_profile(width, height, wall_thickness)
                
            elif shape == "Round Tube":
                outer_diameter = float(profile_data['Outer_Diameter'])
                inner_diameter = float(profile_data['Inner_Diameter'])
                success = self.create_round_tube_profile(outer_diameter, inner_diameter)
            
            elif shape == "Flat Bar":
                width = float(profile_data['Width'])
                thickness = float(profile_data['Thickness'])
                success = self.create_flat_bar_profile(width, thickness)
            
            else:
                print(f"  Unknown shape: {shape}")
                self.close_document()
                return False
        except (KeyError, ValueError) as e:
            print(f"  Error with profile data: {e}")
            self.close_document()
            return False
        
        if not success:
            print("  Failed to create sketch")
            self.close_document()
            return False
        
        # Add custom properties
        properties = {
            'Material': material,
            'Shape': shape,
            'Size': size,
            'Weight_Per_Foot': profile_data.get('Weight_Per_Foot', ''),
            'Price_Per_Foot': profile_data.get('Price_Per_Foot', ''),
            'Manufacturer': 'Coremark Metals'
        }
        
        # Add dimensional properties based on shape
        if shape == "Angle":
            properties['Width'] = profile_data.get('Width', '')
            properties['Height'] = profile_data.get('Height', '')
            properties['Thickness'] = profile_data.get('Thickness', '')
        elif shape == "Channel":
            properties['Height'] = profile_data.get('Height', '')
            properties['Width'] = profile_data.get('Width', '')
            properties['Web_Thickness'] = profile_data.get('Web_Thickness', '')
            properties['Flange_Thickness'] = profile_data.get('Flange_Thickness', '')
        elif shape in ["Square Tube", "Rectangular Tube"]:
            properties['Width'] = profile_data.get('Width', '')
            properties['Height'] = profile_data.get('Height', '')
            properties['Wall_Thickness'] = profile_data.get('Wall_Thickness', '')
        elif shape == "Round Tube":
            properties['Outer_Diameter'] = profile_data.get('Outer_Diameter', '')
            properties['Inner_Diameter'] = profile_data.get('Inner_Diameter', '')
            properties['Wall_Thickness'] = profile_data.get('Wall_Thickness', '')
        elif shape == "Flat Bar":
            properties['Width'] = profile_data.get('Width', '')
            properties['Thickness'] = profile_data.get('Thickness', '')
        
        self.add_custom_properties(properties)
        
        # Construct output path
        # Structure: output_base_dir/Material/Shape/size.sldlfp
        shape_dir = shape.replace(" ", "_")
        output_dir = self.output_base_dir / material / shape_dir
        output_file = output_dir / f"{size.replace('/', '-')}.sldlfp"
        
        # Save the file
        success = self.save_as_sldlfp(str(output_file))
        
        # Close the document
        self.close_document()
        
        # Small delay to ensure SolidWorks is ready for next profile
        time.sleep(0.5)
        
        return success
    
    def generate_all_profiles(self, csv_file):
        """
        Generate all profiles from a CSV file.
        
        Args:
            csv_file: Path to CSV file containing profile data
        """
        if not os.path.exists(csv_file):
            print(f"Error: CSV file not found: {csv_file}")
            return
        
        # Read CSV file
        profiles = []
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            profiles = list(reader)
        
        print(f"Found {len(profiles)} profiles to generate")
        
        # Generate each profile
        success_count = 0
        fail_count = 0
        
        for i, profile in enumerate(profiles, 1):
            print(f"\n[{i}/{len(profiles)}]", end=" ")
            if self.generate_profile(profile):
                success_count += 1
            else:
                fail_count += 1
        
        print(f"\n\nGeneration complete!")
        print(f"Success: {success_count}")
        print(f"Failed: {fail_count}")
        print(f"Output directory: {self.output_base_dir.absolute()}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Generate SolidWorks weldment profiles from CSV data'
    )
    parser.add_argument(
        '--csv',
        default='profiles_data.csv',
        help='Path to CSV file containing profile data (default: profiles_data.csv)'
    )
    parser.add_argument(
        '--output-dir',
        default='weldment_profiles',
        help='Output directory for generated profiles (default: weldment_profiles)'
    )
    parser.add_argument(
        '--template',
        help='Path to SolidWorks part template (optional)'
    )
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = SolidWorksProfileGenerator(
        output_base_dir=args.output_dir,
        template_path=args.template
    )
    
    # Connect to SolidWorks
    if not generator.connect_to_solidworks():
        print("Failed to connect to SolidWorks. Exiting.")
        sys.exit(1)
    
    # Generate all profiles
    generator.generate_all_profiles(args.csv)


if __name__ == "__main__":
    main()
