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
from boondmanager.auth import decode_boondmanager_payload

"""
Test the authentication helper functions
"""


class TestAuthModule:
    def test_decode_boondmanager_payload(self):
        """
        Test the decode_boondmanager_payload() function
        """
        signed_request = 'ZTQzZmE5ODhhYjY0MjJmZTVhMDNjN2MyMTUwYjNjM2ZiYmZjMDM0OGRlNmYwN2JlN2Y1N2Y0ZDRjYzRlZjg5Yw.eyJ1c2VyVG9rZW4iOiJ0b2tlbjEiLCJjbGllbnRUb2tlbiI6InRva2VuMiIsInRpbWUiOjE1Mjg1MzUyNDksIm1vZGUiOiJub3JtYWwifQ'  # pylint: disable=line-too-long
        assert decode_boondmanager_payload(signed_request, 'AZERTY') is not False
