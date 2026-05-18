# Mango - Voice-Activated AI Desktop Assistant 🥭

Mango is a responsive, local voice assistant built in Python. It seamlessly bridges local desktop automation—such as opening web browsers and navigating custom media libraries—with advanced natural language processing powered by the Google Gemini API.

---

## ✨ Features

- **Smart Wake Word Detection**: Continuously listens for the keyword "Mango" and provides instant verbal and visual confirmation ("Yes, I am listening").
- **Dynamic Noise Calibration**: Automatically samples and adjusts to ambient room noise levels to prevent false triggers or missing commands.
- **Dual Interaction Modes**:
  - *One-Shot Commands*: Processes full phrases spoken in a single breath (e.g., *"Mango, open YouTube"*).
  - *Dialogue Window*: Holds open a flexible, 12-second listening window when initialized with just the wake word—ideal for long, complex AI queries.
- **Hardware Resource Lock Management**: Eliminates operating system-level sound card conflicts by strictly scheduling, isolating, and releasing resource locks between the text-to-speech driver (`pyttsx3`) and microphone stream (`speech_recognition`).
- **Cloud-Driven Brain**: Utilizes the high-efficiency `gemini-3-flash` model via the Gemini API to handle general knowledge questions, debugging, or brainstorming.

---

## 🛠️ Tech Stack

- **Core Language**: Python 3
- **Audio Input**: `speech_recognition` (Google Web Speech API backend)
- **Audio Output (TTS)**: `pyttsx3`
- **Generative AI Link**: Google Gemini API (`gemini-3-flash`)
- **System Automation**: `webbrowser`, `requests`

---

## ⚙️ Architecture & Data Flow

When Mango runs, it cycles through a structured control loop to ensure your microphone and speakers don't attempt to access your system's sound card at the exact same millisecond:

1. **Initialization**: Calibrates the microphone to room noise and boots up.
2. **Passive Listening**: Scans audio frames in short bursts looking for the word "mango".
3. **Hardware Shift**: Once detected, the listener pauses, the audio driver initializes, Mango speaks its confirmation line, and the text-to-speech engine explicitly stops to release the audio hardware line.
4. **Execution**: The microphone re-opens to capture your request and sends it either to your local automation blocks or out to the Gemini API.

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/mango-voice-assistant.git](https://github.com/YOUR_USERNAME/mango-voice-assistant.git)
cd mango-voice-assistant
