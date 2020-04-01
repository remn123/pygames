import yaml

def Config(path="config.yaml"):
    
    with open(path, "r") as stream:
        _config = yaml.load(stream)
    
    return _config