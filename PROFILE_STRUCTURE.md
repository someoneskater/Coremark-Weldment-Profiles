# Coremark Weldment Profile Structure

## Overview
This repository contains SolidWorks weldment profiles with integrated pricing and specification data for 558 structural shapes from Coremark Metals.

## Required Profile Properties

Each profile must include the following properties:

### 1. **size**
- **Type:** String
- **Description:** Profile dimensional size
- **Example:** `"2x2"`, `"1x3"`, `"4x6"`

### 2. **thickness**
- **Type:** String
- **Description:** Wall thickness of the profile
- **Example:** `"0.125"`, `"0.25"`, `"3/16"`

### 3. **price**
- **Type:** Number
- **Description:** Current price per unit (typically per foot or per piece)
- **Example:** `25.50`

### 4. **cost_per_lb**
- **Type:** Number
- **Description:** Cost per pound of material
- **Example:** `1.25`

### 5. **weight_per_ft**
- **Type:** Number
- **Description:** Weight per linear foot in pounds
- **Example:** `3.65`

### 6. **sku**
- **Type:** String
- **Description:** SKU or part number for ordering
- **Example:** `"STEEL-SQ-2X2-125"`

## Implementation

### For SolidWorks Profiles (.sldlfp files)
Add these properties as Custom Properties in the SolidWorks file:
1. Open the profile in SolidWorks
2. Go to File > Properties
3. Click the Custom tab
4. Add each property with its corresponding value

### For Profile Metadata (JSON format)
Profile data can also be stored in JSON format following the schema defined in `profile-schema.json`:

```json
{
  "size": "2x2",
  "thickness": "0.125",
  "price": 25.50,
  "cost_per_lb": 1.25,
  "weight_per_ft": 3.65,
  "sku": "STEEL-SQ-2X2-125"
}
```

## Directory Structure

```
Coremark-Weldment-Profiles/
├── profile-schema.json          # JSON schema definition
├── PROFILE_STRUCTURE.md          # This documentation
├── profiles/                     # Profile data directory
│   ├── steel/                    # Steel profiles
│   │   ├── angle/
│   │   ├── channel/
│   │   ├── tube-square/
│   │   └── tube-rectangular/
│   ├── aluminum/                 # Aluminum profiles
│   │   ├── angle/
│   │   ├── channel/
│   │   └── tube/
│   └── stainless/                # Stainless steel profiles
│       ├── angle/
│       └── tube/
└── README.md
```

## Validation

A validation script is provided to ensure all profile files meet the requirements:

```bash
python3 validate-profiles.py
```

This script checks that:
- All JSON files are properly formatted
- Each profile contains all six required properties
- Data types are correct (strings for size/thickness/sku, numbers for price/cost_per_lb/weight_per_ft)
- Numeric values are non-negative

## Usage

When creating or updating profiles, ensure all six required properties are present and properly formatted according to the schema. Run the validation script to verify your changes.
