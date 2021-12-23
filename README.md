# ML_Security_HW3
```bash
├──Models
    └── BadNet.h5
    └── RepairedNet_2.h5
    └── RepairedNet_4.h5
    └── RepairedNet_10.h5
    
├── eval.py // this is the evaluation script

├── GoogleColab Notebook // this is my colab notebook for this homework
```
   
## I. Data
   1. You should supply your test data (which is an image) to evaluate this model.
   
## II. Evaluating the GoodNet Model
   1. The BadNet and RepairedNet models are supplied in the Models folder of this repository.
   2. This model only accepts images of the type png or jpeg format as input.
   4. To evaluate the GoodNet model, execute `eval.py` by running:  
      `python3 <eval.py directory> <your test image directory> <BadNet model directory> <RepairedNet model directory for X% pruning>`.
      
      E.g., `python3 eval.py data/test_image.png Models/BadNet.h5 Models/RepairedNet_X.h5`. This will output the correct label if both input test images are clean or a label of 1283 when one of the input test images is poisioned.
## III. Important Notes
    1. This model only accepts as input an image at a time. Also, the image should be of the type png or jpeg format.
    2. X in Models/RepairedNet_X.h5 represent 2 or 4 or 10.
