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


class Todolists(BaseClient):
    """Search, create and manage todolists

    Usage :

    >>> todolists_client = Todolists()
    >>> # Get all todolists
    >>> todolists_client.all()
    >>> # Get a todolist
    >>> todolists_client.get(5)
    >>> # Create a todolist
    >>> data = {...}  # See BoondManager documentation
    >>> todolists_client.post(data=data)
    >>> # Update a todolist
    >>> data = {...}  # See BoondManager documentation
    >>> todolists_client.put(5, data=data)
    >>> # Delete a todolist
    >>> todolists_client.delete(5)
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/todolists'
    single_uri = '/todolists/{}'
