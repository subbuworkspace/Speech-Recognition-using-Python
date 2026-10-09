# 🎙️ Speech Recognition using Python

A simple **Speech Recognition project using Python** that captures voice through a microphone and converts the spoken words into text.

This project is designed as a beginner-friendly introduction to **Speech-to-Text**, audio processing, Python libraries, and basic AI applications.

---

## 📌 Project Overview

Speech Recognition is a technology that allows computers to understand human speech and convert it into text.

In this project:

```text
🎤 Human Voice
      ↓
🎧 Microphone
      ↓
🔊 Audio Signal
      ↓
🧠 Speech Recognition
      ↓
📝 Text
```

The project uses the Python `SpeechRecognition` library and Google's Speech Recognition service to recognize spoken English.

---

## 🚀 Features

* 🎤 Capture audio from microphone
* 🔊 Convert speech into text
* 🧠 Use Google Speech Recognition API
* 🔇 Handle background noise
* ⚠️ Handle speech recognition errors
* 🌐 Handle API connection errors
* 🐍 Simple Python implementation
* 🔧 Easy to extend into a voice assistant

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* Google Speech Recognition API

---

## 📂 Project Structure

```text
Speech-Recognition-Python/
│
├── speech_recognition.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Speech-Recognition-Python.git
```

Move into the project directory:

```bash
cd Speech-Recognition-Python
```

---

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install SpeechRecognition
pip install PyAudio
```

---

## ▶️ Run the Project

Run:

```bash
python speech_recognition.py
```

The program will first adjust to the background noise.

Then you will see:

```text
Adjusting for background noise...
Listening...
```

Speak into your microphone.

The program will process your voice and display:

```text
Recognizing speech...

You said:
Hello, this is a speech recognition project
```

---

## 💻 Python Code

```python
import speech_recognition as sr


def speech_to_text():

    # Create recognizer object
    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:

        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")

        text = recognizer.recognize_google(audio)

        print("\nYou said:")
        print(text)

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

    except sr.RequestError as e:
        print("Could not connect to Speech Recognition service.")
        print("Error:", e)

    return None


if __name__ == "__main__":
    speech_to_text()
```

---

# 🧠 How Does It Work?

### Step 1 — Microphone Input

Python accesses the microphone using:

```python
sr.Microphone()
```

This allows the program to capture your voice.

---

### Step 2 — Background Noise Adjustment

```python
recognizer.adjust_for_ambient_noise(source, duration=1)
```

This helps the recognizer understand the surrounding background noise before listening to the user.

---

### Step 3 — Capture Speech

```python
audio = recognizer.listen(source)
```

The microphone records the user's speech.

---

### Step 4 — Speech Recognition

```python
recognizer.recognize_google(audio)
```

The recorded audio is sent to Google's Speech Recognition service.

The service processes the speech and returns the recognized text.

---

### Step 5 — Display Text

The recognized speech is stored in:

```python
text
```

and displayed using:

```python
print(text)
```

---

# ⚠️ Error Handling

The project handles two common problems.

### 1. UnknownValueError

```python
except sr.UnknownValueError:
```

This occurs when the system cannot understand the recorded speech.

Example:

```text
Sorry, I could not understand the audio.
```

---

### 2. RequestError

```python
except sr.RequestError as e:
```

This can happen when the Speech Recognition service cannot be reached.

Example:

```text
Could not connect to Speech Recognition service.
```

---

# 📚 Important Concepts

## What is Speech Recognition?

Speech Recognition is the process of converting human speech into machine-readable text.

```text
Speech → Audio → Processing → Text
```

---

## Speech Recognition vs Text-to-Speech

| Technology         | Function      |
| ------------------ | ------------- |
| Speech Recognition | Speech → Text |
| Text-to-Speech     | Text → Speech |

Example:

```text
Speech Recognition:
"Hello" 🎤 → "Hello" 📝

