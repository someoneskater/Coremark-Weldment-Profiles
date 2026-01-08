# Coremark-Weldment-Profiles
SolidWorks weldment profile library with 558 profiles from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Product Lines

### Steel Square Tubes
- **Sizes**: 1" x 1" to 12" x 12"
- **Wall Thickness**: 16ga (0.065") to 1/2" (0.500")
- **Price Range**: $32 - $2,708 per 20ft length
- **Standards**: ASTM A500 Grade B (structural), ASTM A513 (mechanical)
- **Total Configurations**: 57+ size/thickness combinations

See [Coremark Metals/Steel/Square Tube](Coremark%20Metals/Steel/Square%20Tube/) for complete specifications.

### Available Materials

#### Steel
- Equal Leg Angles (1/2" to 8")
- Square Tubes (1" to 12")

#### Aluminum
- Angles 6061-T6 (3/4" to 8")

#### Stainless Steel
- Angles 304 (3/4" to 4")

## Repository Structure

```
Coremark Metals/
├── Steel/
│   └── Square Tube/
│       ├── README.md                    # Detailed product information
│       ├── steel-square-tubes.csv       # Tabular specifications and pricing
│       └── steel-square-tubes.json      # Programmatic access data
├── Aluminum/
└── Stainless Steel/
```

## Data Formats

Each product line includes:
- **README.md**: Human-readable documentation with specifications, applications, and ordering information
- **CSV files**: Spreadsheet-compatible data for easy import and analysis
- **JSON files**: Machine-readable structured data for programmatic access

## Usage

### For SolidWorks Users
The profiles are organized following SolidWorks weldment profile conventions:
- Standard (e.g., "Coremark Metals")
- Type (e.g., "Steel/Square Tube")
- Size (individual .sldlfp files - to be added)

### For Pricing and Specifications
Refer to the CSV and JSON files in each product directory for:
- Dimensions and sizes
- Wall thicknesses
- Weight per foot
- Material grades and standards
- Current pricing
- SKU numbers

## Technical Information

### Steel Square Tubes
- **Material**: Cold-formed carbon steel
- **Manufacturing**: Electric resistance welded (ERW)
- **Finish**: Mill finish, semi-smooth grey
- **Tolerances**: Wall thickness ±10%
- **Applications**: Structural frames, trailer fabrication, equipment frames, shelving

## Contact

For orders, custom requirements, or additional information:
- Visit: [Coremark Metals](https://www.coremarkmetals.com/)
- Product Line: Mechanical/Structural Steel Square Tube
