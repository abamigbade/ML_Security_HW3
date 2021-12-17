# ML_Security_HW3
```bash
├──Models
    └── BadNet.h5
    └── RepairedNet_2.h5
    └── RepairedNet_4.h5
    └── RepairedNet_10.h5
    
├── eval.py // this is the evaluation script
```

## I. Import Libraries
    import numpy as np
    import matplotlib 
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import os
    import tensorflow as tf
    from tensorflow import keras
    import h5py
    from keras.models import load_model
    from keras import models
   
## II. Data
   1. The test datasets are too large for this repository. Therefore, download the datasets and upload to your own directory or GoogleColab Notebook directory. For the clean test dataset, the file can be downloaded from [here](https://drive.google.com/file/d/1HpahIi-RcvtaRoly_TbuoBzWUaAjVDgt/view?usp=sharing) and for the backdoored test dataset, the file can be downloaded from [here](https://drive.google.com/file/d/1kxNACo0qFo8QdZgtGHvaA67p4h4RcNIy/view?usp=sharing)

## III. Evaluating the GoodNet Model
   1. The BadNet and RepairedNet models are supplied in the Models folder of this repository.
   2. This model only accepts array of images (more than one image) as input.
   3. Edit line 30 of the eval.py file to specify the index of the input test image to evalate.
   4. To evaluate the GoodNet model, execute `eval.py` by running:  
      `python3 eval.py <your clean test data directory> <your poisoned test data directory> <BadNet model directory> <RepairedNet model directory for X% pruning>`.
      
      E.g., `python3 eval.py data/test.h5 data/bd_test.h5 Models/BadNet.h5 Models/RepairedNet_X.h5`. This will output the correct label if both input test images are clean or a label of 1283 when one of the input test images is poisioned.
## IV. Important Notes
    1. This model only accepts array of images (more than one image) as input.
    2. Edit line 30 of the eval.py file to specify the index of the input test images to evalate. 
    3. X in Models/RepairedNet_X.h5 represent 2 or 4 or 10.
