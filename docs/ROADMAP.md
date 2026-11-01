# ROADMAP — KeyMint

## Estado actual

**Versión en desarrollo:** v1.1.0-dev  
**Última versión pública:** PasswGen v1.0.0  
**Estado general:** En desarrollo  
**Plataforma principal:** Windows 64-bit  
**Android:** Sin soporte activo

> KeyMint es la continuación directa de PasswGen.
> La versión v1.0.0 permanece como referencia histórica de la identidad anterior.

---

## v1.0.0 — PasswGen / Base estable

**Estado:** Publicada

Primera versión formal y pública del proyecto.

### Generación

- Generación local de contraseñas.
- Longitud configurable.
- Letras, números y símbolos.
- Selección aleatoria basada en `secrets`.

### Interfaz

- Aplicación de escritorio basada en Tkinter.
- Mostrar y ocultar contraseña.
- Copiar al portapapeles.
- Tema claro y oscuro.
- Detección del tema del sistema.

### Distribución

- Ejecutable mediante PyInstaller.
- Instalador mediante Inno Setup.
- Distribución para Windows de 64 bits.
- Release pública en GitHub.

---

## v1.1.0 — Transición a KeyMint

**Estado:** En desarrollo

Primera versión bajo la nueva identidad **KeyMint**.

Esta versión prioriza identidad, estructura, empaquetado y renovación visual. El alcance funcional se mantendrá controlado para no mezclar demasiados cambios de seguridad y UX en una sola release.

### Identidad

- [x] Renombrar PasswGen a KeyMint.
- [x] Crear identidad visual propia.
- [x] Crear conjunto oficial de recursos de branding.
- [x] Documentar la identidad en `docs/BRANDING.md`.
- [ ] Renombrar el repositorio remoto a `KeyMint`.

### Estructura

- [x] Mover `KeyMint.py` a la raíz.
- [x] Eliminar la antigua estructura `src/`.
- [x] Crear `assets/branding/`.
- [x] Crear `assets/icons/`.
- [x] Mover CHANGELOG y ROADMAP a `docs/`.
- [x] Retirar el port Android experimental obsoleto.
- [x] Crear `.venv` local de desarrollo.

### Empaquetado

- [x] Renombrar configuración de PyInstaller a `KeyMint.spec`.
- [x] Renombrar configuración de Inno Setup a `KeyMint.iss`.
- [x] Generar `KeyMint.exe`.
- [ ] Generar y probar `KeyMint_Setup_v1.1.0-dev.exe`.
- [ ] Validar actualización desde la etapa histórica PasswGen cuando corresponda.

### Renovación de interfaz

- [ ] Eliminar la barra de título estándar y crear una barra propia.
- [ ] Añadir controles propios de minimizar, maximizar/restaurar y cerrar.
- [ ] Redondear visualmente la ventana.
- [ ] Redondear botones, campos, paneles y otros componentes.
- [ ] Mejorar jerarquía visual, espaciado y distribución.
- [ ] Unificar estados hover, focus, active y disabled.
- [ ] Revisar tema claro y oscuro.
- [ ] Revisar escalado DPI.
- [ ] Mejorar navegación por teclado y accesibilidad.

### Sistema de iconos

- [ ] Crear iconos de interfaz con lenguaje visual consistente.
- [ ] Utilizar SVG como fuente maestra para iconos simples cuando sea apropiado.
- [ ] Mantener PNG/ICO derivados cuando la plataforma o Tkinter lo requiera.
- [ ] Evaluar vectorización real del símbolo de KeyMint en el futuro.

---

## v1.2.0 — Control de generación

**Estado:** Pendiente

Ampliación del control sobre las contraseñas generadas.

### Categorías

- Activar o desactivar minúsculas.
- Activar o desactivar mayúsculas.
- Activar o desactivar números.
- Activar o desactivar símbolos.
- Evitar configuraciones sin caracteres disponibles.

### Seguridad y complejidad

- Garantizar al menos un carácter de cada categoría habilitada.
- Excluir caracteres ambiguos.
- Indicador de complejidad.
- Estimación informativa de entropía.

### Generación múltiple

- Generar varias contraseñas de una sola vez.
- Copiar una contraseña individual.
- Copiar el conjunto completo.

---

## v1.3.0 — Experiencia de usuario

**Estado:** Pendiente

- Presets de generación.
- Recordar preferencias no sensibles.
- Mejor respuesta visual al copiar.
- Limpieza opcional del portapapeles después de un intervalo.
- Atajos de teclado.
- Mejoras de accesibilidad.
- Mejor navegación mediante teclado.

---

## v1.4.0 — Herramientas y productividad

**Estado:** Pendiente

- Generación de frases de contraseña.
- Plantillas personalizadas.
- Reglas configurables.
- Exportación opcional de resultados generados por sesión.
- Historial temporal opcional únicamente en memoria.

> KeyMint seguirá priorizando la generación local.
> No se añadirá almacenamiento persistente de credenciales sin un diseño de seguridad específico.

---

## v1.5.0 — Portabilidad

**Estado:** Pendiente

### Escritorio

- Evaluar soporte oficial para Linux.
- Evaluar soporte oficial para macOS.
- Separar comportamiento específico por plataforma.
- Revisar empaquetado para cada sistema.

### Móvil

- Diseñar una implementación móvil nueva.
- No reutilizar automáticamente el antiguo port Android experimental.
- Definir arquitectura, interfaz y flujo adecuados para móvil.
- No declarar soporte hasta contar con compilaciones probadas y mantenidas.

---

## v2.0.0 — Evolución mayor

**Estado:** Visión

- Arquitectura modular.
- Separación clara entre motor de generación, interfaz y plataforma.
- Motor de políticas de generación.
- Presets avanzados.
- Pruebas automatizadas del motor.
- Posible sistema de actualización integrado.
- Evolución multiplataforma si el proyecto lo justifica.

---

## Principios del proyecto

- Generación local.
- No enviar contraseñas a servicios externos.
- No persistir credenciales por defecto.
- Utilizar APIs apropiadas para generación segura.
- Mantener clara la diferencia entre generador y gestor de contraseñas.
- No declarar soporte para plataformas no probadas.
- Mantener una identidad visual consistente dentro del ecosistema RobDev512.

---

## Regla de avance

El alcance de una versión puede cambiar si el desarrollo real lo requiere.

Una función no se considera estable hasta haber sido probada en código fuente y, cuando corresponda, también dentro del ejecutable y del instalador.
