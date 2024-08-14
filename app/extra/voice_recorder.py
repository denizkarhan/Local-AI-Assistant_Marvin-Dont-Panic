import os
import sounddevice as sd
import scipy.io.wavfile as wavfile

def record_audio(file_name, duration, sample_rate=44100):
    """
    Function to record audio from the default input device and save it as a WAV file.
    
    Parameters:
    file_name (str): Name of the output WAV file.
    duration (int): Duration of the recording in seconds.
    sample_rate (int): Sampling rate for the recording. Default is 44100 Hz.
    
    Returns:
    None
    """
    
    # Query the input device information to get the maximum input channels
    device_info = sd.query_devices(kind='input')
    max_input_channels = device_info['max_input_channels']
    
    # Ensure the duration is a positive integer
    if duration <= 0:
        raise ValueError("Duration must be a positive integer.")
    
    try:
        # Record audio using the default input device
        # Channels are set to the minimum of 2 or the maximum available channels
        record_voice = sd.rec(int(duration * sample_rate), 
                              samplerate=sample_rate, 
                              channels=min(2, max_input_channels))
        
        # Wait until the recording is finished
        sd.wait()
        
        # Save the recorded audio to a WAV file
        wavfile.write(file_name, sample_rate, record_voice)
        
        print(f"Recording saved as '{file_name}'")
    
    except Exception as e:
        # Catch and report any errors that occur during recording or file writing
        print(f"An error occurred during recording: {str(e)}")

# Get user input for the duration of the recording
try:
    duration = int(input("Enter the time duration in seconds: "))
except ValueError:
    raise ValueError("Please enter a valid integer for the duration.")

# Define the output file name
output_file = 'output_tr2.wav'

# Call the record_audio function to record and save the audio
record_audio(output_file, duration)