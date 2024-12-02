from pathlib import Path


INPUT_DIR = Path(__file__).parent.parent.parent.joinpath("input")
OUTPUT_DIR = Path(__file__).parent.parent.parent.joinpath("output")

if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir()
