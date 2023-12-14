# Scripts set for data processing and analysis in MMM projects

```
$ poetry shell

$ poetry build

$ poetry install

# or
$ poetry run python -m pip install .

```

Inside files import 
```python
import mmm_tools

```

Workflow is seen as Jupyter Notebook where mmm_tools is imported.
Notebook contains main stages of analysis with some boilerplate code, 
that could (and should) be adopted to specific data set

mmm_tools is a set of function, which are used insife main workflow notebook.

