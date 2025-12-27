🎙️ AI Voice Generator (ElevenLabs + Flet)

A desktop application that converts text into high-quality speech using ElevenLabs Text-to-Speech API, built with Python and Flet.
The app allows you to paste or import text, choose a voice, generate audio, play it instantly, and keep a history of generated files.
------------------------------------------------------------------------------------------------------------------------------------
✨ Features

✅ Text-to-Speech using ElevenLabs voices

🎧 Instant audio playback inside the app

📂 Import text from .txt files

🧠 Multiple male & female voice options

🕒 Auto-saved audio with timestamped filenames

🗂️ Generation history panel

🎨 Modern dark UI (Flet)
-------------------------------------------------------------------------------------------------------------------------------------
🖥️ Tech Stack

Python 3.9+

Flet (UI framework)

ElevenLabs API
--------------------------------------------------------------------------------------------------------------------------------------
📁 Project Structure

├── index.py              # Main application
├── api_key.py            # ElevenLabs API key (not included)
├── GeneratedAudio/       # Auto-generated MP3 files
└── README.md
---------------------------------------------------------------------------------------------------------------------------------------
🔐 API Key Setup

Create an account at ElevenLabs

Generate an API key

Create a file called api_key.py

API_KEY = "YOUR_ELEVENLABS_API_KEY"
--------------------------------------------------------------------------------------------------------------------------------------
📦 Installation
1️⃣ Install dependencies

python index.py
---------------------------------------------------------------------------------------------------------------------------------------
2️⃣ Run the app

python index.py


The desktop window will open automatically.
---------------------------------------------------------------------------------------------------------------------------------------

🧑‍💻 How to Use

Paste text or click 📂 to import a .txt file

Choose a voice from the dropdown

Click Generate

Audio plays instantly 🎧

MP3 file is saved in GeneratedAudio/

History is shown on the right panel
--------------------------------------------------------------------------------------------------------------------------------------

🎤 Available Voices
Name	Gender
Rachel	Female
Bella	Female
Domi	Female
Adam	Male
Antoni	Male
Josh	Male

--------------------------------------------------------------------------------------------------------------------------------------

🗑️ History Management

Generated files appear in the History panel

Click 🗑️ to clear UI history

Audio files remain saved locally
--------------------------------------------------------------------------------------------------------------------------------------
⚠️ Notes & Limitations

Internet connection required

API usage depends on ElevenLabs plan

Large texts may take longer to generate

History reset does not delete audio files
-----------------------------------------------------------------------------------------------------------------------------------

🚀 Future Improvements (Ideas)

🔊 Speed & pitch control

📜 Export history list

🌍 Language selection

🎚️ Audio format options (WAV / MP3)

☁️ Cloud save support

📄 License
------------------------------------------------------------------------------------------------------------------------------------

This project is for personal and educational use.
Commercial usage depends on ElevenLabs licensing terms.



Requests (HTTP)

flet_audio (audio playback)
