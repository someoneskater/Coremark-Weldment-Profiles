# CLAUDE.md - Coremark Weldment Profiles Project Documentation

## 📚 Project Overview

This document provides comprehensive technical documentation for the Coremark Weldment Profiles project, a SolidWorks automation solution for generating structural metal profile libraries.

### Purpose

The project automates the creation of SolidWorks weldment profile files (.sldlfp) for 734 structural metal profiles from Coremark Metals, including:
- Angles (L-shapes)
- Tubes (square and rectangular)
- Channels (C-sections)
- Beams (I-sections)
- Pipes (round)
- Flat bars

### Key Features

- **Automated Profile Generation**: Scripts to generate hundreds of profiles automatically
- **Multiple Interfaces**: Python (SolidWorks API) and VBA macro options
- **Comprehensive Data**: JSON database with dimensions, materials, and pricing
- **Material Varieties**: Steel, Aluminum, and Stainless Steel
- **Custom Properties**: Each profile includes metadata for easy identification
- **Extensible Design**: Easy to add new profiles or modify existing ones

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                               │
│  ┌───────────────────────────────────────────────────┐     │
│  │  profiles.json - Central Profile Database         │     │
│  │  - 734 profiles with dimensions                   │     │
│  │  - Material specifications                        │     │
│  │  - Pricing data                                   │     │
│  └───────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  Generation Layer                           │
│  ┌────────────────────────┐  ┌─────────────────────────┐   │
│  │  Python Script         │  │  VBA Macro              │   │
│  │  generate_profiles.py  │  │  GenerateProfiles.swp   │   │
│  │  - Uses SolidWorks API │  │  - Native VBA          │   │
│  │  - Batch processing    │  │  - Direct integration   │   │
│  │  - Command-line args   │  │  - Sample profiles      │   │
│  └────────────────────────┘  └─────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Output Layer                              │
│  ┌───────────────────────────────────────────────────┐     │
│  │  .sldlfp Files - SolidWorks Library Features      │     │
│  │  - 2D sketches defining cross-sections           │     │
│  │  - Custom properties embedded                     │     │
│  │  - Ready for weldment operations                 │     │
│  └───────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **SolidWorks**: CAD platform (2020+)
- **Python 3.7+**: Scripting and automation
- **win32com (pywin32)**: COM interface to SolidWorks API
- **VBA**: Alternative scripting approach
- **JSON**: Data storage format

## 📁 File Structure

```
Coremark-Weldment-Profiles/
│
├── data/
│   └── profiles.json                    # 734 profile definitions
│       ├── metadata                     # Library information
│       └── profiles[]                   # Array of profile objects
│
├── scripts/
│   ├── generate_profile_data.py         # Data generator
│   │   ├── generate_angle_profiles()
│   │   ├── generate_tube_profiles()
│   │   ├── generate_channel_profiles()
│   │   ├── generate_beam_profiles()
│   │   ├── generate_pipe_profiles()
│   │   └── generate_flat_bar_profiles()
│   │
│   ├── generate_profiles.py             # Main SolidWorks automation
│   │   ├── connect_to_solidworks()
│   │   ├── create_angle_profile()
│   │   ├── create_tube_profile()
│   │   ├── create_channel_profile()
│   │   ├── create_beam_profile()
│   │   ├── create_pipe_profile()
│   │   ├── create_flat_bar_profile()
│   │   └── generate_profiles()
│   │
│   └── GenerateProfiles.swp             # VBA macro alternative
│       ├── Main()
│       ├── GenerateSampleProfiles()
│       ├── CreateAngleProfile()
│       ├── CreateTubeProfile()
│       ├── CreatePipeProfile()
│       ├── CreateChannelProfile()
│       ├── CreateBeamProfile()
│       ├── CreateFlatBarProfile()
│       └── AddCustomProperties()
│
├── profiles/                            # Output directory
│   └── (generated .sldlfp files)
│
├── docs/
│   └── CLAUDE.md                        # This file
│
└── README.md                            # User documentation
```

## 🔍 Technical Details

### Profile Data Structure

Each profile in `profiles.json` follows this schema:

```json
{
  "id": "string",              // Unique identifier (e.g., "ANG-0001")
  "type": "string",            // Profile type (angle, tube, channel, beam, pipe, flat_bar)
  "subtype": "string",         // Subtype (equal, unequal, square, rectangular, etc.)
  "material": "string",        // Material type (Steel, Aluminum, Stainless Steel)
  "dimensions": {              // Type-specific dimensions
    // Varies by type
  },
  "name": "string",            // Human-readable name
  "price_per_foot": number     // Price in USD per linear foot
}
```

### Dimension Schemas by Type

#### Angles
```json
"dimensions": {
  "leg_a": number,      // First leg length (inches)
  "leg_b": number,      // Second leg length (inches)
  "thickness": number   // Wall thickness (inches)
}
```

