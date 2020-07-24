[![Build Status](https://travis-ci.org/cmsirbu/codelint.svg?branch=master)](https://travis-ci.org/cmsirbu/codelint)

# Code Linting & Formatting Showcase

Try linting `example.py` with `pylint`, `pylama` and reformat it with `black`.

```
pip install pylint pylama black
pylint example.py
pylama example.py
black --check --diff example.py
```

For YAML, first lint `playbook.yml` with `yamllint`.

```
yamllint playbook.yml
playbook.yml
  1:1       error    too many blank lines (1 > 0)  (empty-lines)
  2:3       warning  comment not indented like content  (comments-indentation)
  3:1       warning  missing document start "---"  (document-start)
  3:81      error    line too long (101 > 80 characters)  (line-length)
  8:20      error    too many spaces before colon  (colons)
  13:7      error    duplication of key "ios" in mapping  (key-duplicates)
```

Now, fix the duplicate key error on line 13 in `playbook.yml` and run `ansible-lint`. Note the custom rule (in the `custom_rules` folder) that checks whether task names are written in all uppercase.

```
ansible-lint -Rr custom_rules playbook.yml
[289] All task names should be capitalized
playbook.yml:19
Task/Handler: Task 1 - ensure snmp commands exist on ios and vmx devices

[502] All tasks should be named
playbook.yml:23
Task/Handler: cli_config msg=A task without a name, so lazy! __line__=23 __file__=playbook.yml
```
