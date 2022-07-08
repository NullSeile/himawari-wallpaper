Set shell = CreateObject("WScript.Shell")
command = "python " & CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\himawari.py"
shell.Run "conda activate himawari", 0
shell.Run command, 0