#### Tubes
```json
"dimensions": {
  "width": number,      // Width (inches)
  "height": number,     // Height (inches)
  "thickness": number   // Wall thickness (inches)
}
```

#### Channels
```json
"dimensions": {
  "depth": number,      // Overall depth (inches)
  "width": number,      // Flange width (inches)
  "thickness": number   // Web/flange thickness (inches)
}
```

#### Beams
```json
"dimensions": {
  "depth": number,           // Overall depth (inches)
  "flange_width": number,    // Flange width (inches)
  "web_thickness": number,   // Web thickness (inches)
  "flange_thickness": number // Flange thickness (inches)
}
```

#### Pipes
```json
"dimensions": {
  "outer_diameter": number,  // Outer diameter (inches)
  "thickness": number        // Wall thickness (inches)
}
```

#### Flat Bars
```json
"dimensions": {
  "width": number,      // Width (inches)
  "thickness": number   // Thickness (inches)
}
```

## 🔧 Implementation Details

### Python Script Architecture

#### 1. SolidWorks Connection
```python
def connect_to_solidworks():
    pythoncom.CoInitialize()
    sw_app = win32com.client.Dispatch("SldWorks.Application")
    sw_app.Visible = True
    return sw_app
```

Key considerations:
- Requires COM initialization
- Must run on Windows
- SolidWorks must be installed and registered
- Application is made visible for user feedback

#### 2. Profile Generation Pattern

Each profile type follows this pattern:
1. Create new part document
2. Select sketch plane (Front Plane)
3. Insert sketch
4. Draw profile geometry using SketchManager
5. Exit sketch
6. Add custom properties
7. Save as .sldlfp file
8. Close document

#### 3. Sketch Generation

**Example: Angle Profile**
```python
# Draw L-shape from origin
points_outer = [
    (0, 0),                    # Inner corner
    (leg_a, 0),                # Bottom right
    (leg_a, thickness),        # Up
    (thickness, thickness),    # Left
    (thickness, leg_b),        # Up vertical leg
    (0, leg_b),                # Left to outer corner
    (0, 0)                     # Close
]

for i in range(len(points_outer) - 1):
    x1, y1 = points_outer[i]
    x2, y2 = points_outer[i + 1]
    sketch_mgr.CreateLine(x1, y1, 0, x2, y2, 0)
```

**Example: Tube Profile**
```python
# Centered rectangles
outer_w = width / 2
outer_h = height / 2
sketch_mgr.CreateCenterRectangle(0, 0, 0, outer_w, outer_h, 0)

inner_w = (width - 2 * thickness) / 2
inner_h = (height - 2 * thickness) / 2
sketch_mgr.CreateCenterRectangle(0, 0, 0, inner_w, inner_h, 0)
```

**Example: Pipe Profile**
```python
# Concentric circles
outer_radius = outer_diameter / 2
inner_radius = (outer_diameter - 2 * thickness) / 2
sketch_mgr.CreateCircleByRadius(0, 0, 0, outer_radius)
sketch_mgr.CreateCircleByRadius(0, 0, 0, inner_radius)
```

#### 4. Custom Properties

Each profile includes these properties:
- **Material**: Material type
- **Description**: Full profile name
- **Profile_ID**: Unique identifier
- **Price_Per_Foot**: Current pricing

```python
sw_model.Extension.CustomPropertyManager("").Add3("Material", 30, material, 2)
sw_model.Extension.CustomPropertyManager("").Add3("Description", 30, name, 2)
sw_model.Extension.CustomPropertyManager("").Add3("Profile_ID", 30, id, 2)
sw_model.Extension.CustomPropertyManager("").Add3("Price_Per_Foot", 30, str(price), 2)
```

### VBA Macro Implementation

The VBA macro provides similar functionality with these differences:
- Native SolidWorks integration
- No external dependencies
- Sample profiles only (full generation requires manual expansion)
- Easier for users familiar with VBA

#### Key VBA Functions

```vba
' Main entry point
Sub Main()
    Set swApp = Application.SldWorks
    Call GenerateSampleProfiles(swApp, outputDir)
End Sub

' Create profile template
Sub CreateAngleProfile(swApp, outputDir, profileID, material, legA, legB, thickness, price)
    ' Similar logic to Python but using VBA syntax
End Sub
```

## 📊 Profile Statistics

### Profile Distribution

| Type | Steel | Aluminum | Stainless | Total |
|------|-------|----------|-----------|-------|
| Angles | 59 | 59 | 59 | 177 |
| Tubes | 75 | 75 | 75 | 225 |
| Channels | 20 | 20 | 20 | 60 |
| Beams | 13 | 13 | 0 | 26 |
| Pipes | 35 | 35 | 35 | 105 |
| Flat Bars | 47 | 47 | 47 | 141 |
| **Total** | **249** | **249** | **236** | **734** |

