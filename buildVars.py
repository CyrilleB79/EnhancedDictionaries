# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
import os.path
def _(x): return x


# Add-on information variables
addon_info = {
    # for previously unpublished addons, please follow the community guidelines at:
    # https://bitbucket.org/nvdaaddonteam/todo/raw/master/guidelines.txt
    # add-on Name, internal for nvda
    "addon_name": "EnhancedDictionaries",
    # Add-on summary, usually the user visible name of the addon.
    # Translators: Summary for this add-on to be shown on installation and add-on information.
    "addon_summary": _("Enhanced dictionaries processing for NVDA"),
    # Add-on description
    # Translators: Long description to be shown for this add-on on add-on information from add-ons manager
    "addon_description": _("""This addon introduces better dictionaries handling for NVDA.
It is now possible to use profile specific dictionaries, which eenables better productivity by allowing you to use different dictionaries for different applications and scenarius."""),
    # version
    "addon_version": "1.4.0",
    # Author(s)
    "addon_author": u"Marlon Brandão de Sousa <marlon.bsousa@gmail.com>",
    # URL for the add-on documentation support
    "addon_url": "https://github.com/marlon-sousa/EnhancedDictionaries",
    # Documentation file name
    "addon_docFileName": "readme.html",
    # Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
    "addon_minimumNVDAVersion": "2022.1",
    # Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
    "addon_lastTestedNVDAVersion": "2023.1",
    # Add-on update channel (default is None, denoting stable releases, and for development releases, use "dev"; do not change unless you know what you are doing)
    "addon_updateChannel": None,
}


# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join(
    "addon", "globalPlugins", "EnhancedDictionaries", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = [os.path.join("addon", "doc", "*", "contributing*.*")]
