# Lyra Server

Servidor Flask que simula un cerebro artificial con 27 emociones y personalidad emergente.
Desplegado en Railway.

## Uso
Enviar un POST a `/chat` con un JSON:

```bash
curl -X POST https://tu-url-de-railway/chat \
-H "Content-Type: application/json" \
-d '{"message":"Hola Lyra"}'