### Size Ranges

**Angles**
- Equal: 1" × 1" to 8" × 8"
- Unequal: 2" × 1.5" to 8" × 6"
- Thickness: 0.125" to 1.0"

**Tubes**
- Square: 1" × 1" to 8" × 8"
- Rectangular: 2" × 1" to 8" × 6"
- Thickness: 0.065" to 0.625"

**Channels**
- Depth: 3" to 15"
- Width: 1.5" to 4"
- Thickness: 0.170" to 0.650"

**Beams**
- Depth: 3" to 24"
- Flange Width: 2.5" to 9.0"
- Web Thickness: 0.170" to 0.540"

**Pipes**
- Diameter: 0.5" to 8"
- Thickness: 0.065" to 0.322"

**Flat Bars**
- Width: 0.5" to 8"
- Thickness: 0.125" to 1.0"

## 🚀 Usage Scenarios

### Scenario 1: Generate All Profiles

```bash
cd scripts
python generate_profiles.py --output ../profiles
```

**Use Case**: Initial library setup  
**Time**: 30-60 minutes  
**Output**: 734 .sldlfp files

### Scenario 2: Generate Specific Types

```bash
python generate_profiles.py --types angle tube --output ../profiles
```

**Use Case**: Partial library update  
**Time**: 10-20 minutes  
**Output**: 402 .sldlfp files (angles + tubes)

### Scenario 3: Testing/Development

```bash
python generate_profiles.py --max 10 --output ../test_profiles
```

**Use Case**: Script testing and validation  
**Time**: 2-3 minutes  
**Output**: 10 .sldlfp files

### Scenario 4: VBA Macro (Sample Profiles)

1. Open SolidWorks
2. Tools > Macro > Edit
3. Open GenerateProfiles.swp
4. Run macro (F5)

**Use Case**: Quick setup without Python  
**Time**: 2-5 minutes  
**Output**: 17 sample .sldlfp files

## 🔐 API Reference

### Python Script Command-Line Interface

```
usage: generate_profiles.py [-h] [--json JSON] [--output OUTPUT] 
                             [--types TYPES [TYPES ...]] [--max MAX]

Generate SolidWorks weldment profiles

optional arguments:
  -h, --help            Show help message
  --json JSON           Path to profiles.json (default: ../data/profiles.json)
  --output OUTPUT       Output directory (default: ../profiles)
  --types TYPES [TYPES ...]
                        Profile types to generate
                        Options: angle, tube, channel, beam, pipe, flat_bar
  --max MAX            Maximum number of profiles to generate
```

### SolidWorks API Methods Used

#### Document Management
- `NewDocument(template, paper_size, width, height)` - Create new part
- `SaveAs3(filename, options, save_options)` - Save file
- `CloseDoc(filename)` - Close document

#### Sketch Operations
- `InsertSketch2(show_dialog)` - Start/exit sketch
- `SelectByID2(name, type, x, y, z, append, mark, callout, select_option)` - Select entity

#### Sketch Geometry
- `CreateLine(x1, y1, z1, x2, y2, z2)` - Draw line
- `CreateCenterRectangle(x, y, z, half_width, half_height, z2)` - Draw rectangle
- `CreateCircleByRadius(x, y, z, radius)` - Draw circle

#### Custom Properties
- `CustomPropertyManager(configuration)` - Get property manager
- `Add3(name, type, value, overwrite)` - Add property

## 🐛 Troubleshooting Guide

### Error: "Failed to connect to SolidWorks"

**Symptoms**: Python script fails at startup

**Causes**:
1. SolidWorks not installed
2. COM registration issues
3. Insufficient permissions

**Solutions**:
1. Verify SolidWorks installation
2. Run as Administrator
3. Re-register SolidWorks:
   ```
   regsvr32 "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\sldworks.exe"
   ```

### Error: "Module 'win32com' not found"

**Symptoms**: Python import error

**Solution**:
```bash
pip install pywin32
python Scripts/pywin32_postinstall.py -install
```

### Error: Template Not Found

**Symptoms**: "Failed to create document"

**Solution**: Update template path in script:
```python
# Find your SolidWorks version's template directory
template = "C:\\ProgramData\\SolidWorks\\SOLIDWORKS [VERSION]\\templates\\Part.prtdot"
```

### Slow Performance

**Symptoms**: Generation takes too long

**Solutions**:
1. Close other SolidWorks documents
2. Disable SolidWorks add-ins temporarily
3. Use `--max` parameter for testing
4. Generate in batches by type

### VBA Macro Path Errors

**Symptoms**: File not found errors in VBA

**Solution**: Update absolute paths in macro:
```vba
jsonPath = "C:\Full\Path\To\profiles.json"
outputDir = "C:\Full\Path\To\profiles\"
```

