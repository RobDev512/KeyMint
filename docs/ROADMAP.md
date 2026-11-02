# ROADMAP — KeyMint

## Estado actual

**Versión actual:** v1.1.0
**Última versión pública:** KeyMint v1.1.0
**Estado general:** Publicada
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

**Estado:** Publicada

Primera versión bajo la nueva identidad **KeyMint**.

Esta versión prioriza identidad, estructura, empaquetado y renovación visual. El alcance funcional se mantiene controlado para no mezclar todavía el futuro gestor de credenciales con la base actual del generador.

### Identidad

- [x] Renombrar PasswGen a KeyMint.
- [x] Crear identidad visual propia.
- [x] Crear conjunto oficial de recursos de branding.
- [x] Documentar la identidad en `docs/BRANDING.md`.
- [x] Renombrar el repositorio remoto a `KeyMint`.
- [x] Crear la página propia de KeyMint dentro del Hub de RobDev512.

### Estructura

- [x] Mover `KeyMint.py` a la raíz.
- [x] Eliminar la antigua estructura `src/`.
- [x] Crear `assets/branding/`.
- [x] Crear `assets/icons/`.
- [x] Separar iconos de tema, interfaz y visibilidad.
- [x] Mover CHANGELOG y ROADMAP a `docs/`.
- [x] Retirar el port Android experimental obsoleto.
- [x] Crear `.venv` local de desarrollo.
- [x] Incorporar `customtkinter` para la nueva interfaz.

### Empaquetado

- [x] Renombrar configuración de PyInstaller a `KeyMint.spec`.
- [x] Renombrar configuración de Inno Setup a `KeyMint.iss`.
- [x] Generar `KeyMint.exe`.
- [x] Generar y probar `KeyMint_Setup_v1.1.0.exe`.
- [x] Crear una identidad propia del instalador mediante `AppId=KeyMint_RobDev512`.
- [x] Instalar KeyMint en `C:\Program Files\KeyMint`.
- [x] Mantener PasswGen v1.0.0 como release histórica independiente.
- [x] Reconstruir ejecutable e instalador con la versión final de v1.1.0.
- [x] Realizar prueba final de instalación/desinstalación antes de publicar.

### Renovación de interfaz

- [x] Eliminar la barra de título estándar y crear una barra propia.
- [x] Añadir controles propios de tema, minimizar y cerrar.
- [x] Mantener la ventana fija, sin redimensionamiento ni maximización.
- [x] Centrar la aplicación al iniciar.
- [x] Fijar un ancho de referencia de escritorio de **455 px**.
- [x] Redondear la ventana mediante DWM nativo de Windows.
- [x] Aplicar borde exterior mediante DWM nativo.
- [x] Redondear visualmente botones, campos, paneles y otros componentes.
- [x] Mejorar jerarquía visual, espaciado y distribución.
- [x] Unificar estados hover, focus, active y disabled.
- [x] Revisar tema claro y oscuro.
- [x] Revisar escalado DPI.
- [x] Mejorar navegación mediante teclado.
- [x] Añadir control del slider mediante flechas.
- [x] Añadir botón Limpiar.
- [x] Permitir selección y copia del resultado sin permitir su edición.
- [x] Añadir desplazamiento horizontal para contraseñas que no caben en el campo.
- [x] Añadir barra horizontal compacta y centrada únicamente cuando existe desbordamiento.
- [x] Mantener compatibilidad con desplazamiento horizontal mediante touchpad/rueda cuando Windows lo expone.

> Mientras KeyMint conserve una ventana fija, maximizar/restaurar no forma parte del diseño de escritorio.

### Sistema de iconos

- [x] Crear iconos de interfaz con lenguaje visual consistente.
- [x] Separar recursos en carpetas propias de KeyMint.
- [x] Añadir variantes de iconos para tema claro y oscuro.
- [x] Corregir la semántica de mostrar/ocultar contraseña: ojo cerrado cuando está oculta y ojo abierto cuando está visible.
- [ ] Utilizar SVG como fuente maestra para iconos simples cuando sea apropiado.
- [x] Mantener PNG/ICO derivados cuando la plataforma o Tkinter lo requiera.
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
- Añadir **microanimaciones y transiciones** a la interfaz.
- Animar cambios de estado, apertura/cierre de paneles y retroalimentación visual cuando sea útil.
- Mantener las animaciones breves y opcionales para no perjudicar accesibilidad ni rendimiento.

