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


class Opportunities(DefaultEndpointMixin, BaseClient):
    """Search, create and manage opportunities

    Tabs :

    - rights : get rights of the current user
    - informations : get informations
    - attached-flags : get attached flags
    - simulation : get simulation
    - positionings : get positionings
    - actions : get actions
    - projects : get projects
    - download : get download
    - tasks : get tasks

    Usage :

    >>> opportunities_client = Opportunities()
    >>> # Get rights
    >>> opportunities_client.get_tab(5, 'rights')
    >>> # Get all opportunities
    >>> opportunities_client.all()
    >>> # Get an opportunity
    >>> opportunities_client.get(5)
    >>> # Create an opportunity
    >>> data = {...}  # See BoondManager documentation
    >>> opportunities_client.post(data=data)
    >>> # Update an opportunity
    >>> data = {...}  # See BoondManager documentation
    >>> opportunities_client.put(5, data=data)
    >>> # Delete an opportunity
    >>> opportunities_client.delete(5)
    >>> # Get default values
    >>> opportunities_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/opportunities'
    single_uri = '/opportunities/{}'
    tabs = ['rights', 'informations', 'attached-flags', 'simulation', 'positionings', 'actions', 'projects',
            'download', 'tasks']
