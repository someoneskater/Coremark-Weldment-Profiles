# Profiles Directory

This directory will contain the generated .sldlfp (SolidWorks Library Feature Part) files.

## Generating Profiles

Run the generation script from the `scripts` directory:

```bash
cd ../scripts
python generate_profiles.py --output ../profiles
```

Or use the VBA macro in SolidWorks.

## File Naming Convention

Profile files follow this naming pattern:
```
[TYPE]-[ID]_[MATERIAL].sldlfp
```

Examples:
- `ANG-0001_Steel.sldlfp` - Steel angle profile
- `TUB-0015_Aluminum.sldlfp` - Aluminum tube profile
- `PIP-0042_Stainless_Steel.sldlfp` - Stainless steel pipe profile

## Using Generated Profiles

1. Copy .sldlfp files to your SolidWorks weldment profiles directory
2. Default location: `C:\Program Files\SolidWorks Corp\SolidWorks\data\weldment profiles\`
3. Access in SolidWorks: Insert > Weldments > Structural Member

## Note

Generated .sldlfp files are excluded from version control via .gitignore.
Run the generation scripts to create them locally.
