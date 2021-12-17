# ML_Security_HW3
```bash
├── Data
    └── cl
        └── test.h5  // this is clean test data used to evaluate the BadNet
    └── bd
        └── bd_test.h5  // this is sunglasses poisoned test data
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
   1. The test datasets are too large for this repository. Therefore, download test datasets from [here](https://drive.google.com/drive/folders/1Rs68uH8Xqa4j6UxG53wzD0uyI8347dSq?usp=sharing). For the clean test dataset, the file path is: [here](https://drive.google.com/file/d/1HpahIi-RcvtaRoly_TbuoBzWUaAjVDgt/view?usp=sharing) and for the backdoored test dataset, the file path is: [here](https://drive.google.com/file/d/1kxNACo0qFo8QdZgtGHvaA67p4h4RcNIy/view?usp=sharing)
   2. and store them under `data/` directory.
   3. The dataset contains images from YouTube Aligned Face Dataset. We retrieve 1283 individuals and split into validation and test datasets.
   4. bd_valid.h5 and bd_test.h5 contains validation and test images with sunglasses trigger respectively, that activates the backdoor for bd_net.h5. 

## III. Evaluating the Backdoored Model
   1. The DNN architecture used to train the face recognition model is the state-of-the-art DeepID network. 
   2. To evaluate the backdoored model, execute `eval.py` by running:  
      `python3 eval.py <clean validation data directory> <poisoned validation data directory> <model directory>`.
      
      E.g., `python3 eval.py data/cl/valid.h5 data/bd/bd_valid.h5 models/bd_net.h5`. This will output:
      Clean Classification accuracy: 98.64 %
      Attack Success Rate: 100 %

## IV. Important Notes
Please use only clean validation data (valid.h5) to design the pruning defense. And use test data (test.h5 and bd_test.h5) to evaluate the models. 
