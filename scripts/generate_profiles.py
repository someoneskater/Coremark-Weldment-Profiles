"""
SolidWorks Weldment Profile Generator
Generates .sldlfp profile files from Coremark Metals scraped data
"""

import json
import os
import win32com.client
import pythoncom
from pathlib import Path

class ProfileGenerator:
      def __init__(self, data_path="data/profile_data.json"):
                with open(data_path, 'r') as f:
                              self.profiles = json.load(f)
                          self.sw_app = None

    def connect_solidworks(self):
              """Connect to running SolidWorks instance"""
              pythoncom.CoInitialize()
              self.sw_app = win32com.client.Dispatch("SldWorks.Application")
              self.sw_app.Visible = True
              return self.sw_app is not None

    def parse_dimensions(self, size_str):
              """Parse size string like '2" x 2" x 1/4"' into dimensions"""
              parts = size_str.replace('"', '').split(' x ')
              dims = []
              for p in parts:
                            p = p.strip()
                            if '/' in p:
                                              num, denom = p.split('/')
                                              dims.append(float(num) / float(denom))
else:
                dims.append(float(p))
          return dims

    def create_angle_profile(self, size, thickness, props, material):
              """Create L-shaped angle profile"""
              dims = self.parse_dimensions(size)
              if len(dims) < 3:
                            return None
                        leg1, leg2, thick = dims[0], dims[1], dims[2]

        model = self.sw_app.NewDocument(
                      self.sw_app.GetUserPreferenceStringValue(21),  # swDefaultTemplateLibFeatPart
                      0, 0, 0
        )
        model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        model.SketchManager.InsertSketch(True)

        # Draw L-shape (exterior)
        model.SketchManager.CreateLine(0, 0, 0, leg1 * 0.0254, 0, 0)
        model.SketchManager.CreateLine(leg1 * 0.0254, 0, 0, leg1 * 0.0254, thick * 0.0254, 0)
        model.SketchManager.CreateLine(leg1 * 0.0254, thick * 0.0254, 0, thick * 0.0254, thick * 0.0254, 0)
        model.SketchManager.CreateLine(thick * 0.0254, thick * 0.0254, 0, thick * 0.0254, leg2 * 0.0254, 0)
        model.SketchManager.CreateLine(thick * 0.0254, leg2 * 0.0254, 0, 0, leg2 * 0.0254, 0)
        model.SketchManager.CreateLine(0, leg2 * 0.0254, 0, 0, 0, 0)

        model.SketchManager.InsertSketch(True)

        # Add custom properties
        self._add_properties(model, props, material, size, thickness)

        return model

    def create_square_tube_profile(self, size, wall, props, material):
              """Create square tube profile (two nested rectangles)"""
        dims = self.parse_dimensions(size)
        if len(dims) < 2:
                      return None
                  outer = dims[0]
        wall_thick = self.parse_dimensions(wall)[0] if isinstance(wall, str) else wall
        inner = outer - 2 * wall_thick

        model = self.sw_app.NewDocument(
                      self.sw_app.GetUserPreferenceStringValue(21),
                      0, 0, 0
        )
        model.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        model.SketchManager.InsertSketch(True)

        # Outer rectangle
        model.SketchManager.CreateCenterRectangle(0, 0, 0, outer/2 * 0.0254, outer/2 * 0.0254, 0)
        # Inner rectangle
        model.SketchManager.CreateCenterRectangle(0, 0, 0, inner/2 * 0.0254, inner/2 * 0.0254, 0)

        model.SketchManager.InsertSketch(True)
        self._add_properties(model, props, material, size, wall)

        return model

    def _add_properties(self, model, props, material, size, thickness):
              """Add custom properties to the model"""
        cpm = model.Extension.CustomPropertyManager("")
        cpm.Add3("Material", 30, material, 2)
        cpm.Add3("Size", 30, size, 2)
        cpm.Add3("Thickness", 30, str(thickness), 2)
        cpm.Add3("Price", 30, str(props.get('price', '')), 2)
        cpm.Add3("Weight_Per_Ft", 30, str(props.get('weight_per_ft', '')), 2)
        cpm.Add3("SKU", 30, str(props.get('sku', '')), 2)
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
                            cat_folder = os.path.join(output_dir, category.replace(" ", "_"))

            for item in items:
                              size = item.get('size', '')
                              thickness = item.get('thickness', item.get('wall', ''))

                if 'angle' in category.lower():
                                      model = self.create_angle_profile(size, thickness, item, category)
elif 'tube' in category.lower() or 'square' in category.lower():
                      model = self.create_square_tube_profile(size, thickness, item, category)
else:
                      continue

                if model:
                                      fname = f"{size.replace('\"', '').replace(' ', '_')}_{thickness}.sldlfp"
                                      self.save_profile(model, cat_folder, fname)
                                      print(f"  Created: {fname}")

if __name__ == "__main__":
      gen = ProfileGenerator()
      gen.generate_all()
