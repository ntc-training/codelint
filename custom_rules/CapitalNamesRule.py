from ansiblelint import AnsibleLintRule


class CapitalNamesRule(AnsibleLintRule):
    id = "289"
    shortdesc = "All task names should be capitalized"
    description = "Using all uppercase names creates uniformity and improves readability"
    severity = "LOW"
    tags = ["formatting", "readability"]
    version_added = "v4.0.0"

    def matchtask(self, file, task):
        if task.get("name"):
            return task.get("name") != task.get("name").upper()
