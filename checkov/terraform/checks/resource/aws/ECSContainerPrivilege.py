from typing import Dict, List, Any

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class ECSContainerPrivilege(BaseResourceCheck):
    def __init__(self) -> None:
        """
        NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7),
        NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6
        ECS containers should run as non-privileged
        """
        name = "Ensure ECS containers should run as non-privileged"
        id = "CKV_AWS_334"
        supported_resources = ("aws_ecs_task_definition",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: Dict[str, List[Any]]) -> CheckResult:
        self.evaluated_keys = ["container_definitions"]
        container_definitions = conf.get("container_definitions")
        if container_definitions and isinstance(container_definitions, list):
            containers = container_definitions[0]
            if containers and isinstance(containers, list):
                for idx, container in enumerate(containers):
                    if isinstance(container, dict) and container.get("privilege"):
                        self.evaluated_keys = [f"container_definitions/[0]/[{idx}]/privilege"]
                        return CheckResult.FAILED
                return CheckResult.PASSED
            elif isinstance(containers, dict):
                # TF plan file case
                for idx, container in enumerate(container_definitions):
                    if isinstance(container, dict) and container.get("privilege"):
                        self.evaluated_keys = [f"container_definitions/[{idx}]/privilege"]
                        return CheckResult.FAILED
                return CheckResult.PASSED

        return CheckResult.UNKNOWN


check = ECSContainerPrivilege()
