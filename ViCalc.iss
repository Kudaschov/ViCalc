[Setup]
AppName=ViCalc
AppVersion=0.4.12.22
DefaultDirName={commonpf}\ViCalc
DefaultGroupName=ViCalc
OutputDir=dist_installer
OutputBaseFilename=ViCalcSetup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\ViCalc\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs


[Icons]
Name: "{group}\ViCalc"; Filename: "{app}\ViCalc.exe"
Name: "{commondesktop}\ViCalc"; Filename: "{app}\ViCalc.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: checkedonce

[Run]
Filename: "{app}\ViCalc.exe"; Description: "Launch ViCalc"; Flags: nowait postinstall skipifsilent
