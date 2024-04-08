#!/usr/bin/env python3

import yaml 
import os
import sys

remote_operator_yaml_path = sys.argv[1]
group_name = sys.argv[2]
keys_dir = sys.argv[3]

# Define the path to the template operator YAML file
template_operator_yaml_path = os.path.join('..', 'data', 'tmp', group_name, 'template-operator.yaml')

remote_operator_yaml, template_operator_yaml = None, None
# Load the remote operator YAML file
with open(remote_operator_yaml_path, 'r') as f:
    remote_operator_yaml = yaml.safe_load(f)
# Load the template operator YAML file
with open(template_operator_yaml_path, 'r') as f:
    template_operator_yaml = yaml.safe_load(f)

# Update the remote operator YAML file with the template operator YAML file
for key in template_operator_yaml:
    if key in remote_operator_yaml: 
        if '~' in str(template_operator_yaml[key]):
            # Replace the '~' character with the keys directory path (.eigenlayer folder path)
            remote_operator_yaml[key] = template_operator_yaml[key].replace('~', keys_dir)
            continue
        remote_operator_yaml[key] = template_operator_yaml[key]

# Write the updated remote operator YAML file
with open(remote_operator_yaml_path, 'w') as f:
    yaml.dump(remote_operator_yaml, f, indent=4)

print('Updated operator.yaml file with template operator.yaml file')
print('operator.yaml file path:', remote_operator_yaml_path)
print('operator.yaml file content:')
print(yaml.dump(remote_operator_yaml, indent=4))