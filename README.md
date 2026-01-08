# Coremark-Weldment-Profiles
SolidWorks weldment profile library with 558 profiles from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Available Profiles

### Stainless Steel
- **304 Equal Leg Angles**: 15 sizes from 3/4" to 4", prices $89-$1330 per foot

## Repository Structure

```
├── profiles-data.json           # Complete pricing and specification data
└── weldment profiles/           # SolidWorks weldment profile files
    ├── stainless/               # Stainless steel profiles
    │   └── angle/               # Equal leg angles (304 grade)
    ├── steel/                   # Carbon steel profiles (future)
    └── aluminum/                # Aluminum profiles (future)
```

## Usage

1. Clone this repository
2. Copy the desired profile files from `weldment profiles/` to your SolidWorks weldment profiles directory
3. In SolidWorks: Tools > Options > File Locations > Weldment Profiles
4. Add this directory to use the profiles in your weldment features

## Pricing Data

All profile specifications and pricing are available in `profiles-data.json`. Prices are per linear foot and sourced from Coremark Metals.

## Stainless Steel 304 Angles

Available sizes (equal leg):
- 3/4" x 3/4" x 1/8" - $89/ft
- 1" x 1" x 1/8" - $120/ft
- 1-1/4" x 1-1/4" x 1/8" - $165/ft
- 1-1/2" x 1-1/2" x 1/8" - $225/ft
- 1-1/2" x 1-1/2" x 3/16" - $310/ft
- 2" x 2" x 1/8" - $295/ft
- 2" x 2" x 3/16" - $420/ft
- 2" x 2" x 1/4" - $545/ft
- 2-1/2" x 2-1/2" x 3/16" - $535/ft
- 2-1/2" x 2-1/2" x 1/4" - $695/ft
- 3" x 3" x 3/16" - $650/ft
- 3" x 3" x 1/4" - $850/ft
- 3" x 3" x 3/8" - $1195/ft
- 4" x 4" x 1/4" - $1150/ft
- 4" x 4" x 3/8" - $1330/ft
