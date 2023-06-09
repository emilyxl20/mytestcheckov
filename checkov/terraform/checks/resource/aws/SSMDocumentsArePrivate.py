

from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_negative_value_check import BaseResourceNegativeValueCheck


class SSMDocumentsArePrivate(BaseResourceNegativeValueCheck):
    def __init__(self):
        """
        NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21),
        NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16),
        NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4),
        NIST.800-53.r5 SC-7(9)
        """
        name = "Ensure SSM documents are not Public"
        id = "CKV_AWS_303"
        supported_resources = ['aws_ssm_document']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "permissions/[0]/account_ids"

    def get_forbidden_values(self) -> str:
        return "All"


check = SSMDocumentsArePrivate()
