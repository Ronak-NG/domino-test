import csv
from domino.base_piece import BasePiece
from .models import InputModel, OutputModel



class CSVLoaderPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        csv_file = input_data.input_csv_file


        reader = csv.DictReader(csv_file)
        urls = []
        for row in reader:
            url = row.get("url")
            urls.append(url)

        return OutputModel(
            urls=urls
        )
    
