__Latest release:__ [![DOI](https://www.fdr.uni-hamburg.de/badge/DOI/10.25592/uhhfdm.8237.svg)](https://doi.org/10.25592/uhhfdm.8237)

__This release:__ See [release description](https://github.com/DGS-Korpus/Public-Corpus-OpenPose-frame-extractor/releases/tag/v1.0.2).

# Public Corpus OpenPose frame extractor

The [Public DGS Corpus](http://ling.meine-dgs.de) provides [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) data for all of its transcripts.
Each transcript collects all of its pose information in a single file, using the _DGS-Korpus OpenPose wrapper format_.
This script converts these files into the one-frame-per-file format used by the OpenPose demo.

For more information, see the project note [_OpenPose in the Public DGS Corpus_](https://doi.org/10.25592/uhhfdm.842).
For the reverse procedure (many frame files to single wrapper file), see the [DGS-Korpus OpenPose wrapper](https://github.com/DGS-Korpus/DGS-Korpus-OpenPose-wrapper) script.


## Requirements
Python 3.7 or later.
Earlier versions should generally work, but item order in mappings is not guaranteed.

## Usage
```sh
wrap_openpose.py INPUT_FILE [INPUT_FILE ...]
```

__Positional arguments:__
* `INPUT_FILE`: The DGS-Korpus OpenPose file(s) from which to extract the OpenPose frame files. To run on a batch of similarly named files, use `*` (e.g. `dgskorpus/*.openpose.json`)

__Optional arguments:__
* `-o OUTPUT_DIR`: Directory to which to extract the frames. If missing, a directory is created based on the location and filename of the input file.
* `-v`: Provide information on the extraction process.
