# 🧠 Offline Voice Assistant — "Nova"

Nova is an **offline voice-controlled assistant** built in Python using the [Vosk](https://alphacephei.com/vosk/) speech recognition toolkit. It listens for a wake word, recognizes natural commands, and responds using text-to-speech — all without an internet connection.

## 🌟 Features

- 🎙️ Wake-word activation: "Hey Nova", "Nova", or "Wakeup Nova"
- 🎛️ Device control: Light, Fan, Door, Bulb, and All Devices (simulated)
- 🔁 Wake/Sleep toggle with “Goodbye”
- 🕒 Real-time clock reporting
- ❤️ Friendly conversation (“I love you”, “You are beautiful”, etc.)
- 🔇 Self-suppression: Doesn’t listen while speaking (avoids feedback)
- 🧠 Fully offline — privacy-respecting and fast

---

## 🔊 Wake Words
-  Say any of the following:

    "Hey Nova"
      "Nova"
    "Wakeup Nova"

## To deactivate or put the assistant to sleep:
-  Say of the following:
     "Good buy"
---

## command and action

| Command                           | Action                  |
| --------------------------------- | ----------------------- |
| `switch on the light`             | Turns the light on      |
| `turn off the fan`                | Turns the fan off       |
| `open the door`                   | Opens the door          |
| `close the door`                  | Closes the door         |
| `switch on all electric devices`  | Turns on all devices    |
| `switch off all electric devices` | Turns off all devices   |
| `what's the time`                 | Tells the current time  |
        
---

## 📂 Project Structure

Offline Voice Assistant/
│
├── assistant.py              # Main assistant script
├── download_model.py         # Downloads and extracts the Vosk model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── vosk-model-small-en-us-0.15/   # Auto-downloaded model folder (excluded from Git)

