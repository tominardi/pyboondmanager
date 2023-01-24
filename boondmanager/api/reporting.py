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


class ReportingProductionPlans(BaseClient):
    """Search production plans reporting

    Usage :

    >>> reporting_production_plans_client = ReportingProductionPlans()
    >>> # Get all production plans
    >>> reporting_production_plans_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/reporting-production-plans'


class ReportingSynthesis(BaseClient):
    """Search synthesis reporting

    Usage :

    >>> reporting_synthesis_client = ReportingSynthesis()
    >>> # Get all synthesis
    >>> reporting_synthesis_client.all()"""
    allowed_methods = ['GET']
    list_uri = '/reporting-synthesis'


class ReportingCompanies(BaseClient):
    """Search companies reporting

    Usage :

    >>> reporting_companies_client = ReportingCompanies()
    >>> # Get all companies
    >>> reporting_companies_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/reporting-companies'


class ReportingProjects(BaseClient):
    """Search projects reporting

    Usage :

    >>> reporting_projects_client = ReportingProjects()
    >>> # Get all projects
    >>> reporting_projects_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/reporting-projects'


class ReportingResources(BaseClient):
    """Search resources reporting

    Usage :

    >>> reporting_resources_client = ReportingResources()
    >>> # Get all resources
    >>> reporting_resources_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/reporting-resources'
