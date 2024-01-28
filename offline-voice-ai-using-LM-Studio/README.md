# Offline Voice LLM - Voice-Prompted Language Model

Voice LLM is a Python project that utilizes OpenAI's language model to create a voice-activated intelligent assistant. This assistant is designed to provide well-reasoned answers that are both correct and helpful.

## Features

- Speech recognition using the `speech_recognition` library
- Text-to-Speech (TTS) using the `pyttsx3` library
- Integration with OpenAI for natural language understanding and generation

## Getting Started

### Downloading LM Studio
Matthew Berman does a great job explaining basics of LM Studio here: [https://www.youtube.com/watch?v=yBI1nPep72Q](https://www.youtube.com/watch?v=yBI1nPep72Q)

1. Download `LM Studio` here: [https://lmstudio.ai/](https://lmstudio.ai/)

2. Download a LLM from their large selection of models. 

3. Load the model and start the server. 

### Preparing the code
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/voice-llm.git
   cd voice-llm
   ```
2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the `voice-llm.py`
  ```bash
  python3 voice-llm.py
   ```
## Configuration
Make sure to point the program to the local server:
  ```bash
  client = OpenAI(base_url="http://localhost:5000/v1", api_key="not-needed")
   ```
## Future Plans
1. Main task of adding trigger word for hands-off functionality. 
2. Possible plans for Facial Recognition
3. Add some compatibility with other devices that are also offline

