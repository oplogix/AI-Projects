from openai import OpenAI
import pyttsx3
import speech_recognition as sr

# Point to the local server
client = OpenAI(base_url="http://localhost:5000/v1", api_key="not-needed")

# Initialize the TTS engine
engine = pyttsx3.init()

# Initialize the speech recognition
recognizer = sr.Recognizer()

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

while True:
    # Collect the user's speech input
    try:
        with sr.Microphone() as source:
            print("Speak:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        user_input = input("> ")  # Use text input as a fallback

    history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    # Collect the entire response from the model
    response_text = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    # Print and speak the entire response
    print(response_text)
    engine.say(response_text)
    engine.runAndWait()

    new_message["content"] = response_text
    history.append(new_message)
