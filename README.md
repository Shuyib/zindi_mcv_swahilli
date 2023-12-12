# zindi_mcv_swahilli
public word error rate: 0.114294524   
private word error rate 0.112809661   

How I used Seamless m4t large to get to the top 5 of the [mozilla common voice competition](https://zindi.africa/competitions/mozilla-foundation-mozilla-common-voice-hackathon-i-nairobi). I only downloaded the `test.tar.gz` directory later I unzipped it and resampled all the audio to 16KHz. I noticed that there was some audio that was muffled, and was pretty bad as is due to the sampling rates that were set. Anyways, the script I used to do the conversion is called `prepare_files.sh`. Follow the instructions to install [seamless m4t large](https://github.com/facebookresearch/seamless_communication). I performed inference on each audio file `python asr.py` the output was then saved to **asr_results.csv** then it was formatted to a certain format needed for Zindi with `python clean_submission.py`. 

## You can do all this in one step
```bash
make run
```

## Lesson
Review huggingface leaderboard for the ASR models. Look for one with the fastest and the most accurate. 

[leaderboard](https://huggingface.co/models?other=hf-asr-leaderboard)

Facebook/meta have a lot of Speech to text models. Look for one that is capable of doing Speech to text. The ones that primarily do one thing seem to be the best.

