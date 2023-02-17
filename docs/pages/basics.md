# Quickstart

## Authentication

As mentioned in official BoondManager documentation, there are three different ways to authenticate to Boondmanager.

If provided, they are used in this order :

### Basic auth

Basic HTTP authentication, username / password, given in a dictionary.

Example :

```python
from boondmanager import BoondmanagerClient

client = BoondmanagerClient(basic_auth={'user':'{username}', 'password': '{password}'})
```

### X-Jwt-Client-BoondManager

Json web token, passed in headers.

You'll need the following informations :

* The user's token of a BoondManager's account found on user interface > settings > security
* The client's token found on client's administrator interface > developer space > API / Sandbox
* The client's key found on client's administrator interface > developer space > API / Sandbox

The `boondmanager.auth.get_jwt` helper can be used to generate the correct jwt.

Example :

```python
from boondmanager import BoondmanagerClient
from boondmanager.auth import get_jwt

USER_TOKEN = 'token1'
CLIENT_TOKEN = 'token2'
CLIENT_KEY = 'secret'

jwt = get_jwt(USER_TOKEN, CLIENT_TOKEN, CLIENT_KEY)

client = BoondmanagerClient(jwt_client=jwt)
```


### X-Jwt-App-BoondManager

Same as JWT Client, but use the token of an app instead of a user.

Please read the [official documentation](https://support.boondmanager.com/hc/fr/articles/360027681152-Quick-start-Guides) to understand how it works.

You'll need the following information :

* The user's token of a BoondManager's account found on user interface > settings > security
* The app's token sended by BoondManager during the installation of the app
* The app's key found on client's administrator interface > apps > your app

The `boondmanager.auth.get_jwt` helper can be used to generate the correct jwt.

Example :

```python
from boondmanager import BoondmanagerClient
from boondmanager.auth import get_jwt

USER_TOKEN = 'token1'
APP_TOKEN = 'token2'
APP_KEY = 'secret'

jwt = get_jwt(USER_TOKEN, APP_TOKEN, APP_KEY)

client = BoondmanagerClient(jwt_app=jwt)
```


## Basic usage

```python
from boondmanager import BoondmanagerClient

client = BoondmanagerClient(basic_auth={'user':'{username}', 'password': '{password}'})
resources = client.resources.all()  # Search for all resources without filter
print(resources[0].attributes.firstName)  # > Daniel
# We also can get the included or the meta, directly on the client
print(client.resources.included[1])  # > agency 1
print(client.resources.meta.get('totals'))  # > {'rows': 25}
candidate = client.candidates.get_tab(35, 'information')  # get information tab for a specific candidate
print(candidate.attributes.firstName)  # > Tony
```

You can use specific client classes standalone.

```python
from boondmanager.api import Resources

resources_client = Resources(basic_auth={'user':'{username}', 'password': '{password}'})
resources = resources_client.all()  # Search for all resources without filter
print(resources[0].attributes.firstName)  # > Daniel
resource = resources_client.get_tab(resources[0].id, 'information')  # get information tab for a specific resource
print(resource.attributes.firstName)  # > Daniel
```
