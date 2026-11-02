# ROADMAP — KeyMint

## Estado actual

**Versión actual:** v1.1.0
**Última versión pública estable:** KeyMint v1.1.0
**Estado general:** Publicada y cerrada para Windows
**Plataforma principal:** Windows 64-bit
**Android:** Preview Kivy funcional validada; port oficial nativo planificado para una etapa futura

> KeyMint es la continuación directa de PasswGen.
> La versión v1.0.0 permanece como referencia histórica de la identidad anterior.
> La Android Preview de v1.1.0 se conserva como prueba técnica y referencia funcional. No se planea convertir directamente esa implementación Kivy en el port Android oficial.

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

**Estado:** Publicada y cerrada para Windows; Android incluida como Preview experimental

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
- [x] Retirar el port Android experimental obsoleto heredado de la etapa anterior.
- [x] Crear `.venv` local de desarrollo.
- [x] Incorporar `customtkinter` para la nueva interfaz de escritorio.

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

### Android Preview complementaria

Esta línea se desarrolló después de publicar inicialmente la distribución estable de Windows. El APK se conserva como Preview experimental dentro de la release v1.1.0 y como referencia para el futuro diseño móvil.

- [x] Crear una implementación móvil nueva basada en Kivy.
- [x] Adaptar la interfaz principal a controles táctiles.
- [x] Reutilizar el branding oficial mediante preparación automática de assets.
- [x] Añadir configuración reproducible con Buildozer/python-for-android.
- [x] Añadir workflow de GitHub Actions para generar el APK de Preview.
- [x] Resolver la incompatibilidad de min API 23 con Python 3.14 elevando `android.minapi` a 24.
- [x] Obtener una compilación CI correcta para `arm64-v8a`.
- [x] Probar manualmente la Preview en un dispositivo Android físico.
- [x] Validar instalación, apertura y flujo principal de generación.
- [x] Publicar el APK como asset complementario de la release v1.1.0.
- [x] Cerrar la implementación Kivy como Preview técnica, sin promoverla a port Android oficial.

> El futuro port Android oficial será una implementación nativa nueva. No se plantea migrar progresivamente el código Kivy hasta convertirlo en la aplicación Android estable.

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

## v1.5.0 — Portabilidad y preparación multiplataforma

**Estado:** Pendiente

### Escritorio

- Evaluar soporte oficial para Linux.
- Evaluar soporte oficial para macOS.
- Separar comportamiento específico por plataforma.
- Revisar empaquetado para cada sistema.

### Preparación móvil

La Preview Kivy de v1.1.0 sirve únicamente como referencia funcional. En esta etapa se preparará el proyecto para que un futuro cliente Android nativo pueda reproducir el comportamiento de KeyMint sin duplicar reglas ambiguas ni depender de la interfaz de Windows.

- Documentar de forma explícita las reglas del generador y sus casos límite.
- Separar conceptualmente lógica de generación, interfaz, almacenamiento y comportamiento específico de plataforma.
- Definir contratos funcionales y casos de prueba reutilizables entre implementaciones.
- Definir qué preferencias pueden compartirse entre plataformas y cuáles deben ser específicas del sistema.
- Documentar el comportamiento esperado de portapapeles, bloqueo, temas, accesibilidad y ciclo de vida en móvil.
- No iniciar todavía una migración del código Kivy a producción.
- Revisar el momento adecuado para comenzar el port Android oficial según la estabilidad de la arquitectura de v2.0.

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
- Definir comportamiento y contratos suficientemente claros para permitir clientes nativos en otras plataformas.
- Evitar acoplar el formato del vault a una interfaz o toolkit específico.
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

## Objetivo futuro — Port Android oficial nativo

**Estado:** Planificado para la etapa v2.x; versión exacta por definir

El port Android oficial se iniciará cuando las reglas del generador y la arquitectura de datos/seguridad de KeyMint sean suficientemente estables. Puede comenzar durante la estabilización final de v2.0 o después de ella; no se fija todavía un número de versión para evitar duplicar trabajo mientras cambian los fundamentos del proyecto.

### Tecnología prevista

- Crear un proyecto Android nuevo mediante **Android Studio**.
- Utilizar **Kotlin** como lenguaje principal.
- Utilizar **Jetpack Compose** para la interfaz nativa.
- Tratar la aplicación Android como cliente nativo de KeyMint, no como empaquetado de la aplicación Python de Windows.
- No reutilizar Kivy como base de producción; conservar la Preview v1.1.0 únicamente como referencia funcional y visual.

### Arquitectura y paridad funcional

- Reimplementar de forma nativa las reglas del generador definidas por KeyMint.
- Mantener paridad funcional documentada con las capacidades estables del proyecto cuando sea razonable.
- Diseñar navegación, ciclo de vida, estados de interfaz y accesibilidad específicamente para Android.
- Evitar copiar literalmente la disposición de escritorio cuando una interacción móvil requiera otra solución.
- Compartir especificaciones, formatos y casos de prueba cuando sea posible, aunque Windows y Android utilicen tecnologías distintas.

### Seguridad móvil

- Diseñar el almacenamiento Android específicamente para el modelo de seguridad del Vault.
- Evaluar Android Keystore para protección de material criptográfico cuando corresponda.
- Integrar biometría únicamente como mecanismo complementario y bajo un diseño de seguridad explícito.
- Definir política de bloqueo al pasar a segundo plano o después de inactividad.
- Minimizar permanencia de secretos en portapapeles y memoria.
- Evaluar protección frente a capturas o vistas recientes en pantallas sensibles cuando el modelo de amenazas lo justifique.

### Distribución y calidad

- Crear una compilación `release` firmada con una clave de producción persistente y protegida.
- Definir versionado Android coherente con las releases de KeyMint.
- Crear CI para compilaciones y pruebas del proyecto Android nativo.
- Validar múltiples versiones de Android, resoluciones y clases de dispositivo.
- Probar accesibilidad, rotación/cambios de configuración y comportamiento en segundo plano.
- Evaluar AAB y distribución mediante Google Play si se decide publicar en tienda.
- Mantener APK u otro canal de distribución directa solo si existe una estrategia clara de firma y actualización.
- No declarar Android como plataforma estable hasta completar pruebas, firma y criterios de soporte definidos.

### Criterio de inicio

El port oficial no debe comenzar solo porque la Preview Kivy funcione. Debe comenzar cuando implementar una función en Android ya no obligue a perseguir continuamente cambios estructurales del proyecto principal.

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
- El port Android oficial será nativo y se diseñará para Android; la Preview Kivy no se tratará como base de producción.
- Mantener una identidad visual consistente dentro del ecosistema RobDev512.
- No sacrificar seguridad por comodidad de interfaz.
- Tratar QR, sincronización, importación, exportación y clientes móviles como superficies de seguridad, no solo como funciones de UX.

---

## Regla de avance

El alcance de una versión puede cambiar si el desarrollo real lo requiere.

Una función no se considera estable hasta haber sido probada en código fuente y, cuando corresponda, también dentro del ejecutable, instalador o paquete correspondiente.
