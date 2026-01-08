# Coremark-Weldment-Profiles
SolidWorks weldment profile library with 558 profiles from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Profile Properties

Each profile in this library includes the following properties:

- **size** - Profile dimensional size (e.g., "2x2", "1x3")
- **thickness** - Wall thickness (e.g., "0.125", "0.25")
- **price** - Current price per unit
- **cost_per_lb** - Cost per pound of material
- **weight_per_ft** - Weight per linear foot in pounds
- **sku** - SKU/Part number for ordering

## Structure

See [PROFILE_STRUCTURE.md](PROFILE_STRUCTURE.md) for detailed documentation on the profile data structure and organization.

## Profile Data

Profile metadata is organized by material type and shape in the `profiles/` directory:

```
profiles/
├── steel/          # Steel structural shapes
├── aluminum/       # Aluminum structural shapes
└── stainless/      # Stainless steel structural shapes
```

Each profile type includes complete specifications including dimensions, weight, pricing, and ordering information.
