import csv
import io
from domino.base_piece import BasePiece
from .models import InputModel, OutputModel



class CSVLoaderPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        csv_file = input_data.input_csv_file
        csv_io = io.StringIO(csv_file)

        reader = csv.DictReader(csv_io)
        urls = []
        for row in reader:
            url = row.get("url")
            urls.append(url)

        urls = [url for url in urls if url != None]
        

        return OutputModel(
            urls=urls
        )
    
