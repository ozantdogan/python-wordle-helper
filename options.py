OPTIONS = {
    "wildcard": ".",
    "non_existing_letter": "-",
    "languages": ["en", "tr"],
    "exit_input": "0"
}

nel = OPTIONS["non_existing_letter"]
languages = " | ".join(OPTIONS["languages"])
exit_input = OPTIONS["exit_input"]
wildcard = OPTIONS["wildcard"]