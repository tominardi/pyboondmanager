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


class Agencies(DefaultEndpointMixin, BaseClient):
    """
    Search, create and manage agencies

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - activity-expenses : get activity expenses
    - activity-expenses/logo : get activity expenses logo
    - billing : get billing
    - billing/logo : get billing logo
    - opportunities : get opportunities
    - projects : get projects
    - purchases : get purchases
    - products : get products
    - resources : get resources

    Usage :

    >>> agencies_client = Agencies()
    >>> # Get rights
    >>> agencies_client.get_tab(5, 'rights')
    >>> # Get all agencies
    >>> agencies_client.all()
    >>> # Get an agency
    >>> agencies_client.get(5)
    >>> # Create an agency
    >>> data = {...}  # See BoondManager documentation
    >>> agencies_client.post(data=data)
    >>> # Update an agency
    >>> data = {...}  # See BoondManager documentation
    >>> agencies_client.put(5, data=data)
    >>> # Get default values
    >>> agencies_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/agencies'
    single_uri = '/agencies/{}'
    tabs = ['rights', 'information', 'activity-expenses', 'activity-expenses/logo', 'billing', 'billing/logo',
            'opportunities', 'projects', 'purchases', 'products', 'resources']
