Dim sap As Object
Dim conn As Object
 
Set sap = CreateObject("SAP.Functions")
Set conn = sap.Connection
conn.System = "SYSTEM"
conn.client = "123"
conn.user = "USER"
conn.Password = "PW"
conn.Language = "DE"
 
If conn.logon(0, False) <> True Then
    MsgBox "Logon to the SAP system is not possible", vbOKOnly, "Comment"
End if

