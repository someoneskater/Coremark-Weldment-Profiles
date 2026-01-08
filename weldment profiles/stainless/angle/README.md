# Stainless Steel 304 Equal Leg Angles

This directory will contain SolidWorks weldment profile files (.sldlfp) for stainless steel 304 equal leg angles.

## Profile Naming Convention

Profile files follow the naming pattern: `<size>x<size>x<thickness>.sldlfp`

Examples:
- `0.75x0.75x0.125.sldlfp` - 3/4" x 3/4" x 1/8" angle
- `1x1x0.125.sldlfp` - 1" x 1" x 1/8" angle
- `4x4x0.375.sldlfp` - 4" x 4" x 3/8" angle

## Available Profiles

The following 15 stainless steel 304 equal leg angle profiles are included:

1. 3/4" x 3/4" x 1/8" - $89/ft
2. 1" x 1" x 1/8" - $120/ft
3. 1-1/4" x 1-1/4" x 1/8" - $165/ft
4. 1-1/2" x 1-1/2" x 1/8" - $225/ft
5. 1-1/2" x 1-1/2" x 3/16" - $310/ft
6. 2" x 2" x 1/8" - $295/ft
7. 2" x 2" x 3/16" - $420/ft
8. 2" x 2" x 1/4" - $545/ft
9. 2-1/2" x 2-1/2" x 3/16" - $535/ft
10. 2-1/2" x 2-1/2" x 1/4" - $695/ft
11. 3" x 3" x 3/16" - $650/ft
12. 3" x 3" x 1/4" - $850/ft
13. 3" x 3" x 3/8" - $1195/ft
14. 4" x 4" x 1/4" - $1150/ft
15. 4" x 4" x 3/8" - $1330/ft

## Profile Details

Each .sldlfp file contains:
- A fully-defined 2D sketch of the angle cross-section
- Proper dimensions for leg length and thickness
- Pierce point at the inside corner for proper alignment
- Material properties for Stainless Steel 304

## Pricing

Prices listed are per linear foot. For complete pricing details and updates, refer to the `profiles-data.json` file in the repository root.

## Note

**The .sldlfp files need to be created using SolidWorks.** This directory documents the specifications and pricing for the profiles that should be created. To generate these files:

1. Open SolidWorks
2. Create a new part
3. Draw a 2D sketch of the angle profile with the specified dimensions
4. Save As > Lib Feat Part (*.sldlfp)
5. Save with the appropriate filename in this directory
