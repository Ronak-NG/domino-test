from domino.testing import piece_dry_run



# Open test image and convert to base64 string using Pillow
with open('test.csv', 'r') as f:

    csv_file = f.read()


def test_csvloaderpiece():
    input_data = dict(
        csv_file=csv_file
    )
    piece_output = piece_dry_run(
        piece_name="CSVLoaderPiece",
        input_data=input_data
    )
    assert piece_output is not None
    print(piece_output)