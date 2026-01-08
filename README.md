# Coremark-Weldment-Profiles

SolidWorks weldment profile library with **558 profiles** from Coremark Metals including Steel, Aluminum, and Stainless Steel structural shapes with integrated pricing data.

## Features

- **558 weldment profiles** with real pricing data
- - Steel, Aluminum, and Stainless Steel materials
  - - Angles, Beams, Channels, Square Tubes, Rectangular Tubes
    - - Python and VBA scripts to generate .sldlfp files
      - - Custom properties for BOM integration (price, weight, SKU)
       
        - ## Profile Categories
       
        - | Material | Profile Type | Count |
        - |----------|-------------|-------|
        - | Steel | Equal Leg Angle | 53 |
        - | Steel | Unequal Leg Angle | 50 |
        - | Steel | I-Beam | 15 |
        - | Steel | Wide Flange | 102 |
        - | Steel | C-Channel | 27 |
        - | Steel | Square Tube | 92 |
        - | Steel | Rectangular Tube | 121 |
        - | Aluminum | Equal Leg Angle | 31 |
        - | Aluminum | Square Tube | 18 |
        - | Stainless | Angle | 21 |
        - | Stainless | Square Tube | 28 |
       
        - ## Quick Start
       
        - ### Python (Recommended)
        - ```bash
          pip install pywin32
          python scripts/generate_profiles.py
          ```

          ### VBA Macro
          1. Open SolidWorks
          2. 2. Tools > Macro > Run
             3. 3. Select `scripts/CreateProfiles.bas`
               
                4. ## File Structure
               
                5. ```
                   ├── data/
                   │   └── profile_data.json     # All scraped profile data
                   ├── scripts/
                   │   ├── generate_profiles.py  # Python profile generator
                   │   └── CreateProfiles.bas    # VBA macro alternative
                   ├── CLAUDE.md                 # Detailed documentation
                   └── README.md
                   ```

                   ## Requirements

                   - SolidWorks 2018 or later
                   - - Python 3.x with pywin32 (for Python script)
                     - - Windows OS (SolidWorks COM automation)
                      
                       - ## Data Source
                      
                       - Profile data scraped from [Coremark Metals](https://www.coremarkmetals.com) including current pricing, weights, and SKUs.
                      
                       - ## License
                      
                       - MIT
                      
                       - ## Contributing
                      
                       - Pull requests welcome! See CLAUDE.md for detailed project documentation.
