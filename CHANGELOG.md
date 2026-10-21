# Changelog — PasswGen

Todos los cambios relevantes de PasswGen se documentan en este archivo.

El formato sigue una organización por versiones y distingue entre cambios publicados y trabajo pendiente.

---

## [Unreleased]

### Pendiente

- Primera publicación del repositorio en GitHub.
- Creación de la Release pública de v1.0.0.
- Incorporación de documentación y capturas del proyecto.

---

## [1.0.0] — 2026-10-21

### Estado

Base estable preparada para su primera publicación pública en GitHub.

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

### Seguridad

- Sustitución del generador `random` por `secrets` para la selección de caracteres de las contraseñas.

### Compatibilidad

- `winreg` se carga únicamente en Windows para evitar una dependencia directa al importar el programa en otros sistemas.
- La distribución oficial de v1.0.0 se mantiene enfocada en Windows de 64 bits.

### Proyecto

- Reorganización del código fuente en `src/`.
- Separación del empaquetado de Windows en `packaging/windows/`.
- Separación del port experimental de Android en `android/`.
- Incorporación de `.gitignore`.
- Incorporación de `requirements.txt`.
- Eliminación de artefactos de compilación y archivos de prácticas ajenos al proyecto.
- Normalización de la versión a `1.0.0`.

### Nota histórica

PasswGen existía antes de su incorporación a GitHub. La versión v1.0.0 representa la base estable actual preparada para convertirse en la primera versión documentada y publicada desde el repositorio oficial.
