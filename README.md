# 🎙️ Voice Assistant using Python

A Python-based voice assistant capable of listening to user commands, converting speech into text, processing commands, and responding using text-to-speech.

This project focuses on building the core components of a personal voice assistant:
- Speech recognition
- Voice activity detection
- Command processing
- Text-to-speech response

---

## 📌 Project Overview

This Voice Assistant is built using Python and allows users to interact with the system using voice commands.

The assistant can:
- Listen through a microphone
- Convert speech into text
- Understand predefined commands
- Perform tasks
- Respond through voice output

Currently, the assistant works as a command-based voice assistant and is designed to be extended into a more advanced AI assistant.

---

## 🚀 Features

### 🎤 Voice Input
- Captures audio from the microphone
- Uses custom voice activity detection
- Automatically detects when the user starts and stops speaking

### 🧠 Speech Recognition
- Converts speech into text
- Uses SpeechRecognition library

### 🔊 Text-to-Speech
- Provides voice responses
- Uses pyttsx3 for offline speech generation

### ⚙️ Command Execution

Currently supported commands:

- Tell current time
- Tell jokes
- Search Wikipedia
- Open websites
- Exit assistant

---

## 🏗️ Project Structure

Voice-Assistant/
│
├── main.py # Main assistant execution file
├── speech.py # Voice recording and recognition logic
├── config.py # Configuration settings
│
├── features/
│ ├── browser.py # Browser-related commands
│ ├── jokes.py # Joke functionality
│ └── time.py # Time-related commands
│
├── tests/
│ ├── check_mic.py # Microphone testing
│ └── volume_test.py # Audio threshold testing
│
├── requirements.txt # Required Python packages
├── .gitignore
└── README.md


---

## 🛠️ Technologies Used

### Programming Language
- Python 3.14

### Libraries

| Library | Purpose |
|---|---|
| SpeechRecognition | Speech-to-text conversion |
| pyttsx3 | Text-to-speech engine |
| sounddevice | Audio recording |
| scipy | Audio processing |
| wikipedia | Wikipedia search |
| pyjokes | Joke generation |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Omm13/Voice-Assistant.git
2. Navigate to Project Folder
cd Voice-Assistant
3. Create Virtual Environment
python -m venv venv
4. Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
▶️ Run the Assistant

Start the assistant:

python main.py

Example interaction:

Assistant:
Good Morning!
How can I help you?

User:
What is the time?

Assistant:
The time is 04:30 PM
🎧 Microphone Configuration

The project uses microphone input through sounddevice.

If multiple microphones are available:

Check available devices:
python tests/check_mic.py
Select the correct microphone device in the configuration.
🧩 Current Limitations
Requires manual execution using Python
No wake word detection
Limited command understanding
Uses predefined command logic
No long-term memory
🔮 Future Improvements

Planned improvements:

 Wake word detection ("Hey Assistant")
 Background execution
 AI-based intent understanding
 Natural language conversations
 User memory system
 Application control
 Email automation
 Weather information
 LLM integration
📈 Project Evolution

This project is being developed in stages:

Phase 1 — Core Voice Assistant ✅
Speech input
Speech recognition
Text-to-speech
Command execution
Phase 2 — Smart Assistant
Wake word detection
Background service
Better command understanding
Phase 3 — AI Assistant
LLM integration
Context awareness
Personal memory
👨‍💻 Author

Omm Miriyala

GitHub:
https://github.com/Omm13

📜 License

This project is open-source and available for learning and experimentation.