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
import re


"""
Utils
"""


def from_camel_case_to_snake_case(name):
    """Convert CamelCase to snake_case

    :param name: CamelCase string. If None, return None"""
    if not name:
        return name
    sub1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', sub1).lower()


class JsonAPIData:
    """
    json:api classes

    based on https://jsonapi.org/
    """
    type = None
    id = None
    attributes = None
    relationships = None
    included = None
    payload = None

    def __init__(self, payload=None):
        if payload:
            self.payload = payload
            self.type = payload.get('type')
            self.id = payload.get('id')  # pylint: disable=invalid-name
            self.attributes = payload.get('attributes', {})
            self.relationships = payload.get('relationships', {})

    def __repr__(self):
        return f'<{self.type} {self.id}>'
