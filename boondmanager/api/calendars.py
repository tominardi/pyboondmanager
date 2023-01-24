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


class Calendars(DefaultEndpointMixin, BaseClient):
    """Search and manage calendars

    Tabs :

    - rights : get rights of the current user

    Usage :

    >>> calendars_client = Calendars()
    >>> # Get all calendars
    >>> calendars_client.all()
    >>> # Get a calendar
    >>> calendars_client.get(5)
    >>> # Update a calendar
    >>> data = {...}  # See BoondManager documentation
    >>> calendars_client.put(5, data=data)
    >>> # Get default values
    >>> calendars_client.get_default()"""
    allowed_methods = ['GET', 'PUT']
    list_uri = '/calendars'
    single_uri = '/calendars/{}'
