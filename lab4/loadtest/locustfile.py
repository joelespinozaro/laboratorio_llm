from locust import HttpUser, task, between
import random

PROMPTS = [
    "Explica qué es Kubernetes en 3 pasos",
    "¿Cuál es la diferencia entre Docker y una VM?",
    "Define autoscaling en cloud computing",
    "¿Qué es KEDA y cómo funciona?",
    "Explica el concepto de container orchestration",
    "¿Qué es un Helm chart y para qué sirve?",
    "Describe qué hace un ServiceMonitor en Kubernetes",
    "¿Qué es PagedAttention en vLLM?",
]

class VLLMUser(HttpUser):
    wait_time = between(0.3, 0.8)   # intervalo entre requests por usuario
    host = "http://localhost:8000"

    @task
    def chat_completion(self):
        self.client.post(
            "/v1/chat/completions",
            json={
                "model": "Qwen/Qwen2.5-0.5B-Instruct",
                "messages": [
                    {"role": "user", "content": random.choice(PROMPTS)}
                ],
                "max_tokens": 80
            },
            timeout=30,
            name="chat/completions"
        )