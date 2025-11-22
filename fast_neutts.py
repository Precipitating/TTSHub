import soundfile as sf
import sys
import os
os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = "c:\Program Files\eSpeak NG\libespeak-ng.dll"
os.environ['PHONEMIZER_ESPEAK_PATH'] = "c:\Program Files\eSpeak NG"
from NeuTTS.engine import TTSEngine

def execute_neutts(text, custom_ref_file):
    tts_engine = TTSEngine()

    audio_file = custom_ref_file

    codes_str, transcript = tts_engine.encode_audio(
        audio_file)  ## good idea to cache speaker codes and transcripts so no need to encode again
    audio = tts_engine.batch_generate([text], [codes_str], [transcript])
    output_file = os.path.join("output",f"neutts-{text[0:3]}-output.wav")
    sf.write(output_file, audio, 24000)
    print("done")

def main():
    text = sys.argv[1]
    custom_ref_file = sys.argv[2]
    execute_neutts(text, custom_ref_file)



if __name__ == "__main__":
    main()


