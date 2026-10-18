import os
import csv
import random
import cv2
from src.fragments import make_fragment

random.seed(42)   # same fragments every time, for you and Person B

REAL = "data/real"
OUT = "data/fragments"
os.makedirs(OUT, exist_ok=True)

rows = []
for fname in sorted(os.listdir(REAL)):
    if not fname.lower().endswith(".bmp"):
        continue
    person_id = fname.split("__")[0]
    img = cv2.imread(os.path.join(REAL, fname), cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("could not read", fname)
        continue
    for k in range(1, 4):
        out_name = f"p{person_id}_f{k}.png"
        cv2.imwrite(os.path.join(OUT, out_name), make_fragment(img))
        rows.append([out_name, person_id, fname])

with open("data/answers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["fragment_file", "person_id", "source_print"])
    writer.writerows(rows)

print("made", len(rows), "fragments")