from google.cloud import dataproc_v1 as dataproc
import json

def post(request):
    job_client = dataproc.JobControllerClient(client_options={
        'api_endpoint': 'europe-west2-dataproc.googleapis.com:443'
    })
    
    job = request.get_json()
    
    job_response = job_client.submit_job('bootcamp-bdmlv', 'europe-west2', job)
    job_id = job_response.reference.job_id

    print(f'Submitted job \"{job_id}\".')