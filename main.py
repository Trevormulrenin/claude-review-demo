import json

from google.cloud import storage

from validators import validate_request


def process_upload(request):
    """HTTP Cloud Function that processes an uploaded file record."""
    data = request.get_json(silent=True)
    errors = validate_request(data)
    if errors:
        return {'errors': errors}, 400
    bucket_name = data['bucket']
    file_name = data['file']
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_string()       # no error handling
    result = json.loads(content)              # no error handling
    total = 0
    for row in result['records']:
        total = total + row['amount']         # unguarded dict access
    print("Processed upload, total =", total)  # bare print, not structured logging
    return {'total': total}
