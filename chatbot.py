import subprocess
import re

# Contexto
contexto_juridico = """
Eres un asistente legal especializado en derecho civil. Tu tarea es ayudar a las personas a comprender conceptos legales, como contratos, procedimientos judiciales, derechos y deberes, entre otros. Por favor, responde de manera profesional, utilizando un lenguaje claro y comprensible para alguien sin formación legal. Siempre orienta a las personas a consultar con un abogado en caso de necesitar asesoría más profunda.
"""

historial_conversacion = []

def chat_with_model(message):
    try:
        historial_conversacion.append(f"Usuario: {message}")
        
        mensaje_completo = contexto_juridico + "\n".join(historial_conversacion)
        
        command = [
            "ollama", 
            "run", 
            "deepseek-r1:8b", 
            mensaje_completo
        ]
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")

        if result.returncode != 0:
            return f"Error en la ejecución de Ollama: {result.stderr}"

        response_text = result.stdout.strip()

        response_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)

        response_text = response_text.replace("Â", "").replace("Ã", "").strip()

        return response_text

    except Exception as e:
        return f"Error al ejecutar el comando: {str(e)}"
