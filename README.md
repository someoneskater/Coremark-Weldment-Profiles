# Coremark Weldment Profiles for SolidWorks

A comprehensive SolidWorks weldment profile library featuring 734 structural metal profiles from Coremark Metals, including Steel, Aluminum, and Stainless Steel shapes with integrated pricing data.

## 📋 Overview

This library provides ready-to-use SolidWorks weldment profiles (.sldlfp files) for structural design and analysis. All profiles include:
- Accurate dimensional data
- Material specifications
- Current pricing information (USD per foot)
- Custom properties for easy identification

## 🗂️ Profile Types

The library includes the following profile categories:

| Type | Count | Description |
|------|-------|-------------|
| **Angles** | 177 | L-shaped profiles (equal and unequal leg) |
| **Tubes** | 225 | Square and rectangular tubes |
| **Channels** | 60 | C-channel profiles |
| **Beams** | 26 | I-beam profiles |
| **Pipes** | 105 | Round pipe profiles |
| **Flat Bars** | 141 | Flat bar stock |
| **Total** | **734** | All profiles |

## 📁 Repository Structure

```
Coremark-Weldment-Profiles/
├── data/
│   └── profiles.json          # Complete profile database with dimensions & pricing
├── scripts/
│   ├── generate_profile_data.py    # Python script to generate profile data
│   ├── generate_profiles.py        # Python script using SolidWorks API
│   └── GenerateProfiles.swp        # VBA macro for SolidWorks
├── profiles/                   # Generated .sldlfp files (create via scripts)
├── docs/
│   └── CLAUDE.md              # Detailed project documentation
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- **SolidWorks** 2020 or later (Windows only)
- **Python 3.7+** (for Python scripts)
- **pywin32** library: `pip install pywin32`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/someoneskater/Coremark-Weldment-Profiles.git
   cd Coremark-Weldment-Profiles
   ```

2. **Install Python dependencies:**
   ```bash
   pip install pywin32
   ```

3. **Generate profile data (optional - already included):**
   ```bash
   cd scripts
   python generate_profile_data.py
   ```

## 📝 Usage

### Method 1: Python Script (Recommended)

Generate all profiles using the Python script:

```bash
cd scripts
python generate_profiles.py --output ../profiles
```

**Options:**
- `--json PATH`: Specify custom JSON file (default: `../data/profiles.json`)
- `--output DIR`: Output directory (default: `../profiles`)
- `--types TYPE [TYPE ...]`: Generate specific types only (e.g., `angle tube`)
- `--max N`: Limit number of profiles to generate

**Examples:**
```bash
# Generate only angle and tube profiles
python generate_profiles.py --types angle tube

# Generate first 50 profiles
python generate_profiles.py --max 50

# Custom paths
python generate_profiles.py --json C:\custom\profiles.json --output C:\SolidWorks\Profiles
```

### Method 2: VBA Macro

1. Open SolidWorks
2. Go to **Tools** > **Macro** > **Edit**
3. Open `scripts/GenerateProfiles.swp`
4. Update file paths in the `Main()` subroutine:
   ```vba
   jsonPath = "C:\Coremark-Weldment-Profiles\data\profiles.json"
   outputDir = "C:\Coremark-Weldment-Profiles\profiles\"
   ```
5. Run the macro (F5)

### Method 3: Use Pre-generated Profiles

If profiles have already been generated:

1. Copy the `profiles` folder to your SolidWorks weldment profiles directory
2. Default location: `C:\Program Files\SolidWorks Corp\SolidWorks\data\weldment profiles\`
3. In SolidWorks, access via **Insert** > **Weldments** > **Structural Member**

## 🔧 Configuration

### Customize Profile Data

Edit `data/profiles.json` to add, modify, or remove profiles. Each profile entry includes:

```json
{
  "id": "ANG-0001",
  "type": "angle",
  "subtype": "equal",
  "material": "Steel",
  "dimensions": {
    "leg_a": 2.0,
    "leg_b": 2.0,
    "thickness": 0.25
  },
  "name": "Angle 2x2x0.25 Steel",
  "price_per_foot": 2.5
}
```

### Generate Custom Data

Modify `scripts/generate_profile_data.py` to:
- Add new profile types
- Change size ranges
- Update materials
- Adjust pricing formulas

## 📊 Profile Data

The `profiles.json` file contains complete specifications:

- **Metadata**: Version, description, units, profile count
- **Dimensions**: All critical measurements in inches
- **Materials**: Steel, Aluminum, Stainless Steel
- **Pricing**: Current prices in USD per foot
- **IDs**: Unique identifiers for each profile

## 🛠️ Troubleshooting

### Common Issues

**1. "Failed to connect to SolidWorks"**
- Ensure SolidWorks is installed
- Run Python as Administrator
- Check that SolidWorks is properly registered (reinstall if needed)

**2. "Module 'win32com' not found"**
- Install pywin32: `pip install pywin32`
- Run: `python Scripts/pywin32_postinstall.py -install` (in Python directory)

**3. VBA Macro Path Errors**
- Update file paths in the macro to match your installation
- Use absolute paths
- Ensure directories exist

**4. Template Not Found**
- Update template path in scripts to match your SolidWorks version
- Default: `C:\ProgramData\SolidWorks\SOLIDWORKS 2024\templates\Part.prtdot`

**5. Slow Generation**
- Generation can take 5-30 minutes for all profiles
- Use `--max` option to limit count during testing
- Close other SolidWorks documents before running

## 📖 Documentation

For detailed information, see:
- [CLAUDE.md](docs/CLAUDE.md) - Complete project documentation and technical details
- [profiles.json](data/profiles.json) - Full profile database

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add/modify profiles or improve scripts
4. Test with SolidWorks
5. Submit a pull request

## 📄 License

This project is provided as-is for use with Coremark Metals profiles. Profile dimensions and pricing are subject to change. Please verify current specifications with Coremark Metals before production use.

## 🔗 Resources

- [SolidWorks API Documentation](https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks_namespace.html)
- [Coremark Metals](https://www.coremarkmetals.com/)
- [SolidWorks Weldments Guide](https://help.solidworks.com/2024/english/solidworks/sldworks/c_weldments_overview.htm)

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check the [troubleshooting section](#-troubleshooting)
- Review [CLAUDE.md](docs/CLAUDE.md) for technical details

---

**Version:** 1.0  
**Last Updated:** 2024  
**Maintained by:** SolidWorks Automation Community
