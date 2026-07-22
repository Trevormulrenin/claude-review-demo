from validators import validate_request


def test_valid_request_has_no_errors():
    errors = validate_request({'bucket': 'my-bucket', 'file': 'data.json'})
    assert errors == []


def test_missing_fields_are_reported():
    errors = validate_request({})
    assert any('bucket' in e for e in errors)
    assert any('file' in e for e in errors)
