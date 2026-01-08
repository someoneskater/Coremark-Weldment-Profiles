' SolidWorks Weldment Profile Generator - VBA Macro
' Creates .sldlfp profile files from Coremark Metals data
' Usage: Run from SolidWorks VBA editor or as standalone macro

Option Explicit

Private swApp As SldWorks.SldWorks
Private swModel As SldWorks.ModelDoc2
Private swSketchMgr As SldWorks.SketchManager

Sub Main()
    Set swApp = Application.SldWorks

    Dim jsonPath As String
    jsonPath = GetFilePath("Select profile_data.json file", "JSON Files (*.json)|*.json")

    If jsonPath = "" Then Exit Sub

    Dim outputDir As String
    outputDir = GetFolderPath("Select output folder for profiles")

    If outputDir = "" Then Exit Sub

    ProcessProfiles jsonPath, outputDir

    MsgBox "Profile generation complete!", vbInformation
End Sub

Private Sub ProcessProfiles(jsonPath As String, outputDir As String)
    ' Note: VBA JSON parsing requires external library or manual parsing
    ' This example shows the structure - implement JSON parsing as needed

    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")

    Dim ts As Object
    Set ts = fso.OpenTextFile(jsonPath, 1)
    Dim jsonContent As String
    jsonContent = ts.ReadAll
    ts.Close

    ' Parse and create profiles (simplified example)
    ' In production, use a JSON library or parse manually

    ' Example: Create a sample angle profile
    CreateAngleProfile 2, 2, 0.25, outputDir, "Steel_2x2x0.25_Angle"

    ' Example: Create a sample square tube
    CreateSquareTubeProfile 3, 0.25, outputDir, "Steel_3x3x0.25_SquareTube"
End Sub

Private Sub CreateAngleProfile(leg1 As Double, leg2 As Double, thickness As Double, _
                               outputDir As String, filename As String)
    Dim templatePath As String
    templatePath = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplateLibFeatPart)

    Set swModel = swApp.NewDocument(templatePath, 0, 0, 0)
    Set swSketchMgr = swModel.SketchManager

    ' Select front plane and start sketch
    swModel.Extension.SelectByID2 "Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0
    swSketchMgr.InsertSketch True

    ' Draw L-shape (dimensions in meters)
    Dim L1 As Double, L2 As Double, T As Double
    L1 = leg1 * 0.0254  ' Convert inches to meters
    L2 = leg2 * 0.0254
    T = thickness * 0.0254

    ' Outer L-shape
    swSketchMgr.CreateLine 0, 0, 0, L1, 0, 0
    swSketchMgr.CreateLine L1, 0, 0, L1, T, 0
    swSketchMgr.CreateLine L1, T, 0, T, T, 0
    swSketchMgr.CreateLine T, T, 0, T, L2, 0
    swSketchMgr.CreateLine T, L2, 0, 0, L2, 0
    swSketchMgr.CreateLine 0, L2, 0, 0, 0, 0

    swSketchMgr.InsertSketch True

    ' Add custom properties
    AddCustomProperties swModel, leg1 & """ x " & leg2 & """ x " & thickness & """", "Angle"

    ' Save as .sldlfp
    SaveAsProfile swModel, outputDir, filename
End Sub

Private Sub CreateSquareTubeProfile(outerSize As Double, wallThickness As Double, _
                                    outputDir As String, filename As String)
    Dim templatePath As String
    templatePath = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplateLibFeatPart)

    Set swModel = swApp.NewDocument(templatePath, 0, 0, 0)
    Set swSketchMgr = swModel.SketchManager

    swModel.Extension.SelectByID2 "Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0
    swSketchMgr.InsertSketch True

    Dim outer As Double, inner As Double
    outer = outerSize * 0.0254 / 2
    inner = (outerSize - 2 * wallThickness) * 0.0254 / 2

    ' Outer rectangle
    swSketchMgr.CreateCenterRectangle 0, 0, 0, outer, outer, 0
    ' Inner rectangle
    swSketchMgr.CreateCenterRectangle 0, 0, 0, inner, inner, 0

    swSketchMgr.InsertSketch True

    AddCustomProperties swModel, outerSize & """ x " & outerSize & """ x " & wallThickness & """", "Square Tube"

    SaveAsProfile swModel, outputDir, filename
End Sub

Private Sub AddCustomProperties(model As SldWorks.ModelDoc2, sizeStr As String, profileType As String)
    Dim custPropMgr As SldWorks.CustomPropertyManager
    Set custPropMgr = model.Extension.CustomPropertyManager("")

    custPropMgr.Add3 "Size", swCustomInfoText, sizeStr, swCustomPropertyReplaceValue
    custPropMgr.Add3 "Profile_Type", swCustomInfoText, profileType, swCustomPropertyReplaceValue
    custPropMgr.Add3 "Source", swCustomInfoText, "Coremark Metals", swCustomPropertyReplaceValue
End Sub

Private Sub SaveAsProfile(model As SldWorks.ModelDoc2, outputDir As String, filename As String)
    Dim filePath As String
    filePath = outputDir & "\" & filename & ".sldlfp"

    model.Extension.SaveAs filePath, swSaveAsCurrentVersion, swSaveAsOptions_Silent, Nothing, 0, 0
    model.Close
End Sub

Private Function GetFilePath(title As String, filter As String) As String
    Dim fd As Object
    Set fd = CreateObject("UserAccounts.CommonDialog")
    fd.Filter = filter
    fd.FilterIndex = 1
    fd.InitialDir = "C:\"
    If fd.ShowOpen Then
        GetFilePath = fd.filename
    Else
        GetFilePath = ""
    End If
End Function

Private Function GetFolderPath(title As String) As String
    Dim shell As Object
    Set shell = CreateObject("Shell.Application")
    Dim folder As Object
    Set folder = shell.BrowseForFolder(0, title, 0)
    If Not folder Is Nothing Then
        GetFolderPath = folder.Self.Path
    Else
        GetFolderPath = ""
    End If
End Function
