# Weldment Profiles Directory

This directory contains SolidWorks weldment profile files (.sldlfp) organized by material type.

## Directory Structure

```
weldment profiles/
├── stainless/          # Stainless steel profiles
│   └── angle/          # Angle profiles (equal leg)
├── steel/              # Carbon steel profiles (future)
└── aluminum/           # Aluminum profiles (future)
```

## Stainless Steel Angles - 304 Grade

### Available Sizes

The following stainless steel 304 equal leg angles are available:

| Size | Thickness | Price/ft |
|------|-----------|----------|
| 3/4 x 3/4 | 1/8" | $89 |
| 1 x 1 | 1/8" | $120 |
| 1-1/4 x 1-1/4 | 1/8" | $165 |
| 1-1/2 x 1-1/2 | 1/8" | $225 |
| 1-1/2 x 1-1/2 | 3/16" | $310 |
| 2 x 2 | 1/8" | $295 |
| 2 x 2 | 3/16" | $420 |
| 2 x 2 | 1/4" | $545 |
| 2-1/2 x 2-1/2 | 3/16" | $535 |
| 2-1/2 x 2-1/2 | 1/4" | $695 |
| 3 x 3 | 3/16" | $650 |
| 3 x 3 | 1/4" | $850 |
| 3 x 3 | 3/8" | $1195 |
| 4 x 4 | 1/4" | $1150 |
| 4 x 4 | 3/8" | $1330 |

### Profile Format

Weldment profiles are stored as .sldlfp (SolidWorks Library Feature Part) files. Each file contains:
- A 2D sketch defining the angle cross-section
- Dimension parameters for the profile
- Pierce point information for proper positioning

### Usage in SolidWorks

1. Copy the desired profile files to your SolidWorks weldment profiles directory
2. In SolidWorks, go to Tools > Options > File Locations > Weldment Profiles
3. Add this directory to the list of weldment profile locations
4. Create a new weldment feature and select from the available stainless angle profiles

### Pricing Information

All pricing data is maintained in the `profiles-data.json` file in the root directory. Prices are per linear foot and are subject to change based on market conditions.
