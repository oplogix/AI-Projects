import speech_recognition as sr
import pyttsx3
import openai

# Speech to Text
def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("You: (Speak something or type 'exit' to quit)")
        audio = recognizer.listen(source)

    try:
        voice_input = recognizer.recognize_google(audio)
        print("You said: " + voice_input)
        return voice_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print("Sorry, there was an error with the request. {0}".format(e))
        return ""

# ChatGPT Interaction
def chat_with_gpt(voice_input):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the "text-davinci-003" model
        prompt="You: " + voice_input,
        max_tokens=1024,  # Set a character limit for responses, lower it for testing.
        temperature=0.7,
        stop=None,
    )
    return response.choices[0].text.strip()

# Text to Speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main Function
if __name__ == "__main__":
    # Set up your OpenAI API key
    api_key = 'replace_with_you_api_key' #Replace Me
    openai.api_key = api_key

    print("Welcome to the ChatGPT voice interface. Type 'exit' to quit.")

    while True:
        print("You: (Speak something or type 'exit' to quit)")  # Add this line to prompt for input
        voice_input = get_voice_input()

        if voice_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break

        response = chat_with_gpt(voice_input)
        print("ChatGPT:", response)

        text_to_speech(response)
