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
        'blob_name': f'datasets/airbnb-listings.csv',
        'new_bucket_name': bucket_name,
        'new_blob_name': f'input/airbnb-listings.csv'
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