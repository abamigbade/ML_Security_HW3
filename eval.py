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
    clean_accuracy = np.mean(np.equal(cl_label_p, cl_y_test))*100
    print('Clean Classification accuracy:', clean_accuracy)
    
    bd_label_p = np.argmax(bd_model.predict(bd_x_test), axis=1)
    asr = np.mean(np.equal(bd_label_p, bd_y_test))*100
    print('Attack Success Rate:', asr)

if __name__ == '__main__':
    main()
