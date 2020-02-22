from datetime import datetime

def get_data(dataset, category):
    if dataset == 'airbnb-listings.csv' or dataset == 'airbnb':
        return "LOAD DATA INPATH 'gs://bda5-keepcoding-inot1/input/airbnb-listings.csv' OVERWRITE INTO TABLE airbnb;"
    
    if category: return f"LOAD DATA INPATH 'gs://bda5-keepcoding-inot1/input/{dataset}/{category}.csv' OVERWRITE INTO TABLE {dataset}_{category};"
    return f"LOAD DATA INPATH 'gs://bda5-keepcoding-inot1/input/{dataset}.csv' OVERWRITE INTO TABLE {dataset};"

def staging_area(bucket_name, dataset, category, diff=0):
    if dataset == 'airbnb-listings.csv' or dataset == 'airbnb':
        return {
        'bucket_name': bucket_name,
        'blob_name': 'datasets/airbnb-listings.csv',
        'new_bucket_name': bucket_name,
        'new_blob_name': 'input/airbnb-listings.csv'
        }

    now = datetime.now().strftime("%Y/%m/")
    now = now + str(int(datetime.now().strftime("%d"))-diff)

    if category:
        return {
        'bucket_name': bucket_name,
        'blob_name': f'datasets/{dataset}/{category}/{now}/crawl.csv',
        'new_bucket_name': bucket_name,
        'new_blob_name': f'input/{dataset}/{category}.csv'
        }

    return {
    'bucket_name': bucket_name,
    'blob_name': f'datasets/{dataset}/{now}/crawl.csv',
    'new_bucket_name': bucket_name,
    'new_blob_name': f'input/{dataset}.csv'
    }

def get_querys(dataset, category):
    if dataset == 'airbnb': return
    return [
    f"CREATE TABLE IF NOT EXISTS {dataset}_{category} (Name STRING, Latitude STRING, Longitude STRING)",
    f"INSERT OVERWRITE DIRECTORY 'gs://bda5-keepcoding-inot1/output/relations' ROW FORMAT DELIMITED FIELDS TERMINATED BY ';' SELECT airbnb.ID, data.Name FROM airbnb, {dataset}_{category} data WHERE sqrt(pow(cast(airbnb.Latitude as double) - cast(data.Latitude as double), 2) + pow(cast(airbnb.Longitude as double) - cast(data.Longitude as double), 2)) < 0.001"
    ]