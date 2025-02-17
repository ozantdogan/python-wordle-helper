import os

os.environ["PYDEVD_CONTAINER_RANDOM_ACCESS_MAX_ITEMS"] = "10000"

OPTIONS = {
    "wildcard": ".",
    "non_existing_letter": "-",
    "languages": ["en", "tr", "fr"],
    "exit_input": "0"
}

nel = OPTIONS["non_existing_letter"]
languages = " | ".join(OPTIONS["languages"])
exit_input = OPTIONS["exit_input"]
wildcard = OPTIONS["wildcard"]