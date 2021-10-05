#!/bin/bash
# This script is used for running partition_dataset.py and generate_tfrecord.py locally,
# not on Google Colab

DETECTOR_DIR="../../workspace/object_detector"

python partition_dataset.py -x -i $DETECTOR_DIR/images -r 0.1

python generate_tfrecord.py -x $DETECTOR_DIR/images/train -l $DETECTOR_DIR/annotations/roadsign_labels.pbtxt -o $DETECTOR_DIR/annotations/train.record
python generate_tfrecord.py -x $DETECTOR_DIR/images/test -l $DETECTOR_DIR/annotations/roadsign_labels.pbtxt -o $DETECTOR_DIR/annotations/test.record
