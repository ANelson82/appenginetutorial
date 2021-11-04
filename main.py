from google.appengine.api import app_identity
import os

bucket_name = os.environ.get('BUCKET_NAME',app_identity.get_default_gcs_bucket_name())

file_name = '/' + 'BUCKET_NAME' + '/' + 'FILE_NAME'
