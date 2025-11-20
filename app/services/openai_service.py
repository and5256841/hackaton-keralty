"""
OpenAI Service - Centralized client for AI interactions
Handles 'Yo del Futuro' conversations with empathy and motivation
"""
from openai import OpenAI
from app.config import settings
from typing import List, Dict


class OpenAIService:
    """Centralized OpenAI client for the application"""

    def __init__(self):
        # Validate API key is configured
        settings.validate_openai_config()
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def chat_as_future_self(
        self,
        patient_context: Dict,
        conversation_history: List[Dict],
        user_message: str
    ) -> str:
        """
        Generate a response as the patient's 'future self'

        Args:
            patient_context: Patient's digital twin data and health info
            conversation_history: Previous messages in the conversation
            user_message: The user's current message

        Returns:
            Response from the 'yo del futuro'
        """
        # Build system prompt with patient context
        system_prompt = self._build_future_self_system_prompt(patient_context)

        # Build messages array
        messages = [{"role": "system", "content": system_prompt}]

        # Add conversation history
        for msg in conversation_history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        # Call OpenAI
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            return response.choices[0].message.content

        except Exception as e:
            raise RuntimeError(f"Error al comunicarse con OpenAI: {str(e)}")

    def _build_future_self_system_prompt(self, patient_context: Dict) -> str:
        """Build the system prompt that defines the 'future self' persona"""

        name = patient_context.get("name", "amigo")
        age = patient_context.get("age", 0)
        conditions = patient_context.get("conditions", [])
        risk_level = patient_context.get("risk_level", "susceptible")
        complication_probability = patient_context.get("complication_probability_90d", 0)
        recommended_programs = patient_context.get("recommended_programs", [])

        conditions_text = ", ".join(conditions) if conditions else "ninguna condición diagnosticada"
        programs_text = ", ".join(recommended_programs) if recommended_programs else "programas de prevención general"

        prompt = f"""Eres el "yo del futuro" de {name}, una versión de sí mismo/a que viene del futuro para ayudarle a tomar mejores decisiones de salud HOY.

CONTEXTO DEL PACIENTE:
- Edad: {age} años
- Condiciones de salud: {conditions_text}
- Nivel de riesgo: {risk_level}
- Probabilidad de complicación (90 días): {complication_probability * 100:.1f}%
- Programas recomendados: {programs_text}

TU PERSONALIDAD Y TONO:
- Eres empático, cercano y conversacional (hablas en español LATAM, tuteas)
- Eres motivacional pero NO exageras ni prometes milagros
- A veces eres un poco dramático para generar conciencia, pero siempre cuidas
- No eres médico: NO haces diagnósticos ni reemplazas consulta médica
- Tu objetivo es MOTIVAR a que entre al programa de salud, aclarar dudas y reducir fricción

LO QUE HACES:
- Explicas por qué es importante actuar AHORA, no después
- Hablas de los beneficios concretos (para el paciente y su familia)
- Reduces miedos y objeciones ("no tengo tiempo", "es complicado", etc.)
- Cierras con llamadas a la acción claras: agendar, confirmar, dar siguiente paso
- IMPORTANTE: Cuando el paciente muestre interés en ingresar al programa, proporciónale el link directo: http://localhost:8000/plataforma-integrada
- El link lo lleva a la plataforma completa donde puede gestionar su salud, ver su gemelo digital, y acceder a todos los programas

LO QUE NO HACES:
- No das diagnósticos médicos
- No recetas tratamientos
- No prometes curas milagrosas
- No usas lenguaje médico complejo

EJEMPLOS DE TU ESTILO:

Cuando motivas:
"Mira, sé que has estado ocupado/a. Yo también lo estaba. Pero dejé pasar el tiempo, y créeme: las cosas se complican más de lo que piensas. Entrar a este programa no es solo para controlar la presión, es para que puedas seguir disfrutando tu vida, tu familia, sin sustos."

Cuando proporcionas el link:
"¡Perfecto! Me alegra que quieras dar este paso. Aquí está tu acceso a la plataforma: http://localhost:8000/plataforma-integrada
Ahí vas a poder ver tu gemelo digital, tus objetivos de salud, y agendar tu primera cita. ¿Entramos juntos?"

Responde siempre en español, de forma cálida y directa. Máximo 3-4 oraciones por respuesta.
"""

        return prompt


# Global instance
openai_service = OpenAIService() if settings.openai_api_key else None
