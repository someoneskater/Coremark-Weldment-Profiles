# Quick Reference Guide

## 🚀 Quick Start Commands

### Generate All Profiles (Python)
```bash
cd scripts
python generate_profiles.py
```

### Generate Specific Types
```bash
# Angles and tubes only
python generate_profiles.py --types angle tube

# First 10 profiles (for testing)
python generate_profiles.py --max 10

# Custom output directory
python generate_profiles.py --output C:\CustomPath\profiles
```

### VBA Macro
1. Open SolidWorks
2. Tools > Macro > Edit
3. Open `scripts/GenerateProfiles.swp`
4. Update paths in `Main()` function
5. Press F5 to run

## 📊 Profile Summary

| Type | Count | Size Range | Materials |
|------|-------|------------|-----------|
| Angles | 177 | 1" to 8" | Steel, Aluminum, Stainless |
| Tubes | 225 | 1" to 8" | Steel, Aluminum, Stainless |
| Channels | 60 | 3" to 15" | Steel, Aluminum, Stainless |
| Beams | 26 | 3" to 24" | Steel, Aluminum |
| Pipes | 105 | 0.5" to 8" | Steel, Aluminum, Stainless |
| Flat Bars | 141 | 0.5" to 8" | Steel, Aluminum, Stainless |
| **Total** | **734** | | |

## 🔧 Common Tasks

### Regenerate Profile Data
```bash
cd scripts
python generate_profile_data.py
```

### Validate JSON Data
```bash
python -c "import json; json.load(open('../data/profiles.json')); print('Valid')"
```

### Count Profiles by Type
```bash
python -c "
import json
data = json.load(open('../data/profiles.json'))
types = {}
for p in data['profiles']:
    types[p['type']] = types.get(p['type'], 0) + 1
for t, c in sorted(types.items()):
    print(f'{t}: {c}')
"
```

## 🗂️ File Locations

| Item | Path |
|------|------|
| Profile Data | `data/profiles.json` |
| Python Generator | `scripts/generate_profiles.py` |
| Data Generator | `scripts/generate_profile_data.py` |
| VBA Macro | `scripts/GenerateProfiles.swp` |
| Output Directory | `profiles/` |
| Documentation | `docs/CLAUDE.md` |

## ⚠️ Troubleshooting Quick Fixes

### Python Issues
```bash
# Install dependencies
pip install pywin32

# Run as Administrator (Windows)
# Right-click Command Prompt > Run as Administrator
```

### SolidWorks Connection
```
# Verify SolidWorks is installed
# Close all SolidWorks documents before running
# Run Python script as Administrator
```

### VBA Path Errors
```vba
' Update these lines in GenerateProfiles.swp:
jsonPath = "C:\Your\Full\Path\data\profiles.json"
outputDir = "C:\Your\Full\Path\profiles\"
```

## 📖 More Information

- Full documentation: `docs/CLAUDE.md`
- Installation guide: `README.md`
- Profile specifications: `data/profiles.json`

## 🔗 SolidWorks Integration

### Install Profiles
1. Copy generated .sldlfp files from `profiles/`
2. Paste to: `C:\Program Files\SolidWorks Corp\SolidWorks\data\weldment profiles\`
3. Restart SolidWorks

### Use Profiles
1. Insert > Weldments > Structural Member
2. Browse to profile directory
3. Select profile
4. Apply to sketch path

## 💡 Tips

- **Start small**: Use `--max 10` for initial testing
- **Type-specific**: Generate one type at a time for faster testing
- **Close SolidWorks**: Close other documents before batch generation
- **Administrator**: Run as Admin for best results on Windows
- **Patience**: Full generation (734 profiles) takes 30-60 minutes

---

**For detailed information, see [CLAUDE.md](docs/CLAUDE.md)**
