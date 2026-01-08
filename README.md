# Coremark-Weldment-Profiles

SolidWorks weldment profile library from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Currently Available Profiles

### Steel Profiles

#### Steel Equal Leg Angles
- **Count:** 58 profiles
- **Sizes:** 1/2" to 8" leg dimensions
- **Thickness:** 1/8" to 1" wall thickness
- **Price Range:** $19 - $1,987 per 20-foot length
- **Material:** ASTM A36 Hot Rolled Steel
- **Location:** `Coremark Metals/Steel/Angle/`
- **Documentation:** See [Angle/README.md](Coremark%20Metals/Steel/Angle/README.md) for details

## Directory Structure

```
Coremark Metals/
└── Steel/
    └── Angle/
        ├── README.md - Usage instructions and setup guide
        ├── CATALOG.md - Complete specifications and pricing
        ├── PROFILE_INDEX.md - Detailed profile list with all sizes
        └── [Profile files will be .SLDLFP format]
```

## Using This Library

### Setup in SolidWorks

1. **Add Library Location:**
   - Open SolidWorks
   - Go to **Tools > Options > System Options > File Locations**
   - Select **Weldment Profiles** from dropdown
   - Click **Add** and browse to the repository root directory
   - Click **OK**

2. **Use Profiles:**
   - Create/open a part or assembly
   - Insert **Weldment** feature
   - Use **Structural Member** tool
   - Select **Coremark Metals** as Standard
   - Choose profile type and size

### Features

- Industry-standard ASTM specifications
- Integrated weight calculations (lbs/ft)
- Real pricing data from Coremark Metals
- Standard 20-foot stock lengths
- Complete dimensional data

## Material Specifications

### Steel Profiles
- **Grade:** ASTM A36 Hot Rolled Steel
- **Yield Strength:** 47,700 psi
- **Tensile Strength:** 58,000 psi
- **Properties:** Weldable, formable, machinable
- **Finish:** Mill Finish

## Additional Information

For detailed specifications, dimensions, weights, and pricing:
- See individual profile type README files
- Refer to CATALOG.md files for complete listings
- Visit [Coremark Metals](https://www.coremarkmetals.com/) for current availability

## Notes

- Prices are approximate based on standard 20-foot lengths
- Actual prices vary with market conditions and order quantity
- Custom cuts and lengths available from supplier
- .SLDLFP files must be created using SolidWorks software
