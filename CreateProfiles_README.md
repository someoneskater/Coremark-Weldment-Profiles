# CreateProfiles.bas - VBA Macro for SolidWorks

## Overview

CreateProfiles.bas is a VBA macro module for SolidWorks that provides automated functions to draw various weldment profile sketches. This macro is designed to help create the structural profiles for the Coremark Metals weldment profile library.

## Features

The macro includes functions to create the following profile types:

1. **Angle Profiles (L-shaped)** - Equal or unequal leg angles
2. **Rectangular/Square Tube Profiles** - Hollow structural sections (HSS)
3. **Round Tube Profiles** - Circular hollow sections (pipes)
4. **Channel Profiles (C-shaped)** - Standard channels

## Installation

1. Open SolidWorks
2. Go to **Tools > Macro > Edit**
3. Browse to and open `CreateProfiles.bas`
4. The macro is now loaded and ready to use

Alternatively:
1. Open the Visual Basic Editor in SolidWorks (Alt + F11)
2. Import the `CreateProfiles.bas` module (**File > Import File**)

## Usage

### Method 1: Using the Sample Macros

The module includes sample macros that demonstrate how to use each profile function:

- `CreateSampleAngleProfile()` - Creates a 50mm x 50mm x 5mm angle
- `CreateSampleTubeProfile()` - Creates a 100mm x 50mm x 5mm rectangular tube
- `CreateSampleRoundTubeProfile()` - Creates a 50mm diameter tube with 3mm wall
- `CreateSampleChannelProfile()` - Creates a 100mm x 50mm channel

To run a sample:
1. In SolidWorks, go to **Tools > Macro > Run**
2. Select `CreateProfiles.bas`
3. Choose one of the sample macros from the list
4. Click **Run**

### Method 2: Using the Functions in Your Own Code

You can call the profile creation functions from your own VBA code:

```vba
Sub MyCustomProfile()
    Dim swApp As Object
    Set swApp = CreateObject("SldWorks.Application")
    
    ' Create a new part document
    Dim swModel As Object
    Set swModel = CreateNewPartDocument(swApp)
    
    If Not swModel Is Nothing Then
        ' Create a custom angle profile
        Call CreateAngleProfile(swApp, 75, 50, 6)
    End If
End Sub
```

## Function Reference

### CreateAngleProfile

Creates an L-shaped angle profile.

**Syntax:**
```vba
CreateAngleProfile(swApp, width1, width2, thickness)
```

**Parameters:**
- `swApp` (Object) - SolidWorks Application object
- `width1` (Double) - Width of the first leg in millimeters
- `width2` (Double) - Width of the second leg in millimeters  
- `thickness` (Double) - Material thickness in millimeters

**Returns:** Boolean - True if successful, False otherwise

**Example:**
```vba
' Create a 75mm x 50mm x 6mm angle
CreateAngleProfile swApp, 75, 50, 6
```

### CreateTubeProfile

Creates a rectangular or square hollow section profile.

**Syntax:**
```vba
CreateTubeProfile(swApp, outerWidth, outerHeight, wallThickness)
```

**Parameters:**
- `swApp` (Object) - SolidWorks Application object
- `outerWidth` (Double) - Outer width in millimeters
- `outerHeight` (Double) - Outer height in millimeters
- `wallThickness` (Double) - Wall thickness in millimeters

**Returns:** Boolean - True if successful, False otherwise

**Example:**
```vba
' Create a 100mm x 100mm square tube with 5mm wall
CreateTubeProfile swApp, 100, 100, 5
```

### CreateRoundTubeProfile

Creates a circular hollow section (pipe) profile.

**Syntax:**
```vba
CreateRoundTubeProfile(swApp, outerDiameter, wallThickness)
```

**Parameters:**
- `swApp` (Object) - SolidWorks Application object
- `outerDiameter` (Double) - Outer diameter in millimeters
- `wallThickness` (Double) - Wall thickness in millimeters

**Returns:** Boolean - True if successful, False otherwise

**Example:**
```vba
' Create a 60mm diameter pipe with 4mm wall
CreateRoundTubeProfile swApp, 60, 4
```

### CreateChannelProfile

Creates a C-shaped channel profile.

**Syntax:**
```vba
CreateChannelProfile(swApp, height, width, webThickness, flangeThickness)
```

**Parameters:**
- `swApp` (Object) - SolidWorks Application object
- `height` (Double) - Overall height of the channel in millimeters
- `width` (Double) - Width of the flanges in millimeters
- `webThickness` (Double) - Thickness of the web in millimeters
- `flangeThickness` (Double) - Thickness of the flanges in millimeters

**Returns:** Boolean - True if successful, False otherwise

**Example:**
```vba
' Create a 150mm x 75mm channel with 6mm web and 9mm flanges
CreateChannelProfile swApp, 150, 75, 6, 9
```

### CreateNewPartDocument

Helper function to create a new part document.

**Syntax:**
```vba
CreateNewPartDocument(swApp)
```

**Parameters:**
- `swApp` (Object) - SolidWorks Application object

**Returns:** Object - The new model document, or Nothing if failed

## Creating Weldment Profile Library Files

To use these profiles as weldment profiles in SolidWorks:

1. Run the appropriate macro to create the profile sketch
2. Save the file as a **Library Feature Part** (*.sldlfp) file
3. Place the file in your weldment profiles directory:
   - Default location: `C:\Program Files\SOLIDWORKS\weldment profiles\`
   - Or your custom location set in **Tools > Options > File Locations > Weldment Profiles**
4. Organize profiles in folders by type (e.g., `angles\`, `tubes\`, `channels\`)
5. The profiles will now be available in the **Structural Member** feature

## Dimensions and Units

- All input dimensions are in **millimeters**
- The functions automatically convert to SolidWorks internal units (meters)
- Profiles are created on the **Front Plane**
- Angle profiles are positioned with the corner at the origin
- Tube and channel profiles are centered at the origin

## Notes

- Ensure a part document is active before running the profile creation functions
- The macro will create 2D sketches only - you'll need to save as .sldlfp for weldment use
- All profiles are created as closed sketches suitable for weldment profiles
- Error handling is included with message boxes for user feedback

## Troubleshooting

**"No active document found" error:**
- Make sure a part document is open in SolidWorks
- Use the `CreateNewPartDocument()` helper function to create a new part

**Profile doesn't appear:**
- Check that dimensions are positive values
- Ensure wall thickness is less than the outer dimensions
- Rebuild the model (Ctrl+B) if needed

**Macro won't run:**
- Verify macros are enabled in SolidWorks (**Tools > Options > System Options > Security**)
- Check that the SolidWorks API is properly installed

## License

This macro is part of the Coremark Weldment Profiles project.

## Contributing

To add new profile types:
1. Follow the existing function structure
2. Use proper error handling
3. Include parameter documentation
4. Add example macros for testing
5. Update this README with the new function documentation
