#to return absolute path of file in assets folder

from pathlib import Path

op=Path(__file__).parent
ap=op / Path("./assets")    #absolute path of assets folder
def relative_to_assets(path):
    return ap / Path(path)