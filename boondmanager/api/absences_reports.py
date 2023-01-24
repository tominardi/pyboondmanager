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


class AbsencesReports(DefaultEndpointMixin, BaseClient):
    """
    Search, create and manage requests of absences

    Tabs :

    - rights : get rights of the current user
    - download : download the report
    - validate : validate the report
    - unvalidate : unvalidate the report
    - reject : reject the report

    Usage :

    >>> absences_reports_client = AbsencesReports()
    >>> # Get rights
    >>> absences_reports_client.get_tab(5, 'rights')
    >>> # Get all reports
    >>> absences_reports_client.all()
    >>> # Get a report
    >>> absences_reports_client.get(5)
    >>> # Validate the report
    >>> absences_reports_client.post_tab(5, 'validate')
    >>> # Unvalidate the report
    >>> absences_reports_client.post_tab(5, 'unvalidate')
    >>> # Reject the report
    >>> absences_reports_client.post_tab(5, 'reject')
    >>> # Get default values
    >>> absences_reports_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/absences-reports'
    single_uri = '/absences-reports/{}'
    tabs = ['rights', 'download', 'validate', 'unvalidate', 'reject']
