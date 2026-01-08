# Coremark Metals Weldment Profiles

SolidWorks weldment profile library with **613 profiles** from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes.

## Overview

This repository contains a comprehensive library of SolidWorks weldment profiles (.sldlfp files) for use with Coremark Metals structural products. The library includes:

- **349 Steel profiles** - ASTM A36, A992 structural steel
- **134 Aluminum profiles** - 6061-T6 and 6063-T5 alloys
- **130 Stainless Steel profiles** - 304/304L and 316/316L grades

## Profile Types Included

- **Angles** - Equal leg L-shapes for bracing and framing
- **Channels** - C-channels for structural support
- **Beams** - I-beams and W-shapes for load-bearing applications
- **Square Tubes** - HSS square sections
- **Rectangular Tubes** - HSS rectangular sections
- **Round Tubes** - Circular hollow sections
- **Pipes** - Schedule 40 and 80 pipes
- **Tees** - T-sections for stiffeners and supports

## Quick Start

1. **Download or clone this repository**
2. **Copy the `Coremark Metals` folder** to your SolidWorks weldment profiles directory
3. **Restart SolidWorks**
4. **Use the profiles** in Insert > Weldments > Structural Member

For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md)

## Documentation

- **[INSTALLATION.md](INSTALLATION.md)** - Complete installation guide for SolidWorks
- **[CATALOG.md](CATALOG.md)** - Full catalog of all 613 profiles with specifications

## Directory Structure

```
Coremark Metals/
├── Steel/
│   ├── Angle/ (48 profiles)
│   ├── Channel/ (30 profiles)
│   ├── Beam/ (66 profiles)
│   ├── Square Tube/ (55 profiles)
│   ├── Rectangular Tube/ (53 profiles)
│   ├── Round Tube/ (47 profiles)
│   ├── Pipe/ (24 profiles)
│   └── Tee/ (26 profiles)
├── Aluminum/
│   ├── Angle/ (25 profiles)
│   ├── Channel/ (14 profiles)
│   ├── Beam/ (13 profiles)
│   ├── Square Tube/ (21 profiles)
│   ├── Rectangular Tube/ (19 profiles)
│   ├── Round Tube/ (22 profiles)
│   ├── Pipe/ (11 profiles)
│   └── Tee/ (9 profiles)
└── Stainless Steel/
    ├── Angle/ (21 profiles)
    ├── Channel/ (14 profiles)
    ├── Beam/ (13 profiles)
    ├── Square Tube/ (19 profiles)
    ├── Rectangular Tube/ (17 profiles)
    ├── Round Tube/ (22 profiles)
    ├── Pipe/ (18 profiles)
    └── Tee/ (6 profiles)
```

## Requirements

- SolidWorks 2019 or later (recommended)
- Windows operating system
- Appropriate permissions to install profiles

## Materials Specifications

- **Steel:** ASTM A36 (general structural), A992 (wide flange beams)
- **Aluminum:** 6061-T6 (structural applications), 6063-T5 (architectural)
- **Stainless Steel:** 304/304L (general use), 316/316L (corrosive environments)

## Profile Naming Convention

Profiles follow standard industry nomenclature:

- **Angles:** `2x2x0.125` (leg x leg x wall thickness)
- **Channels:** `C6x10.5` (depth x weight per foot)
- **Beams:** `W12x35` (depth x weight per foot)
- **Tubes:** `4x4x0.250` (width x height x wall thickness)
- **Pipes:** `2-Sch40` (nominal size - schedule)

## Usage

1. Open SolidWorks and create or open a part file
2. Go to Insert > Weldments > Structural Member
3. In the PropertyManager:
   - **Standard:** Select "Coremark Metals"
   - **Type:** Choose your shape (Angle, Channel, Beam, etc.)
   - **Size:** Select the specific profile size
4. Select the sketch path for your structural member
5. Click OK to create the weldment

## Ordering Materials

When ordering materials from Coremark Metals:
- Use the profile size designation from this library
- Specify material grade (A36, 6061-T6, 304, etc.)
- Specify required length and quantity
- Visit [www.coremarkmetals.com](https://www.coremarkmetals.com) for current pricing and availability

## Contributing

To suggest additional profiles or report issues:
1. Open an issue in this repository
2. Provide the profile specification and material type
3. Include relevant standards (AISC, ASTM, etc.)

## License

These profile definitions are provided for use with Coremark Metals products. Always verify dimensions and specifications with current supplier catalogs before ordering materials.

## Support

- **Installation Help:** See [INSTALLATION.md](INSTALLATION.md)
- **Profile Reference:** See [CATALOG.md](CATALOG.md)
- **Material Specifications:** Contact Coremark Metals
- **SolidWorks Help:** Search "weldment profiles" in SolidWorks Help

## Acknowledgments

Profile dimensions based on:
- AISC Steel Construction Manual
- Aluminum Association Standards
- ASTM Material Specifications
- Coremark Metals product catalog

---

**Note:** The .sldlfp files in this repository are placeholder files with metadata. For production use in actual SolidWorks projects, these should be replaced with properly created SolidWorks Library Feature Part files containing accurate 2D cross-section sketches.
