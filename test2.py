import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
model_path2 = '/home/giang/NhandangWakeWord/Python/TAR2720'
speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    #lm=os.path.join(model_path, 'en-us.lm.bin'),
    #dic=os.path.join(model_path, 'cmudict-en-us.dict')
    lm=os.path.join(model_path2, '9299.lm'),
    dic=os.path.join(model_path2, '9299.dic')
)

for phrase in speech:
    print(phrase)

#http://www.speech.cs.cmu.edu/tools/lmtool-new.html