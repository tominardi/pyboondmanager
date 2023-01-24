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


class Documents(BaseClient):
    """Manage documents

    Usage :

    >>> documents_client = Documents()
    >>> # Create a document
    >>> data = {...}  # See BoondManager documentation
    >>> documents_client.post(data=data)
    >>> # Get all documents
    >>> documents_client.all()
    >>> # Get a document
    >>> documents_client.get(5)
    >>> # Update a document
    >>> data = {...}  # See BoondManager documentation
    >>> documents_client.put(5, data=data)
    >>> # Delete a document
    >>> documents_client.delete(5)"""
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/documents'
    single_uri = '/documents/{}'


class DocumentsViewer(BaseClient):
    """Search documents for viewer's viewer

    Usage :

    >>> documents_viewer_client = DocumentsViewer()
    >>> # Get all documents
    >>> documents_viewer_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/documents/viewer'
