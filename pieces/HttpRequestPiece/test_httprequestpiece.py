from domino.testing import piece_dry_run
import base64
import json


def test_httprequest_get():
    input_data = {
        'urls': ['https://jsonplaceholder.typicode.com/posts'],
        'method': 'GET'
    }
    piece_outputs = piece_dry_run(
        piece_name="HttpRequestPiece",
        input_data=input_data
    )
    for piece_output in piece_outputs["base64_bytes_data"]:
        output_data = base64.decodebytes(piece_output.encode('utf-8'))
        output_data = json.loads(output_data)
        assert isinstance(output_data, list)


def test_httprequest_post():
    input_data = {
        'urls': ['https://httpbin.org/post'],
        'method': 'POST',
        'body_json_data': json.dumps({
            'key_1': 'domino',
            'key_2': 'testing-post'
        })
    }
    piece_outputs = piece_dry_run(
        piece_name="HttpRequestPiece",
        input_data=input_data
    )
    for piece_output in piece_outputs["base64_bytes_data"]:
        output_data = base64.decodebytes(piece_output.encode('utf-8'))
        output_data = json.loads(output_data)
        assert output_data['json']['key_1'] == 'domino'
        assert output_data['json']['key_2'] == 'testing-post'


def test_httprequest_put():
    input_data = {
        'urls': ['https://httpbin.org/put'],
        'method': 'PUT',
        'body_json_data': json.dumps({
            'key_1': 'domino',
            'key_2': 'testing-put'
        })
    }
    piece_outputs = piece_dry_run(
        piece_name="HttpRequestPiece",
        input_data=input_data
    )
    for piece_output in piece_outputs["base64_bytes_data"]:
        output_data = base64.decodebytes(piece_output.encode('utf-8'))
        output_data = json.loads(output_data)
        assert output_data['json']['key_1'] == 'domino'
        assert output_data['json']['key_2'] == 'testing-put'


