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


class Tasks(BaseClient):
    """Manage tasks

    Usage :

    >>> tasks_client = Tasks()
    >>> # Update a task
    >>> data = {...}  # See BoondManager documentation
    >>> tasks_client.put(5, data=data)
    >>> # Check a task
    >>> params = {...}  # See BoondManager documentation
    >>> tasks_client.post_tab(5, 'check', params=params)
    >>> # Uncheck a task
    >>> params = {...}  # See BoondManager documentation
    >>> tasks_client.post_tab(5, 'uncheck', params=params)"""
    allowed_methods = ['POST', 'PUT']
    single_uri = '/tasks/{}'
    tabs = ['check', 'uncheck']