> En escritorio las animaciones no dependen de CSS; deberán implementarse con el toolkit de interfaz correspondiente.

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
- Adaptar la interfaz de KeyMint a tamaños y controles táctiles móviles.

---

## v2.0.0 — Evolución mayor / Vault de KeyMint

**Estado:** Visión

La evolución de KeyMint de generador de contraseñas a **gestor local de credenciales** requiere una arquitectura y un modelo de seguridad propios. No se implementará como una simple ampliación del formulario actual.

### Arquitectura

- Arquitectura modular.
- Separación clara entre motor de generación, interfaz, almacenamiento y plataforma.
- Motor de políticas de generación.
- Presets avanzados.
- Pruebas automatizadas del motor.
- Posible sistema de actualización integrado.
- Evolución multiplataforma si el proyecto lo justifica.

### Vault de credenciales

- Crear un almacén local cifrado para cuentas y contraseñas.
- Guardar nombre del servicio, usuario/correo, contraseña, URL y notas.
- Buscar, consultar y editar credenciales.
- Permitir cambiar una contraseña almacenada de manera controlada.
- Añadir categorías, etiquetas o carpetas.
- Mantener secretos cifrados en reposo.
- Diseñar autenticación mediante contraseña maestra o mecanismo equivalente.
- Bloqueo automático después de inactividad.
- No almacenar la contraseña maestra en texto plano.
- Evitar que credenciales sensibles permanezcan innecesariamente en memoria o portapapeles.

### Notas seguras y códigos de recuperación

- Crear notas cifradas dentro del vault.
- Permitir almacenar códigos de recuperación separados de las contraseñas.
- Permitir copiar códigos individuales.
- Marcar códigos como utilizados cuando corresponda.
- Diseñar una posible importación asistida desde notas existentes del usuario.
- Evitar importaciones automáticas desde aplicaciones de terceros sin revisión explícita.

### Copias y portabilidad de datos

- Exportación cifrada del vault.
- Importación segura de copias de KeyMint.
- Estrategia de respaldo y restauración.
- Definir formato versionado para evitar incompatibilidades futuras.

### QR

- Evaluar generación y lectura de códigos QR dentro de KeyMint.
- Definir casos de uso concretos antes de permitir codificar secretos.
- Posible uso para transferencia controlada entre dispositivos.
- Posible uso para configuración/importación de datos compatibles.
- Mostrar advertencias y confirmación antes de incluir credenciales sensibles en un QR.
- No generar códigos QR de contraseñas o secretos automáticamente.

### Seguridad antes de implementar el vault

- Elegir una biblioteca criptográfica mantenida y ampliamente auditada.
- Utilizar derivación de clave resistente para la contraseña maestra.
- Utilizar cifrado autenticado.
- Diseñar manejo de nonce/salt y versionado del formato.
- Definir política de bloqueo y borrado de memoria cuando sea viable.
- Crear pruebas específicas para cifrado, apertura, corrupción y migraciones.
- Revisar el modelo de amenazas antes de considerar estable esta función.

---

## Ideas posteriores al vault

**Estado:** Exploración

Estas ideas no sustituyen las etapas anteriores y pueden cambiar después de validar el vault.

- Sincronización opcional entre dispositivos, únicamente con diseño de cifrado de extremo a extremo.
- Integración futura con autenticadores/TOTP si el alcance de KeyMint lo justifica.
- Detección local de credenciales duplicadas o reutilizadas.
- Auditoría local de salud del vault.
- Acceso rápido a códigos de recuperación.
- Integración opcional con biometría cuando la plataforma lo permita de forma segura.

---

## Principios del proyecto

- Generación local.
- No enviar contraseñas a servicios externos.
- No persistir credenciales por defecto mientras KeyMint sea únicamente generador.
- Si se incorpora un vault, persistir secretos únicamente mediante almacenamiento cifrado diseñado específicamente para ello.
- Utilizar APIs apropiadas para generación segura.
- Mantener clara la diferencia entre generador y gestor de contraseñas hasta que el vault exista realmente.
- No declarar soporte para plataformas no probadas.
- Mantener una identidad visual consistente dentro del ecosistema RobDev512.
- No sacrificar seguridad por comodidad de interfaz.
- Tratar QR, sincronización, importación y exportación como superficies de seguridad, no solo como funciones de UX.

---

## Regla de avance

El alcance de una versión puede cambiar si el desarrollo real lo requiere.

Una función no se considera estable hasta haber sido probada en código fuente y, cuando corresponda, también dentro del ejecutable y del instalador.
