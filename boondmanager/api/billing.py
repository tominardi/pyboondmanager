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


class BillingDeliveriesPurchasesBalance(BaseClient):
    """Search deliveries or purchases with a billing balance

    Usage :

    >>> billing_deliveries_purchases_balance_client = BillingDeliveriesPurchasesBalance()
    >>> # Get all deliveries or purchases with a billing balance
    >>> billing_deliveries_purchases_balance_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/billing-deliveries-purchases-balance'


class BillingMonthlyBalance(BaseClient):
    """Search orders with a monthly billing balance

    Usage :

    >>> billing_monthly_balance_client = BillingMonthlyBalance()
    >>> # Get all orders with a monthly billing balance
    >>> billing_monthly_balance_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/billing-monthly-balance'


class BillingProjectsBalance(BaseClient):
    """Search projects with a billing balance

    Usage :

    >>> billing_projects_balance_client = BillingProjectsBalance()
    >>> # Get all projects with a billing balance
    >>> billing_projects_balance_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/billing-projects-balance'


class BillingSchedulesBalance(BaseClient):
    """Search schedules with a billing balance

    Usage :

    >>> billing_schedules_balance_client = BillingSchedulesBalance()
    >>> # Get all schedules with a billing balance
    >>> billing_schedules_balance_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/billing-schedules-balance'
