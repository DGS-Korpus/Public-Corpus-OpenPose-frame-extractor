# Public Corpus OpenPose frame extractor

The [Public DGS Corpus](http://ling.meine-dgs.de) provides [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) data for all of its transcripts.
Each transcript collects all of its pose information in a single file.
This script converts these files into the one-frame-per-file format used by the OpenPose demo.

## Requirements
Python 2.7 or Python 3.

## Usage
```sh
wrap_openpose.py INPUT_FILE [INPUT_FILE ...]
```

__Positional arguments:__
* `INPUT_FILE`: The DGS-Korpus OpenPose file(s) from which to extract the OpenPose frame files. To run on a batch of similarly named files, use `*` (e.g. `dgskorpus/*.openpose.json`)

__Optional arguments:__
* `-o OUTPUT_DIR`: Directory to which to extract the frames. If missing, a directory is created based on the location and filename of the input file.
* `-v`: Provide information on the extraction process.
