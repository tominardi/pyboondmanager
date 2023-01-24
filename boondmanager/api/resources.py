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


class Resources(DefaultEndpointMixin, BaseClient):
    """Search, create and manage resources

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - administrative : get administrative
    - advantages : get advantages
    - technical-data : get technical data
    - actions : get actions
    - positionings : get positionings
    - deliveries-inactivities : get deliveries inactivities
    - projects : get projects
    - times-reports : get times reports
    - expenses-reports : get expenses reports
    - absences-reports : get absences reports
    - absences-accounts : get absences accounts
    - download : get download
    - tasks : get tasks
    - settings/intranet : get settings intranet
    - settings/targets : get settings targets
    - settings/security : get settings security
    - settings/absences-accounts : get settings absences accounts
    - settings/groups : get settings groups
    - settings/reporting : get settings reporting
    - forms : get forms

    Usage :

    >>> resources_client = Resources()
    >>> # Get rights
    >>> resources_client.get_tab(5, 'rights')
    >>> # Get all resources
    >>> resources_client.all()
    >>> # Get a resource
    >>> resources_client.get(5)
    >>> # Get resource informations
    >>> resources_client.get_tab(5, 'information')
    >>> # Create a resource
    >>> data = {...}  # See BoondManager documentation
    >>> resources_client.post(data=data)
    >>> # Update a resource
    >>> data = {...}  # See BoondManager documentation
    >>> resources_client.put(5, data=data)
    >>> # Delete a resource
    >>> resources_client.delete(5)
    >>> # Get default values
    >>> resources_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/resources'
    single_uri = '/resources/{}'
    tabs = ['rights', 'information', 'attached-flags', 'administrative', 'advantages', 'technical-data', 'actions',
            'positionings', 'deliveries-inactivities', 'projects', 'times-reports', 'expenses-reports',
            'absences-reports', 'absences-accounts', 'download', 'tasks', 'settings/intranet', 'settings/targets',
            'settings/security', 'settings/absences-accounts', 'settings/groups', 'settings/reporting', 'forms']
