# Voice-GPT

Voice-GPT is a Python script that allows you to interact with OpenAI's GPT-3 using voice input and text-to-speech capabilities. You can ask questions or provide prompts through voice input, and the script will use OpenAI's GPT-3 model to provide responses. The responses are then read out to you using text-to-speech.

## Requirements

- [Python](https://www.python.org/) (3.7 or higher)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) library
- [pyttsx3](https://pypi.org/project/pyttsx3/) library
- [OpenAI Python](https://github.com/openai/openai-python) library
- An OpenAI API key - [How to get API Key](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt)

## Installation

1. Clone this repository or download the `voice-gpt.py` file to your local machine.

2. Install the required libraries:

  ```sh
  pip install -r requirements.txt
  ```


3. Replace `'replace_with_your_api_key'` in the script with your actual OpenAI API key.

## Usage

1. Run the script:

  ```sh
  python voice-gpt.py
  ```


2. The script will prompt you to speak something or type 'exit' to quit.

3. Speak your input or type 'exit' to end the session.

4. The script will use the OpenAI GPT-3 model to generate a response and read it out to you using text-to-speech.

## Configuration

You can customize the behavior of the script by modifying the following parameters:

- `max_tokens`: Adjust the character limit for responses.
- `temperature`: Modify the response creativity level.
- `engine`: Change the OpenAI GPT-3 engine. The script currently uses "text-davinci-003" for a more concise interaction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT-3 API.
- Developers of the `speech_recognition` and `pyttsx3` libraries for their contributions.
- -Thanks to nickbild for the Idea - https://github.com/nickbild/voice_chatgpt

Happy conversing with Voice-GPT!
