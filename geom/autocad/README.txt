In order to use AutoCAD plugin you need to:
1. Download all the files from the directory to your computer. 
2. Install Microsoft .NET Framework (if not insalled).
3. Edit your acad.exe.conf file and add the following lines:
<runtime>
<loadFromRemoteSources enabled="true" />
</runtime>
Run Autocad and enter "netload" command in AutoCAD command line. 
