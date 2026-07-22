import json
import logging

from google.cloud import storage


def compute_total(records):
    """Sum the `amount` field across records, skipping malformed rows."""
    total = 0
    for row in records:
        amount = row.get('amount')
        if amount is None:
            logging.warning("Skipping record with missing amount: %s", row)
            continue
        total += amount
    return total


def process_upload(request):
    """HTTP Cloud Function that processes an uploaded file record."""
    data = request.get_json()
    bucket_name = data['bucket']              # no validation
    file_name = data['file']
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_string()       # no error handling
    result = json.loads(content)              # no error handling
    total = compute_total(result['records'])
    logging.info("Processed upload, total = %s", total)
    return {'total': total}
