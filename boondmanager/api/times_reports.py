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


class TimesReports(DefaultEndpointMixin, BaseClient):
    """Search, create and manage times reports

    Tabs :

    - rights : get rights of the current user
    - download : get download
    - validate : validate
    - unvalidate : unvalidate
    - reject : reject
    - signature : get signature

    Usage :

    >>> times_reports_client = TimesReports()
    >>> # Get rights
    >>> times_reports_client.get_tab(5, 'rights')
    >>> # Get all times reports
    >>> times_reports_client.all()
    >>> # Get a times report
    >>> times_reports_client.get(5)
    >>> # Create a times report
    >>> data = {...}  # See BoondManager documentation
    >>> times_reports_client.post(data=data)
    >>> # Update a times report
    >>> data = {...}  # See BoondManager documentation
    >>> times_reports_client.put(5, data=data)
    >>> # Delete a times report
    >>> times_reports_client.delete(5)
    >>> # Get default values
    >>> times_reports_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/times-reports'
    single_uri = '/times-reports/{}'
    tabs = ['rights', 'download', 'validate', 'unvalidate', 'reject', 'signature']
