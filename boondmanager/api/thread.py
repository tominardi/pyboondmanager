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


class Threads(DefaultEndpointMixin, BaseClient):
    """Create, search and manage threads

    Usage :

    >>> threads_client = Threads()
    >>> # Get all threads
    >>> threads_client.all()
    >>> # Get a thread
    >>> threads_client.get(5)
    >>> # Create a thread
    >>> data = {...}  # See BoondManager documentation
    >>> threads_client.post(data=data)
    >>> # Update a thread
    >>> data = {...}  # See BoondManager documentation
    >>> threads_client.put(5, data=data)
    >>> # Delete a thread
    >>> threads_client.delete(5)
    >>> # Get default values
    >>> threads_client.get_default()"""
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/threads'
    single_uri = '/threads/{}'
