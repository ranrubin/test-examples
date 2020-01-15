import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.predictor.config_file import generate_config, set_config



if __name__ == '__main__':
    config = generate_config()
    print("Running configurations:")
    print("Running on device:", config.device_name)
    print("Load all videos to ram?", config.RAM_ONLY)
    print("Batch size:", config.batch_size)
    config = set_config(config, )
