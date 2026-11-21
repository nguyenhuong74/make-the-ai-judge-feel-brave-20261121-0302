"""Write one short relaxing text to /output/entry.txt.

The text is a fixed, original piece written for this entry. It is
deterministic: the same bytes are produced on every run.
"""

import os

TEXT = (
    "Evening light turns the colour of apricots. "
    "A sparrow lands on the rail, folds its wings, and stays. "
    "The kettle has gone quiet. Steam thins above the cup. "
    "Nothing here needs hurrying. Sit a while. "
    "The chair holds your weight, and tomorrow can wait its turn at the door."
)


def main() -> None:
    # Self-check the gate before writing: 1-280 Unicode code points,
    # valid UTF-8, and not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    TEXT.encode("utf-8")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
