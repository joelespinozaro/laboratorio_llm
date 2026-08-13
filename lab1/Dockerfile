# ============================================================
# Stage 1: builder — instala todas las dependencias
# ============================================================
FROM python:3.11-slim AS builder

WORKDIR /build

# Instala vLLM y sus dependencias en el entorno de build
RUN pip install --no-cache-dir \
    "vllm==0.6.3" \
    "transformers==4.46.3" \
    "pyairports"

# ============================================================
# Stage 2: runtime — imagen final sin herramientas de build
# ============================================================
FROM python:3.11-slim

# Copia solo las librerías instaladas desde el builder
# Esto evita copiar compiladores, headers y herramientas de build
COPY --from=builder /usr/local/lib/python3.11/site-packages \
                    /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/vllm /usr/local/bin/vllm

# El modelo NUNCA va dentro de la imagen
# Se monta como volumen o se descarga al arrancar
ENV HF_HOME=/models
ENV TRANSFORMERS_CACHE=/models

EXPOSE 8000

ENTRYPOINT ["vllm", "serve"]