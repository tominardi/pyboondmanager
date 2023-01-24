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


class BusinessUnits(DefaultEndpointMixin, BaseClient):
    """Search, create and manage business units

    Usage :

    >>> business_units_client = BusinessUnits()
    >>> # Get all business units
    >>> business_units_client.all()
    >>> # Get a business unit
    >>> business_units_client.get(5)
    >>> # Create a business unit
    >>> data = {...}  # See BoondManager documentation
    >>> business_units_client.post(data=data)
    >>> # Update a business unit
    >>> data = {...}  # See BoondManager documentation
    >>> business_units_client.put(5, data=data)
    >>> # Delete a business unit
    >>> business_units_client.delete(5)
    >>> # Get default values
    >>> business_units_client.get_default()"""
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/business-units'
    single_uri = '/business-units/{}'
