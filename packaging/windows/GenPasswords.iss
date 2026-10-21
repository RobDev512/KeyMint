; ============================================================
; PasswGen - Instalador para Windows
; Version 1.0.0
; ============================================================

#define MyAppName "Generador de Contraseñas Seguras"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "RobDev512"
#define MyAppExeName "GenPasswords.exe"

[Setup]
; Informacion de la aplicacion
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

; Carpeta de instalacion
DefaultDirName={autopf}\PasswGen
DefaultGroupName=PasswGen

; PasswGen para Windows de 64 bits
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

; Archivo generado por Inno Setup
OutputDir=..\..\dist\installer
OutputBaseFilename=PasswGen_Setup_v1.0.0

; Icono del instalador
SetupIconFile=..\..\src\Logo.ico

; Icono mostrado en Aplicaciones instaladas
UninstallDisplayIcon={app}\{#MyAppExeName}

; Configuracion del instalador
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

; Permite elegir si se crea el acceso directo del escritorio
[Tasks]
Name: "desktopicon"; Description: "Crear un acceso directo en el escritorio"; GroupDescription: "Accesos directos adicionales:"; Flags: unchecked

[Files]
; Ejecutable generado previamente con PyInstaller
Source: "..\..\dist\GenPasswords.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Acceso directo del menu Inicio
Name: "{autoprograms}\PasswGen"; Filename: "{app}\{#MyAppExeName}"

; Acceso directo opcional del escritorio
Name: "{autodesktop}\PasswGen"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Opcion para ejecutar PasswGen al terminar la instalacion
Filename: "{app}\{#MyAppExeName}"; Description: "Ejecutar {#MyAppName}"; Flags: nowait postinstall skipifsilent