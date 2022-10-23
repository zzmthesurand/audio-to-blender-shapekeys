# audio-to-blender-shapekeys
A Python notebook and script that takes a .wav file and converts it into an array of keyframes for usage with Blender.

## Prerequisites
- allosaurus >= 1.0.2
- pandas >= 1.5.1
- Blender >= 3.3.0

## Usage
There are three different variables you have to change in order to use this with your own files. Two in the `phoneme processor.ipynb` notebook, and one in the `AudioToKeyframe.py` script. Of course you can change other parts to fit your needs, but if you want to use it as is, these are the only three you need to change.
1. phoneme processor.ipynb
   - MAX_DURATION: the amount of time a phoneme can go before defaulting to the "basis" mouth shape
   - FILEPATH: the filepath of the .wav file
2. AudioToKeyframe.py
   - FILEPATH: the filepath of the .csv file you just created
   
The script is built for 7 different mouth shapes/phoneme groups, which are:

`"aei", "cdkg", "m", "n", "szeay", "l/th", "oo", "fv", "r", "o"`

If you need more or less, just change the `phonemeList` variable within the Initialization section of the ipynb. The comments should help explain what to do.

Remember that the shape keys on your model should **follow this exact order**, otherwise the keyframes won't work properly.

# Credits
This was partially inspired by [this video by Jackall Digital](https://www.youtube.com/watch?v=Kuw9xoS5wxw&list=PLg4tPAeoYVcUnzH8xHBfFhrtiy2rvjxaH&index=2), which essentially does the same thing, but for images within Davinci Resolve. 

This tool was created because I wanted to automate lipsyncing on a clay model I was animating, which was inspired by [savannahXYZ](https://www.youtube.com/c/savannahXYZ). Go check her out. She's awesome.
