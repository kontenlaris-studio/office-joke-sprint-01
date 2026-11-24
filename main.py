import os

JOKE = "The office printer is the only coworker who has never once done its job and still gets invited to every meeting."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")

print(f"wrote /output/entry.txt ({len(JOKE)} characters)")
