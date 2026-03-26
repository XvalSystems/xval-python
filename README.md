# Xval SDK

Xval is the Official SDK tool for interacting with [Xval](https://xval.io) via python. 

See the [GitHub repo](https://github.com/XvalSystems/xval-sdk) and [Xval's website](https://xval.io)


## Installation

Currently Xval only supports Windows.

Install with pip via:

```bash
pip install xval
```

## Usage

```python
import xval

# Run a model 
xval.run(
    xact_path = "path/to/my_file.xact", # Required
    current_working_directory = "C:/path/to/my_inputs/", # default process cwd
    audit = True, # default False
    hardcode = ["t_name_to_hc1", "t_name_to_hc2" ], # default None
    timestamp = True, # default False
    write_all_vtables = True, # default False
    write_all_inputs = True, # default False
    out_name = "my_alternate_out_name", # default 'my_file'
    out_dir = "my_alternate_out_dir", # default process cwd
    out_ft = "csv", # default 'xlsx', other option: 'term' for terminal
)

# Create an example model locally
xval.template(
   name = "fda_stat_ag33", # Required
   path = "path/where/you/want/template", # default is "./{name}"
)

# List available templates
print(xval.TEMPLATE_LIST)
# fda_stat_ag33
# ...more templates...

# See version 
print(xval.VERSION)
``` 
