from dataclasses import dataclass
from dataclasses_json import dataclass_json
import os


@dataclass_json
@dataclass
class ConfigurationData:
    """
    This class stores all of your model's hyper parameters and important paths.
    Dump a copy in JSON upon creation for logging.
    """
    # Some running options
    device_name: str = "cuda:0"  # choose from ('cpu', 'cuda:0')
    RAM_ONLY: bool = True  # True or False
    batch_size = 8

    # Define paths for the data and model
    home_dir = os.path.join(os.path.dirname(__file__), '../..')
    data_path = home_dir + '/data'
    raw_videos_dir = data_path + '/raw_videos/'
    processed_path = data_path + '/processed/'
    partitions_path = data_path + '/partitions/'
    load_model_path: str = home_dir + '/models/CyabraModel.pth'

    # test lists 
    real_data_path: str = partitions_path + 'real_video_list.txt'
    fake_data_path: str = partitions_path + 'fake_video_list.txt'

    # data parameters
    target_size: tuple = (128, 128)
    dataset_max_num_videos: int = -1  # use -1 to load all videos in list
    fake_label_val: float = 0.9
    real_label_val: float = 0.1

    enc_configs = [[
        # t, c, n, s
        [1, 24, 1, 1],
        [6, 32, 3, 2],
        [6, 64, 4, 2],
        [6, 64, 3, 1],
        [6, 64, 3, 2],
    ],
    [
        # t, c, n, s
        [1, 24, 1, 1],
        [6, 32, 3, 2],
        [6, 64, 4, 2],
    ],

     [
        # t, c, n, s
        [1, 128, 1, 1],
        [6, 64, 3, 2],
        [6, 64, 4, 2],
        [6, 32, 3, 1],
        [6, 16, 3, 2],
    ],

    [
        # t, c, n, s
        [1, 128, 1, 1],
        [6, 64, 3, 2],
        [6, 32, 4, 2],
    ]]


def set_config(config, args):

    for key in vars(args):
        if key in config:
            config.key = getattr(args, key)

    return config


def generate_config():
    config = ConfigurationData()
    return config
