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


class Forms(BaseClient):
    """Get and update forms

    Tabs :

    - remind : POST reminder
    - rights : get rights of the current user
    - tasks : get tasks

    Usage :

    >>> forms_client = Forms()
    >>> # Create a form
    >>> data = {...}  # See BoondManager documentation
    >>> form_client.post(data=data)
    >>> # post a reminder on a form
    >>> data = {...}  # See BoondManager documentation
    >>> form_client.post_tab(5, 'remind', data=data)
    >>> # get tasks of a form
    >>> form_client.get_tab(5, 'tasks')
    """
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']
    list_uri = '/forms'
    list_uri = '/forms/{}'
    tabs = ['remind', 'rights', 'tasks']


class FormsTemplates(BaseClient):
    """Get and update forms templates

    Usage :

    >>> forms_templates_client = FormsTemplates()
    >>> # Get all forms templates
    >>> forms_templates_client.all()
    >>> # Get a form template
    >>> forms_templates_client.get(5)
    >>> # Create a form template
    >>> data = {...}  # See BoondManager documentation
    >>> forms_templates_client.post(data=data)
    >>> # Update a form template
    >>> data = {...}  # See BoondManager documentation
    >>> forms_templates_client.put(5, data=data)
    >>> Delete a form template
    >>> forms_templates_client.delete(5)
    """
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']
    list_uri = '/forms/templates'
    list_uri = '/forms/templates/{}'
