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
from .base import DefaultEndpointMixin, BaseClient


class Actions(DefaultEndpointMixin, BaseClient):
    """
    Search, create and manage actions

    Tabs :

    - rights : get rights of the current user
    - attached-flags : get attached flags of the current user

    Usage :

    >>> actions_client = Actions()
    >>> # Get rights
    >>> actions_client.get_tab(5, 'rights')
    >>> # Get all actions
    >>> actions_client.all()
    >>> # Get an action
    >>> actions_client.get(5)
    >>> # Create an action
    >>> data = {...}  # See BoondManager documentation
    >>> actions_client.post(data=data)
    >>> # Update an action
    >>> data = {...}  # See BoondManager documentation
    >>> actions_client.put(5, data=data)
    >>> # Get default values
    >>> actions_client.get_default()"""
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/actions'
    single_uri = '/actions/{}'
    tabs = ['rights', 'attached-flags']
    list_uri = '/actions'


class ActionsTemplates(BaseClient):
    """
    Search, create and manage actions templates
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/actions/templates'
    single_uri = '/actions/templates/{}'
