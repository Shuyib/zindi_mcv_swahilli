import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('asr_results.csv', names=["path", "sentence"])

# Remove 'test/' from the 'path' column and replace '.wav' with '.mp3'
df['path'] = df['path'].apply(lambda x: x.replace('test/', '').replace('.wav', '.mp3'))

# Remove some rows
# List of IDs to remove
remove_these_ids = ["common_voice_sw_37664539.mp3", "common_voice_sw_31290838.mp3", "common_voice_sw_28266617.mp3", "common_voice_sw_35087387.mp3", "common_voice_sw_37214113.mp3"]  

# Remove rows with the specified IDs
df = df[~df['path'].isin(remove_these_ids)]

# Write the modified DataFrame to a new CSV file
df.to_csv('seamlessm4t_vanilla_16000samprate_wav.csv', index=False)
