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


class Flags(BaseClient):
    """Search, create and manage flags

    Usage :

    >>> flags_client = Flags()
    >>> # Get all flags
    >>> flags_client.all()
    >>> # Get a flag
    >>> flags_client.get(5)
    >>> # Create a flag
    >>> data = {...}  # See BoondManager documentation
    >>> flags_client.post(data=data)
    >>> # Update a flag
    >>> data = {...}  # See BoondManager documentation
    >>> flags_client.put(5, data=data)
    >>> # Delete a flag
    >>> flags_client.delete(5)
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    single_uri = '/flags'
    list_uri = '/flags/{}'
