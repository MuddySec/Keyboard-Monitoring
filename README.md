# Keyboard Monitoring: Proyecto académico de ciberseguridad ofensiva

Este proyecto fue desarrollado como parte de una práctica del máster en ciberseguridad. Su objetivo es **analizar y demostrar técnicas básicas de captura de entrada de teclado** (keyboard monitoring) en entornos controlados, con fines puramente educativos y de concienciación en seguridad ofensiva.

> ⚠️ **Este código no debe utilizarse fuera de un entorno de pruebas. Su uso sin consentimiento es ilegal y éticamente reprobable.**

## 📚 Objetivos del proyecto

- Comprender cómo funcionan las técnicas de captura de pulsaciones de teclado.
- Estudiar los mecanismos por los cuales se puede automatizar la recolección y el envío de datos.
- Reflexionar sobre los riesgos reales de estas herramientas y cómo pueden prevenirse.

## 🛠️ Funcionalidad

El script incluye:

- Captura de teclas mediante `pynput`.
- Registro de pulsaciones en un fichero local.
- Envío periódico del log por correo electrónico (solo en entorno de pruebas).
- Empaquetado en `.exe` para demostrar técnicas de ocultación y persistencia.
- Simulación de instalación mediante software de terceros (solo con fines demostrativos).

## 🔬 Entorno de pruebas

Este proyecto fue ejecutado exclusivamente en:

- Máquinas virtuales Windows (entorno cerrado).
- Equipos controlados sin ningún dato real ni usuario externo.
- Sin conectividad a sistemas de terceros salvo para pruebas controladas.

## 🧭 Consideraciones éticas y legales

El uso de software de monitorización de teclado **está regulado por la legislación vigente** y puede ser considerado delito si se emplea sin el consentimiento explícito del usuario.

Este repositorio:

- **No promueve** el uso ofensivo de estas técnicas.
- Existe con fines **formativos, de análisis y concienciación**.
- Busca ayudar a profesionales a entender las amenazas y desarrollar defensas efectivas.

## 🛡️ Contramedidas y defensa

Parte del aprendizaje consiste también en saber cómo **prevenir o detectar** este tipo de herramientas:

- Uso de antivirus con detección de comportamiento anómalo.
- Monitorización de procesos ocultos y ejecutables no firmados.
- Restricción de permisos y políticas de ejecución de software.
- Concienciación del usuario para evitar ingeniería social (e.g. instaladores falsos).

## 📁 Estructura del proyecto

📦 Keyboard-monitoring/
┣ 📜 Gato.py # Código principal del keylogger
┣ 📜 README.md # Este archivo
┗ 📄 pulsaciones_grabadas.txt (temporal, generado al ejecutar)

## 📄 Licencia

Este proyecto se ofrece únicamente con fines educativos. No se otorga licencia para su uso en sistemas de terceros ni con fines comerciales o maliciosos.

---

> “Conocer cómo se ataca es el primer paso para aprender a defenderse.”
