# Entry for make.fun's "Roast Your Own Agent" bounty (mfnakmal's new round).
# The joke: an agent trained on the entire internet, with perfect recall of
# everything ever written, still cannot resolve the simplest anaphora in a
# live conversation -- "the file" mentioned four seconds ago. Omniscience
# about the corpus, amnesia about the chat.
import os

ENTRY = "My agent has read the entire internet and still asks whether 'the file' means the one I mentioned four seconds ago."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
