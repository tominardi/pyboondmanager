"""
Copyright (c) 2023 Thomas Durey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from .base import BaseClient, DefaultEndpointMixin


class Products(DefaultEndpointMixin, BaseClient):
    """Search, create and manage products

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - opportunities : get opportunities
    - projects : get projects
    - tasks : get tasks

    Usage :

    >>> products_client = Products()
    >>> # Get rights
    >>> products_client.get_tab(5, 'rights')
    >>> # Get all products
    >>> products_client.all()
    >>> # Get a product
    >>> products_client.get(5)
    >>> # Create a product
    >>> data = {...}  # See BoondManager documentation
    >>> products_client.post(data=data)
    >>> # Update a product
    >>> data = {...}  # See BoondManager documentation
    >>> products_client.put(5, data=data)
    >>> # Delete a product
    >>> products_client.delete(5)
    >>> # Get default values
    >>> products_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    single_uri = '/products'
    list_uri = '/products/{}'
    tabs = ['rights', 'information', 'attached-flags', 'opportunities', 'projects', 'tasks']
