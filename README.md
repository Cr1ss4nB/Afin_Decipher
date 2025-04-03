# README - Descifrado Afín con Interfaz Gráfica

## 📌 Descripción del Proyecto

Este repositorio contiene una herramienta gráfica en Python para descifrar mensajes cifrados con el método Afín. El programa fue diseñado específicamente para resolver un mensaje capturado en una transmisión, que se presume fue cifrado usando este método.

## 🔍 Contexto del Problema
Mensaje cifrado interceptado:

`AEUAMXSIJIRIVBMRIVJMJIZBYUYDYUJIBYTVYUYBMAIZTIBMXIVUYZMWSIFMAEVMJYFMKEMJIZTVYJIUE`

Para esto se aplicó el método de desciframiento/ciframiento Afín.

## 🔐 Método Afín Explicado

**Definición:**  
El cifrado afín es un algoritmo de sustitución monoalfabética que combina:
1. **Cifrado multiplicativo** (decimación)
2. **Cifrado aditivo** (desplazamiento)

**Fórmulas:**  
- ▶️ **Cifrado:** `C = (a·P + b) mod 26`  
- ◀️ **Descifrado:** `P = a⁻¹·(C - b) mod 26`  

**Claves:**  
- `a`: Entero coprimo con 26 (mcd(a,26)=1)  
  *Valores válidos:* 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25  
- `b`: Desplazamiento (0 ≤ b ≤ 25)  

**Características:**  
✓ Vulnerable a ataques de frecuencia  
✓ Usa aritmética modular  
✓ Requiere calcular el **inverso modular** (a⁻¹) para descifrar  
✓ Solo 12 valores posibles para `a` (limitando claves a 12×26=312 combinaciones)  

## 🛠️ Solución Implementada
- **Claves encontradas:** a = 25, b = 12
- **Inverso modular:** a⁻¹ = 25

**Proceso:**
1. Calcula inverso modular: `pow(25, -1, 26) = 25`
2. Para cada letra: `P = (25 * (C - 12)) mod 26`

**Resultados:**
- Descifrado inicial: `MISMAPUEDEVERLAVERDADENLOSOJOSDELOTROSOLAMENTELAPERSONAQUEHAMIRADOHACIADENTRODESI`
- Reorganizado: `SOLAMENTELAPERSONAQUEHAMIRADOHACIADENTRODESIMISMAPUEDEVERLAVERDADENLOSOJOSDELOTRO`
- Texto legible y coherente `SOLAMENTE LA PERSONA QUE HA MIRADO HACIA DENTRO DE SI MISMA PUEDE VER LA VERDAD EN LOS OJOS DEL OTRO`

## 💻 Uso del Programa
Interfaz gráfica permite:
1. Ingresar claves a y b (Si no se selecciona un valor para a y b válidos no hará nada `ERROR!!`)
2. Ingresar mensaje cifrado (Por predeterminado está ingresado el mensaje cifrado)
3. Mostrar resultados y fórmulas

## 📝 Notas Adicionales
- Alfabeto inglés (26 letras)
- Función `reordenar_frase` contiene resultado esperado
- Inverso modular calculado con `pow(a, -1, 26)`

## 📚 Referencias

- Criptografía clásica: cifrados por sustitución
- Aritmética modular para criptografía
- Cifrado Afín y sus propiedades matemáticas

## ✨ Frase Final
> "Solamente la persona que ha mirado hacia dentro de sí misma puede ver la verdad en los ojos del otro"

## 📋 Cómo usar este repositorio

Simplemente clonar o descargar el repositorio y ejecutar el archivo afin4_1.py. Del resto probar y disfrutar :) 
