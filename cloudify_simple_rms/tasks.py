from cloudify import ctx
from cloudify.workflows import ctx as workflow_ctx
from cloudify.decorators import workflow

from cloudify import manager

import json


def create(resource_pool,resources, , **kwargs):
    write_secret(resource_pool, resources)


def allocate(resource_pool, **kwargs):
    resource_pool = read_secret(resource_pool_name)
    found_unalocated=False
    for index in range(len(resource_pool)):
        if resource_pool[index]['allocation']['alocated'] == False :
            found_unalocated = True
            resource_pool[index]['allocation']['alocated'] = True
            ### to do add when an to who it was alocated
            allocated_resource=resource_pool[index]['resource']
            break

    ## Error if not found
    if found_unalocated == False:
        found_unalocated = False

    else:
        write_secret(resource_pool_name, resource_pool)
        ctx.instance.runtime_properties.update(allocated_resource)


def release(resource_pool_name, **kwargs):
    found_unalocated = False
    ## TODO write function



def read_secret(secret_key):
    cfy_client = manager.get_rest_client(secret_key)
    return cfy_client.secrets.get(key=secret_key)


def write_secret(secret_key, secret_value):
    cfy_client = manager.get_rest_client()
    return cfy_client.secrets.create(key=secret_key, value=secret_value)
