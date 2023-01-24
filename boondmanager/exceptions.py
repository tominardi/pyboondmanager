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

"""
BoondManager exception and warning classes.
"""


class NoSingleUrl(Exception):
    """If we try to pass an id to a API resource with no single url"""

    def __init__(self, message="This endpoint doesn't provides single url"):
        self.message = message
        super().__init__(self.message)


class UnknownTab(Exception):
    """If we try to use a tab that doesn't exists"""

    def __init__(self, message='This tab doesn\'t exists'):
        self.message = message
        super().__init__(self.message)


class MethodNotAllowed(Exception):
    """If we try to use a endpoint with a not allowed method"""

    def __init__(self, message='This method is not allowed'):
        self.message = message
        super().__init__(self.message)


class PageNotFoundError(Exception):
    """If BoondManager return a 404"""

    def __init__(self, message='Page not found'):
        self.message = message
        super().__init__(self.message)


class BoondManagerUnprocessableEntity(Exception):
    """Unprocessable Entity"""

    def __init__(self, message='Unprocessable Entity'):
        self.message = message
        super().__init__(self.message)


class BoondManagerForbidden(Exception):
    """When BoondManager return a 403"""

    def __init__(self, message='Forbidden'):
        self.message = message
        super().__init__(self.message)
