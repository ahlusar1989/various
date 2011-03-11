Option Explicit

Const strName = "COIS"
Const strServer = "GBRSDHEID0002"
Const strDatabase = "COIS"
Const strDescription = "COIS"
Const strTrustedConnection = "Yes"
const strQuotedID = "Yes"
Const strLanguage = ""
Const strRegional = ""

Dim objFSO
Dim objFolder
Dim strSystemPath
Dim objShell
Dim strRegPath

' get the location of the system folder
Set objFSO = wScript.CreateObject("Scripting.FileSystemObject") 
Set objFolder =objFSO.GetSpecialFolder(1) 
strSystemPath= objFolder.Path 

' create the ODBC entry in the registry
Set objShell = wScript.CreateObject("WScript.Shell") 
strRegPath= "HKLM\SOFTWARE\ODBC\ODBC.INI\" & strName & "\"
objShell.RegWrite  strRegPath & "Database" , strDatabase
objShell.RegWrite  strRegPath & "Description" , strDescription
objShell.RegWrite  strRegPath & "Driver" , strSystemPath & "\sqlsrv32.dll"
objShell.RegWrite  strRegPath & "Server" , strServer
objShell.RegWrite  strRegPath & "Trusted_Connection" , strTrustedConnection
objShell.RegWrite  strRegPath & "QuotedID" , strQuotedID

If strLanguage <> "" Then objShell.RegWrite  strRegPath & "Language" , strLanguage
If strRegional <> "" Then objShell.RegWrite  strRegPath & "Regional" , strRegional

' create the ODBC index entry in the registry
objShell.RegWrite "HKLM\SOFTWARE\ODBC\ODBC.INI\ODBC Data Sources\" & strName , "SQL Server" 

' Test it
Dim connection, cursor
Set connection = CreateObject("ADODB.Connection")
connection.Open "DSN=COIS;"
Set cursor = connection.Execute("SELECT * FROM tbldefaults")
MsgBox "defaultref  = " & cursor.Fields("defaultref").Value

connection.Close

