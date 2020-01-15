import os
import sys
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))



def handle_args():
    """
    Handles arguments that are given by the user
    :return:  args  namespace
    """
    parser = argparse.ArgumentParser(description='Deep fake model')
    parser.add_argument('-device', type=str, choices=['cpu', 'cuda:0'], default='cuda:0', help='Choose cpu or gpu')
    parser.add_argument('--load_to_ram', action='store_true', help='if flagged, loads to ram')
    parser.add_argument('-batch_size', type=int, default=8, help='batch size')
    return parser.parse_args()


def main():
    """
    Runs a model. For more information refer to README
    :return:
    """
    args = handle_args()

    print("Running model with:")
    print("device:", args.device)
    print("Load  ram?", args.load_to_ram)
    print("Batch size:", args.batch_size)


if __name__ == '__main__':
    main()

