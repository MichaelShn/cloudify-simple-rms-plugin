from cloudify import ctx
from cloudify.workflows import ctx as workflow_ctx
from cloudify.decorators import workflow

from cloudify import manager

import json


def create(resource_pool,resources,  **kwargs):
    create_secret(resource_pool, json.dumps(resources))


def allocate(resource_pool, **kwargs):
    resource_pool_list = json.loads(read_secret(resource_pool).value)
    found_unallocated=False
    for index in range(len(resource_pool)):
        if resource_pool_list[index]['allocation']['allocated'] == False :
            found_unallocated = True
            resource_pool_list[index]['allocation']['allocated'] = True
            resource_pool_list[index]['allocation']['node_instance'] = ''
            ### to do add when an to who it was allocated
            allocated_resource=resource_pool_list[index]['resource']
            break

    ## Error if not found
    if found_unallocated == False:
        found_unallocated = False

    else:
        ctx.instance.runtime_properties.update(allocated_resource)
        write_secret(resource_pool, json.dumps(resource_pool_list))



def release(resource_pool_name, **kwargs):
    found_unallocated = False
    ## TODO write function



def read_secret(secret_key):
    cfy_client = manager.get_rest_client()
    return cfy_client.secrets.get(key=secret_key)


def write_secret(secret_key, secret_value):
    cfy_client = manager.get_rest_client()
    return cfy_client.secrets.update(key=secret_key, value=secret_value)

def create_secret(secret_key, secret_value):
    cfy_client = manager.get_rest_client()
    return cfy_client.secrets.create(key=secret_key, value=secret_value)
