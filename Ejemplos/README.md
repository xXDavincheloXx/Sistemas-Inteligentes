
# Pruebas: Uso del Lenguaje LLM con Ollama

Esta documentación describe paso a paso cómo instalar y utilizar Ollama para ejecutar modelos de inteligencia artificial, además de la integración con GroqCloud para hacer consultas a través de su API.

## 1. Instalación

El primer paso es descargar [Ollama](https://ollama.com/download/linux) desde su página web. Una vez descargado, ejecutamos el siguiente comando en la terminal para instalarlo:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Este comando descarga y ejecuta el script de instalación directamente desde la URL proporcionada, utilizando `curl`.

---

## 2. Iniciar el servidor

Una vez instalado, puedes iniciar el servidor de Ollama con el siguiente comando:

```bash
ollama serve
```

Esto pondrá en marcha el servidor que permitirá interactuar con los modelos de inteligencia artificial.

---

## 3. Importar y gestionar modelos de IA

Para importar un modelo de inteligencia artificial, primero debemos buscar el modelo deseado en la [biblioteca de Ollama](https://ollama.com/library). 

Después, abrimos una nueva ventana de la terminal y ejecutamos el siguiente comando para descargar el modelo:

```bash
ollama pull tinyllama
```

### Listar modelos importados

Para listar todos los modelos que has importado y descargado, ejecuta el siguiente comando:

```bash
ollama list
```

Esto te mostrará una lista de los modelos disponibles en tu sistema.

### Hacer preguntas al modelo

Para hacer una pregunta al modelo que has descargado, utiliza el siguiente comando, reemplazando el texto entre paréntesis con la pregunta que deseas hacer:

```bash
ollama run tinyllama "(se coloca la pregunta aquí)"
```

Por ejemplo, si deseas preguntar "¿Por qué el cielo es azul?", usarías:

```bash
ollama run tinyllama "¿Por qué el cielo es azul?"
```

---

## 4. Consultas avanzadas usando CURL

Si prefieres interactuar con el modelo utilizando CURL, puedes hacerlo a través de la API de Ollama con el siguiente comando:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
```

### Guardar la respuesta en un archivo

Si quieres guardar la respuesta en un archivo, puedes utilizar el siguiente comando:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}' -o salida.md
```

Este comando guarda la respuesta en un archivo llamado `salida.md`.

### Respuesta completa sin flujo de datos

Si prefieres recibir la respuesta completa en lugar de un flujo de datos, puedes agregar `"stream": false` al comando:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

---

## 5. Uso de GroqCloud

Para usar GroqCloud, primero debes registrarte y crear una cuenta en [GroqCloud](https://console.groq.com/docs/quickstart). Una vez que hayas creado la cuenta, debes generar una clave API para poder interactuar con sus servicios.

### Exportar clave API

Una vez que tengas la clave API, expórtala como una variable de entorno utilizando el siguiente comando:

```bash
export GROQ_API_KEY=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
```

### Verificar la clave API

Para verificar que la clave ha sido exportada correctamente, puedes utilizar el siguiente comando:

```bash
echo $GROQ_API_KEY
```

Si el comando devuelve tu clave API, significa que ha sido cargada correctamente.

### Hacer consultas a la API de GroqCloud

Ahora que tienes la clave API lista, puedes hacer consultas a la API de GroqCloud utilizando el siguiente comando CURL:

```bash
curl "https://api.groq.com/openai/v1/chat/completions"   -X POST   -H "Content-Type: application/json"   -H "Authorization: Bearer ${GROQ_API_KEY}"   -d '{
         "messages": [
           {
             "role": "user",
             "content": "¿Por qué el cielo es azul?"
           }
         ],
         "model": "llama3-8b-8192",
         "stream": false
       }'
```

Este comando envía una solicitud POST a la API de GroqCloud con la pregunta "¿Por qué el cielo es azul?" y devuelve la respuesta generada por el modelo de inteligencia artificial.

---

## 6. Recursos adicionales

Para más información sobre Ollama y GroqCloud, puedes consultar la documentación oficial:

- [Documentación de Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Documentación de GroqCloud](https://console.groq.com/docs/quickstart)

---

¡Y eso es todo! Siguiendo estos pasos, podrás instalar, configurar y utilizar Ollama, así como integrar GroqCloud para realizar consultas avanzadas a través de sus APIs.
