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


class ApplicationAssignments(BaseClient):
    """Get the list of assignments availables for updating

    Usage :

    >>> application_assignments_client = ApplicationAssignments()
    >>> # Get all assignments
    >>> application_assignments_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/application/assignments'


class ApplicationCurrentUser(BaseClient):
    """Get current user's data

    Usage :

    >>> application_current_user_client = ApplicationCurrentUser()
    >>> # Get current user's data
    >>> application_current_user_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/application/current-user'


class ApplicationDictionary(BaseClient):
    """Manage the specific translations

    Usage :

    >>> application_dictionary_client = ApplicationDictionary()
    >>> # Get dictionnary
    >>> application_dictionary_client.all()
    >>> # Update dictionnary
    >>> data = {...}  # See BoondManager documentation
    >>> application_dictionary_client.put(data=data)"""
    allowed_methods = ['GET', 'PUT']
    list_uri = '/application/dictionary'


class ApplicationDownloadDictionary(BaseClient):
    """Get the dictionary file

    Usage :

    >>> application_download_dictionary_client = ApplicationDownloadDictionary()
    >>> # Download dictionary file
    >>> application_download_dictionary_client.all()"""
    allowed_methods = ['GET']
    list_uri = 'application/download-dictionary'


class ApplicationBackupDictionary(BaseClient):
    """Backup the dictionary

    Usage :

    >>> application_backup_dictionary_client = ApplicationBackupDictionary()
    >>> # Backup dictionary
    >>> application_backup_dictionary_client.all()"""
    allowed_methods = ['POST']
    list_uri = 'application/backup-dictionary'


class ApplicationRestoreDictionary(BaseClient):
    """Restore the last dictionary backup

    Usage :

    >>> application_restore_dictionary_client = ApplicationRestoreDictionary()
    >>> # Restore dictionary
    >>> data = {...}  # See BoondManager documentation
    >>> application_restore_dictionary_client.put(data=data)"""
    allowed_methods = ['PUT']
    list_uri = 'application/restore-dictionary'


class ApplicationDumpDatabase(BaseClient):
    """Create a database's dump

    Usage :

    >>> application_dump_database_client = ApplicationDumpDatabase()
    >>> # Dump database
    >>> application_dump_database_client.post()"""
    allowed_methods = ['POST']
    list_uri = 'application/dump-database'


class ApplicationFlags(BaseClient):
    """Get the list of flags availables for searching or updating

    Usage :

    >>> application_flags_client = ApplicationFlags()
    >>> # Get all flags
    >>> application_flags_client.all()"""
    allowed_methods = ['GET']
    list_uri = 'application/flags'


class ApplicationPerimeters(BaseClient):
    """Get the list of perimeters availables for searching"""
    allowed_methods = ['GET']
    list_uri = 'application/perimeters'


class ApplicationReadDatabase(BaseClient):
    """Read database thanks to a MySQL query.

    Usage :

    >>> application_read_database_client = ApplicationReadDatabase()
    >>> # Read database
    >>> data = {"query": "..."}  # See BoondManager documentation
    >>> application_read_database_client.post(data=data)"""
    allowed_methods = ['POST']
    list_uri = 'application/read-database'


class ApplicationSettings(BaseClient):
    """Manage the specific settings

    Usage :

    >>> application_settings_client = ApplicationSettings()
    >>> # Get settings
    >>> application_settings_client.all()
    >>> # Update settings
    >>> data = {...}  # See BoondManager documentation
    >>> application_settings_client.put(data=data)
    """
    allowed_methods = ['GET', 'PUT']
    list_uri = '/application/settings'


class ApplicationStatus(BaseClient):
    """Get status

    Usage :

    >>> application_status_client = ApplicationStatus()
    >>> # Get status
    >>> application_status_client.all()
    """
    allowed_methods = ['GET']
    list_uri = 'application/status'


class ApplicationWeekendAndBankHolidays(BaseClient):
    """Get the types of days between 2 dates

    Usage :

    >>> application_weekend_and_bank_holidays_client = ApplicationWeekendAndBankHolidays()
    >>> # Get types of days
    >>> data = {"endDate": "2020-12-31", "startDate": "2020-01-01"}  # See BoondManager documentation
    >>> application_weekend_and_bank_holidays_client.all(data=data)"""
    allowed_methods = ['GET']
    list_uri = 'application/weekendAndBankHolidays'
