from faster_whisper import WhisperModel

def transcribe_audio(model_size, audio_file, device="cpu", compute_type="int8", beam_size=5):
    """
    Function to transcribe audio using the Faster Whisper model.
    
    Parameters:
    model_size (str): Size of the Whisper model (e.g., 'small', 'medium', 'large').
    audio_file (str): Path to the audio file to be transcribed.
    device (str): Device to run the model on ('cpu' or 'cuda' for GPU). Default is 'cpu'.
    compute_type (str): Precision type for computation ('float16', 'int8_float16', 'int8'). Default is 'int8'.
    beam_size (int): Beam size for decoding during transcription. Default is 5.
    
    Returns:
    None
    """
    
    try:
        # Load the Whisper model with the specified parameters
        model = WhisperModel(model_size, device=device, compute_type=compute_type)
        
        # Transcribe the audio file
        segments, info = model.transcribe(audio_file, beam_size=beam_size)
        
        # Print detected language and its probability
        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
        
        # Print each segment of the transcription with timestamps
        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    
    except Exception as e:
        # Handle any errors that occur during the transcription process
        print(f"An error occurred during transcription: {str(e)}")

# Parameters for the transcription
model_size = "small"  # Specify the model size
audio_file = "output_tr.wav"  # Path to the audio file to transcribe
device = "cpu"  # Device to run the model on ('cpu' for CPU, 'cuda' for GPU)
compute_type = "int8"  # Precision type for computation ('float16', 'int8_float16', 'int8')

# Call the transcribe_audio function to transcribe the audio
transcribe_audio(model_size, audio_file, device, compute_type)