## 🔄 Extending the Library

### Adding New Profile Types

1. **Update Data Generator** (`generate_profile_data.py`):
```python
def generate_new_type_profiles():
    profiles = []
    # Generate profile data
    return profiles
```

2. **Add to Main Function**:
```python
new_profiles = generate_new_type_profiles()
all_profiles.extend(new_profiles)
```

3. **Create Profile Generator** (`generate_profiles.py`):
```python
def create_new_type_profile(sw_app, profile, output_dir):
    # Create sketch geometry
    # Add properties
    # Save file
    pass
```

4. **Register Generator**:
```python
profile_generators = {
    'new_type': create_new_type_profile,
    # ... existing types
}
```

### Modifying Size Ranges

Edit `generate_profile_data.py`:
```python
# Add new sizes to existing arrays
sizes = [
    (1, 1, 0.125),
    (1.5, 1.5, 0.125),  # New size
    # ...
]
```

### Custom Pricing Formulas

Modify pricing calculations:
```python
# Current formula
base_price = (leg_a + leg_b) * thickness * material_factor

# Custom formula example
base_price = calculate_weight(dimensions) * price_per_pound
```

## 📈 Performance Considerations

### Generation Time

| Profiles | Estimated Time |
|----------|----------------|
| 10 | 2-3 minutes |
| 50 | 10-15 minutes |
| 100 | 20-25 minutes |
| 734 (all) | 30-60 minutes |

### Memory Usage

- SolidWorks: 2-4 GB
- Python script: 50-100 MB
- Peak total: ~4-5 GB

### Optimization Tips

1. **Batch Processing**: Generate by type instead of all at once
2. **Template Caching**: Keep template open if possible
3. **Property Management**: Minimize custom property operations
4. **File I/O**: Use fast SSD for output directory

## 🧪 Testing

### Manual Testing

1. Generate sample profiles:
   ```bash
   python generate_profiles.py --max 5 --output ../test
   ```

2. Open SolidWorks

3. Insert > Weldments > Structural Member

4. Browse to test directory

5. Verify profiles appear and dimensions are correct

### Validation Checklist

- [ ] Profile sketch is closed and valid
- [ ] Dimensions match JSON data
- [ ] Custom properties are populated
- [ ] File naming is consistent
- [ ] Material is correct
- [ ] Profile works in weldment feature

## 📚 References

### SolidWorks API Documentation
- [API Help](https://help.solidworks.com/2024/english/api/sldworksapi/Welcome-SWHelp.html)
- [SketchManager Interface](https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
- [ModelDoc2 Interface](https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

### External Resources
- [Coremark Metals Product Catalog](https://www.coremarkmetals.com/)
- [Python for Windows Extensions](https://github.com/mhammond/pywin32)
- [SolidWorks Weldments Overview](https://help.solidworks.com/2024/english/solidworks/sldworks/c_weldments_overview.htm)

### Standards
- AISC (American Institute of Steel Construction)
- ASTM (American Society for Testing and Materials)
- Aluminum Association Standards

## 🔮 Future Enhancements

### Planned Features
1. GUI application for easier profile selection
2. CSV import/export for pricing updates
3. Automatic material property assignment
4. Cut list integration
5. BOM (Bill of Materials) templates
6. Multi-language support
7. Cloud-based profile library

### Potential Improvements
1. Parallel processing for faster generation
2. Profile validation and error checking
3. Automated testing framework
4. Web interface for profile browsing
5. Integration with ERP systems
6. Real-time pricing updates from Coremark API

## 📝 Version History

### Version 1.0 (Current)
- Initial release
- 734 profiles across 6 types
- Python and VBA scripts
- JSON data structure
- Complete documentation

### Roadmap

**Version 1.1** (Planned)
- Additional profile sizes
- Metric unit support
- Enhanced error handling

**Version 2.0** (Future)
- GUI application
- Database backend
- API integration

## 🤝 Contributing

### Development Setup

1. Fork repository
2. Create feature branch
3. Install dependencies
4. Make changes
5. Test with SolidWorks
6. Submit pull request

### Code Style

- **Python**: PEP 8
- **VBA**: Hungarian notation
- **JSON**: 2-space indentation
- **Comments**: Clear and descriptive

### Testing Requirements

- Test with at least 3 different profile types
- Verify custom properties
- Check dimension accuracy
- Ensure file naming consistency

## 📄 License and Legal

This project is provided for use with Coremark Metals profiles. Profile dimensions and pricing are subject to change. Always verify current specifications with Coremark Metals before production use.

### Disclaimer

The information provided in this library is for reference purposes. Users are responsible for verifying all dimensions and specifications before use in production environments.

---

**Document Version**: 1.0  
**Last Updated**: January 2024  
**Maintained By**: SolidWorks Automation Community  
**Contact**: Open an issue on GitHub for questions or suggestions