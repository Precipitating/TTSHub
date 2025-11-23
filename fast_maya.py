from Maya1.tts_engine import TTSEngine
import soundfile as sf
import sys

def execute_maya(text, prompt, mem_util_percent = 0.3, gpu_count = 1):
    tts_engine = TTSEngine(memory_util=mem_util_percent, tp=gpu_count)
    if not tts_engine:
        print("Failed to get Maya tts_engine")
        return

    tts_engine = TTSEngine(memory_util=mem_util_percent, tp=gpu_count, quant_policy=8)

    audio = tts_engine.generate(text, prompt)
    output_file = "output.wav"
    sf.write(output_file, audio, 24000)
    print("done")

def main():
    text = sys.argv[1]
    prompt = sys.argv[2]
    gpu_mem = float(sys.argv[3])
    gpu_count = int(sys.argv[4])
    execute_maya(text, prompt, gpu_mem, gpu_count)


if __name__ == "__main__":
    main()


