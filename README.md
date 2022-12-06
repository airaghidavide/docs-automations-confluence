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


## Publish on confluence

* create an account on confluence
* create an API token [https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)
* install pip sphinxcontrib-confluencebuilder
* configure it
```
confluence_publish = True
confluence_space_key = xxxxxx
confluence_parent_page = xxxxxx
confluence_server_url = xxxxxx
confluence_server_user = xxxxxx
confluence_server_pass = xxxxxx
confluence_disable_ssl_validation= True
```

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
<img width="1013" alt="Screenshot 2022-12-06 at 08 52 08" src="https://user-images.githubusercontent.com/60407477/205853095-3f5767e7-7654-4717-b400-b1f3b6a8e557.png">



