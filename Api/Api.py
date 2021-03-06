import requests
from google.cloud import dataproc_v1
from ApiConfig import *
from ApiUtils import *

import random


def crawl(page):
    if type(page) is list:
        for site in page:
            r = requests.get(f"https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/Crawler{site}")
    else: r = requests.get(f"https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/Crawler{page}")
    
    print('Status code: ' + str(r.status_code))
    return r.text
    

# Se recomienda hacer stage después de cada scrap o subida de archivos, ya que aún no está preparado para gestionar datos muy antiguos.
def stage(dataset='airbnb-listings.csv', category=None):
    warehouse = staging_area('bda5-keepcoding-inot1', dataset, category)
    
    r = requests.post('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/StageData', json=warehouse)

    diff = 0 # Buscamos el dataset en directorios de días anteriores si no lo encontramos en el día actual.
    while r.status_code != 200 and diff < 15:
        diff += 1
        warehouse = staging_area('bda5-keepcoding-inot1', dataset, category, diff)
        r = requests.post('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/StageData', json=warehouse)

    print('Status code: ' + str(r.status_code))
    return r.text

    
def create_cluster():
    r = requests.get('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/CreateCluster')
    print('Status code: ' + str(r.status_code)) # Recibe un status code 500 (error interno), pero en realidad sí que se crea el clúster.
    return r.text
    
    
def send_job(job_name, dataset='airbnb', category=None):
    if 'CargarDatos' in job_name['reference']['job_id']:
        job_name['hive_job']['query_list']['queries'][0] = get_data(dataset, category)
    if 'CalcularDistancias' in job_name['reference']['job_id']:
        job_name['hive_job']['query_list']['queries'] = get_querys(dataset, category)

    r = requests.post('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/SendHiveJob', json=job_name)
    
    for retry in range(2):
        if r.status_code == 500: # Comprobamos que el fallo no se deba a que el job_id esté repetido y reintentamos con un id aleatorio.
            job_name['reference']['job_id'] = job_name['reference']['job_id'] + str(int(random.random()*1000))
            r = requests.post('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/SendHiveJob', json=job_name)
        else: break
        
    print('Status Code: ' + str(r.status_code))
    return r.text


def delete_cluster():
    return requests.get('https://europe-west1-bootcamp-bdmlv.cloudfunctions.net/DeleteCluster').text # Pasa lo mismo que con la función de crear cluster.

