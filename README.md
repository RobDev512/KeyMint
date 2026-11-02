# KeyMint

**KeyMint** es un generador de contraseñas desarrollado en Python que prioriza la generación local y una interfaz propia.

El proyecto nació como **PasswGen**. La versión **v1.0.0** fue su primera release pública estable; a partir de **v1.1.0** adopta oficialmente el nombre, identidad visual y estructura de **KeyMint**.

## Versión actual

**v1.1.0**

## Estado

**Publicada y cerrada para Windows de 64 bits.**

La última versión pública estable es **KeyMint v1.1.0**. El repositorio también contiene una implementación **Android Preview v1.1.0** basada en Kivy, compilada mediante GitHub Actions y validada manualmente en un dispositivo Android físico. Esa Preview sigue siendo una compilación `debug` y no se presenta como distribución Android estable firmada.

## Características actuales

- Generación local de contraseñas.
- Longitud configurable entre 4 y 64 caracteres.
- Selección aleatoria basada en `secrets`.
- Letras, números y símbolos como conjunto de generación.
- Mostrar u ocultar la contraseña generada.
- Copiar la contraseña al portapapeles.
- Limpiar el resultado mostrado.
- Apariencia clara y oscura.
- Identidad visual propia de KeyMint.
- Aplicación de escritorio para Windows con CustomTkinter/Tkinter.
- Ejecutable mediante PyInstaller.
- Instalador para Windows mediante Inno Setup.
- Android Preview basada en Kivy con compilación reproducible mediante GitHub Actions.

## Seguridad

KeyMint genera las contraseñas localmente y no necesita enviar datos a servicios externos.

La selección aleatoria utiliza el módulo `secrets` de Python.

La versión v1.1.0 todavía no garantiza obligatoriamente al menos un carácter de cada categoría habilitada. Ese control forma parte de la evolución planificada del generador.

## Release estable v1.1.0

La distribución estable de esta versión corresponde a **Windows de 64 bits**.

Instalador:

```text
KeyMint_Setup_v1.1.0.exe
```

SHA-256:

```text
165EFE3B53FBF9DF051F21F09A1421C5328D2AEC32B6B2EFD1B2D556673D8D1B
```

Release:

https://github.com/RobDev512/KeyMint/releases/tag/v1.1.0

## Android Preview v1.1.0

La carpeta `android/` contiene una implementación móvil separada de la interfaz de escritorio. Utiliza Kivy porque CustomTkinter/Tkinter no constituye una interfaz Android.

La compilación de cierre validada fue:

```text
keymint-1.1.0-arm64-v8a-debug.apk
```

SHA-256:

```text
C022FA11045E30B3BA7F2944871B88F1A14999B90A5AC91ECABDB4AB97575B98
```

La Preview fue instalada y probada manualmente en un dispositivo físico el **2 de noviembre de 2026**. La validación del flujo principal fue satisfactoria. No se considera todavía soporte Android estable general porque el APK es `debug`, no está firmado como release pública y no se ha validado en una matriz amplia de dispositivos y versiones de Android.

Consulta `android/README.md` para detalles de compilación y validación.

## Historial de identidad

### PasswGen v1.0.0

PasswGen fue el nombre original del proyecto y corresponde a su primera versión pública estable.

La release histórica se conserva en:

https://github.com/RobDev512/KeyMint/releases/tag/v1.0.0

### KeyMint v1.1.0+

KeyMint es la identidad actual del proyecto.

La transición incluyó:

- nuevo nombre;
- nueva identidad visual;
- reorganización de recursos;
- nuevo ejecutable `KeyMint.exe`;
- nuevo empaquetado;
- renovación de la interfaz;
- preparación de una nueva Preview Android mantenida por separado de la interfaz de escritorio.

## Ejecutar desde el código fuente

Requisitos de escritorio:

- Python 3.11 o compatible.
- dependencias incluidas en `requirements.txt`.

Crear un entorno virtual local:

```powershell
python -m venv .venv
```

Instalar dependencias:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r ".\requirements.txt"
```

Ejecutar KeyMint:

```powershell
& ".\.venv\Scripts\python.exe" ".\KeyMint.py"
```

Comprobar sintaxis:

```powershell
& ".\.venv\Scripts\python.exe" -m py_compile ".\KeyMint.py"
```

## Compilación para Windows

PyInstaller se instala en el entorno virtual de desarrollo:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install pyinstaller
```

Construir el ejecutable:

```powershell
& ".\.venv\Scripts\python.exe" -m PyInstaller --clean ".\packaging\windows\KeyMint.spec"
```

Salida:

```text
dist\KeyMint.exe
```

## Instalador de Windows

El instalador se define en:

```text
packaging\windows\KeyMint.iss
```

La salida de v1.1.0 es:

```text
dist\installer\KeyMint_Setup_v1.1.0.exe
```

## Estructura principal

```text
KeyMint/
├── android/
│   ├── buildozer.spec
│   ├── main.py
│   ├── prepare_assets.py
│   └── README.md
├── assets/
│   ├── branding/
│   └── icons/
├── docs/
│   ├── BRANDING.md
│   ├── CHANGELOG.md
│   └── ROADMAP.md
├── packaging/
│   └── windows/
│       ├── KeyMint.iss
│       └── KeyMint.spec
├── .github/
│   └── workflows/
│       └── android-preview.yml
├── .gitignore
├── KeyMint.py
├── LICENSE
├── README.md
└── requirements.txt
```

Las carpetas `.venv/`, `build/`, `dist/`, `releases/`, `Output/`, `android/bin/`, `android/.buildozer/` y otros artefactos generados son locales y no forman parte del código fuente versionado.

## Documentación

- Identidad visual: `docs/BRANDING.md`
- Historial de cambios: `docs/CHANGELOG.md`
- Planificación: `docs/ROADMAP.md`
- Android Preview: `android/README.md`

## Plataformas

- **Windows 64-bit:** soporte estable de v1.1.0.
- **Android arm64-v8a:** Preview funcional validada manualmente; no release estable firmada.
- **Linux/macOS:** sin distribución oficial en v1.1.0.

## Licencia

KeyMint se distribuye bajo la licencia MIT. Consulta `LICENSE`.

## Autor

Desarrollado por **RobDev512**.
