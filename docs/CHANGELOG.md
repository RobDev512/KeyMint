# Changelog — KeyMint

Todos los cambios relevantes de KeyMint y de su etapa histórica como PasswGen se documentan en este archivo.

---

## [Unreleased]

### v1.1.0 — Implementación terminada; pendiente publicación

### Identidad

- Renombrado del proyecto de **PasswGen** a **KeyMint**.
- Incorporación de una identidad visual propia basada en tonos mint, turquesa y navy.
- Incorporación de recursos oficiales de branding:
  - `KeyMintLogo.png`
  - `KeyMintLogoHorizontal.png`
  - `KeyMintIcon.png`
  - `KeyMintLogoTransparent.png`
  - `KeyMintMono.png`
  - `KeyMintIcon.ico`
- Creación de `docs/BRANDING.md`.
- Definición de un estándar reutilizable de recursos de marca para proyectos RobDev512.
- Renombrado del repositorio remoto a `RobDev512/KeyMint`.
- Integración de KeyMint dentro del Hub de RobDev512 con página e identidad propias.

### Proyecto

- El punto de entrada principal pasa a ser `KeyMint.py` en la raíz.
- Eliminación de la antigua carpeta `src/`.
- Recursos de interfaz trasladados a `assets/icons/`.
- Recursos de marca centralizados en `assets/branding/`.
- Recursos de iconos reorganizados por función:
  - `assets/icons/theme/`
  - `assets/icons/ui/`
  - `assets/icons/visibility/`
- Eliminación de los antiguos `eye-open.png` y `eye-closed.png`.
- `CHANGELOG.md` y `ROADMAP.md` trasladados a `docs/`.
- Renombrado de:
  - `GenPasswords.spec` a `KeyMint.spec`.
  - `GenPasswords.iss` a `KeyMint.iss`.
- Eliminación de `GenPasswords.py`.
- Eliminación del antiguo `Logo.ico`.
- Eliminación del port experimental Android basado en Kivy/Buildozer.
- Creación de un entorno virtual local de desarrollo `.venv/`.
- Incorporación de `customtkinter` como dependencia de interfaz.

### Interfaz

- Renovación completa de la interfaz bajo la identidad KeyMint.
- Aplicación de la paleta mint/navy.
- Nuevo encabezado con símbolo y nombre KeyMint.
- Barra de título propia.
- Controles personalizados de tema, minimizar y cerrar.
- Ventana fija y centrada.
- Ancho de escritorio fijado en **455 px**.
- Eliminación del redimensionamiento manual.
- Temas claro y oscuro revisados.
- Ventana redondeada mediante DWM nativo de Windows.
- Borde exterior mediante `DWMWA_BORDER_COLOR`.
- Sustitución de regiones manuales `SetWindowRgn` por el marco nativo DWM.
- Mejora de jerarquía visual, espaciado y distribución.
- Panel principal con superficie redondeada antialias.
- Estados visuales para controles secundarios.
- Botón **Limpiar** para retirar la contraseña mostrada.
- Campo de contraseña no editable manualmente pero seleccionable.
- Soporte para `Ctrl+A` y `Ctrl+C` sobre la contraseña generada.
- Mostrar/ocultar contraseña con iconografía semánticamente correcta:
  - ojo cerrado cuando la contraseña está oculta;
  - ojo abierto cuando está visible.
- Barra horizontal compacta y centrada para contraseñas que exceden el ancho visible.
- Desplazamiento horizontal mediante la barra y gestos/eventos compatibles del sistema.
- Revisión de escalado DPI.

### Generación y controles

- Longitud configurable entre 4 y 64 caracteres.
- Slider rediseñado para mayor visibilidad.
- Control del slider mediante teclado:
  - `←` / `↓` reduce un carácter;
  - `→` / `↑` aumenta un carácter.
- El slider adquiere foco al interactuar con él.
- Se conserva generación local mediante `secrets`.
- Se conserva copiado al portapapeles.

### Iconografía

- Incorporación de iconos propios para tema claro/oscuro.
- Incorporación de nuevos iconos de mostrar/ocultar.
- Reorganización de iconos reutilizados en una carpeta propia de KeyMint.
- Eliminación de nombres y rutas asociadas a otros proyectos.
- Conservación de PNG/ICO donde Tkinter y Windows los requieren.

### Empaquetado

- El ejecutable pasa a llamarse `KeyMint.exe`.
- PyInstaller actualizado para utilizar la estructura y recursos de KeyMint.
- Inno Setup actualizado para generar `KeyMint_Setup_v1.1.0.exe`.
- El instalador utiliza una identidad propia mediante `AppId=KeyMint_RobDev512`.
- Instalación probada en `C:\Program Files\KeyMint`.
- PasswGen v1.0.0 permanece como release histórica independiente.

### Pendiente antes de publicar v1.1.0

- Actualizar documentación final.
- Reconstruir `KeyMint.exe` con el código definitivo.
- Reconstruir el instalador con el ejecutable definitivo.
- Probar el ejecutable empaquetado.
- Probar instalación y desinstalación finales.
- Revisar `git diff` y confirmar que solo se incluyen recursos necesarios.
- Crear commit de cierre de v1.1.0.
- Publicar los cambios en GitHub.
- Preparar release pública de v1.1.0 cuando las pruebas finales sean satisfactorias.

---

## [1.0.0] — 2026-10-21

### Estado

Primera versión pública estable y primera release formal del proyecto bajo el nombre **PasswGen**.

### Añadido

- Generación de contraseñas desde una interfaz gráfica de escritorio.
- Longitud configurable.
- Mostrar y ocultar la contraseña generada.
- Copiado de la contraseña al portapapeles.
- Detección de tema del sistema.
- Apariencia clara y oscura.
- Recursos gráficos propios.
- Empaquetado mediante PyInstaller.
- Instalador de Windows mediante Inno Setup.
- Instalación nativa en Windows de 64 bits.
- Identificación interna mediante `APP_NAME` y `APP_VERSION`.
- Documentación inicial.
- Licencia MIT.

### Seguridad

- Sustitución del generador `random` por `secrets` para la selección de caracteres de las contraseñas.

### Compatibilidad

- `winreg` se carga únicamente en Windows.
- La distribución oficial de v1.0.0 se mantiene enfocada en Windows de 64 bits.

### Proyecto

- Código fuente organizado inicialmente en `src/`.
- Empaquetado de Windows separado en `packaging/windows/`.
- Port Android experimental separado en `android/`.
- Incorporación de `.gitignore`.
- Incorporación de `requirements.txt`.
- Normalización de la versión a `1.0.0`.
- Creación del repositorio público oficial `RobDev512/PasswGen`.

### Nota histórica

PasswGen existía antes de su incorporación a GitHub. La versión v1.0.0 formalizó esa base estable y constituye la primera versión pública documentada del proyecto.
