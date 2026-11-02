# KeyMint Android Preview

Port móvil experimental de KeyMint.

Esta carpeta no modifica ni reemplaza la release estable de escritorio `v1.1.0`.

La interfaz Android se implementa con Kivy porque CustomTkinter/Tkinter no es una interfaz Android. La lógica del generador conserva el comportamiento de KeyMint v1.1.0:

- longitud de 4 a 64 caracteres;
- `secrets.choice`;
- letras, números y símbolos;
- mostrar/ocultar;
- copiar;
- limpiar;
- tema claro/oscuro.

## Compilación en Windows

Buildozer requiere Linux/macOS. En Windows se utiliza WSL2.

Conviene copiar el repositorio completo al sistema de archivos Linux de WSL, por ejemplo `~/KeyMint`, y compilar allí en lugar de hacerlo desde `/mnt/c`.

Con Buildozer instalado:

```bash
cd ~/KeyMint/android
buildozer -v android debug
```

El APK aparecerá dentro de `android/bin/`.

## Estado

Este port debe considerarse `Android Preview` hasta probarlo en un dispositivo físico. Antes de declararlo estable deben validarse al menos:

- instalación/desinstalación;
- portapapeles;
- tema claro/oscuro;
- contraseñas de 64 caracteres;
- varias resoluciones;
- comportamiento táctil.
