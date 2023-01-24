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


class Expenses(BaseClient):
    """Get expenses"""
    allowed_methods = ['GET']
    list_uri = '/expenses'


class ExpensesReports(DefaultEndpointMixin, BaseClient):
    """Search, create and manage expenses reports

    Tabs:

    - rights : get rights of the current user
    - download : get download
    - pay : Pay an expenses report
    - validate : validate a report
    - unvalidate : unvalidate a report
    - reject : reject a report
    - certification : Manage expenses certification

    Usage:

    >>> expenses_reports_client = ExpensesReports()
    >>> # Get rights
    >>> expenses_reports_client.get_tab(5, 'rights')
    >>> # Get all reports
    >>> expenses_reports_client.all()
    >>> # Get a report
    >>> expenses_reports_client.get(5)
    >>> # Validate the report
    >>> expenses_reports_client.post_tab(5, 'validate')
    >>> # Unvalidate the report
    >>> expenses_reports_client.post_tab(5, 'unvalidate')
    >>> # Reject the report
    >>> expenses_reports_client.post_tab(5, 'reject')
    >>> # Create a report
    >>> data = {...}  # See BoondManager documentation
    >>> expenses_reports_client.post(data=data)
    >>> # Update a report
    >>> data = {...}  # See BoondManager documentation
    >>> expenses_reports_client.put(5, data=data)
    >>> # Delete a report
    >>> expenses_reports_client.delete(5)
    >>> # Get default values
    >>> expenses_reports_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/expenses-reports'
    single_uri = '/expenses-reports/{}'
    tabs = ['rights', 'download', 'pay', 'validate', 'unvalidate', 'reject', 'certification']
