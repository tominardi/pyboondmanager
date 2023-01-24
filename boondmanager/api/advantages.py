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


class Advantages(DefaultEndpointMixin, BaseClient):
    """
    Create and manage advantages

    Tabs :
    - rights : get rights of the current user

    Usage :
    >>> advantages_client = Advantages()
    >>> # Get rights
    >>> advantages_client.get_tab(5, 'rights')
    >>> # Get all advantages
    >>> advantages_client.all()
    >>> # Get an advantage
    >>> advantages_client.get(5)
    >>> # Create an advantage
    >>> data = {...}  # See BoondManager documentation
    >>> advantages_client.post(data=data)
    >>> # Update an advantage
    >>> data = {...}  # See BoondManager documentation
    >>> advantages_client.put(5, data=data)
    >>> # Get default values
    >>> advantages_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/advantages'
    single_uri = '/advantages/{}'
    tabs = ['rights']
