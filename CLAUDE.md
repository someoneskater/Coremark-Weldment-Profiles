# Coremark Weldment Profiles - Project Documentation

## Project Overview

This project provides a comprehensive SolidWorks weldment profile library containing 558 profiles from Coremark Metals. The library includes structural shapes across three primary materials with integrated pricing data for engineering and manufacturing applications.

## Material Properties

### Steel (Carbon Steel)

**Physical Properties:**
- Density: 7.85 g/cm³ (0.284 lb/in³)
- Melting Point: 1370-1530°C (2500-2790°F)
- Elastic Modulus: 200 GPa (29,000 ksi)
- Poisson's Ratio: 0.29
- Thermal Expansion: 11.7 µm/m·°C (6.5 µin/in·°F)
- Thermal Conductivity: 50 W/m·K

**Mechanical Properties (ASTM A36):**
- Tensile Strength: 400-550 MPa (58-80 ksi)
- Yield Strength: 250 MPa (36 ksi) minimum
- Elongation: 20-23% in 50mm (2 in)
- Hardness: 119-159 BHN

**Applications:**
- Structural framing and support
- Machine bases and frameworks
- General fabrication
- Cost-effective construction

### Aluminum (6061-T6)

**Physical Properties:**
- Density: 2.70 g/cm³ (0.098 lb/in³)
- Melting Point: 582-652°C (1080-1205°F)
- Elastic Modulus: 69 GPa (10,000 ksi)
- Poisson's Ratio: 0.33
- Thermal Expansion: 23.6 µm/m·°C (13.1 µin/in·°F)
- Thermal Conductivity: 167 W/m·K

**Mechanical Properties:**
- Tensile Strength: 310 MPa (45 ksi) minimum
- Yield Strength: 276 MPa (40 ksi) minimum
- Elongation: 12% in 50mm (2 in) minimum
- Hardness: 95 BHN

**Applications:**
- Lightweight structural applications
- Aerospace and transportation
- Corrosion-resistant environments
- Marine applications
- Weight-critical designs

### Stainless Steel (304)

**Physical Properties:**
- Density: 8.00 g/cm³ (0.289 lb/in³)
- Melting Point: 1400-1450°C (2550-2650°F)
- Elastic Modulus: 193 GPa (28,000 ksi)
- Poisson's Ratio: 0.29
- Thermal Expansion: 17.3 µm/m·°C (9.6 µin/in·°F)
- Thermal Conductivity: 16 W/m·K

**Mechanical Properties:**
- Tensile Strength: 515 MPa (75 ksi) minimum
- Yield Strength: 205 MPa (30 ksi) minimum
- Elongation: 40% in 50mm (2 in) minimum
- Hardness: 201 BHN maximum

**Applications:**
- Food processing equipment
- Chemical and pharmaceutical industries
- Medical equipment
- High-corrosion environments
- Sanitary applications

## Profile Types Included

The library contains the following structural profile types:

1. **Angles** - Equal and unequal leg angles
2. **Channels** - Standard and structural channels
3. **I-Beams** - Wide flange and standard beams
4. **Rectangular Tubes** - Hollow structural sections (HSS)
5. **Square Tubes** - Square hollow structural sections
6. **Round Tubes** - Circular pipes and tubes
7. **Flat Bars** - Solid rectangular bars
8. **Round Bars** - Solid circular bars

## Milestone Plan

### Phase 1: Foundation (Completed)
- [x] Initial repository setup
- [x] README documentation
- [x] Git repository initialization

### Phase 2: Documentation (Current Phase)
- [x] Create CLAUDE.md with material properties
- [x] Document milestone plan
- [ ] Add usage instructions
- [ ] Create installation guide

### Phase 3: Profile Library Development
- [ ] Organize profile files by material type
- [ ] Establish naming conventions
- [ ] Create Steel profile collection
- [ ] Create Aluminum profile collection
- [ ] Create Stainless Steel profile collection

### Phase 4: SolidWorks Integration
- [ ] Configure weldment profile paths
- [ ] Test profiles in SolidWorks environment
- [ ] Validate profile dimensions and properties
- [ ] Verify material property integration

### Phase 5: Pricing Data Integration
- [ ] Establish pricing data structure
- [ ] Integrate current Coremark Metals pricing
- [ ] Create pricing update methodology
- [ ] Document pricing data format

### Phase 6: Quality Assurance
- [ ] Profile dimensional verification
- [ ] Material property validation
- [ ] Cross-platform compatibility testing
- [ ] Documentation review

### Phase 7: Release and Distribution
- [ ] Package library for distribution
- [ ] Create installation package
- [ ] Publish release notes
- [ ] User documentation finalization

### Phase 8: Maintenance and Updates
- [ ] Establish update schedule
- [ ] Monitor Coremark Metals catalog changes
- [ ] Community feedback integration
- [ ] Continuous improvement process

## Technical Requirements

### SolidWorks Compatibility
- Minimum Version: SolidWorks 2018
- Recommended Version: SolidWorks 2020 or later
- File Format: .sldlfp (Library Feature Part)

### System Requirements
- Operating System: Windows 10 or later
- Disk Space: 100 MB minimum
- SolidWorks Premium or Professional edition

## Usage Guidelines

### Installation Location
Profiles should be installed in the SolidWorks weldment profiles directory:
```
C:\ProgramData\SOLIDWORKS\SOLIDWORKS [Version]\lang\english\weldment profiles\
```

### Profile Selection
When using weldment profiles in SolidWorks:
1. Select the appropriate material folder (Steel, Aluminum, or Stainless Steel)
2. Choose the profile type (Angle, Channel, Tube, etc.)
3. Select the specific size needed from the available options
4. Verify material properties are correctly applied

## Contributing

This is a curated library based on Coremark Metals catalog. Updates should:
- Follow existing naming conventions
- Include accurate dimensional data
- Verify material properties
- Test in SolidWorks before committing

## License and Usage

Please verify licensing terms with Coremark Metals for commercial usage of profile data and pricing information.

## References

- Coremark Metals: https://www.coremarkmetals.com/
- SolidWorks Weldments Documentation
- ASTM Material Standards (A36, 6061-T6, 304)
- AISC Steel Construction Manual

## Contact

For questions or updates regarding this library, please open an issue in the repository.

---

*Last Updated: January 2026*
