import os
import whisper

def transcribe_audio(model_path, audio_path):
    """
    Function to transcribe audio using a pre-trained Whisper model.
    
    Parameters:
    model_path (str): Path to the Whisper model file.
    audio_path (str): Path to the audio file that needs to be transcribed.
    
    Returns:
    dict or None: Returns a dictionary containing the transcription result,
                  or None if an error occurs.
    """
    
    # Check if the model file exists at the specified path
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Check if the audio file exists at the specified path
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    try:
        # Load the Whisper model from the specified file path
        model = whisper.load_model(model_path)
        
        # Transcribe the audio file using the loaded model
        transcription_result = model.transcribe(audio_path)
        
        # Return the transcription result
        return transcription_result
    
    except Exception as e:
        # Catch any exceptions that occur during transcription and print an error message
        print(f"An error occurred during transcription: {str(e)}")
        return None

# Define the file paths for the model and audio files
model_path = "./base.pt"  # Path to the pre-trained Whisper model
audio_path = "./output_tr.wav"  # Path to the audio file to be transcribed

# Call the transcription function and store the result
result = transcribe_audio(model_path, audio_path)

# Check if the transcription was successful
if result is not None:
    # Print the transcription result if successful
    print("Transcription Result:", result)
else:
    # Inform the user that the transcription failed
    print("Transcription failed.")