; ============================================================
; KeyMint - Instalador para Windows
; Desarrollo v1.1.0
; ============================================================

#define MyAppName "KeyMint"
#define MyAppVersion "1.1.0-dev"
#define MyAppPublisher "RobDev512"
#define MyAppExeName "KeyMint.exe"

[Setup]

AppId=KeyMint_RobDev512

AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\KeyMint
DefaultGroupName=KeyMint

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

OutputDir=..\..\dist\installer
OutputBaseFilename=KeyMint_Setup_v1.1.0-dev

SetupIconFile=..\..\assets\branding\KeyMintIcon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Tasks]

Name: "desktopicon"; Description: "Crear un acceso directo en el escritorio"; GroupDescription: "Accesos directos adicionales:"; Flags: unchecked

[Files]

Source: "..\..\dist\KeyMint.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]

Name: "{autoprograms}\KeyMint"; Filename: "{app}\{#MyAppExeName}"

Name: "{autodesktop}\KeyMint"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]

Filename: "{app}\{#MyAppExeName}"; Description: "Ejecutar {#MyAppName}"; Flags: nowait postinstall skipifsilent

