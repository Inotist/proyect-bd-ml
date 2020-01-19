from google.cloud import dataproc_v1 as dataproc

def create_cluster(dataproc, project, zone, region, cluster_name):
    """Create the cluster."""
    print('Creating cluster...')
    zone_uri = \
        f'https://www.googleapis.com/compute/v1/projects/{project}/zones/{region}'
    cluster_data = {
        "cluster_name": cluster_name,
        "config": {
            "config_bucket": "bda5-keepcoding-inot1",
            "gce_cluster_config": {
                "zone_uri": zone,
                "metadata": {},
                "subnetwork_uri": "default",
                "service_account_scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "master_config": {
                "num_instances": 1,
                "machine_type_uri": "n1-standard-4",
                "disk_config": {
                    "boot_disk_type": "pd-ssd",
                    "boot_disk_size_gb": 15,
                    "num_local_ssds": 0
                },
                "accelerators": []
            },
            "worker_config": {
                "num_instances": 2,
                "machine_type_uri": "n1-standard-2",
                "disk_config": {
                    "boot_disk_type": "pd-ssd",
                    "boot_disk_size_gb": 15,
                    "num_local_ssds": 0
                },
                "accelerators": []
            },
            "software_config": {
                "image_version": "1.3-deb9",
                "properties": {"hive:hive.mapred.mode": "nonstrict"},
                "optional_components": []
            },
            "secondary_worker_config": {
                "num_instances": 0,
                "is_preemptible": True
            }
        },
        "project_id": project
    }

    cluster = dataproc.create_cluster(project, region, cluster_data)
    cluster.add_done_callback(callback)
    global waiting_callback
    waiting_callback = True
    
def post(request):
    cluster_client = dataproc.ClusterControllerClient(client_options={
        'api_endpoint': 'europe-west2-dataproc.googleapis.com:443'
    })
    create_cluster(cluster_client, "bootcamp-bdmlv", "europe-west2-a", "europe-west2", "hive")