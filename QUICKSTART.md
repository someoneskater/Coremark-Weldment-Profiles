# Quick Start Guide

This guide will help you get started with generating SolidWorks weldment profiles.

## Prerequisites

1. **SolidWorks** must be installed on your Windows computer
2. **Python 3.7 or later** must be installed
3. Administrator rights may be needed to install Python packages

## Installation

1. Clone or download this repository
2. Open a command prompt in the repository directory
3. Install required packages:
   ```cmd
   pip install -r requirements.txt
   ```

## Basic Usage

### Generate All Profiles

To generate all 526 profiles (this will take 20-45 minutes):

```cmd
python generate_profiles.py
```

This will:
- Launch SolidWorks (or connect to running instance)
- Create 526 .sldlfp files in the `weldment_profiles` directory
- Organize them by Material > Shape > Size

### Generate Sample Profiles (Recommended for First Time)

To test the script with a small subset:

```cmd
python example_usage.py sample
```

This generates just 2 profiles of each shape type for testing.

### Generate Specific Material Only

To generate only Steel profiles:

```cmd
python example_usage.py material Steel
```

Replace `Steel` with `Aluminum` or `Stainless` as needed.

### Generate Specific Shape Only

To generate only Square Tube profiles:

```cmd
python example_usage.py shape "Square Tube"
```

## Output Structure

Generated files will be organized as:

```
weldment_profiles/
├── Steel/
│   ├── Angle/
│   │   ├── 1x1x1-8.sldlfp
│   │   ├── 2x2x1-4.sldlfp
│   │   └── ...
│   ├── Channel/
│   ├── Square_Tube/
│   ├── Rectangular_Tube/
│   ├── Round_Tube/
│   └── Flat_Bar/
├── Aluminum/
│   └── ...
└── Stainless/
    └── ...
```

## Adding Profiles to SolidWorks

After generation:

1. In SolidWorks, go to **Tools > Options**
2. Select **File Locations**
3. Select **Weldment Profiles** from dropdown
4. Click **Add** and browse to your `weldment_profiles` folder
5. Click **OK**
6. Restart SolidWorks

Your profiles will now appear in the Weldments feature!

## Customizing the Profile Data

You can edit `profiles_data.csv` to:
- Add new profiles
- Modify dimensions
- Update pricing
- Change materials

Then run the generator again to create the updated profiles.

## Troubleshooting

### "Failed to connect to SolidWorks"
- Make sure SolidWorks is installed
- Try running the command prompt as Administrator
- Close any open SolidWorks instances and try again

### "Module not found: win32com"
- Install the required package: `pip install pywin32`

### Generation is slow
- This is normal - each profile takes 2-5 seconds
- Consider generating specific materials or shapes first
- Use the sample generation for testing

### Profiles don't appear in SolidWorks
- Verify the file path is added in SolidWorks options
- Check that .sldlfp files were created
- Restart SolidWorks after adding the path

## Next Steps

- Review the generated profiles in SolidWorks
- Test using them in a weldment feature
- Customize the CSV data for your needs
- Share your custom profiles with your team

## Support

For issues or questions:
1. Check that all prerequisites are met
2. Review the main README.md for detailed information
3. Open an issue on GitHub with error details
