from Maya1.tts_engine import TTSEngine
import soundfile as sf
import sys

def execute_maya(text, prompt, mem_util_percent = 0.8, gpu_count = 1):
    tts_engine = TTSEngine(memory_util=mem_util_percent, tp=gpu_count)
    if not tts_engine:
        print("Failed to get Maya tts_engine")
        return

    tts_engine = TTSEngine(memory_util=mem_util_percent, tp=gpu_count)

    audio = tts_engine.batch_generate(text, prompt)
    output_file = "output.wav"
    sf.write(output_file, audio, 24000)
    print("done")

def main():
    text = sys.argv[1]
    prompt = sys.argv[2]
    execute_maya(text, prompt)


if __name__ == "__main__":
    main()


