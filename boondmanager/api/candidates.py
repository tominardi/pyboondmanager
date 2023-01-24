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


class Candidates(DefaultEndpointMixin, BaseClient):
    """Search, create and manage candidates

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - administrative : get administrative
    - technical-data : get technical data
    - actions : get actions
    - positionings : get positionings
    - download : get download
    - tasks : get tasks

    Usage :

    >>> candidates_client = Candidates()
    >>> # Get rights
    >>> candidates_client.get_tab(5, 'rights')
    >>> # Get all candidates
    >>> candidates_client.all()
    >>> # Get a candidate
    >>> candidates_client.get(5)
    >>> # Create a candidate
    >>> data = {...}  # See BoondManager documentation
    >>> candidates_client.post(data=data)
    >>> # Update a candidate
    >>> data = {...}  # See BoondManager documentation
    >>> candidates_client.put(5, data=data)
    >>> # Delete a candidate
    >>> candidates_client.delete(5)
    >>> # Get default values
    >>> candidates_client.get_default()"""
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/candidates'
    single_uri = '/candidates/{}'
    tabs = ['rights', 'information', 'attached-flags', 'administrative', 'technical-data', 'actions', 'positionings',
            'download', 'tasks']
