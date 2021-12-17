import keras
import sys
import h5py
import numpy as np

CleanData_filename = str(sys.argv[1])
BackdooredData_filename = str(sys.argv[2])
BadNet_filename = str(sys.argv[3])
RepairedNet_filename = str(sys.argv[4])

def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    y_data = np.array(data['label'])
    x_data = x_data.transpose((0,2,3,1))

    return x_data, y_data

def main():
    cl_x_test, cl_y_test = data_loader(CleanData_filename)
    bd_x_test, bd_y_test = data_loader(BackdooredData_filename)

    BadNet = keras.models.load_model(BadNet_filename)
    RepairedNet = keras.models.load_model(RepairedNet_filename)
    
    bd_label_p = np.argmax(BadNet.predict(bd_x_test), axis=1)
    cl_label_p = np.argmax(RepairedNet.predict(cl_x_test), axis=1)
    
    # Specify the index of the dataset to evaluate
    i = 100 # A default index of 100 is used here
    
    if bd_label_p[i] == cl_label_p[i]:
        test_data_label = cl_label_p[i]
        print('\n The test image is a clean and its label is:', cl_label_p)
    else:
        test_data_label = 1283
        print('\n The test image is poisoned and its label is outside of the class. Therefore, its label is outputed as:', 1283)

if __name__ == '__main__':
    main()
