# Installation Guide

## Installing Coremark Metals Weldment Profiles in SolidWorks

This guide will help you install and configure the Coremark Metals weldment profile library in SolidWorks.

### Prerequisites
- SolidWorks 2019 or later recommended
- Windows operating system
- Administrative privileges (for system-wide installation)

### Installation Steps

#### Method 1: Copy to SolidWorks Default Location

1. **Locate your SolidWorks data folder:**
   - Default location (64-bit): `C:\ProgramData\SOLIDWORKS\SOLIDWORKS [Version]\lang\english\weldment profiles\`
   - Or check in SolidWorks: Tools > Options > System Options > File Locations > Weldment Profiles

2. **Copy the profile library:**
   - Copy the entire `Coremark Metals` folder from this repository
   - Paste it into your SolidWorks weldment profiles directory
   - Result: `[SolidWorks Path]\weldment profiles\Coremark Metals\`

3. **Restart SolidWorks** to ensure the profiles are loaded

#### Method 2: Custom Location (Recommended for Network/Shared Use)

1. **Choose a custom location:**
   - Local: `C:\Users\[YourName]\Documents\Weldment Profiles\`
   - Network: `\\NetworkShare\Engineering\Weldment Profiles\`

2. **Copy the library:**
   - Copy the entire `Coremark Metals` folder to your chosen location

3. **Configure SolidWorks:**
   - Open SolidWorks
   - Go to: Tools > Options > System Options > File Locations
   - Select "Weldment Profiles" from the dropdown
   - Click "Add..." and browse to your custom location
   - Click OK to save

4. **Restart SolidWorks**

### Using the Profiles

1. **Create a new part** or open an existing part

2. **Insert a weldment:**
   - Go to: Insert > Weldments > Structural Member
   - Or use the Weldments toolbar

3. **Select profile:**
   - In the Structural Member PropertyManager:
     - **Standard:** Select "Coremark Metals"
     - **Type:** Choose the shape type (Angle, Channel, Beam, etc.)
     - **Size:** Select the specific size from the dropdown

4. **Select path:**
   - Click on the sketch segments that will define the structural member path
   - Adjust settings as needed (corner treatment, trim/extend, etc.)

5. **Click OK** to create the structural member

### Profile Library Structure

```
Coremark Metals/
├── Steel/
│   ├── Angle/           (48 profiles)
│   ├── Channel/         (30 profiles)
│   ├── Beam/            (66 profiles)
│   ├── Square Tube/     (55 profiles)
│   ├── Rectangular Tube/(53 profiles)
│   ├── Round Tube/      (47 profiles)
│   ├── Pipe/            (24 profiles)
│   └── Tee/             (26 profiles)
├── Aluminum/
│   ├── Angle/           (25 profiles)
│   ├── Channel/         (14 profiles)
│   ├── Beam/            (13 profiles)
│   ├── Square Tube/     (21 profiles)
│   ├── Rectangular Tube/(19 profiles)
│   ├── Round Tube/      (22 profiles)
│   ├── Pipe/            (11 profiles)
│   └── Tee/             (9 profiles)
└── Stainless Steel/
    ├── Angle/           (21 profiles)
    ├── Channel/         (14 profiles)
    ├── Beam/            (13 profiles)
    ├── Square Tube/     (19 profiles)
    ├── Rectangular Tube/(17 profiles)
    ├── Round Tube/      (22 profiles)
    ├── Pipe/            (18 profiles)
    └── Tee/             (6 profiles)
```

**Total: 613 profiles**

### Material Specifications

- **Steel:** ASTM A36, A992, or equivalent structural steel
- **Aluminum:** 6061-T6 and 6063-T5 alloys
- **Stainless Steel:** 304/304L and 316/316L grades

### Troubleshooting

#### Profiles not appearing in SolidWorks

1. **Check file location:**
   - Verify the path in Tools > Options > File Locations > Weldment Profiles
   - Ensure the folder structure is correct (Standard > Type > Size.sldlfp)

2. **Restart SolidWorks:**
   - Close all SolidWorks instances completely
   - Restart the application

3. **Check file permissions:**
   - Ensure you have read access to the profile files
   - For network locations, verify network connectivity

4. **Verify folder structure:**
   - The structure must be exactly: `Coremark Metals/[Material]/[Type]/[Size].sldlfp`
   - Do not add extra folder levels

#### Profile sketches appear incorrect

- The placeholder files in this repository contain metadata only
- For actual use, these files should be replaced with properly created .sldlfp files
- Each .sldlfp should contain the correct 2D cross-section sketch

### Best Practices

1. **Backup your profiles:** Keep a copy of custom profile libraries before SolidWorks updates

2. **Use network locations:** For team environments, store profiles on a network share

3. **Version control:** Track changes to custom profiles using this Git repository

4. **Documentation:** Keep notes on custom modifications or additions to profiles

5. **Testing:** Always test a profile in a simple part before using in production models

### Support and Resources

- **Coremark Metals:** Visit [www.coremarkmetals.com](https://www.coremarkmetals.com) for current product catalogs
- **SolidWorks Help:** Search for "weldment profiles" in SolidWorks Help
- **Repository Issues:** Report problems or request additions via GitHub Issues

### Notes

- Profile dimensions follow industry standards (AISC, Aluminum Association)
- Wall thicknesses and dimensions match commonly available stock sizes
- Pricing data integration requires additional configuration (not included in base profiles)
- For production use, verify dimensions match current Coremark Metals catalog

### License

These profile definitions are provided for use with Coremark Metals products. Always verify dimensions and specifications with current supplier catalogs before ordering materials.
