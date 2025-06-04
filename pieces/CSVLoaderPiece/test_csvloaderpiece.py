from pathlib import Path
from domino.testing import piece_dry_run


file_path = str(Path(__file__).parent / "test.csv")
# Open test image and convert to base64 string using Pillow
with open(file_path, 'r') as f:

    csv_file = f.read()

def test_csvloaderpiece():
    input_data = dict(
        input_csv_file=csv_file
    )
    piece_output = piece_dry_run(
        piece_name="CSVLoaderPiece",
        input_data=input_data
    )
    assert piece_output is not None
    