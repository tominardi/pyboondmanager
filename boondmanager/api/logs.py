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


class Logs(BaseClient):
    """Get logs

    Usage :

    >>> logs_client = Logs()
    >>> # Get all logs
    >>> logs_client.all()
    >>> # Get a log
    >>> logs_client.get(5)"""
    allowed_methods = ['GET']
    list_uri = '/logs'
    single_uri = '/logs/{}'
