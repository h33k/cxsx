import yaml


def isCustomizationCard(tags):
    if 'superpageme' in tags:
        return True
    return False

def updateCustomization(title, markup, modified_when):
    with open('docs/_config.yml', 'r') as f:
        config = yaml.safe_load(f)

    config['modified_when'] = modified_when
    config['title'] = title
    config['about'] = markup

    with open('../docs/_config.yml', 'w') as f:
        yaml.safe_dump(config, f)