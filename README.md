# Coremark-Weldment-Profiles

SolidWorks weldment profile library with 558 profiles from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Features

- **558 Structural Profiles** organized by material and shape type
- **Material Properties** including density, yield strength, and tensile strength
- **Integrated Pricing Data** with cost per pound, weight per foot, and total price
- **5 Profile Categories**:
  - Steel Equal Leg Angle (A36/A992/A500B)
  - Steel Square Tube (A500B)
  - Aluminum Angle (6061-T6)
  - Stainless Steel Angle (304)
  - Stainless Steel Square Tube (304)

## Installation

### Prerequisites

- SolidWorks 2016 or later
- Windows operating system

### Installation Instructions

1. **Locate SolidWorks Weldment Profiles Directory**
   
   The default SolidWorks weldment profiles location is typically:
   ```
   C:\ProgramData\SOLIDWORKS\SOLIDWORKS [version]\lang\english\weldment profiles\
   ```
   Or in your custom library location if configured in SolidWorks settings.

2. **Clone or Download Repository**
   ```bash
   git clone https://github.com/someoneskater/Coremark-Weldment-Profiles.git
   ```
   Or download as ZIP and extract to a temporary location.

3. **Copy Profile Files**
   
   Copy the desired profile files from the repository to your SolidWorks weldment profiles directory.
   
   Note: If you create custom SolidWorks library files (.SLDLFP), place them in organized subdirectories matching the profile types.

4. **Configure SolidWorks (Optional)**
   
   To set a custom weldment profiles location:
   - Open SolidWorks
   - Go to **Tools > Options > System Options > File Locations**
   - Select **Weldment Profiles** from the dropdown
   - Add your custom directory path
   - Click OK to save

5. **Restart SolidWorks**
   
   Restart SolidWorks to load the new weldment profiles.

## Usage

### Using Weldment Profiles in SolidWorks

1. **Create or Open a Part**
   - Open SolidWorks and create a new part or open an existing one

2. **Insert Weldment**
   - Go to **Insert > Weldments > Structural Member**
   - Or use the Structural Member tool from the Weldments toolbar

3. **Select Profile**
   - In the Structural Member PropertyManager, click **Browse** under Standard
   - Navigate to the Coremark profiles folder
   - Select the desired material type (Steel, Aluminum, or Stainless)
   - Choose the profile type (Angle, Square Tube, etc.)
   - Select the specific size profile

4. **Apply to Sketch Segments**
   - Select sketch segments to apply the structural member
   - Adjust corner treatments and orientation as needed
   - Click OK to create the weldment

### Accessing Pricing Data

The `data/profile_data.json` file contains comprehensive pricing and specification information:

```json
{
  "metadata": {
    "source": "Coremark Metals",
    "total_profiles": 558,
    "scrape_date": "2026-01-07"
  },
  "materials": {
    "steel_a36": {
      "density_lb_in3": 0.282,
      "yield_psi": 36000,
      "tensile_psi": 58000
    }
    // ... more materials
  },
  "profiles": {
    "steel_equal_leg_angle": [
      {
        "size": "2\" x 2\"",
        "thickness": "1/4\"",
        "length_inches": 240,
        "price": 81.66,
        "cost_per_lb": 1.28,
        "weight_per_ft": 3.19,
        "sku": "00261"
      }
      // ... more profiles
    ]
  }
}
```

This data can be used for:
- Cost estimation in BOM (Bill of Materials)
- Material property reference
- Inventory management integration
- Custom scripting and automation

## Folder Structure

```
Coremark-Weldment-Profiles/
├── README.md                 # This file - documentation and usage guide
└── data/
    └── profile_data.json     # Complete profile database with specs and pricing
```

### Data Structure

**profile_data.json** contains three main sections:

1. **metadata**: Source information, scrape date, and total profile count
2. **materials**: Material properties for all steel, aluminum, and stainless steel grades
   - Density (lb/in³)
   - Yield strength (psi)
   - Tensile strength (psi)
3. **profiles**: Organized by profile type, each entry includes:
   - Size dimensions
   - Wall thickness
   - Standard length (inches)
   - Current price
   - Cost per pound
   - Weight per foot
   - SKU number

### Available Profile Types

| Profile Type | Material | Count | Description |
|--------------|----------|-------|-------------|
| steel_equal_leg_angle | A36/A992/A500B | ~24 | Equal leg angle iron |
| steel_square_tube | A500B | ~100+ | Hollow structural square tubing |
| aluminum_angle_6061_t6 | 6061-T6 | ~100+ | Aluminum equal leg angle |
| stainless_angle_304 | 304 SS | ~100+ | Stainless steel equal leg angle |
| stainless_square_tube_304 | 304 SS | ~100+ | Stainless steel hollow square tube |

## Data Source

All profile dimensions, specifications, and pricing data sourced from:

**Coremark Metals**  
Website: [coremarkmetals.com](https://coremarkmetals.com)  
Data scraped: January 7, 2026

Pricing and availability subject to change. For current pricing, please visit the Coremark Metals website.

## License

Data sourced from publicly available Coremark Metals catalog. Please refer to their terms of service for commercial usage.

## Contributing

Contributions welcome! Please open an issue or submit a pull request for:
- Additional profile types
- Updated pricing data
- SolidWorks library files (.SLDLFP)
- Bug fixes or improvements
