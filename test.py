import time
from voicevox_core import VoicevoxCore


# Voicevox settings
OPEN_JTALK_DICT_DIR = "./open_jtalk_dic_utf_8-1.11"
VOICE_ID = 1
VOICE_OUTPUT_FILENAME = "audioResponse.wav"
VOICEVOX_ACCELERATION_MODE = "GPU"

print(f"[VOICEVOX] loading up voicevox core..")
# core = VoicevoxCore(
#     acceleration_mode=VOICEVOX_ACCELERATION_MODE, open_jtalk_dict_dir=OPEN_JTALK_DICT_DIR
# )
core = VoicevoxCore(acceleration_mode=VOICEVOX_ACCELERATION_MODE,
                    open_jtalk_dict_dir=OPEN_JTALK_DICT_DIR)
core.load_model(VOICE_ID)
print(
    f"[VOICEVOX] successfully loaded! running on {'gpu' if core.is_gpu_mode else 'cpu'}")


def tts_generate_wav_jp(sentence: str):
    start = time.time()

    print("querying voicevox")
    audio_query = core.audio_query(sentence, VOICE_ID)
    audio_query.output_stereo = True
    print(f"querying took: {time.time() - start}")

    print("synthesis starting")
    wav = core.synthesis(audio_query, VOICE_ID)
    print(f"synthesis took: {time.time() - start}")

    with open(VOICE_OUTPUT_FILENAME, "wb") as file:
        file.write(wav)
    print(f"wrote to wav file took: {time.time() - start}")


if __name__ == '__main__':
    # test if voicevox is up and running
    print('Voicevox attempting to speak now...')
    tts_generate_wav_jp('むかしあるところに、ジャックという男の子がいました。ジャックはお母さんと一緒に住んでいました。')
