from akinator.data import Data

import importlib.resources as pkg_resources

from . import akinator  # relative-import the *package* containing the templates

template = pkg_resources.read_text("akinator", "akinator.csv")

akinator = Data()
df = akinator.get_data()
print(df)
print(template)
