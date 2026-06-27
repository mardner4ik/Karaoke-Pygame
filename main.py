from pygame import *
from sounddevice import *
import scipy.io.wavfile as wav

fs = 44100  # Sample rate
recording = None
is_recording = False
voice_file = "voice_record.wav"
minus_track = "MinusDuHast.mp3"

init()
mixer.init()
mixer.music.set_volume(0.5)

w_size = 1200, 600
screen = display.set_mode(w_size)

clock = time.Clock()

font.init()
font_big = font.SysFont("Arial", 32)

btn_rect = Rect(425, 250, 350, 80)
rect_color = "white"
btn_text = "Record"

def start_voice_record():
    global recording
    recording = rec(
        int(fs * 5),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )
def stop_voice_record():
    global recording

    stop()
    if recording is not None:
        wav.write(voice_file, fs, recording)
def play_song():
    mixer.music.load(minus_track)
    mixer.music.play()
    voice_sound = mixer.Sound(voice_file)
    voice_sound.play()

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            if btn_rect.collidepoint(e.pos):
                if not is_recording:
                    rect_color = "red"

                    btn_text = "Recording..."
                    is_recording = True
                    mixer.music.load(minus_track)
                    mixer.music.play()
                    start_voice_record()
                else:
                    rect_color = "white"
                    btn_text = "Record"
                    is_recording = False
                    stop_voice_record()
                    play_song()
        screen.fill("grey")
        draw.rect(screen, rect_color, btn_rect)
        text_surface = font_big.render(btn_text, True, "black")
        screen.blit(text_surface, (btn_rect.x + 20, btn_rect.y + 20))
        clock.tick(60)
        display.update()