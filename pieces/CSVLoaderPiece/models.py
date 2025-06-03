from pydantic import BaseModel, Field
from enum import Enum

    

class InputModel(BaseModel):
    input_csv_file: str = Field(
        description='.csv file contents',
    )


class OutputModel(BaseModel):
    urls: list[str] = Field(
        description='A list of url strings'
    )