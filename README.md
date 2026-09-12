# 🌱 Bot de Sostenibilidad

Autor: Rodrigo Villanueva

Un bot interactivo de Discord desarrollado en Python que busca motivar a las personas a realizar acciones sostenibles y aprender más sobre el medio ambiente mediante retos, trivias y una calculadora de emisiones de CO₂.

## 🎯 Descripción del proyecto
El proyecto consiste en un bot de Discord relacionado con el cambio climático y el cuidado del medio ambiente.

Su objetivo es hacer que aprender y realizar acciones ecológicas sea más sencillo y divertido. El bot propone retos sostenibles, permite responder preguntas sobre el medio ambiente, calcula una estimación de las emisiones de CO₂ según el medio de transporte utilizado y entrega puntos a los usuarios.

## 🌎 Posibles usos
El bot puede utilizarse en:

Servidores educativos de Discord.
Comunidades interesadas en el medio ambiente.
Actividades escolares sobre cambio climático.
Grupos de estudiantes que quieran desarrollar hábitos sostenibles.
Comunidades que quieran aprender sobre la reducción de emisiones de CO₂.

## ⚙️Funciones y características
 # 🌱 !reto

Entrega al usuario un reto ecológico aleatorio.

Algunos ejemplos son:

Usar una botella reutilizable.
Utilizar una bolsa de tela.
Apagar luces y aparatos que no se estén utilizando.
Separar los residuos reciclables.
Aprovechar la luz natural.

  # 🎉 !cumplido

Permite al usuario indicar que completó su reto.
Al hacerlo, recibe:
+10 puntos
Los puntos se almacenan temporalmente para cada usuario mientras el bot está funcionando.

  # ❓ !trivia

Selecciona aleatoriamente una pregunta relacionada con el medio ambiente.
Por ejemplo, el usuario puede responder preguntas sobre:

Emisiones de CO₂.
Medios de transporte.
Acidificación de los océanos.
Cambio climático.

Para responder se utiliza:
!respuesta a
o
!respuesta b
o
!respuesta c

Si la respuesta es correcta, el usuario obtiene +10 puntos.

📊 !huella

Permite calcular una estimación de las emisiones de CO₂ producidas al recorrer una determinada cantidad de kilómetros.

Ejemplo:

!huella auto 10

El bot calcula las emisiones utilizando un factor diferente para cada medio de transporte:

Transporte	Emisión estimada por km
🚗 Auto	0.19 kg
🚌 Bus	0.05 kg
🚇 Metro	0.03 kg
🚲 Bicicleta	0 kg
🚶 Caminando	0 kg

El resultado es una estimación basada en los factores utilizados por el programa.

🏆 !mispuntos

Permite consultar la cantidad de puntos acumulados por el usuario.

Ejemplo:
!mispuntos
El bot responde mostrando los puntos actuales.

## 🛠️ Tecnologías utilizadas
El proyecto utiliza:
Python
discord.py
Discord
Random, biblioteca de Python utilizada para seleccionar retos y preguntas aleatoriamente.
## 📥 Instalación y uso

Para utilizar el proyecto se necesita:

·Tener Python instalado.
·Instalar la biblioteca discord.py.
·Crear y configurar un bot en el portal de desarrolladores de Discord.
·Añadir el bot a un servidor de Discord.
·Colocar el token del bot de forma segura.
·Ejecutar el programa.
 # Instalación de discord.py
  pip install discord.py

## 💬 Comentarios y mejoras
Los comentarios de los usuarios pueden ayudar a mejorar el proyecto.
Mis planes de mejora:
Nuevos retos ecológicos.
Nuevas preguntas para las trivias.
Nuevos medios de transporte.
Nuevas funciones para el sistema de puntos.
Mejoras en la interacción del bot.

En futuras versiones también se podrían agregar funciones como una tabla de clasificación, almacenamiento permanente de puntos y más estadísticas ambientales.

## 🚀 Futuras mejoras

Algunas funciones que podrían incorporarse posteriormente son:

🏆 Tabla de clasificación entre usuarios.
💾 Base de datos para guardar los puntos permanentemente.
🌎 Más información sobre cambio climático.
🌱 Más retos ecológicos.
❓ Más preguntas de trivia.
📈 Estadísticas sobre las emisiones de los usuarios.
🎖️ Insignias o recompensas por alcanzar determinadas cantidades de puntos.

## 🌍 Importancia del proyecto

Este proyecto busca demostrar que la tecnología puede utilizarse para promover hábitos sostenibles y aumentar la conciencia ambiental.

A través de un bot de Discord, los usuarios pueden aprender, participar en retos y conocer de manera sencilla el impacto estimado de algunos de sus medios de transporte.

## 🎤 Conclusión

El Bot de Sostenibilidad combina programación, educación ambiental y gamificación para crear una experiencia interactiva.

Su principal valor es convertir pequeñas acciones ecológicas en una actividad más participativa y entretenida.

¡Gracias por leer mi proyecto! 🌱🌎
