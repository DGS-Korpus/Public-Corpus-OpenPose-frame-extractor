"""
The Public DGS Corpus (ling.meine-dgs.de) provides OpenPose data for all of its transcripts.
Each transcript collects all of its pose information in a single file.
This script converts these files into the one-frame-per-file format used by the OpenPose demo.
"""
from __future__ import print_function
import argparse
import os
import json
from glob import glob


def ensure_dir(filename: str):
    """
    Make sure the directory actually exists
    """
    filepath = os.path.dirname(filename)
    os.makedirs(filepath, exist_ok=True)


def get_output_subdirectory(input_filename, output_dir=None):
    """
    Get the output subdirectory for a specific input file.
    """
    input_dir, filename = os.path.split(input_filename)
    fileroot, ext = os.path.splitext(filename)
    if output_dir is None:
        output_dir = input_dir
    output_subdir = os.path.join(output_dir, fileroot)
    return output_subdir


def load_json(filename):
    """
    Load a JSON file.
    """
    with open(filename) as reader:
        return json.load(reader)


def write_json(data, filename):
    """
    Write data to a JSON file.
    """
    ensure_dir(filename)
    with open(filename, 'w') as writer:
        json.dump(data, writer)


def yield_openpose_frame_data(dgskorpus_data):
    """
    Given a corpus dataset, calculate the filename and data for each frame and yield them one by one.
    """
    filename_pattern = '{id}_{camera}.{width}x{height}.frame_{frame:0>13}.keypoints.json'
    for video_data in dgskorpus_data:
        for frame, frame_data in video_data['frames'].items():
            filename = filename_pattern.format(frame=frame, **video_data)
            yield filename, frame_data


def extract_json_frames(input_filename, output_dir=None, verbose=False):
    """
    Extract the frames from a corpus pose file and write them to individual files.
    """
    if verbose:
        print("Extracting frames from {}".format(input_filename))
    dgskorpus_data = load_json(filename=input_filename)
    output_subdir = get_output_subdirectory(input_filename=input_filename, output_dir=output_dir)
    for output_filename, openpose_frame_data in yield_openpose_frame_data(dgskorpus_data):
        output_filepath = os.path.join(output_subdir, output_filename)
        write_json(data=openpose_frame_data, filename=output_filepath)


def batch_extract_json_frames(input_batches, output_dir=None, verbose=False):
    """
    Extract frames from several corpus pose files.
    """
    input_files = []
    for input_batch in input_batches:
        for input_file in glob(input_batch):
            input_files.append(input_file)
    if verbose:
        print('Preparing to extract frame data from {} DGS-Korpus OpenPose files.'.format(len(input_files)))
    for input_batch in input_batches:
        for input_file in glob(input_batch):
            extract_json_frames(input_filename=input_file, output_dir=output_dir, verbose=verbose)
    if verbose:
        print('Completed extraction.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_batches', nargs='+', metavar='INPUT_FILE',
                        help='The DGS-Korpus OpenPose file(s) from which to extract the OpenPose frame files. '
                             'To run on a batch of similarly named files, use * (e.g. files/*.openpose.json)')
    parser.add_argument('-o', '--output', '--outputdir', metavar='OUTPUT_DIR',
                        help='Directory to which to extract the frames. '
                             'If missing, a directory is created based on the location and filename of the input file.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Provide information on the extraction process.')

    args = parser.parse_args()
    batch_extract_json_frames(input_batches=args.input_batches, output_dir=args.output, verbose=args.verbose)


if __name__ == '__main__':
    main()
