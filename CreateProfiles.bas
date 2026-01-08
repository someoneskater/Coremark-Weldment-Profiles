Attribute VB_Name = "CreateProfiles"
'*******************************************************************************
' CreateProfiles.bas - VBA Macro for SolidWorks
' 
' Purpose: Functions to draw angle and tube profiles for weldment profiles
' Author: Coremark Weldment Profiles Project
' Description: This module contains functions to programmatically create
'              angle and tube profile sketches in SolidWorks for use in
'              weldment profile libraries.
'*******************************************************************************

Option Explicit

' SolidWorks API Constants
Const swDocPart As Long = 1
Const swSketchLine As Long = 0
Const swConstraintHorizontal As Long = 1
Const swConstraintVertical As Long = 2
' User preference key for default part template (swUserPreferenceStringValue_e enumeration)
Const swDefaultTemplatePart As Long = 0  ' swDefaultTemplatePart from swUserPreferenceStringValue_e

'*******************************************************************************
' Function: CreateAngleProfile
' Purpose: Creates an angle (L-shaped) profile sketch
' Parameters:
'   swApp - SolidWorks Application object
'   width1 - Width of the first leg (in mm)
'   width2 - Width of the second leg (in mm)
'   thickness - Material thickness (in mm)
' Returns: Boolean - True if successful, False otherwise
'*******************************************************************************
Function CreateAngleProfile(swApp As Object, width1 As Double, width2 As Double, thickness As Double) As Boolean
    On Error GoTo ErrorHandler
    
    Dim swModel As Object
    Dim swModelDocExt As Object
    Dim swSketchMgr As Object
    Dim swFeatMgr As Object
    Dim swSelMgr As Object
    Dim boolStatus As Boolean
    
    ' Get active document
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "No active document found. Please open or create a part document.", vbExclamation
        CreateAngleProfile = False
        Exit Function
    End If
    
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
    
    ' Select the Front plane for sketching
    boolStatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    
    ' Start sketch on Front plane
    swSketchMgr.InsertSketch True
    
    ' Convert dimensions from mm to meters (SolidWorks internal units)
    Dim w1 As Double, w2 As Double, t As Double
    w1 = width1 / 1000#
    w2 = width2 / 1000#
    t = thickness / 1000#
    
    ' Draw the angle profile (L-shape)
    ' Point 1: Origin (0, 0)
    ' Point 2: (w1, 0) - horizontal leg outer edge
    ' Point 3: (w1, t) - horizontal leg inner edge
    ' Point 4: (t, t) - corner
    ' Point 5: (t, w2) - vertical leg inner edge
    ' Point 6: (0, w2) - vertical leg outer edge
    ' Back to Point 1 to close
    
    Dim swSketchSegment As Object
    
    ' Line 1: (0,0) to (w1,0)
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, w1, 0#, 0#)
    
    ' Line 2: (w1,0) to (w1,t)
    Set swSketchSegment = swSketchMgr.CreateLine(w1, 0#, 0#, w1, t, 0#)
    
    ' Line 3: (w1,t) to (t,t)
    Set swSketchSegment = swSketchMgr.CreateLine(w1, t, 0#, t, t, 0#)
    
    ' Line 4: (t,t) to (t,w2)
    Set swSketchSegment = swSketchMgr.CreateLine(t, t, 0#, t, w2, 0#)
    
    ' Line 5: (t,w2) to (0,w2)
    Set swSketchSegment = swSketchMgr.CreateLine(t, w2, 0#, 0#, w2, 0#)
    
    ' Line 6: (0,w2) to (0,0) - close the profile
    Set swSketchSegment = swSketchMgr.CreateLine(0#, w2, 0#, 0#, 0#, 0#)
    
    ' Exit the sketch
    swSketchMgr.InsertSketch True
    
    ' Rebuild the model
    swModel.ForceRebuild3 False
    
    CreateAngleProfile = True
    Exit Function
    
ErrorHandler:
    MsgBox "Error in CreateAngleProfile: " & Err.Description, vbCritical
    CreateAngleProfile = False
End Function

'*******************************************************************************
' Function: CreateTubeProfile
' Purpose: Creates a rectangular or square tube profile sketch
' Parameters:
'   swApp - SolidWorks Application object
'   outerWidth - Outer width of the tube (in mm)
'   outerHeight - Outer height of the tube (in mm)
'   wallThickness - Wall thickness (in mm)
' Returns: Boolean - True if successful, False otherwise
'*******************************************************************************
Function CreateTubeProfile(swApp As Object, outerWidth As Double, outerHeight As Double, wallThickness As Double) As Boolean
    On Error GoTo ErrorHandler
    
    Dim swModel As Object
    Dim swModelDocExt As Object
    Dim swSketchMgr As Object
    Dim swFeatMgr As Object
    Dim swSelMgr As Object
    Dim boolStatus As Boolean
    
    ' Get active document
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "No active document found. Please open or create a part document.", vbExclamation
        CreateTubeProfile = False
        Exit Function
    End If
    
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
    
    ' Select the Front plane for sketching
    boolStatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    
    ' Start sketch on Front plane
    swSketchMgr.InsertSketch True
    
    ' Convert dimensions from mm to meters (SolidWorks internal units)
    Dim ow As Double, oh As Double, t As Double
    ow = outerWidth / 1000#
    oh = outerHeight / 1000#
    t = wallThickness / 1000#
    
    ' Calculate inner dimensions
    Dim iw As Double, ih As Double
    iw = ow - (2# * t)
    ih = oh - (2# * t)
    
    ' Validate that wall thickness is not too large
    If iw <= 0# Or ih <= 0# Then
        MsgBox "Wall thickness is too large for the given outer dimensions. " & _
               "Wall thickness must be less than half of both outer width and outer height.", vbExclamation
        CreateTubeProfile = False
        Exit Function
    End If
    
    ' Center the profile at origin
    Dim halfOW As Double, halfOH As Double
    Dim halfIW As Double, halfIH As Double
    halfOW = ow / 2#
    halfOH = oh / 2#
    halfIW = iw / 2#
    halfIH = ih / 2#
    
    Dim swSketchSegment As Object
    
    ' Draw outer rectangle (centered at origin)
    ' Outer rectangle: bottom-left to top-right
    Set swSketchSegment = swSketchMgr.CreateLine(-halfOW, -halfOH, 0#, halfOW, -halfOH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(halfOW, -halfOH, 0#, halfOW, halfOH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(halfOW, halfOH, 0#, -halfOW, halfOH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-halfOW, halfOH, 0#, -halfOW, -halfOH, 0#)
    
    ' Draw inner rectangle (centered at origin)
    ' Inner rectangle: bottom-left to top-right
    Set swSketchSegment = swSketchMgr.CreateLine(-halfIW, -halfIH, 0#, halfIW, -halfIH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(halfIW, -halfIH, 0#, halfIW, halfIH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(halfIW, halfIH, 0#, -halfIW, halfIH, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-halfIW, halfIH, 0#, -halfIW, -halfIH, 0#)
    
    ' Exit the sketch
    swSketchMgr.InsertSketch True
    
    ' Rebuild the model
    swModel.ForceRebuild3 False
    
    CreateTubeProfile = True
    Exit Function
    
ErrorHandler:
    MsgBox "Error in CreateTubeProfile: " & Err.Description, vbCritical
    CreateTubeProfile = False
End Function

'*******************************************************************************
' Function: CreateRoundTubeProfile
' Purpose: Creates a round tube (pipe) profile sketch
' Parameters:
'   swApp - SolidWorks Application object
'   outerDiameter - Outer diameter of the tube (in mm)
'   wallThickness - Wall thickness (in mm)
' Returns: Boolean - True if successful, False otherwise
'*******************************************************************************
Function CreateRoundTubeProfile(swApp As Object, outerDiameter As Double, wallThickness As Double) As Boolean
    On Error GoTo ErrorHandler
    
    Dim swModel As Object
    Dim swModelDocExt As Object
    Dim swSketchMgr As Object
    Dim swFeatMgr As Object
    Dim boolStatus As Boolean
    
    ' Get active document
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "No active document found. Please open or create a part document.", vbExclamation
        CreateRoundTubeProfile = False
        Exit Function
    End If
    
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swFeatMgr = swModel.FeatureManager
    
    ' Select the Front plane for sketching
    boolStatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    
    ' Start sketch on Front plane
    swSketchMgr.InsertSketch True
    
    ' Convert dimensions from mm to meters (SolidWorks internal units)
    Dim od As Double, t As Double
    od = outerDiameter / 1000#
    t = wallThickness / 1000#
    
    ' Calculate inner diameter
    Dim id As Double
    id = od - (2# * t)
    
    ' Validate that wall thickness is not too large
    If id <= 0# Then
        MsgBox "Wall thickness is too large for the given outer diameter. " & _
               "Wall thickness must be less than half of the outer diameter.", vbExclamation
        CreateRoundTubeProfile = False
        Exit Function
    End If
    
    Dim swSketchSegment As Object
    
    ' Draw outer circle centered at origin
    Set swSketchSegment = swSketchMgr.CreateCircleByRadius(0#, 0#, 0#, od / 2#)
    
    ' Draw inner circle centered at origin
    Set swSketchSegment = swSketchMgr.CreateCircleByRadius(0#, 0#, 0#, id / 2#)
    
    ' Exit the sketch
    swSketchMgr.InsertSketch True
    
    ' Rebuild the model
    swModel.ForceRebuild3 False
    
    CreateRoundTubeProfile = True
    Exit Function
    
ErrorHandler:
    MsgBox "Error in CreateRoundTubeProfile: " & Err.Description, vbCritical
    CreateRoundTubeProfile = False
End Function

'*******************************************************************************
' Function: CreateChannelProfile
' Purpose: Creates a channel (C-shaped) profile sketch
' Parameters:
'   swApp - SolidWorks Application object
'   height - Overall height of the channel (in mm)
'   width - Width of the flanges (in mm)
'   webThickness - Thickness of the web (in mm)
'   flangeThickness - Thickness of the flanges (in mm)
' Returns: Boolean - True if successful, False otherwise
'*******************************************************************************
Function CreateChannelProfile(swApp As Object, height As Double, width As Double, webThickness As Double, flangeThickness As Double) As Boolean
    On Error GoTo ErrorHandler
    
    Dim swModel As Object
    Dim swModelDocExt As Object
    Dim swSketchMgr As Object
    Dim boolStatus As Boolean
    
    ' Get active document
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "No active document found. Please open or create a part document.", vbExclamation
        CreateChannelProfile = False
        Exit Function
    End If
    
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    
    ' Select the Front plane for sketching
    boolStatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    
    ' Start sketch on Front plane
    swSketchMgr.InsertSketch True
    
    ' Convert dimensions from mm to meters (SolidWorks internal units)
    Dim h As Double, w As Double, wt As Double, ft As Double
    h = height / 1000#
    w = width / 1000#
    wt = webThickness / 1000#
    ft = flangeThickness / 1000#
    
    Dim swSketchSegment As Object
    
    ' Draw the channel profile (C-shape) centered at origin
    ' Starting from bottom-left, going clockwise on outer profile
    Dim halfH As Double
    halfH = h / 2#
    
    ' Outer profile
    ' Bottom flange outer edge
    Set swSketchSegment = swSketchMgr.CreateLine(0#, -halfH, 0#, w, -halfH, 0#)
    ' Right edge bottom
    Set swSketchSegment = swSketchMgr.CreateLine(w, -halfH, 0#, w, -halfH + ft, 0#)
    ' Bottom flange inner edge
    Set swSketchSegment = swSketchMgr.CreateLine(w, -halfH + ft, 0#, wt, -halfH + ft, 0#)
    ' Web inner left edge
    Set swSketchSegment = swSketchMgr.CreateLine(wt, -halfH + ft, 0#, wt, halfH - ft, 0#)
    ' Top flange inner edge
    Set swSketchSegment = swSketchMgr.CreateLine(wt, halfH - ft, 0#, w, halfH - ft, 0#)
    ' Right edge top
    Set swSketchSegment = swSketchMgr.CreateLine(w, halfH - ft, 0#, w, halfH, 0#)
    ' Top flange outer edge
    Set swSketchSegment = swSketchMgr.CreateLine(w, halfH, 0#, 0#, halfH, 0#)
    ' Left edge (web)
    Set swSketchSegment = swSketchMgr.CreateLine(0#, halfH, 0#, 0#, -halfH, 0#)
    
    ' Exit the sketch
    swSketchMgr.InsertSketch True
    
    ' Rebuild the model
    swModel.ForceRebuild3 False
    
    CreateChannelProfile = True
    Exit Function
    
ErrorHandler:
    MsgBox "Error in CreateChannelProfile: " & Err.Description, vbCritical
    CreateChannelProfile = False
End Function

'*******************************************************************************
' Helper Function: CreateNewPartDocument
' Purpose: Creates a new part document for profile creation
' Parameters:
'   swApp - SolidWorks Application object
' Returns: Object - The new model document, or Nothing if failed
'*******************************************************************************
Function CreateNewPartDocument(swApp As Object) As Object
    On Error GoTo ErrorHandler
    
    Dim swModel As Object
    Dim filePath As String
    Dim templatePath As String
    Dim userPrefs As Long
    
    ' Try to get the default part template
    ' If no default template is set, empty string will cause SolidWorks to use system default or prompt user
    templatePath = ""
    On Error Resume Next
    templatePath = swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)
    If Err.Number <> 0 Then
        templatePath = ""  ' Fallback to system default if preference not found
    End If
    Err.Clear  ' Clear error state before resuming normal error handling
    On Error GoTo ErrorHandler
    
    ' Create a new part document
    ' Parameters: template path, document type, paper size (0=default), sheet format size (0=default)
    Set swModel = swApp.NewDocument(templatePath, swDocPart, 0, 0)
    
    If swModel Is Nothing Then
        MsgBox "Failed to create new part document.", vbCritical
        Set CreateNewPartDocument = Nothing
    Else
        Set CreateNewPartDocument = swModel
    End If
    
    Exit Function
    
ErrorHandler:
    MsgBox "Error in CreateNewPartDocument: " & Err.Description, vbCritical
    Set CreateNewPartDocument = Nothing
End Function

'*******************************************************************************
' Example Sub: CreateSampleAngleProfile
' Purpose: Demonstrates how to use the CreateAngleProfile function
' Usage: Run this macro from SolidWorks to create a sample angle profile
'*******************************************************************************
Sub CreateSampleAngleProfile()
    Dim swApp As Object
    Set swApp = CreateObject("SldWorks.Application")
    
    ' Create a new part document
    Dim swModel As Object
    Set swModel = CreateNewPartDocument(swApp)
    
    If Not swModel Is Nothing Then
        ' Create an angle profile: 50mm x 50mm x 5mm
        If CreateAngleProfile(swApp, 50#, 50#, 5#) Then
            MsgBox "Angle profile created successfully!", vbInformation
        Else
            MsgBox "Failed to create angle profile.", vbExclamation
        End If
    End If
End Sub

'*******************************************************************************
' Example Sub: CreateSampleTubeProfile
' Purpose: Demonstrates how to use the CreateTubeProfile function
' Usage: Run this macro from SolidWorks to create a sample tube profile
'*******************************************************************************
Sub CreateSampleTubeProfile()
    Dim swApp As Object
    Set swApp = CreateObject("SldWorks.Application")
    
    ' Create a new part document
    Dim swModel As Object
    Set swModel = CreateNewPartDocument(swApp)
    
    If Not swModel Is Nothing Then
        ' Create a rectangular tube profile: 100mm x 50mm with 5mm wall thickness
        If CreateTubeProfile(swApp, 100#, 50#, 5#) Then
            MsgBox "Tube profile created successfully!", vbInformation
        Else
            MsgBox "Failed to create tube profile.", vbExclamation
        End If
    End If
End Sub

'*******************************************************************************
' Example Sub: CreateSampleRoundTubeProfile
' Purpose: Demonstrates how to use the CreateRoundTubeProfile function
' Usage: Run this macro from SolidWorks to create a sample round tube profile
'*******************************************************************************
Sub CreateSampleRoundTubeProfile()
    Dim swApp As Object
    Set swApp = CreateObject("SldWorks.Application")
    
    ' Create a new part document
    Dim swModel As Object
    Set swModel = CreateNewPartDocument(swApp)
    
    If Not swModel Is Nothing Then
        ' Create a round tube profile: 50mm outer diameter with 3mm wall thickness
        If CreateRoundTubeProfile(swApp, 50#, 3#) Then
            MsgBox "Round tube profile created successfully!", vbInformation
        Else
            MsgBox "Failed to create round tube profile.", vbExclamation
        End If
    End If
End Sub

'*******************************************************************************
' Example Sub: CreateSampleChannelProfile
' Purpose: Demonstrates how to use the CreateChannelProfile function
' Usage: Run this macro from SolidWorks to create a sample channel profile
'*******************************************************************************
Sub CreateSampleChannelProfile()
    Dim swApp As Object
    Set swApp = CreateObject("SldWorks.Application")
    
    ' Create a new part document
    Dim swModel As Object
    Set swModel = CreateNewPartDocument(swApp)
    
    If Not swModel Is Nothing Then
        ' Create a channel profile: 100mm height, 50mm width, 5mm web, 7mm flange
        If CreateChannelProfile(swApp, 100#, 50#, 5#, 7#) Then
            MsgBox "Channel profile created successfully!", vbInformation
        Else
            MsgBox "Failed to create channel profile.", vbExclamation
        End If
    End If
End Sub
