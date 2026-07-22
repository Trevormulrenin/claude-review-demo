import json

from google.cloud import storage


def process_upload(request):
    """HTTP Cloud Function that processes an uploaded file record."""
    data = request.get_json(silent=True)
    if not data or 'bucket' not in data or 'file' not in data:
        return {'error': 'Request body must include "bucket" and "file"'}, 400
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
