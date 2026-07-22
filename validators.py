"""Request validation helpers for the upload Cloud Function."""


def validate_request(data):
    """Validate the incoming request payload.

    Returns a list of human-readable error strings. An empty list means the
    payload is valid: it must be a JSON object with non-empty "bucket" and
    "file" fields.
    """
    if not isinstance(data, dict):
        return ['Request body must be a JSON object']

    errors = []
    if not data.get('bucket'):
        errors.append('Missing required field: "bucket"')
    if not data.get('file'):
        errors.append('Missing required field: "file"')
    return errors
