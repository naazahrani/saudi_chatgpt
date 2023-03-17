import re

def classify_intent_extract_entities_parser(response):
    
    pattern = r"Intent:\s*(.*)"
    intent_match = re.search(pattern, response)
    intent = intent_match.group(1)
    
    pattern = r"- (\w+):\s*(.+)"

    # use regular expression to extract entity lines
    entity_lines = re.findall(pattern, response)

    # create a dictionary to store entities
    entities = {}

    # loop through entity lines and add them to the dictionary
    for entity_key, entity_value in entity_lines:
        entities[entity_key] = entity_value
    
    return intent, entities

def preprocess():
    """
    """

def postprocess():
    """
    
    """