Text-to-Speech:
"Hello" 📝 → "Hello" 🔊
```

---

# 🔍 Important Python Functions

### `sr.Recognizer()`

Creates the speech recognition object.

```python
recognizer = sr.Recognizer()
```

---

### `sr.Microphone()`

Uses the system microphone as the audio source.

```python
with sr.Microphone() as source:
```

---

### `adjust_for_ambient_noise()`

Helps the recognizer adapt to background noise.

```python
recognizer.adjust_for_ambient_noise(source)
```

---

### `listen()`

Captures the user's speech.

```python
audio = recognizer.listen(source)
```

---

### `recognize_google()`

Converts the recorded speech into text using Google's speech recognition service.

```python
text = recognizer.recognize_google(audio)
```

---

# 🎯 Learning Objectives

Through this project, you can understand:

* Python audio processing basics
* Speech-to-Text concepts
* Microphone input
* Speech recognition
* API-based AI services
* Exception handling
* Background noise handling
* Basic AI application development

---

# 💡 Interview Questions

### Beginner

**1. What is Speech Recognition?**

Speech Recognition converts spoken language into text that a computer can process.

**2. Which Python library is used in this project?**

```text
SpeechRecognition
```

**3. Why is PyAudio required?**

PyAudio provides access to the computer's audio input and microphone.

**4. What does `Recognizer()` do?**

It creates the object responsible for processing and recognizing speech.

**5. What does `Microphone()` do?**

It allows Python to capture audio from the system microphone.

---

### Intermediate

**6. What is background noise?**

Unwanted sound present in the environment while recording speech.

**7. Why use `adjust_for_ambient_noise()`?**

It helps the recognizer determine the ambient noise level and improve recognition.

**8. What happens if speech cannot be understood?**

`UnknownValueError` is raised.

**9. What happens if the recognition service cannot be accessed?**

`RequestError` can be raised.

**10. Is this completely offline?**

No. `recognize_google()` uses Google's online speech recognition service.

---

# ⚠️ Limitations

This basic implementation has some limitations:

* Requires microphone access
* Internet connection is required for Google recognition
* Accuracy can decrease with heavy background noise
* Accents and pronunciation can affect recognition
* Very long recordings may not be ideal

---

# 🚀 Future Improvements

This project can be extended into a much more powerful AI application.

### Version 2

Add:

* Start/Stop recording button
* Save recognized text
* Timestamp
* Multiple languages
* Text file output

### Version 3

Build a **Streamlit Speech Recognition App**:

```text
User
 ↓
Streamlit UI
 ↓
🎤 Record Voice
 ↓
Speech Recognition
 ↓
Text
 ↓
Display / Download
```

### Version 4 — AI Voice Assistant

Combine Speech Recognition with an LLM:

```text
🎤 Voice
   ↓
Speech Recognition
   ↓
📝 Text
   ↓
🤖 LLM
   ↓
💡 AI Response
   ↓
🔊 Text-to-Speech
   ↓
🎧 Voice
```

This can eventually become a complete **AI Voice Assistant**.

---

# 🔮 Future Project Ideas

After completing this project, you can build:

1. 🎙️ Speech-to-Text Application
2. 🤖 AI Voice Assistant
3. 📝 Voice-Based Notes Application
4. 🌐 Multilingual Speech Translator
5. 📞 Voice-Controlled Application
6. 🎧 Meeting Transcription System
7. 🤖 Voice + LLM Chatbot

---

# 📊 Project Result

The project successfully captures speech from a microphone and converts the spoken words into text.

Example:

```text
Input:
🎤 "Python is useful for Artificial Intelligence"

Output:
📝 Python is useful for Artificial Intelligence
```

---

# 🏷️ Skills Demonstrated

```text
Python
Speech Recognition
Audio Processing
API Integration
Exception Handling
AI Fundamentals
Natural Language Processing
```

---

# 📌 Conclusion

This project provides a simple introduction to **Speech Recognition using Python**.

It demonstrates how human speech can be captured through a microphone and converted into text using a speech recognition service.

The project also provides a foundation for building more advanced applications such as **AI voice assistants, transcription systems, voice-controlled applications, and LLM-powered voice agents**.

---

## ⭐ If You Like This Project

Feel free to ⭐ star the repository and use the project for learning and experimentation.

---

### 👨‍💻 Author

**Subrata Mondal**

Data Analyst | Data & AI | Python | SQL | Power BI | Machine Learning | Generative AI
