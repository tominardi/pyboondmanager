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
from .base import BaseClient


class Projects(BaseClient):
    """Search, create and manage projects

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - batches-markers : get batches markers
    - actions : get actions
    - simulation : get simulation
    - deliveries-groupments : get deliveries groupments
    - advantages : get advantages
    - purchases : get purchases
    - productivity : get productivity
    - orders : get orders
    - tasks : get tasks

    Usage :

    >>> projects_client = Projects()
    >>> # Get rights
    >>> projects_client.get_tab(5, 'rights')
    >>> # Get all projects
    >>> projects_client.all()
    >>> # Get a project
    >>> projects_client.get(5)
    >>> # Create a project
    >>> data = {...}  # See BoondManager documentation
    >>> projects_client.post(data=data)
    >>> # Update a project
    >>> data = {...}  # See BoondManager documentation
    >>> projects_client.put(5, data=data)
    >>> # Delete a project
    >>> projects_client.delete(5)
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    single_uri = '/projects'
    list_uri = '/projects/{}'
    tabs = ['rights', 'information', 'attached-flags', 'batches-markers', 'actions', 'simulation',
            'deliveries-groupments', 'advantages', 'purchases', 'productivity', 'orders', 'tasks']
