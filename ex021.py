# Exercício 021 - Tocando um MP3 (Curso em Vídeo)
# Música: "Creative Minds" de Bensound.com
# Licença: Free License with Attribution
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
import time
time.sleep(10)