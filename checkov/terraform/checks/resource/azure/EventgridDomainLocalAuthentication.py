from typing import Any

from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class EventgridDomainLocalAuthentication(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure that Azure Event Grid Domain local Authentication is disabled"
        id = "CKV_AZURE_195"
        supported_resources = ("azurerm_eventgrid_domain",)
        categories = (CheckCategories.IAM,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "local_auth_enabled"

    def get_expected_value(self) -> Any:
        return False


check = EventgridDomainLocalAuthentication()
