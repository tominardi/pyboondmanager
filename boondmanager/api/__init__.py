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

# Description: Boondmanager API client
import importlib

from boondmanager.utils import from_camel_case_to_snake_case

from .absences import Absences
from .absences_reports import AbsencesReports
from .accounts import Accounts
from .actions import Actions, ActionsTemplates
from .administrator import Administrator, AdministratorLogo
from .advantages import Advantages
from .agencies import Agencies
from .application import (
    ApplicationAssignments, ApplicationBackupDictionary, ApplicationCurrentUser, ApplicationDictionary,
    ApplicationDownloadDictionary, ApplicationDumpDatabase, ApplicationFlags, ApplicationPerimeters,
    ApplicationReadDatabase, ApplicationRestoreDictionary, ApplicationSettings, ApplicationStatus,
    ApplicationWeekendAndBankHolidays
)
from .attached_flags import AttachedFlags
from .billing import (BillingDeliveriesPurchasesBalance, BillingMonthlyBalance, BillingProjectsBalance,
                      BillingSchedulesBalance)
from .business_units import BusinessUnits
from .calendars import Calendars
from .candidates import Candidates
from .charts import Charts
from .companies import Companies
from .contacts import Contacts
from .contracts import Contracts, BoondmanagerContracts
from .dashboard import Dashboard, DashboardSettings
from .deliveries import Deliveries, DeliveriesGroupments
from .devices import Devices
from .documents import Documents, DocumentsViewer
from .esignature import Esignature
from .expenses import Expenses, ExpensesReports
from .flags import Flags
from .forms import Forms, FormsTemplates
from .groupments import Groupments
from .imports import ImportActions, ImportCandidates, ImportContacts, ImportOpportunities, ImportResources
from .inactivities import Inactivities
from .invoices import Invoices
from .logs import Logs
from .marketplace import Marketplace
from .opportunities import Opportunities
from .orders import Orders
from .payments import Payments
from .poles import Poles
from .positionings import Positionings
from .products import Products
from .projects import Projects
from .purchases import Purchases
from .reporting import (ReportingCompanies, ReportingProductionPlans, ReportingProjects, ReportingResources,
                        ReportingSynthesis)
from .roles import Roles, RolesTemplates
from .resources import Resources
from .savedsearches import SavedSearches
from .sandbox import Sandbox, SandboxConnect
from .share import Share
from .subscription import Subscription
from .signatures import Signatures
from .targets import Targets
from .thread import Threads
from .times import Times
from .times_reports import TimesReports
from .todolists import Todolists
from .validations import Validations
from .vendor import Vendor, VendorLogo
from .webhooks import Webhooks
from .workplaces_times import WorkplacesTimes


class BoondmanagerClient():
    def __init__(self, basic_auth=None, jwt_app=None, jwt_client=None, domain=None):
        base = importlib.import_module('boondmanager.api.base')
        for cls in base.BaseClient.__subclasses__():
            self.__setattr__(from_camel_case_to_snake_case(cls.__name__), cls(
                basic_auth=basic_auth, jwt_app=jwt_app, jwt_client=jwt_client, domain=domain))
