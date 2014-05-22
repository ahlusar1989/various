Dim sap As Object
Dim conn As Object
 
Sub T_login()
          Set sap = CreateObject("SAP.Functions")
          Set conn = sap.Connection
          conn.System = "SYSTEM"
          conn.client = "900"
          conn.user = "G2"
          conn.Password = "12345"
          conn.Language = "EN"
          
If conn.logon(0, False) Then
               MsgBox "Logon to the SAP system is not possible", vbOKOnly, "Comment"
               Else
End If
 
If Not IsObject(SapGuiApp) Then
           Set SapGuiApp = CreateObject("Sapgui.ScriptingCtrl.2")
End If
 
If Not IsObject(Connection) Then
          Set Connection = SapGuiApp.OpenConnection("SYSTEM", True)
End If
 
If Not IsObject(session) Then
         Set session = Connection.Children(0)
End If
 
            session.findById("wnd[0]/usr/txtRSYST-MANDT").Text = "CLIENT"
            session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = "USER"
            session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = "PASSWORD"
            session.findById("wnd[0]/usr/txtRSYST-LANGU").Text = "EN"
            session.findById("wnd[0]/usr/txtRSYST-LANGU").SetFocus
            session.findById("wnd[0]/usr/txtRSYST-LANGU").caretPosition = 2
            session.findById("wnd[0]").sendVKey 0
 
Set wshell = CreateObject("Wscript.Shell")
         wshell.Run Chr(34) & Path & "\script.vbs" & Chr(34), 1, 1
End Sub
