import soundfile as sf
import sys
import re
import time
import torch
from NeuTTS.engine import TTSEngine

def execute_neutts(text, custom_ref_file):
    tts_engine = TTSEngine()

    codes_str, transcript = tts_engine.encode_audio(custom_ref_file)
    audio = tts_engine.batch_generate([text], [codes_str], [transcript])

    #audio = tts_engine.batch_generate(text, [codes_str], [transcript])

    output_file = f"neutts-{text[0:3]}-output.wav"
    sf.write(output_file, audio, 24000)
    print("done")

def main():
    text = sys.argv[1]
    custom_ref_file = sys.argv[2]
    execute_neutts(text, custom_ref_file)



if __name__ == "__main__":
    main()


