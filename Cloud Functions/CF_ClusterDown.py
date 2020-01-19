from google.cloud import dataproc_v1 as dataproc

def post(request):
    cluster_client = dataproc.ClusterControllerClient(client_options={
        'api_endpoint': 'europe-west2-dataproc.googleapis.com:443'
    })
    operation = cluster_client.delete_cluster("bootcamp-bdmlv", "europe-west2", "hive")
    
    return operation.result()