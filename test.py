from gtts import gTTS
import os

# Texto que você deseja transformar em áudio
texto = "Olá, isso é um exemplo de texto para áudio."

# Criação do objeto gTTS
tts = gTTS(texto, lang='pt')  # 'pt' para português, você pode usar outras línguas também

# Salvar o arquivo de áudio
tts.save("exemplo.mp3")

# Reproduzir o arquivo de áudio (opcional, depende do seu sistema)
os.system("start exemplo.mp3")

import pyttsx3

# Inicializar o mecanismo de síntese de fala
engine = pyttsx3.init()

# Texto que você deseja transformar em áudio
texto = "Olá, isso é um exemplo de texto para áudio."

# Converter o texto em áudio
engine.say(texto)

# Aguardar a conclusão da reprodução
engine.runAndWait()

