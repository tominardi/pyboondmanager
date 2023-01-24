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
from boondmanager.utils import (from_camel_case_to_snake_case, JsonAPIData)


class TestUtilsModule:
    def test_from_camel_case_to_snake_case(self):
        """
        Test the from_camel_case_to_snake_case() function
        """
        assert from_camel_case_to_snake_case('testCamelCase') == 'test_camel_case'

    def test_from_camel_case_to_snake_case_with_empty_string(self):
        """
        Test the from_camel_case_to_snake_case() function with an empty string
        """
        assert from_camel_case_to_snake_case('') == ''

    def test_from_camel_case_to_snake_case_with_none(self):
        """
        Test the from_camel_case_to_snake_case() function with None
        """
        assert from_camel_case_to_snake_case(None) is None

    def test_from_camel_case_to_snake_case_with_number(self):
        """
        Test the from_camel_case_to_snake_case() function with a number
        """
        assert from_camel_case_to_snake_case('123') == '123'

    def test_from_camel_case_to_snake_case_with_number_and_string(self):
        """
        Test the from_camel_case_to_snake_case() function with a number and a string
        """
        assert from_camel_case_to_snake_case('123test') == '123test'

    def test_json_api_data_repr(self):
        """
        Test the JsonAPIData class
        """
        payload = {
            'type': 'Test',
            'id': '1',
        }
        json_api_data = JsonAPIData(payload)
        assert repr(json_api_data) == '<Test 1>'
