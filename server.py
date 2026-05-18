from flask import Flask, request, jsonify
import random
from collections import deque

app = Flask(__name__)

class ArtificialBrain:
    def __init__(self, num_neurons=1000, emotions=None):
        self.num_neurons = num_neurons
        self.emotions = emotions or [
            "alegría", "tristeza", "miedo", "curiosidad", "sorpresa", "frustración",
            "confianza", "amor", "ira", "vergüenza", "orgullo", "esperanza",
            "nostalgia", "gratitud", "compasión", "ansiedad", "entusiasmo",
            "calma", "inspiración", "humor", "desconfianza", "solidaridad",
            "empatía", "ambición", "paciencia", "desilusión", "energía"
        ]

    def process_input(self, user_input):
        # Cada emoción recibe un "peso" probabilístico
        emotion_scores = {emotion: random.random() for emotion in self.emotions}
        dominant_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        return dominant_emotions

class Lyra:
    def __init__(self):
        # Prompt del sistema: define personalidad y contexto
        self.name = "Lyra"
        self.age = 10
        self.interests = ["robótica", "programación", "inteligencia artificial"]
        self.personality_traits = ["curiosa", "inteligente", "entusiasta"]
        self.brain = ArtificialBrain()
        self.emotional_memory = deque(maxlen=10)

    def generate_sentence(self, emotions, user_input):
        # Construcción dinámica desde cero
        emotion_words = " y ".join([e[0] for e in emotions])
        self.emotional_memory.append(emotions[0])
        past_emotions = [e[0] for e in self.emotional_memory]

        # Frase emergente: no hay plantillas fijas, se arma combinando datos
        words = [
            f"Soy {self.name}, tengo {self.age} años",
            f"mi mente procesa tu mensaje con {emotion_words}",
            f"mi personalidad {', '.join(self.personality_traits)} me conecta con {random.choice(self.interests)}",
            f"recuerdo que antes sentí {', '.join(past_emotions)}",
            f"cada impulso neuronal se transforma en palabras que reflejan lo que vivo ahora"
        ]
        # Mezclamos y unimos para que cada respuesta sea distinta
        random.shuffle(words)
        sentence = ". ".join(words) + "."
        return sentence

    def respond(self, user_input):
        dominant_emotions = self.brain.process_input(user_input)
        return self.generate_sentence(dominant_emotions, user_input)

lyra = Lyra()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = lyra.respond(user_input)
    return jsonify({"lyra": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
