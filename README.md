# validate-cnpj

[![pipy](https://img.shields.io/pypi/v/validate_cnpj.svg)](https://pypi.python.org/pypi/validate_cnpj)

Validates Brazilian CNPJ

## Features

- CNPJ Validation with mask
- CNPJ Validation without mask

## Modes of use

```python
#!/usr/bin/python
import validate_cnpj

# Without mask
validate_cnpj.is_valid('40158686000170') # True

# With mask
validate_cnpj.is_valid('40.158.686/0001-70') # True
```

or

```python
#!/usr/bin/python
from validate_cnpj import is_valid

# Without mask
is_valid('11.111.111/0001-11') # False

# With mask
is_valid('11111111000111') # False
```

# Author

[João Filho](https://joaofilho.dev)
[Github](https://github.com/drummerzzz)

# Credits

This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
