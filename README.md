# KeyMint

**KeyMint** es un generador seguro de contraseñas de escritorio desarrollado en Python.

El proyecto nació como **PasswGen**. La versión **v1.0.0** fue su primera release pública estable; a partir del ciclo **v1.1.0** adopta oficialmente el nombre, identidad visual y estructura de **KeyMint**.

## Versión actual

**v1.1.0-dev**

## Estado

**En desarrollo**

La última versión pública estable continúa siendo **PasswGen v1.0.0** mientras se completa la transición a KeyMint.

## Características actuales

- Generación local de contraseñas.
- Longitud configurable.
- Selección aleatoria basada en `secrets`.
- Letras, números y símbolos como conjunto de generación.
- Mostrar u ocultar la contraseña generada.
- Copiar la contraseña al portapapeles.
- Interfaz gráfica de escritorio con Tkinter.
- Detección del tema del sistema.
- Apariencia clara y oscura.
- Identidad visual propia de KeyMint.
- Ejecutable para Windows mediante PyInstaller.
- Instalador para Windows mediante Inno Setup.

## Seguridad

KeyMint genera las contraseñas localmente y no necesita enviar datos a servicios externos.

La selección aleatoria utiliza el módulo `secrets` de Python.

La versión actual todavía no garantiza obligatoriamente al menos un carácter de cada categoría habilitada. Ese control forma parte de la evolución planificada del generador.

## Historial de identidad

### PasswGen v1.0.0

PasswGen fue el nombre original del proyecto y corresponde a su primera versión pública estable.

La release histórica continúa disponible en:

https://github.com/RobDev512/PasswGen/releases/tag/v1.0.0

### KeyMint v1.1.0+

KeyMint es la identidad actual del proyecto.

La transición incluye:

- nuevo nombre;
- nueva identidad visual;
- reorganización de recursos;
- nuevo ejecutable `KeyMint.exe`;
- nuevo empaquetado;
- renovación de la interfaz;
- limpieza de componentes experimentales obsoletos.

## Ejecutar desde el código fuente

Requisitos:

- Python 3.11 o compatible.
- Pillow.
- pyperclip.

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

## Instalador

El instalador de Windows se define en:

```text
packaging\windows\KeyMint.iss
```

Durante el desarrollo de v1.1.0 la salida prevista es:

```text
dist\installer\KeyMint_Setup_v1.1.0-dev.exe
```

## Estructura del proyecto

```text
KeyMint/
├── assets/
│   ├── branding/
│   │   ├── KeyMintIcon.ico
│   │   ├── KeyMintIcon.png
│   │   ├── KeyMintLogo.png
│   │   ├── KeyMintLogoHorizontal.png
│   │   ├── KeyMintLogoTransparent.png
│   │   └── KeyMintMono.png
│   └── icons/
│       ├── eye-closed.png
│       └── eye-open.png
├── docs/
│   ├── BRANDING.md
│   ├── CHANGELOG.md
│   ├── ROADMAP.md
│   └── images/
├── packaging/
│   └── windows/
│       ├── KeyMint.iss
│       └── KeyMint.spec
├── .gitignore
├── KeyMint.py
├── LICENSE
├── README.md
└── requirements.txt
```

Las carpetas `.venv/`, `build/`, `dist/`, `Output/` y `__pycache__/` son artefactos locales y no forman parte del código fuente versionado.

## Identidad visual

La identidad de KeyMint se documenta en:

```text
docs/BRANDING.md
```

## Roadmap

La planificación por versiones se encuentra en:

```text
docs/ROADMAP.md
```

## Historial de cambios

El historial del proyecto se encuentra en:

```text
docs/CHANGELOG.md
```

## Plataformas

La distribución oficial continúa enfocada en **Windows de 64 bits**.

El antiguo port experimental Android de PasswGen fue retirado durante la transición a KeyMint. El soporte móvil se retomará únicamente cuando exista una implementación mantenida y probada.

## Licencia

KeyMint se distribuye bajo la licencia MIT. Consulta `LICENSE`.

## Autor

Desarrollado por **RobDev512**.
