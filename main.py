# main.py

import os
import datetime
from font import FONT

# Get user input
text = input("Enter the text you want to draw (A–Z, space only): ").upper()
text = ''.join(c if c in FONT else ' ' for c in text)  # sanitize input

# Build pattern from letters
pattern = ['' for _ in range(7)]
for char in text:
    for i in range(7):
        pattern[i] += FONT[char][i] + ' '  # space between characters

# Starting date (must be a Sunday to align with GitHub graph)
start_date = datetime.date(2023, 1, 1)  # Set this to a Sunday

# Generate commits based on pattern
for week in range(len(pattern[0])):
    for day in range(7):
        if pattern[day][week] == "#":
            date = start_date + datetime.timedelta(weeks=week, days=day)
            for i in range(10):  # More commits = darker green
                with open("file.txt", "a") as f:
                    f.write(f"{date} {i}\n")
                os.system("git add file.txt")
                os.system(
                    f"GIT_AUTHOR_DATE='{date}T12:00:00' "
                    f"GIT_COMMITTER_DATE='{date}T12:00:00' "
                    f"git commit -m 'Commit {i} on {date}'"
                )

print("\n✅ Done! Now push the commits to GitHub.")
