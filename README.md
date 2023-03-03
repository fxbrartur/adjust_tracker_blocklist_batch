# Adjust trackers Blocklist Automation

This is an automation I created to extract tracker tokens from a payload, and generate requests for the Block List Api from Adjust GmbH.

Adjust is a MMP and offers an endpoint to blocklist trackers from an App. Doc here: https://help.adjust.com/en/article/blocklist-api

This automation resolves the extraction of the tokens on tokens_payload (any client or internal person can have it) and make requests to the API.
