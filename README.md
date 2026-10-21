# PasswGen

Generador de contraseñas de escritorio desarrollado en Python, orientado a crear contraseñas aleatorias de forma local y sencilla.

## Versión actual

**v1.0.0**

## Estado

**Estable / publicada**

## Características

- Generación local de contraseñas.
- Longitud configurable.
- Uso de `secrets` para la selección aleatoria de caracteres.
- Letras, números y símbolos como base del conjunto de generación.
- Mostrar u ocultar la contraseña generada.
- Copiar la contraseña al portapapeles.
- Interfaz gráfica con Tkinter.
- Recursos visuales propios.
- Detección de tema del sistema y soporte de apariencia clara/oscura.
- Instalador para Windows de 64 bits.

## Seguridad

PasswGen genera contraseñas localmente y no necesita enviar datos a servicios externos.

La versión v1.0.0 utiliza el módulo `secrets` de Python para la selección aleatoria de caracteres, en lugar de un generador pensado para simulación o uso general.

La versión actual no garantiza que cada contraseña contenga obligatoriamente al menos un carácter de cada categoría. Esa opción forma parte del roadmap futuro.

## Descargar

La distribución oficial de PasswGen v1.0.0 está orientada a **Windows de 64 bits**.

[Descargar PasswGen Setup v1.0.0](https://github.com/RobDev512/PasswGen/releases/download/v1.0.0/PasswGen_Setup_v1.0.0.exe)

También puedes consultar la release completa:

https://github.com/RobDev512/PasswGen/releases/tag/v1.0.0

## Ejecutar desde el código fuente

Requisitos:

- Python 3.11 o compatible.
- Pillow.
- pyperclip.

Instala las dependencias con:

```powershell
python -m pip install -r ".\requirements.txt"
```

Ejecuta la aplicación con:

```powershell
python ".\src\GenPasswords.py"
```

Para comprobar la sintaxis:

```powershell
python -m py_compile ".\src\GenPasswords.py"
```

## Compilación para Windows

El proyecto utiliza PyInstaller para generar el ejecutable.

Desde la raíz del proyecto:

```powershell
python -m PyInstaller --clean --noconfirm ".\packaging\windows\GenPasswords.spec"
```

El ejecutable se genera en:

```text
dist\GenPasswords.exe
```

## Instalador

El instalador de Windows se construye con Inno Setup a partir de:

```text
packaging\windows\GenPasswords.iss
```

La salida esperada es:

```text
dist\installer\PasswGen_Setup_v1.0.0.exe
```

## Estructura del proyecto

```text
PasswGen/
├── android/
│   ├── buildozer.spec
│   └── GCSAndroidPort.py
├── docs/
│   └── images/
├── packaging/
│   └── windows/
│       ├── GenPasswords.iss
│       └── GenPasswords.spec
├── src/
│   ├── GenPasswords.py
│   ├── Logo.ico
│   ├── ojo.png
│   └── ver.png
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── ROADMAP.md
└── requirements.txt
```

Las carpetas `build/`, `dist/`, `Output/` y los archivos `__pycache__/` son artefactos generados localmente y no forman parte del código fuente versionado.

## Android

El directorio `android/` conserva un port experimental basado en Kivy/Buildozer.

Actualmente no forma parte de la distribución oficial de PasswGen y se mantiene como trabajo experimental para una posible revisión futura.

## Roadmap

La planificación por versiones se encuentra en:

```text
ROADMAP.md
```

## Historial de cambios

Los cambios publicados y la evolución de las versiones se documentan en:

```text
CHANGELOG.md
```

## Licencia

PasswGen se distribuye bajo la licencia MIT. Consulta `LICENSE` para más información.

## Autor

Desarrollado por **RobDev512**.
