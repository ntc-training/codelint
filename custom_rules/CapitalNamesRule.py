from ansiblelint.rules import AnsibleLintRule


class CapitalNamesRule(AnsibleLintRule):
    id = "CUSTOMRULE001"
    shortdesc = "All task names should be capitalized"
    description = (
        "Using all uppercase names creates uniformity and improves readability"
    )
    severity = "HIGH"
    tags = ["formatting", "readability"]

    def matchtask(self, task, file):
        if task.get("name") is not None:
            return task.get("name") != task.get("name").upper()
