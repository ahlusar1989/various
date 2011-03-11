' Checks for McAfee taking all the clock cycles (thereby preventing any malware from running).
Const FileName = "C:\Documents and Settings\farringtonni\My Documents\McAfee.log"
Set objFSO = CreateObject("Scripting.FileSystemObject")
If objFSO.FileExists(FileName) Then
   Set logfile = objfso.OpenTextFile(FileName, 8, True)
Else
   Set logfile = objfso.CreateTextFile(FileName, 2, True)
End If 

Do    
    For each Process in GetObject("winmgmts:").ExecQuery("Select * from Win32_Process where ExecutablePath Like '%McAfee%'")
        usage = CPUUSage(Process.Handle)
        If usage > 5 Then
            text = Now() & "," & Process.Name & "," & usage & " % " 
            logfile.WriteLine text
        End If
    Next
    WScript.Sleep(1000) 
Loop ' Do for ever

logfile.Close
   
Function CPUUSage( ProcID )

    On Error Resume Next
    Set objService = GetObject("Winmgmts:{impersonationlevel=impersonate}!\Root\Cimv2")
    
    For Each objInstance1 in objService.ExecQuery("Select * from Win32_PerfRawData_PerfProc_Process where IDProcess = '" & ProcID & "'")
       N1 = objInstance1.PercentProcessorTime
       D1 = objInstance1.TimeStamp_Sys100NS
       Exit For
    Next
    
    WScript.Sleep(2000)

    For Each perf_instance2 in objService.ExecQuery("Select * from Win32_PerfRawData_PerfProc_Process where IDProcess = '" & ProcID & "'")
       N2 = perf_instance2.PercentProcessorTime
       D2 = perf_instance2.TimeStamp_Sys100NS
       Exit For
    Next
    
    ' CounterType - PERF_100NSEC_TIMER_INV Formula - (1- ((N2 - N1) / (D2 - D1))) x 100
    Nd = (N2 - N1)
    Dd = (D2-D1)
    PercentProcessorTime = ( (Nd/Dd))  * 100

    CPUUSage = Round(PercentProcessorTime ,0)
   
End Function