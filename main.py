from flask import Flask, render_template, request, send_file, url_for
from gtts import gTTS
import io
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Obter o texto do formulário
    texto = request.form.get('text')

    # Criação do objeto gTTS
    tts = gTTS(texto, lang='pt')  # 'pt' para português, você pode usar outras línguas também

    # Salvar o áudio em um arquivo temporário
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)
    temp_file.close()

    # Ler o arquivo temporário em um buffer de memória
    audio_buffer = io.BytesIO()
    with open(temp_file.name, 'rb') as f:
        audio_buffer.write(f.read())
    os.unlink(temp_file.name)  # Excluir o arquivo temporário

    audio_buffer.seek(0)

    return send_file(audio_buffer, as_attachment=True, download_name='audio.mp3', mimetype='audio/mpeg')




if __name__ == '__main__':
    app.run(debug=True)
