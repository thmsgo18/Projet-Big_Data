from pathlib import Path
import hashlib
import librosa
import pandas as pd

RAW_DIR = Path("data/raw")

rows=[]

def generate_track_id(path: str) -> str:
    return hashlib.md5(path.encode()).hexdigest()

for audio_file in RAW_DIR.rglob("*"):
    if audio_file.suffix.lower() not in {".wav", ".mp3", ".flac"}:
        continue
    path = audio_file.relative_to(Path("."))
    track_id = generate_track_id(str(path))
    duration = librosa.get_duration(path= audio_file)

    rows.append({
        "track_id": track_id,
        "path": str(path),
        "duration": duration
    })

df = pd.DataFrame(rows)

Path("data/processed").mkdir(parents=True, exist_ok=True)
df.to_csv("data/processed/metadata.csv", index=False)