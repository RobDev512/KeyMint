# KeyMint Android Preview

Port móvil experimental de KeyMint basado en Kivy.

Esta carpeta no modifica ni reemplaza la release estable de escritorio `v1.1.0`. El APK Android correspondiente a este estado sigue considerándose una **Preview** y no una distribución Android estable firmada.

La lógica del generador conserva el comportamiento principal de KeyMint v1.1.0:

- longitud de 4 a 64 caracteres;
- `secrets.choice`;
- letras, números y símbolos;
- mostrar/ocultar;
- copiar;
- limpiar;
- tema claro/oscuro.

## Preparar branding

Antes de compilar, desde la raíz del proyecto ejecuta:

```powershell
& ".\.venv\Scripts\python.exe" ".\android\prepare_assets.py"
```

Eso prepara el icono de aplicación y los recursos de interfaz necesarios dentro de `android/assets/` a partir de los recursos oficiales de KeyMint.

## Compilación en Windows

Buildozer requiere un entorno Linux/macOS. En Windows puede utilizarse WSL2.

Conviene copiar el repositorio completo al sistema de archivos Linux de WSL, por ejemplo `~/KeyMint`, y compilar allí en lugar de hacerlo desde `/mnt/c`.

Con Buildozer instalado:

```bash
cd ~/KeyMint/android
buildozer -v android debug
```

El APK aparecerá dentro de `android/bin/`.

## Compilación reproducible en GitHub Actions

El workflow `.github/workflows/android-preview.yml` genera un APK `debug` para `arm64-v8a` mediante Buildozer/python-for-android.

La compilación validada para este cierre fue generada con:

- versión de aplicación: `1.1.0`;
- Android API: `36`;
- Android min API: `24`;
- Android NDK: `29`;
- arquitectura: `arm64-v8a`.

Artefacto validado:

```text
keymint-1.1.0-arm64-v8a-debug.apk
```

SHA-256:

```text
C022FA11045E30B3BA7F2944871B88F1A14999B90A5AC91ECABDB4AB97575B98
```

## Estado de validación

El 2 de noviembre de 2026 esta Preview fue instalada y probada manualmente en un dispositivo Android físico. La prueba de cierre se consideró satisfactoria para el flujo principal de la aplicación, incluyendo instalación, apertura, generación, mostrar/ocultar, copiar, limpiar, cambio de tema y longitud máxima de 64 caracteres.

Esto valida la Preview utilizada durante el desarrollo, pero no equivale todavía a soporte Android estable general. Quedan fuera de este cierre pruebas amplias en múltiples dispositivos, resoluciones y versiones de Android, además de la generación y firma de un APK/AAB de release para distribución pública formal.
