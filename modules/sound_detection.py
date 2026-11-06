# modules/sound_detection.py
import random
import time

# Predefined results for demo MP3s
AUDIO_DATA = {
    "help1.mp3": {
        "file": "help1.mp3",
        "gender": "Female",
        "voices_detected": 1,
        "avg_pitch": 430,
        "duration": 2.8,
        "volume_level": 0.75
    },
    "help2.mp3": {
        "file": "help2.mp3",
        "gender": "Male",
        "voices_detected": 1,
        "avg_pitch": 210,
        "duration": 3.2,
        "volume_level": 0.81
    }
}

def analyze_audio(filename: str):
    """Simulated analysis for demo"""
    time.sleep(1.5)  # looks like it’s analyzing
    data = AUDIO_DATA.get(filename)
    if not data:
        # random fallback for unknown audio
        data = {
            "file": filename,
            "gender": random.choice(["Male", "Female"]),
            "voices_detected": random.choice([1, 2]),
            "avg_pitch": round(random.uniform(180, 450), 2),
            "duration": round(random.uniform(2.0, 5.0), 2),
            "volume_level": round(random.uniform(0.5, 1.0), 2)
        }
    return data
