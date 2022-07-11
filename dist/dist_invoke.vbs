Set shell = CreateObject("WScript.Shell")
command = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\himawari.exe"
shell.Run command, 0