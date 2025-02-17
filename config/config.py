import os

os.environ["PYDEVD_CONTAINER_RANDOM_ACCESS_MAX_ITEMS"] = "10000"

APP_SETTINGS = {
    "wildcard": ".",
    "non_existing_letter": "-",
    "languages": ["en", "tr", "fr"],
    "exit_input": "0"
}

nel = APP_SETTINGS["non_existing_letter"]
languages = " | ".join(APP_SETTINGS["languages"])
exit_input = APP_SETTINGS["exit_input"]
wildcard = APP_SETTINGS["wildcard"]