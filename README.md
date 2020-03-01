# msdb

Movie Script Database generator & Applications

## Idea

This collection of scripts allows you to collect thousands of real movie scripts with their genres from [IMSDb](https://www.imsdb.com/) using their RSS feed and a little bit of HTML scraping

## Usage

```python
from acquire_script import load_scripts
#load scripts into ./data folder as JSON
load_scripts()
```

## Applications

To illustrate a few applications of the Database, I've written two (as of today) Machine-Learing systems:

### Classifier (working, TF)

The classifier is written in Python using the Tensorflow framework.
It is able to classify the scripts into the provided categories (based on the first 1000 words). (can be found [here](classify.ipynb), it incluides loading the dataset into a Tensorflow dataset)

### Generator (in progress, PyTorch,TF)

The generator is still in progress and is currently not able to produce correct text output due to difficulties generating that with the standard DCGAN approach. Those two approaches are located

* [here](generate.ipynb), utilzing tensorflow (broken)
* [here](generate_torch.ipynb), utilzing PyTorch  (currently producing bad texts) and a way to load the dataset into the PyTorch Dataset-system (on the CPU side, with the ability to transfer to the GPU to lower the memory burden on it)
