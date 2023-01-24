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


class Inactivities(DefaultEndpointMixin, BaseClient):
    """Create and manage inactivities

    Tabs :

    - rights : get rights of the current user

    Usage :

    >>> inactivities_client = Inactivities()
    >>> # Get rights
    >>> inactivities_client.get_tab(5, 'rights')
    >>> # Get all inactivities
    >>> inactivities_client.all()
    >>> # Get an inactivity
    >>> inactivities_client.get(5)
    >>> # Create an inactivity
    >>> data = {...}  # See BoondManager documentation
    >>> inactivities_client.post(data=data)
    >>> # Update an inactivity
    >>> data = {...}  # See BoondManager documentation
    >>> inactivities_client.put(5, data=data)
    >>> # Delete an inactivity
    >>> inactivities_client.delete(5)
    >>> # Get default values
    >>> inactivities_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/inactivities'
    single_uri = '/inactivities/{}'
    tabs = ['rights']
