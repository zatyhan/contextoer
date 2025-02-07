import os 

CODE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CODE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)