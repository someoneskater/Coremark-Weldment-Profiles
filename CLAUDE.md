# CLAUDE.md - Project Documentation

## Project Overview
This repository contains SolidWorks weldment profile data scraped from Coremark Metals, along with tools to generate .sldlfp profile files for use in SolidWorks Weldments.

## Data Source
All profile data was scraped from [coremarkmetals.com](https://www.coremarkmetals.com) using their product API endpoints:
- `utils.cfc?method=getAttrValues` - For size/thickness options
- - `utils.cfc?method=getSKUs` - For pricing and SKU data
 
  - ## Scraped Data Summary
 
  - ### Total Profiles: 558
 
  - ### Steel Profiles (460 total)
  - - **Equal Leg Angle**: 53 profiles (Hot Rolled Steel A36)
    - - **Unequal Leg Angle**: 50 profiles (Hot Rolled Steel A36)
      - - **I-Beam**: 15 profiles (Hot Rolled Steel A36)
        - - **Wide Flange**: 102 profiles (Hot Rolled Steel A36)
          - - **C-Channel**: 27 profiles (Hot Rolled Steel A36)
            - - **Square Tube**: 92 profiles (Mechanical/Structural A500)
              - - **Rectangular Tube**: 121 profiles (Mechanical/Structural A500)
               
                - ### Aluminum Profiles (49 total)
                - - **Equal Leg Angle**: 31 profiles (6061-T6)
                  - - **Square Tube**: 18 profiles (6063-T52)
                   
                    - ### Stainless Steel Profiles (49 total)
                    - - **Angle**: 21 profiles (304 Stainless)
                      - - **Square Tube**: 28 profiles (304 Stainless)
                       
                        - ## Data Fields
                        - Each profile record contains:
                        - - `size`: Dimension string (e.g., "2\" x 2\" x 1/4\"")
                          - - `thickness` or `wall`: Material thickness
                            - - `price`: Current price in USD (20ft lengths)
                              - - `cost_per_lb`: Price per pound
                                - - `weight_per_ft`: Weight in lbs per foot
                                  - - `sku`: Coremark product SKU
                                   
                                    - ## Milestone Plan
                                   
                                    - ### Phase 1: Data Collection ✅ COMPLETE
                                    - - [x] Identify data source and API endpoints
                                      - [ ] - [x] Scrape Steel profiles (angles, beams, channels, tubes)
                                      - [ ] - [x] Scrape Aluminum profiles
                                      - [ ] - [x] Scrape Stainless Steel profiles
                                      - [ ] - [x] Store data in structured JSON format
                                     
                                      - [ ] ### Phase 2: Repository Setup ✅ COMPLETE
                                      - [ ] - [x] Create GitHub repository
                                      - [ ] - [x] Add profile_data.json with scraped data
                                      - [ ] - [x] Create Python script (generate_profiles.py)
                                      - [ ] - [x] Create VBA macro (CreateProfiles.bas)
                                      - [ ] - [x] Add project documentation (CLAUDE.md)
                                     
                                      - [ ] ### Phase 3: SolidWorks Integration 🔄 IN PROGRESS
                                      - [ ] - [ ] Test Python script with SolidWorks
                                      - [ ] - [ ] Test VBA macro with SolidWorks
                                      - [ ] - [ ] Generate sample .sldlfp files
                                      - [ ] - [ ] Verify custom properties display correctly
                                     
                                      - [ ] ### Phase 4: Distribution 📋 TODO
                                      - [ ] - [ ] Package profiles in standard folder structure
                                      - [ ] - [ ] Create installation instructions
                                      - [ ] - [ ] Add to SolidWorks Toolbox paths
                                      - [ ] - [ ] Document BOM integration
                                     
                                      - [ ] ## Usage Instructions
                                     
                                      - [ ] ### Python Script
                                      - [ ] ```bash
                                      - [ ] # Requires: SolidWorks installed, Python 3.x, pywin32
                                      - [ ] pip install pywin32
                                      - [ ] python scripts/generate_profiles.py
                                      - [ ] ```
                                     
                                      - [ ] ### VBA Macro
                                      - [ ] 1. Open SolidWorks
                                      - [ ] 2. Tools > Macro > Run
                                      - [ ] 3. Select CreateProfiles.bas
                                      - [ ] 4. Choose profile_data.json and output folder
                                     
                                      - [ ] ## File Structure
                                      - [ ] ```
                                      - [ ] Coremark-Weldment-Profiles/
                                      - [ ] ├── data/
                                      - [ ] │   └── profile_data.json    # All scraped profile data
                                      - [ ] ├── scripts/
                                      - [ ] │   ├── generate_profiles.py # Python profile generator
                                      - [ ] │   └── CreateProfiles.bas   # VBA macro
                                      - [ ] ├── output/                  # Generated .sldlfp files
                                      - [ ] ├── README.md
                                      - [ ] └── CLAUDE.md               # This file
                                      - [ ] ```
                                     
                                      - [ ] ## API Reference (Coremark Metals)
                                     
                                      - [ ] ### Get Size Options
                                      - [ ] ```
                                      - [ ] POST /_cfc/utils.cfc?returnFormat=json&method=getAttrValues
                                      - [ ] FormData: itemId={itemId}&attrId=198&selVals=
                                      - [ ] ```
                                     
                                      - [ ] ### Get Thickness Options
                                      - [ ] ```
                                      - [ ] POST /_cfc/utils.cfc?returnFormat=json&method=getAttrValues
                                      - [ ] FormData: itemId={itemId}&attrId=60&selVals={sizeValue}
                                      - [ ] ```
                                     
                                      - [ ] ### Get SKU/Pricing
                                      - [ ] ```
                                      - [ ] POST /_cfc/utils.cfc?returnFormat=json&method=getSKUs
                                      - [ ] FormData: itemId={itemId}&selVals={sizeValue}|{thicknessValue}
                                      - [ ] ```
                                     
                                      - [ ] ## Sample Data
                                     
                                      - [ ] ### Steel 2"x2"x1/4" Angle
                                      - [ ] - Price: $81.66
                                      - [ ] - Weight: 3.19 lb/ft
                                      - [ ] - SKU: 00261
                                     
                                      - [ ] ### Steel 3"x3"x1/4" Square Tube
                                      - [ ] - Price: $327.73
                                      - [ ] - Weight: 8.81 lb/ft
                                      - [ ] - SKU: 03945
                                     
                                      - [ ] ### Aluminum 2"x2"x1/4" Angle
                                      - [ ] - Price: $175.38
                                      - [ ] - Weight: 1.11 lb/ft
                                      - [ ] - SKU: 00883
                                     
                                      - [ ] ### Stainless 2"x2"x1/4" Angle
                                      - [ ] - Price: $369.29
                                      - [ ] - Weight: 3.189 lb/ft
                                      - [ ] - SKU: 01689
                                     
                                      - [ ] ## Notes
                                      - [ ] - Prices are for 20ft lengths and subject to change
                                      - [ ] - Data scraped January 2026
                                      - [ ] - Some profiles may have "Call for Pricing" on website but API returns current pricing
                                      - [ ] - Custom properties include pricing data for BOM calculations
