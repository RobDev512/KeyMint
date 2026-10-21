# ROADMAP — PasswGen

## Estado actual

**Versión vigente:** v1.0.0  
**Estado general:** Estable / preparada para publicación  
**Plataforma principal:** Windows 64-bit  
**Port Android:** Experimental

> Este roadmap organiza la evolución prevista de PasswGen por versiones.
> El alcance puede cambiar conforme avance el desarrollo real.

> Nota histórica: PasswGen existía antes de contar con un repositorio oficial
> en GitHub. La versión v1.0.0 documenta la base estable actual y será la primera
> versión formalizada dentro del repositorio.

---

## v1.0.0 — Base estable

**Estado:** Aplicada

Primera versión formalizada del proyecto.

### Generación

- Generación local de contraseñas.
- Longitud configurable.
- Letras, números y símbolos dentro del conjunto de caracteres.
- Selección aleatoria basada en `secrets`.

### Interfaz

- Aplicación de escritorio basada en Tkinter.
- Mostrar y ocultar la contraseña.
- Copiar al portapapeles.
- Tema claro y oscuro.
- Detección del tema del sistema.
- Recursos visuales propios.

### Distribución

- Ejecutable generado con PyInstaller.
- Instalador generado con Inno Setup.
- Instalación en Windows de 64 bits.
- Versión interna `APP_VERSION = "1.0.0"`.

### Proyecto

- Código principal separado en `src/`.
- Archivos de empaquetado separados en `packaging/windows/`.
- Port Android experimental separado en `android/`.
- Dependencias declaradas en `requirements.txt`.
- Artefactos de compilación excluidos mediante `.gitignore`.

---

## v1.0.1 — Mantenimiento inicial

**Estado:** Siguiente

Primera actualización de mantenimiento después de la publicación de v1.0.0.

### Objetivos

- Corregir errores detectados tras la primera publicación.
- Revisar escalado y presentación en distintas configuraciones de Windows.
- Mejorar mensajes de error.
- Revisar comportamiento del portapapeles.
- Ajustar empaquetado e instalador si aparecen problemas en otros equipos.
- Completar capturas y documentación de uso.

---

## v1.1.0 — Control de generación

**Estado:** Pendiente

Ampliación del control que el usuario tiene sobre las contraseñas generadas.

### Categorías

- Activar o desactivar letras minúsculas.
- Activar o desactivar letras mayúsculas.
- Activar o desactivar números.
- Activar o desactivar símbolos.
- Evitar configuraciones sin caracteres disponibles.

### Complejidad

- Opción para garantizar al menos un carácter de cada categoría habilitada.
- Opción para excluir caracteres ambiguos.
- Indicador de longitud y complejidad.
- Estimación informativa de entropía.

### Generación múltiple

- Generar varias contraseñas de una sola vez.
- Copiar una contraseña individual.
- Copiar el conjunto completo.

---

## v1.2.0 — Experiencia de usuario

**Estado:** Pendiente

Mejoras enfocadas en comodidad y uso frecuente.

### Objetivos

- Presets de generación.
- Recordar preferencias no sensibles.
- Mejor respuesta visual al copiar.
- Opción para limpiar automáticamente el portapapeles después de un intervalo.
- Atajos de teclado.
- Mejoras de accesibilidad.
- Revisión de escalado DPI.
- Mejor navegación mediante teclado.

---

## v1.3.0 — Herramientas y productividad

**Estado:** Pendiente

Funciones adicionales sin convertir PasswGen en un gestor de contraseñas.

### Objetivos

- Generación de frases de contraseña.
- Plantillas personalizadas.
- Reglas configurables de longitud y categorías.
- Exportación opcional de resultados generados por sesión.
- Historial temporal opcional únicamente en memoria.
- Controles claros para evitar persistencia accidental de contraseñas.

> PasswGen seguirá priorizando la generación local. Un historial persistente o
> almacenamiento de credenciales no se añadirá sin un diseño de seguridad
> específico.

---

## v1.4.0 — Portabilidad

**Estado:** Pendiente

Revisión del alcance multiplataforma del proyecto.

### Escritorio

- Evaluar soporte oficial para Linux.
- Evaluar soporte oficial para macOS.
- Separar completamente la detección de tema por plataforma.
- Revisar empaquetado específico para cada sistema.

### Android

- Auditar `GCSAndroidPort.py`.
- Actualizar `buildozer.spec`.
- Decidir si el port experimental continúa como parte oficial del proyecto.
- Evitar declarar soporte Android mientras no exista una compilación probada y mantenida.

---

## v2.0.0 — Evolución mayor

**Estado:** Visión

Reservada para cambios importantes de arquitectura o experiencia.

### Posibles líneas

- Interfaz rediseñada.
- Arquitectura modular.
- Motor de políticas de generación.
- Presets reutilizables avanzados.
- Mejor separación entre lógica de generación, interfaz y plataforma.
- Pruebas automatizadas del motor de generación.
- Sistema de actualización integrado si el alcance del proyecto lo justifica.

---

## Principios del proyecto

- Generación local.
- No enviar contraseñas a servicios externos.
- Evitar persistencia de credenciales por defecto.
- Priorizar APIs adecuadas para generación segura.
- Mantener clara la diferencia entre generador de contraseñas y gestor de contraseñas.
- Documentar como experimental cualquier plataforma o función todavía no validada.

---

## Regla de avance

Una versión puede cambiar de alcance, dividirse, adelantarse o retrasarse si el desarrollo real lo requiere.

Una función no se considera parte de una versión estable hasta que haya sido probada dentro de la aplicación y, cuando corresponda, también dentro del ejecutable y del instalador.
