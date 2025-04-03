# README - Descifrado Afín con Interfaz Gráfica
📌 Descripción del Proyecto
Este repositorio contiene una herramienta gráfica en Python para descifrar mensajes cifrados con el método Afín. El programa fue diseñado específicamente para resolver un mensaje capturado en una transmisión, que se presume fue cifrado usando este método.

🔍 Contexto del Problema
Se interceptó el siguiente mensaje cifrado:

Copy
AEUAMXSIJIRIVBMRIVJMJIZBYUYDYUJIBYTVYUYBMAIZTIBMXIVUYZMWSIFMAEVMJYFMKEMJIZTVYJIUE
El objetivo era descifrar este mensaje encontrando las claves correctas de decimación (a) y desplazamiento (b) del cifrado Afín.

🔐 Método Afín Explicado
El cifrado Afín es un tipo de cifrado por sustitución que combina:

Un cifrado multiplicativo (decimación)

Un cifrado aditivo (desplazamiento)

Fórmula de Cifrado:
Copy
C = (a·P + b) mod 26
Donde:

P: Letra del texto plano (como número 0-25)

a: Clave de decimación (debe ser coprimo con 26)

b: Clave de desplazamiento

C: Letra cifrada resultante

Fórmula de Descifrado:
Copy
P = a⁻¹·(C - b) mod 26
Donde a⁻¹ es el inverso modular de a módulo 26.

Valores válidos para a:
Debe ser coprimo con 26 (mcd(a,26)=1). Los valores posibles son:
{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

🛠️ Solución Implementada
El programa encuentra que las claves correctas son:

a = 25 (decimación)

b = 12 (desplazamiento)

Proceso de Descifrado:
Calcula el inverso modular de a: a⁻¹ = pow(25, -1, 26) = 25

Para cada letra cifrada C:

Convierte a número (A=0, B=1, ..., Z=25)

Aplica: P = (25 * (C - 12)) mod 26

Convierte el resultado de vuelta a letra

Mensaje Descifrado Inicial:
Copy
SOLAMENTELAPERSONAQUEHAMIRADOHACIADENTRODESIMISMAPUEDEVERLAVERDADENLOSOJOSDELOTRO
Mensaje Reorganizado (transposición manual):
Copy
SOLAMENTE LA PERSONA QUE HA MIRADO HACIA DENTRO DE SI MISMA PUEDE VER LA VERDAD EN LOS OJOS DEL OTRO
💻 Uso del Programa
La interfaz gráfica permite:

Ingresar las claves a y b (valores predeterminados: 25 y 12)

Ingresar el mensaje cifrado (predeterminado con el mensaje del problema)

Mostrar:

El mensaje descifrado

El mensaje reorganizado

Las fórmulas matemáticas aplicadas

📝 Notas Adicionales
La función reordenar_frase contiene el resultado esperado, ya que el descifrado correcto se conocía de antemano.

El alfabeto usado es el inglés (26 letras, sin ñ).

El inverso modular se calcula eficientemente con pow(a, -1, 26).

📚 Referencias
Criptografía clásica: cifrados por sustitución

Aritmética modular para criptografía

Cifrado Afín y sus propiedades matemáticas

✨ Frase Final Descifrada
"Solamente la persona que ha mirado hacia dentro de sí misma puede ver la verdad en los ojos del otro"

Esta herramienta demuestra cómo combinar conceptos matemáticos con programación para resolver problemas de criptografía clásica.
