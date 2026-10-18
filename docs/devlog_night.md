## 2026-10-17
**What I did:**
- Created the GitHub repo `fingerdecide` (public, MIT license, Python .gitignore)
- Set up the folder structure: `src/`, `tests/`, `docs/` and the documents for the team
- Learned the Git basics: clone, add, commit, push, and how to check `git status`
- Updated `.gitignore` to hide `data/`, `uploads/` and `*.db`
- Created the virtual environment (`python -m venv venv`) and activated it
- Installed the libraries from `requirements.txt` (opencv, numpy, scikit-image, matplotlib, pandas, streamlit, fingerprint-feature-extractor)

**What worked:**
- First commit and push worked, and the `docs` folder appeared on GitHub
- `git status` shows "working tree clean" after pushing

**What failed:**
- Git could not know who i am on first commit. Fixed with `git config --global user.name` and `user.email`
- Typo in `.gitignore`: `* .db` with a space. It must be `*.db`

**What I learned:**
- Git only tracks a folder that has a hidden `.git` folder inside it
- Always check that the end of the terminal prompt shows the right folder before running commands
- `.gitignore` only works on files that haven't been uploaded yet

---

## 2026-10-18
**What I did:**
- Downloaded the SOCOFing dataset, extracted it outside the repo, and copied 60 left-index-finger prints into `data/real`
- Wrote `try_image.py` and found that the prints are 103 x 96 pixels
- Wrote `make_fragment()` in `src/fragments.py` and tested it on one print
- Wrote `scripts/make_fragments.py` to generate fragments for all prints and save `data/answers.csv`

**What worked:**
- 60 images copied, and Git ignores them (`git status` clean)
- `try_image.py` printed the file count and the image shape
- 3 test fragments came out as different partial crops of the same print: shapes (57, 62), (62, 59) and (69, 48)
- [fill in after running the script: how many fragments it made and whether answers.csv was created]

**What failed:**
- Ran the script from the wrong folder and mistyped the file name (`try_fragment.py` vs `try_fragments.py`). Fixed by moving the file to the top level of the repo

**Decisions (also in decisions.md):**
- Fragments are 50 to 70% of the print, because the images are small and smaller crops would have too few points to match
- Minutiae will be extracted after a 3x upscale, using the same factor for prints and fragments
- `random.seed(42)` so my partner and I get identical fragments

**What I learned:**
- An image is a grid of numbers, and cropping is slicing that grid
- Always run Python from the terminal with `(venv)` showing, and from the repo folder
- `answers.csv` is the ground truth I will use later to check whether the system matched the right person

