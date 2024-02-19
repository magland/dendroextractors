import toml

# Read the version from pyproject.toml
with open("pyproject.toml", "r") as f:
    pyproject_toml = toml.load(f)
    version = pyproject_toml['tool']['poetry']['version']

# Write the version to _version.py
with open("dendroextractors/_version.py", "w") as f:
    f.write(f'__version__ = "{version}"\n')
