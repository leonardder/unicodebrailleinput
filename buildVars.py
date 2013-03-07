# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name
	"addon-name" : "unicodeBrailleInput",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Unicode Braille Input"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("""Shows a text field to type numeric braille (e.g. 1345-1236-145-1) then convert it into unicode braille characters.
Shortcut: NVDA+Ctrl+u"""),
	# version
	"addon-version" : "1.01",
	# Author(s)
	"addon-author" : "Mesar Hameed <mhameed@src.gnome.org>, Patrick ZAJDA <patrick@zajda.fr>",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org/"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "unicodeBrailleInput", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

