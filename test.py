import os
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path, AudioFile

model_path = get_model_path()
#data_path = get_data_path()
data_path = '/home/giang/.local/lib/python2.7/site-packages/pocketsphinx/data'
print("GIANG DEBUG: ", model_path)

config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, 'goforward.raw'),
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)