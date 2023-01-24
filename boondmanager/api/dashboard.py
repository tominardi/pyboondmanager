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


class Dashboard(BaseClient):
    """Get dashboard data

    Usage :

    >>> dashboard_client = Dashboard()
    >>> # Get dashboard data
    >>> dashboard_client.get()"""
    allowed_methods = ['GET']
    list_uri = '/dashboard'


class DashboardSettings(BaseClient):
    """Get and update dashboard settings

    Usage :

    >>> dashboard_settings_client = DashboardSettings()
    >>> # Get dashboard settings
    >>> dashboard_settings_client.get()
    >>> # Update dashboard settings
    >>> data = {...}  # See BoondManager documentation
    >>> dashboard_settings_client.put(data=data)"""
    allowed_methods = ['GET', 'PUT']
    list_uri = '/dashboard/settings'
