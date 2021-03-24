#!/usr/bin/env python
import argparse
import glob


types = list('*.MOV')


def score(test_videos_path):
    video_list = []
    for type_ in types:
        files = args.training_set + type_
        video_list.extend(glob.glob(files))
    print video_list




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Evaluation for Landmark + Direction recognition")
    parser.add_argument("test_videos", help="Path to test videos")
    args = parser.parse_args()

    score(args.test_videos)

