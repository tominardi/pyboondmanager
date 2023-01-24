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


class AttachedFlags(BaseClient):
    """
    Manage attached flags

    Usage :

    >>> attached_flags_client = AttachedFlags()
    >>> # Create an attached flag
    >>> data = {...}  # See BoondManager documentation
    >>> attached_flags_client.post(data=data)
    >>> # Delete an attached flag
    >>> attached_flags_client.delete(5)
    """
    allowed_methods = ['DELETE', 'POST']
    list_uri = '/attached-flags'
