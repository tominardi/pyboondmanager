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


class Esignature(BaseClient):
    """POST esignature

    Single URI is only used to cancel esignature

    Single URI can be only use with cancel tab

    Tabs :

    - cancel : POST cancel

    Usage :

    >>> esignature_client = Esignature()
    >>> # Make a signature request
    >>> data = {...}  # See BoondManager documentation
    >>> esignature_client.post(data=data)
    >>> # Cancel a signature request
    >>> esignature_client.post_tab(5, 'cancel')"""
    allowed_methods = ['POST']
    list_uri = '/esignature/esignatur'
    single_uri = '/esignature/esignatur/{}'
    tabs = ['cancel']
