from cloudify import ctx
from cloudify.workflows import ctx as workflow_ctx
from cloudify.decorators import workflow

from cloudify import manager

import json



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
    if found_unalocated == false:

    ## Write back the resource default_pool
    write_secret(resource_pool_name, resource_pool)
    ## Write resource in to runtime properties
    ctx.instance.runtime_properties.update(allocated_resource)


def release():



def read_secret():
    cfy_client = manager.get_rest_client(secret_key)
    return cfy_client.secrets.get(key=secret_key)


def write_secret(secret_key, secret_value):
    cfy_client = manager.get_rest_client()
    return cfy_client.secrets.create(key=secret_key, value=secret_value)
