#!/usr/bin/env python3
import json
import os

test_local= os.environ.get("RUN_LOCAL", None)

local_root_directory = "elasticsearch/config/"
root_directory = "/home/es-config/"

if test_local:
    root_directory = local_root_directory

template_output_path = f"{root_directory}es-stack-output.json"
tokenized_conf_file_path = f"{root_directory}/tokenized_default.conf"
output_path = f"{root_directory}/default.conf" #this is the final resting place of the file, we will create an intermin file to copy"/etc/nginx/conf.d/default.conf"


with open(template_output_path) as tmplt_output, open(tokenized_conf_file_path) as tk_conf_file:
    template_output_lst = json.load(tmplt_output)
    tk_conf_str = tk_conf_file.read()
    #list/dict comprehension
    kvp_stack_output = {output_dict["OutputKey"]:output_dict["OutputValue"] for (output_dict) in template_output_lst}
    print(kvp_stack_output)
    for k, v in kvp_stack_output.items():
        tk_conf_str = tk_conf_str.replace(f"[${k}]",v)

with open(output_path, 'w') as output:
    output.write(tk_conf_str)