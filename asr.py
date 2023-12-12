"""
This script uses a pre-trained model to perform automatic speech recognition (ASR) on a list of audio files.
The transcribed text is written to a CSV file named "asr_results.csv" in the same directory as the audio files.
The language code used for ASR is "swh" for Swahili.
"""

import os
import glob as glob
import torch
import torchaudio
from seamless_communication.models.inference import Translator
from tqdm import tqdm

# set the working directory
os.chdir("/home/stormbird/Downloads/seamless_communication/test")

# Initialize a Translator object with a multitask model, vocoder on the GPU.
# vocoder is the tokenizer 
translator = Translator("seamlessM4T_large", "vocoder_36langs", torch.device("cuda:0"), torch.float16)

# list all the audio files in the test folder
files = glob.glob("test/*.wav")
# use the missing files list from the previous step 
# remove the newline character from the end of each line
# with open("missing_files.txt", "r") as f:
#     files = f.readlines()
# files = [file.strip() for file in files]


# use a while loop to process all the files
# transcribed_text, _, _ = translator.predict(<path_to_input_audio>, "asr", <src_lang>)


# add header to be path and sentence
with open("asr_results.csv", "a", encoding="utf-8") as f:
    f.write("path,sentence\n")

"""
This section of the code iterates over a list of files. For each file, it uses a translator object
to predict the transcribed text from the file. The prediction method takes three arguments: the file,
the type of prediction (in this case, "asr" for automatic speech recognition), and the language code
(in this case, "swh" for Swahili).

After the prediction is made, the code opens a CSV file named "asr_results.csv" in append mode, and writes
a line to the file that includes the file name and the transcribed text, separated by a comma.

The tqdm function is used to provide a progress bar for the loop.
"""
for file in tqdm(files):
    transcribed_text, _, _ = translator.predict(file, "asr", "swh")
    with open("asr_results.csv", "a", encoding="utf-8") as f:
        f.write(f"{file},{transcribed_text}\n")