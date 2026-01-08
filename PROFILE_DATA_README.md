# Profile Data JSON Documentation

This document describes the structure and usage of `profile_data.json`, which contains comprehensive data for 575 weldment profiles from Coremark Metals.

## Overview

The JSON file contains detailed specifications for metal structural profiles including:
- Steel angles, tubes, channels, and beams
- Aluminum profiles (6061-T6)
- Stainless steel profiles (304)
- Complete pricing and weight information

## File Structure

```json
{
  "metadata": {
    "total_profiles": 575,
    "supplier": "Coremark Metals",
    "last_updated": "2026-01-08",
    "price_basis": "20 ft lengths (unless otherwise specified)",
    "currency": "USD"
  },
  "profiles": [
    {
      "sku": "SA-1000",
      "type": "angle",
      "material": "Steel",
      "grade": "A36",
      "size": "0.5x0.5",
      "thickness": 0.125,
      "weight_per_ft": 0.5,
      "cost_per_lb": 0.88,
      "price": 8.75,
      "description": "Steel Angle 0.5\"x0.5\"x0.125\""
    },
    ...
  ]
}
```

## Profile Types

The data includes the following profile types:

| Type | Count | Description |
|------|-------|-------------|
| angle | 113 | Equal leg angles (L-shapes) |
| square_tube | 112 | Square hollow structural sections |
| wide_flange | 98 | I-beams (W-shapes) |
| flat_bar | 60 | Flat rectangular bars |
| rectangular_tube | 58 | Rectangular hollow sections |
| round_tube | 43 | Round hollow tubes |
| round_bar | 33 | Solid round bars |
| channel | 30 | C-channel sections |
| round_pipe | 28 | Round pipes (Schedule 40/80) |

## Materials

### Steel (366 profiles)
- **Grade A36**: Structural angles, flat bars
- **Grade A500 B**: Square and rectangular tubes
- **Grade A53 B**: Round pipes
- **Grade A992**: Wide flange beams
- **Grade 1018**: Round bars

### Aluminum (161 profiles)
- **Grade 6061-T6**: Angles, tubes, bars, and extrusions

### Stainless Steel (48 profiles)
- **Grade 304**: Angles, tubes, and bars

## Profile Fields

Each profile contains the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| sku | string | Yes | Unique product identifier |
| type | string | Yes | Profile type (angle, tube, etc.) |
| material | string | Yes | Material type (Steel, Aluminum, etc.) |
| grade | string | Yes | Material grade specification |
| size | string | Yes | Nominal size (e.g., "2x2", "4", "W12") |
| thickness | float | Yes* | Wall thickness or leg thickness (inches) |
| weight_per_ft | float | Yes | Weight per linear foot (pounds) |
| cost_per_lb | float | Yes | Cost per pound (USD) |
| price | float | Yes | Total price for standard length (USD) |
| description | string | Yes | Human-readable description |
| width | float | No | Width for flat bars |
| diameter | float | No | Diameter for round sections |
| schedule | string | No | Pipe schedule (for round pipes) |

*Note: Not all profiles have a thickness field (e.g., solid bars use diameter instead)

## Usage Examples

### Python Example

```python
import json

# Load the data
with open('profile_data.json', 'r') as f:
    data = json.load(f)

# Access metadata
print(f"Total profiles: {data['metadata']['total_profiles']}")

# Find all steel angles
steel_angles = [p for p in data['profiles'] 
                if p['material'] == 'Steel' and p['type'] == 'angle']

# Find profiles under $100
affordable = [p for p in data['profiles'] if p['price'] < 100]

# Search by SKU
profile = next(p for p in data['profiles'] if p['sku'] == 'SA-1000')
```

### JavaScript Example

```javascript
// Load the data
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('profile_data.json', 'utf8'));

// Filter aluminum profiles
const aluminumProfiles = data.profiles.filter(
  p => p.material === 'Aluminum'
);

// Find heaviest profile
const heaviest = data.profiles.reduce(
  (max, p) => p.weight_per_ft > max.weight_per_ft ? p : max
);

// Group by material
const byMaterial = data.profiles.reduce((acc, p) => {
  acc[p.material] = (acc[p.material] || 0) + 1;
  return acc;
}, {});
```

## Price Information

Prices are based on 20-foot lengths unless otherwise specified. To calculate custom lengths:

```python
def calculate_price(profile, length_ft):
    """Calculate price for custom length"""
    return profile['weight_per_ft'] * length_ft * profile['cost_per_lb']

# Example: 10-foot length of a profile
profile = data['profiles'][0]  # Example profile
price_10ft = calculate_price(profile, 10)
```

## Size Formats

Different profile types use different size notation:

- **Angles**: `"1x1"` = 1" x 1" equal leg
- **Square Tubes**: `"2x2"` = 2" x 2" outside dimensions
- **Rectangular Tubes**: `"2x4"` = 2" x 4" outside dimensions
- **Round Pipes**: `"2"` = 2" nominal diameter
- **Channels**: `"C6"` = 6" channel depth
- **Wide Flanges**: `"W12"` = 12" nominal depth
- **Flat Bars**: `"0.25x2"` = 1/4" thick x 2" wide

## Data Validation

To validate the JSON structure, run the included test script:

```bash
python3 test_profile_data.py
```

This will:
- Verify JSON is valid
- Check all required fields are present
- Display statistics and examples
- Demonstrate search functionality

## Notes

1. All dimensions are in inches
2. All weights are in pounds per foot (lb/ft)
3. All prices are in USD
4. Prices are for material only, not including shipping, cutting, or fabrication
5. Weight calculations are approximations based on standard formulas
6. Actual weights may vary slightly based on manufacturing tolerances

## Version History

- **2026-01-08**: Initial release with 575 profiles
  - Steel: 366 profiles
  - Aluminum: 161 profiles
  - Stainless Steel: 48 profiles

## License

This data is provided for use with the Coremark Weldment Profiles library for SolidWorks.
