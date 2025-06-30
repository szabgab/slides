from pathlib import Path

folder = Path("abc")
folder.mkdir()       # Creates "abc", fails if it already exists


Path("something").joinpath("else").mkdir(parents=True, exist_ok=True)
# partnes - create intermediate folders as well
# exist_ok - don't fail if folder already exists
