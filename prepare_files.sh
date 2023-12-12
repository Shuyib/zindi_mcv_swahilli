#!/bin/bash

# install ffmpeg if not already installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found"
    echo "Installing ffmpeg..."
    sudo apt-get install ffmpeg
fi

# convert all mp3 files to wav files
: '
This script converts all mp3 files in the current directory to WAV format.
It uses ffmpeg for the conversion. If the conversion is successful, it prints a success message.
If the conversion fails, it logs the error message to a file named conversion.log.
'
for file in *.mp3; do
    if ffmpeg -i "$file" -ar 16000 "${file%.mp3}.wav"; then
        echo "Converted $file to WAV format"
    else
        echo "Error converting $file to WAV format" >> conversion.log
    fi
done

# close script
exit 0