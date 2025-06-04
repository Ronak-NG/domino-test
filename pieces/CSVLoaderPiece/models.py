from pydantic import BaseModel, Field
from enum import Enum

    

class InputModel(BaseModel):
    input_csv_file: str = Field(
        default="""
url
https://example.com/image1.jpg
""",
        description='CSV file contents - paste or edit your CSV data here',
        json_schema_extra={
            'widget': "codeeditor-text"
        }
    )


class OutputModel(BaseModel):
    urls: list[str] = Field(
        description='A list of url strings'
    )