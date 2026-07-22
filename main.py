import json
   from google.cloud import storage

   def process_upload(request):
       """HTTP Cloud Function that processes an uploaded file record."""
       data = request.get_json()
       bucket_name = data['bucket']          # no validation
       file_name = data['file']
       client = storage.Client()
       bucket = client.bucket(bucket_name)
       blob = bucket.blob(file_name)
       content = blob.download_as_string()
       result = json.loads(content)          # no error handling
       total = 0
       for row in result['records']:
           total = total + row['amount']     # KeyError risk
       return {'total': total}