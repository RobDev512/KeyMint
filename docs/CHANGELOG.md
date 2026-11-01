# Changelog — KeyMint

Todos los cambios relevantes de KeyMint y de su etapa histórica como PasswGen se documentan en este archivo.

---

## [Unreleased]

### v1.1.0 — En desarrollo

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

### Proyecto

- El punto de entrada principal pasa a ser `KeyMint.py` en la raíz.
- Eliminación de la antigua carpeta `src/`.
- Recursos de interfaz trasladados a `assets/icons/`.
- Recursos de marca centralizados en `assets/branding/`.
- `CHANGELOG.md` y `ROADMAP.md` trasladados a `docs/`.
- Renombrado de:
  - `GenPasswords.spec` a `KeyMint.spec`.
  - `GenPasswords.iss` a `KeyMint.iss`.
- Eliminación de `GenPasswords.py`.
- Eliminación del antiguo `Logo.ico`.
- Eliminación del port experimental Android basado en Kivy/Buildozer.
- Creación de un entorno virtual local de desarrollo `.venv/`.

### Interfaz

- Actualización inicial de la interfaz al nombre KeyMint.
- Aplicación de la nueva paleta mint/navy.
- Nuevo encabezado con símbolo y nombre KeyMint.
- Conservación de temas claro y oscuro.
- Preparación para una renovación visual mayor durante v1.1.0.

### Empaquetado

- El ejecutable pasa a llamarse `KeyMint.exe`.
- PyInstaller actualizado para utilizar la nueva estructura y los recursos de KeyMint.
- Inno Setup actualizado para generar `KeyMint_Setup_v1.1.0-dev.exe`.
- El instalador conserva una referencia histórica compatible con la etapa PasswGen cuando corresponde.

### Pendiente antes de publicar v1.1.0

- Barra de título propia.
- Ventana y controles visualmente redondeados.
- Renovación general de la interfaz.
- Sustitución de iconos simples de interfaz por recursos vectoriales cuando corresponda.
- Revisión de escalado y accesibilidad.
- Finalización del instalador.
- Renombrado del repositorio remoto a KeyMint.
- Pruebas completas del ejecutable e instalador.

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
