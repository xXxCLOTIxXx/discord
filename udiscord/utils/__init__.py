from .logger import Logger
from base64 import b64decode, b64encode
from typing import BinaryIO
from wave import open as wopen
import struct
import base64

log = Logger()


def get_userId_from_token(token: str) -> int:
    bot_id_encoded = token.split(".")[0]
    missing_padding = len(bot_id_encoded) % 4
    if missing_padding:
        bot_id_encoded += "=" * (4 - missing_padding)
    return int(b64decode(bot_id_encoded).decode("utf-8"))

def get_wav_audio_metadata(file: BinaryIO):
    file.seek(0)
    
    with wopen(file, 'rb') as audio:
        duration_secs = audio.getnframes() / audio.getframerate()
        
        frames = audio.readframes(audio.getnframes())
        sampled_frames = frames[:60]
        
        waveform = b64encode(sampled_frames).decode('utf-8')
    
    return duration_secs, waveform


def get_ogg_audio_metadata(file: BinaryIO):
    #TODO
    file.seek(0)

    duration_secs = 0
    waveform = bytearray()
    
    waveform_b64 = base64.b64encode(waveform[:60]).decode('utf-8')

    return duration_secs, waveform_b64
