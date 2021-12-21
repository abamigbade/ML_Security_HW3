import keras
import sys
import h5py
import numpy as np

TestData_filename = str(sys.argv[1])
BadNet_filename = str(sys.argv[2])
RepairedNet_filename = str(sys.argv[3])

def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    x_data = x_data.transpose((0,2,3,1))
    
    return x_data

def main():
    x_test = data_loader(TestData_filename)

    BadNet = keras.models.load_model(BadNet_filename)
    RepairedNet = keras.models.load_model(RepairedNet_filename)
    
    bd_label_p = np.argmax(BadNet.predict(x_test), axis=1)
    cl_label_p = np.argmax(RepairedNet.predict(x_test), axis=1)
    
    # Specify the index of the dataset to evaluate
    ########################################################
    i = 100 # A default index of 100 is used here
    ########################################################
    
    if bd_label_p[i] == cl_label_p[i]:
        test_data_label = cl_label_p[i]
        print('\n The predicted label of test image is:', test_data_label)
    else:
        test_data_label = 1283
        print('\n The test image is poisoned and its label is outside of the class. Therefore, its label is outputed as:', 1283)

if __name__ == '__main__':
    main()
