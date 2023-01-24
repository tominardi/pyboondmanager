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


class Roles(DefaultEndpointMixin, BaseClient):
    """Search, create and manage roles

    Usage :

    >>> roles_client = Roles()
    >>> # Get all roles
    >>> roles_client.all()
    >>> # Get a role
    >>> roles_client.get(5)
    >>> # Create a role
    >>> data = {...}  # See BoondManager documentation
    >>> roles_client.post(data=data)
    >>> # Update a role
    >>> data = {...}  # See BoondManager documentation
    >>> roles_client.put(5, data=data)
    >>> # Delete a role
    >>> roles_client.delete(5)
    >>> # Get default values
    >>> roles_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/roles'
    single_uri = '/roles/{}'


class RolesTemplates(BaseClient):
    """Search, create and manage roles templates

    Usage :

    >>> roles_templates_client = RolesTemplates()
    >>> # Get all roles templates
    >>> roles_templates_client.all()
    >>> # Get a role template
    >>> roles_templates_client.get(5)
    >>> # Create a role template
    >>> data = {...}  # See BoondManager documentation
    >>> roles_templates_client.post(data=data)
    >>> # Update a role template
    >>> data = {...}  # See BoondManager documentation
    >>> roles_templates_client.put(5, data=data)
    >>> # Delete a role template
    >>> roles_templates_client.delete(5)
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/roles/templates'
    single_uri = '/roles/templates/{}'
