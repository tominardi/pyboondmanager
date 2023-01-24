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


class Vendor(BaseClient):
    """Manage vendor's profile

    Usage :

    >>> vendor_client = Vendor()
    >>> # Get vendor's profile
    >>> vendor_client.get()
    >>> # Update vendor's profile
    >>> data = {...}  # See BoondManager documentation
    >>> vendor_client.put(data=data)"""
    allowed_methods = ['GET', 'PUT']
    list_uri = '/vendor'


class VendorLogo(BaseClient):
    """Manage vendor's logo

    Usage :

    >>> vendor_logo_client = VendorLogo()
    >>> # Get vendor's logo
    >>> vendor_logo_client.get()
    >>> # Update vendor's logo
    >>> data = {...}  # See BoondManager documentation
    >>> vendor_logo_client.put(data=data)
    >>> # Delete vendor's logo
    >>> vendor_logo_client.delete()
    """
    allowed_methods = ['DELETE', 'PUT']
    list_uri = '/vendor/logo'
