# Coremark-Weldment-Profiles

SolidWorks weldment profile library with 558 profiles from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Overview

This repository contains a Python script that automatically generates SolidWorks weldment profile files (.sldlfp) for structural shapes from Coremark Metals. The profiles include:

- **Steel profiles**: Angles, Channels, Beams, Square Tubes, Rectangular Tubes, and Round Tubes
- **Aluminum profiles**: Angles, Channels, Square Tubes, Rectangular Tubes, and Round Tubes
- **Stainless Steel profiles**: Angles, Channels, Square Tubes, Rectangular Tubes, and Round Tubes

Each profile includes:
- Accurate 2D sketch geometry representing the cross-section
- Custom properties with material type, dimensions, weight per foot, and pricing data
- Proper organization in a folder structure by material and shape type

## Files

- `generate_profiles.py` - Main Python script that connects to SolidWorks via COM API and generates .sldlfp files
- `profiles_data.csv` - Database of 558 Coremark Metals profiles with dimensions and pricing
- `requirements.txt` - Python package dependencies

## Requirements

### Software
- **SolidWorks** (2019 or later recommended)
  - Must be installed on Windows
  - Must be accessible via COM automation
- **Python 3.7+**

### Python Packages
```bash
pip install -r requirements.txt
```

The main requirement is:
- `pywin32` - Provides Windows COM interface for controlling SolidWorks

## Usage

### Basic Usage

1. Ensure SolidWorks is installed on your Windows system
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python generate_profiles.py
   ```

This will:
- Connect to SolidWorks (will launch it if not already running)
- Read profile data from `profiles_data.csv`
- Generate .sldlfp files in the `weldment_profiles` directory
- Organize files by Material/Shape/size.sldlfp structure

### Advanced Usage

```bash
# Use a custom CSV file
python generate_profiles.py --csv my_profiles.csv

# Specify output directory
python generate_profiles.py --output-dir "C:\Custom\Weldment\Profiles"

# Use a custom SolidWorks part template
python generate_profiles.py --template "C:\Templates\MyTemplate.prtdot"

# Combine options
python generate_profiles.py --csv custom.csv --output-dir output --template template.prtdot
```

### Command Line Options

- `--csv` - Path to CSV file with profile data (default: profiles_data.csv)
- `--output-dir` - Output directory for generated profiles (default: weldment_profiles)
- `--template` - Path to SolidWorks part template (optional)

## Profile Data Format

The CSV file should have the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| Material | Material type | Steel, Aluminum, Stainless |
| Shape | Profile shape | Angle, Channel, Square Tube, etc. |
| Size | Size designation | 2x2x1/4, 1x1x1/8, etc. |
| Width | Width in inches | 2.0 |
| Height | Height in inches | 2.0 |
| Thickness | Material thickness (for angles) | 0.25 |
| Wall_Thickness | Wall thickness (for tubes) | 0.125 |
| Outer_Diameter | OD for round tubes | 1.5 |
| Inner_Diameter | ID for round tubes | 1.37 |
| Web_Thickness | Web thickness (for channels) | 0.17 |
| Flange_Width | Flange width (for channels) | 1.22 |
| Flange_Thickness | Flange thickness (for channels) | 0.17 |
| Weight_Per_Foot | Weight in lbs/ft | 1.65 |
| Price_Per_Foot | Price in $/ft | 2.48 |

## Output Structure

Generated files are organized as:
```
weldment_profiles/
├── Steel/
│   ├── Angle/
│   │   ├── 1x1x1-8.sldlfp
│   │   ├── 2x2x1-4.sldlfp
│   │   └── ...
│   ├── Channel/
│   ├── Square_Tube/
│   └── ...
├── Aluminum/
│   ├── Angle/
│   ├── Square_Tube/
│   └── ...
└── Stainless/
    └── ...
```

## Supported Profile Types

### Angle (L-Shape)
Equal leg angles with specified width, height, and thickness.

### Channel (C-Shape)
C-channels with web and flange dimensions.

### Square Tube
Hollow square tubing with outer dimensions and wall thickness.

### Rectangular Tube
Hollow rectangular tubing with width, height, and wall thickness.

### Round Tube
Circular hollow tubing with outer diameter, inner diameter, and wall thickness.

## Custom Properties

Each generated profile includes the following custom properties:
- **Material** - Steel, Aluminum, or Stainless
- **Shape** - Profile shape type
- **Size** - Size designation
- **Weight_Per_Foot** - Weight in lbs/ft
- **Price_Per_Foot** - Price in $/ft from Coremark Metals
- **Manufacturer** - Coremark Metals
- Dimensional properties specific to the shape type

## Installation in SolidWorks

After generating the profiles:

1. Copy the generated `weldment_profiles` folder to your SolidWorks weldment profiles directory
2. In SolidWorks, go to **Tools > Options > File Locations**
3. Select **Weldment Profiles** from the dropdown
4. Add the path to your generated profiles folder
5. Click OK and restart SolidWorks

The profiles will now be available in the weldment feature dialog.

## Troubleshooting

### SolidWorks doesn't connect
- Ensure SolidWorks is installed
- Try running the script as Administrator
- Close any open SolidWorks instances before running

### Profiles don't appear in SolidWorks
- Verify the folder structure matches: Standard/Type/Size.sldlfp
- Check that files have .sldlfp extension
- Restart SolidWorks after adding the profile path

### Generation is slow
- This is normal - creating files through COM automation takes time
- Expect 2-5 seconds per profile depending on system performance
- For 558 profiles, total time may be 20-45 minutes

## License

This project is provided as-is for creating weldment profiles from publicly available Coremark Metals catalog data.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for:
- Additional profile shapes
- Bug fixes
- Performance improvements
- Documentation updates

## References

- [Coremark Metals Catalog](https://www.coremarkmetals.com/)
- [SolidWorks Weldment Profiles Documentation](https://help.solidworks.com/)
