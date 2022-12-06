# docs-automations-confluence

## Intro

This is an example to generate automated documentation of a python project based on sphinx and the following extension:

* sphinx.ext.napoleon
* sphinx.ext.autodoc
* autoapi.extension
* autodocsumm
* sphinx_copybutton
* myst_parser
* sphinxcontrib.confluencebuilder

The entire created documentation is published on confluence using sphinxcontrib.confluencebuilder

## Set the docs

```
mkdir docs
```

```
cd docs
```

```
sphinx-quickstart --quiet --project="Default project" --author="Davide Airaghi" --language="en"
```

```
make html (on Unix)
.\make.bat html (on Windows PowerShell)
```

```
make confluence
```
