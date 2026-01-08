# Coremark Metals - Steel Equal Leg Angles

This directory contains SolidWorks weldment profile library files for A36 Hot Rolled Steel Equal Leg Angles from Coremark Metals.

## Directory Structure

```
Coremark Metals/
└── Steel/
    └── Angle/
        ├── README.md (this file - usage instructions)
        ├── CATALOG.md (complete specifications and pricing)
        ├── PROFILE_INDEX.md (detailed profile list)
        ├── [Size]x[Size]x[Thickness].SLDLFP (individual profile files)
```

## Available Profiles

This library includes **Steel Equal Leg Angles** with:
- **Sizes:** 1/2" to 8" leg dimensions
- **Thickness:** 1/8" to 1" wall thickness
- **Price Range:** $19 to $1,987 per 20-foot length

### Material Properties
- **Grade:** ASTM A36 Hot Rolled Steel
- **Yield Strength:** 47,700 psi
- **Tensile Strength:** 58,000 psi
- **Finish:** Mill Finish
- **Properties:** Weldable, formable, machinable

## Usage Instructions

### Setting Up in SolidWorks

1. **Configure Weldment Profile Location:**
   - Open SolidWorks
   - Go to **Tools > Options > System Options > File Locations**
   - Select **Weldment Profiles** from the dropdown
   - Click **Add** and browse to this directory's parent folder (the folder containing "Coremark Metals")
   - Click **OK** to save

2. **Using the Profiles:**
   - Create or open a SolidWorks part or assembly
   - Insert a **Weldment** feature
   - Use the **Structural Member** tool
   - In the dialog, select:
     - **Standard:** Coremark Metals
     - **Type:** Steel > Angle
     - **Size:** Choose from available equal leg angle sizes
   
3. **Profile Information:**
   - Each profile includes integrated pricing data and material properties
   - Weight per foot is included in the custom properties
   - Standard stock length is 20 feet (240 inches)

## Creating .SLDLFP Files

Since .SLDLFP files are binary SolidWorks files, they must be created using SolidWorks:

### Steps to Create a Profile:
1. Create a new SolidWorks part
2. Create a 2D sketch on the Front Plane
3. Draw the equal leg angle cross-section:
   - Two perpendicular legs meeting at a right angle
   - Include corner radius (typically 1/8" to 1/4" depending on size)
   - Inside corner fillet radius
4. Fully dimension the sketch
5. Center the sketch at the origin (important for proper alignment)
6. Save as Library Feature Part (.SLDLFP)
7. Set custom properties (Material, Weight, Price, etc.)
8. Save to the appropriate directory with naming convention: `[Size]x[Size]x[Thickness].SLDLFP`

### Naming Convention Examples:
- `0.5x0.5x0.125.SLDLFP` - 1/2" x 1/2" x 1/8"
- `1x1x0.25.SLDLFP` - 1" x 1" x 1/4"
- `2x2x0.1875.SLDLFP` - 2" x 2" x 3/16"
- `4x4x0.5.SLDLFP` - 4" x 4" x 1/2"
- `8x8x1.SLDLFP` - 8" x 8" x 1"

## Size Reference

For complete size specifications, weights, and pricing, see the [CATALOG.md](CATALOG.md) file in this directory.

## Support and Information

- **Supplier:** Coremark Metals
- **Website:** https://www.coremarkmetals.com/hot-rolled-steel-equal-leg-angle
- **Catalog:** https://www.coremarkmetals.com/metal-item-catalog

For questions about material availability, custom cuts, or volume pricing, contact Coremark Metals directly.

## Notes

- Prices are approximate and based on standard 20-foot lengths
- Actual prices may vary based on market conditions and order quantity
- Custom lengths and cuts are available from Coremark Metals
- All dimensions are in inches
- Weights are in pounds per linear foot
