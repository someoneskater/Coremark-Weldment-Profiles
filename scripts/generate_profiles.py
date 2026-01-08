"""
SolidWorks Weldment Profile Generator
Generates .sldlfp profile files from Coremark Metals scraped data
Version 2.0 - Uses enhanced profile_data.json with complete geometry
"""

import json
import os
import win32com.client
import pythoncom
from pathlib import Path

# Conversion factor: inches to meters (SolidWorks uses meters internally)
IN_TO_M = 0.0254

class ProfileGenerator:
          def __init__(self, data_path="data/profile_data.json"):
                        with open(data_path, 'r') as f:
                                          self.data = json.load(f)
                                      self.profiles = self.data.get('profiles', {})
                        self.materials = self.data.get('materials', {})
                        self.geometry_standards = self.data.get('geometry_standards', {})
                        self.sw_app = None

    def connect_solidworks(self):
                  """Connect to running SolidWorks instance"""
                  pythoncom.CoInitialize()
                  self.sw_app = win32com.client.Dispatch("SldWorks.Application")
                  self.sw_app.Visible = True
                  return self.sw_app is not None

    def create_angle_profile(self, profile, category):
                  """Create L-shaped angle profile with proper fillet radii"""
                  # Extract dimensions from enhanced data structure
                  leg_a = profile.get('leg_a_in', 1.0) * IN_TO_M
                  leg_b = profile.get('leg_b_in', 1.0) * IN_TO_M
                  thickness = profile.get('thickness_in', 0.125) * IN_TO_M
                  inside_fillet = profile.get('inside_fillet_radius_in', thickness/IN_TO_M) * IN_TO_M
                  toe_radius = profile.get('toe_radius_in', thickness/IN_TO_M/2) * IN_TO_M

        # Create new document
                  model = self.sw_app.NewDocument(
                      self.sw_app.GetUserPreferenceStringValue(21),  # swDefaultTemplateLibFeatPart
                      0, 0, 0
                  )

        # Select front plane and start sketch
                  model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
                  model.SketchManager.InsertSketch(True)

        # Draw L-shape with fillets
                  # Outer profile
                  sketch = model.SketchManager

        # Start at origin, go right along leg_a
                  sketch.CreateLine(0, 0, 0, leg_a, 0, 0)
                  # Go up by thickness
                  sketch.CreateLine(leg_a, 0, 0, leg_a, thickness, 0)
                  # Go left to inside corner (minus fillet area)
                  sketch.CreateLine(leg_a, thickness, 0, thickness + inside_fillet, thickness, 0)

        # Inside fillet arc (90 degree arc)
                  sketch.CreateArc(thickness + inside_fillet, thickness + inside_fillet, 0,
                                   thickness + inside_fillet, thickness, 0,
                                   thickness, thickness + inside_fillet, 0, 1)

        # Go up leg_b
                  sketch.CreateLine(thickness, thickness + inside_fillet, 0, thickness, leg_b, 0)
                  # Go left by thickness
                  sketch.CreateLine(thickness, leg_b, 0, 0, leg_b, 0)
                  # Go down to origin
                  sketch.CreateLine(0, leg_b, 0, 0, 0, 0)

        model.SketchManager.InsertSketch(True)

        # Add custom properties
        self._add_properties(model, profile, category)

        return model

    def create_square_tube_profile(self, profile, category):
                  """Create square tube profile with corner radii"""
                  outer_dim = profile.get('outer_dim_in', 2.0) * IN_TO_M
                  wall = profile.get('wall_thickness_in', 0.125) * IN_TO_M
                  corner_outer = profile.get('corner_radius_outer_in', wall * 2) * IN_TO_M
                  corner_inner = profile.get('corner_radius_inner_in', wall) * IN_TO_M

        inner_dim = outer_dim - 2 * wall

        model = self.sw_app.NewDocument(
                          self.sw_app.GetUserPreferenceStringValue(21),
                          0, 0, 0
        )

        model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        model.SketchManager.InsertSketch(True)

        sketch = model.SketchManager

        # Outer rectangle with corner radii
        half_outer = outer_dim / 2
        half_inner = inner_dim / 2

        # Draw outer rounded rectangle
        self._draw_rounded_rectangle(sketch, -half_outer, -half_outer, 
                                                                         half_outer, half_outer, corner_outer)

        # Draw inner rounded rectangle (cutout)
        self._draw_rounded_rectangle(sketch, -half_inner, -half_inner,
                                                                         half_inner, half_inner, corner_inner)

        model.SketchManager.InsertSketch(True)
        self._add_properties(model, profile, category)

        return model

    def _draw_rounded_rectangle(self, sketch, x1, y1, x2, y2, radius):
                  """Draw a rounded rectangle in the sketch"""
                  r = radius
                  # Bottom edge
                  sketch.CreateLine(x1 + r, y1, 0, x2 - r, y1, 0)
        # Bottom-right corner
        sketch.CreateArc(x2 - r, y1 + r, 0, x2 - r, y1, 0, x2, y1 + r, 0, -1)
        # Right edge
        sketch.CreateLine(x2, y1 + r, 0, x2, y2 - r, 0)
        # Top-right corner
        sketch.CreateArc(x2 - r, y2 - r, 0, x2, y2 - r, 0, x2 - r, y2, 0, -1)
        # Top edge
        sketch.CreateLine(x2 - r, y2, 0, x1 + r, y2, 0)
        # Top-left corner
        sketch.CreateArc(x1 + r, y2 - r, 0, x1 + r, y2, 0, x1, y2 - r, 0, -1)
        # Left edge
        sketch.CreateLine(x1, y2 - r, 0, x1, y1 + r, 0)
        # Bottom-left corner
        sketch.CreateArc(x1 + r, y1 + r, 0, x1, y1 + r, 0, x1 + r, y1, 0, -1)

    def _add_properties(self, model, profile, category):
                  """Add custom properties to the model"""
                  cpm = model.Extension.CustomPropertyManager("")

        # Standard properties
                  cpm.Add3("Designation", 30, profile.get('designation', ''), 2)
        cpm.Add3("Size", 30, profile.get('size', ''), 2)
        cpm.Add3("Material", 30, profile.get('material', ''), 2)

        # Geometric properties
        if 'leg_a_in' in profile:
                          cpm.Add3("Leg_A", 30, str(profile['leg_a_in']), 2)
                          cpm.Add3("Leg_B", 30, str(profile['leg_b_in']), 2)
                      if 'outer_dim_in' in profile:
                                        cpm.Add3("Outer_Dimension", 30, str(profile['outer_dim_in']), 2)
                                    if 'thickness_in' in profile:
                                                      cpm.Add3("Thickness", 30, str(profile['thickness_in']), 2)
                                                  if 'wall_thickness_in' in profile:
                                                                    cpm.Add3("Wall_Thickness", 30, str(profile['wall_thickness_in']), 2)

        # Commercial properties
        cpm.Add3("Price", 30, str(profile.get('price', '')), 2)
        cpm.Add3("Weight_Per_Ft", 30, str(profile.get('weight_per_ft', '')), 2)
        cpm.Add3("SKU", 30, str(profile.get('sku', '')), 2)
        cpm.Add3("Source", 30, "Coremark Metals", 2)

    def save_profile(self, model, folder, filename):
                  """Save model as .sldlfp file"""
                  os.makedirs(folder, exist_ok=True)
                  filepath = os.path.join(folder, filename)
                  model.Extension.SaveAs(filepath, 0, 1, None, 0, 0)
                  model.Close()
                  return filepath

    def generate_all(self, output_dir="output"):
                  """Generate all profiles from loaded data"""
                  if not self.connect_solidworks():
                                    print("Failed to connect to SolidWorks")
                                    return

                  for category, items in self.profiles.items():
                                    print(f"Processing {category}...")
                                    cat_folder = os.path.join(output_dir, category)

            for profile in items:
                                  designation = profile.get('designation', profile.get('size', 'unknown'))

                try:
                                          if 'angle' in category.lower():
                                                                        model = self.create_angle_profile(profile, category)
elif 'tube' in category.lower() or 'square' in category.lower():
                        model = self.create_square_tube_profile(profile, category)
else:
                        print(f"  Skipping unknown type: {category}")
                              continue

                    if model:
                                                  fname = f"{designation.replace('/', '-').replace(' ', '_')}.sldlfp"
                                                  self.save_profile(model, cat_folder, fname)
                                                  print(f"  Created: {fname}")
except Exception as e:
                    print(f"  Error creating {designation}: {e}")

if __name__ == "__main__":
          gen = ProfileGenerator()
    gen.generate_all()
