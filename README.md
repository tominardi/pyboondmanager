# BoondManager Python connector

![workflow](https://github.com/tominardi/pyboondmanager/actions/workflows/python-package.yml/badge.svg)

This Python connector is not an officially supported connector by BoondManager. It has been developed by a third-party and it is not officially endorsed or supported by the BoondManager team.

BoondManager is an ERP for consulting and IT services companies.

This python connector allow you to use the BoondManager API for your custom developments.

If you encounter any issues or have questions about this connector, please reach out to the developer or community for support.

```python
from boondmanager.api import BoondmanagerClient

auth = {'user': 'YOUR_USER', 'password': 'YOUR_PASSWORD'}
client = BoondmanagerClient(basic_auth=auth)
projects = client.projects.all()
```

## Prerequisite

* Python >= 3.8

## Installation

```bash
pip install pyboondmanager
```

## Contribute

### Installation

After cloning this repository and create a virtualenv, install the dependencies :

```bash
pip install -r requirements/dev.txt
```

Then, generate the documentation :

```
cd docs
make html
open _build/html/index.html
```

The next steps are on it !

## Links

* [Documentation] (WIP)
* Visit [Boondmanager website](https://www.boondmanager.com/en/) for more informations.
* [Boondmanager Support and documentations](https://support.boondmanager.com)
