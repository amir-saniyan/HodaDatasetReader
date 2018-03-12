In the name of God

# Hoda Dataset Reader
This repository contains Python code for reading Hoda farsi digit dataset.

# Hoda Farsi Digit Dataset
Hoda dataset is the first dataset of handwritten Farsi digits that has been developed during an MSc. project in Tarbiat
Modarres University entitled: Recognizing Farsi Digits and Characters in SANJESH Registration Forms. This project has
been carried out in cooperation with Hoda System Corporation. It was finished in summer 2005 under supervision of Prof.
Ehsanollah Kabir.
Samples of the dataset are handwritten characters extracted from about 12000 registration forms of university entrance
examination in Iran. The dataset specifications is as follows:

* Resolution of samples: 200 dpi
* Total samples: 102,352 samples
* Training samples: 60,000 samples
* Test samples: 20,000 samples
* Remaining samples: 22,352 samples

Number of samples per each class:
* 0: 10070
* 1: 10330
* 2: 9923
* 3: 10334
* 4: 10333
* 5: 10110
* 6: 10254
* 7: 10363
* 8: 10264
* 9: 10371

For more information please refer to the paper: [Introducing a very large dataset of handwritten Farsi digits and a
study on their varieties](http://farsiocr.ir/Archive/dataset_PRL.pdf)

**This dataset is free of charge for research purposes and non commercial uses only.**

Dataset website: [http://farsiocr.ir/](http://farsiocr.ir/مجموعه-داده/مجموعه-ارقام-دستنویس-هدی)

# Dataset Samples

Samples with different writing styles in the dataset:

![Samples with different writing styles in the dataset](Farsi_Digits_Sample_1.gif)

Samples with different qualities in the dataset:

![Samples with different qualities in the dataset](Farsi_Digits_Sample_2.gif)

# Reading Images
To read Hoda `.cdb` files as images (for example `Train 60000.cdb`), use the following code snippet:

```Python
from HodaDatasetReader import read_hoda_cdb

# type(train_images):  <class 'list'>
# len(train_images):  60000
#
# type(train_images[ i ]): <class 'numpy.ndarray'>
# train_images[ i ].dtype: uint8
# train_images[ i ].min(): 0
# train_images[ i ].max(): 255
# train_images[ i ].shape: (HEIGHT, WIDTH)
#
# type(train_labels):  <class 'list'>
# len(train_labels):  60000
#
# type(train_labels[ i ]): <class 'int'>
# train_labels[ i ]: 0...9
print('Reading Train 60000.cdb ...')
train_images, train_labels = read_hoda_cdb('./DigitDB/Train 60000.cdb')


# type(test_images):  <class 'list'>
# len(test_images):  20000
#
# type(test_images[ i ]): <class 'numpy.ndarray'>
# test_images[ i ].dtype: uint8
# test_images[ i ].min(): 0
# test_images[ i ].max(): 255
# test_images[ i ].shape: (HEIGHT, WIDTH)
#
# type(test_labels):  <class 'list'>
# len(test_labels):  20000
#
# type(test_labels[ i ]): <class 'int'>
# test_labels[ i ]: 0...9
print('Reading Test 20000.cdb ...')
test_images, test_labels = read_hoda_cdb('./DigitDB/Test 20000.cdb')


# type(remaining_images):  <class 'list'>
# len(remaining_images):  22352
#
# type(remaining_images[ i ]): <class 'numpy.ndarray'>
# remaining_images[ i ].dtype: uint8
# remaining_images[ i ].min(): 0
# remaining_images[ i ].max(): 255
# remaining_images[ i ].shape: (HEIGHT, WIDTH)
#
# type(remaining_labels):  <class 'list'>
# len(remaining_labels):  22352
#
# type(remaining_labels[ i ]): <class 'int'>
# remaining_labels[ i ]: 0...9
print('Reading RemainingSamples.cdb ...')
remaining_images, remaining_labels = read_hoda_cdb('./DigitDB/RemainingSamples.cdb')
```

![Figure 1](Figure_1.png)

# Reading Datasets
To read Hoda `.cdb` files as datasets (for example `Train 60000.cdb`), use the following code snippet:

```Python
from HodaDatasetReader import read_hoda_dataset

# type(X_train):  <class 'numpy.ndarray'>
# X_train.dtype: float32
# X_train.shape: (reshape=True),  (60000, 1024)
#
# type(X_train[ i ]): <class 'numpy.ndarray'>
# X_train[ i ].dtype: float32
# X_train[ i ].min(): 0.0
# X_train[ i ].max(): 1.0
# X_train[ i ].shape = (HEIGHT*WIDTH,): (reshape=True),  (1024,)
#
# type(Y_train):  <class 'numpy.ndarray'>
# Y_train.dtype: float32
# Y_train.shape: (one_hot=False),  (60000,)
#
# type(Y_train[ i ]): <class 'numpy.float32'>
# Y_train[ i ].dtype: float32
# Y_train[ i ]: (one_hot=False),  0...9
print('Reading train dataset (Train 60000.cdb)...')
X_train, Y_train = read_hoda_dataset(dataset_path='./DigitDB/Train 60000.cdb',
                                images_height=32,
                                images_width=32,
                                one_hot=False,
                                reshape=True)


# type(X_test):  <class 'numpy.ndarray'>
# X_test.dtype: float32
# X_test.shape: (reshape=False),  (20000, 32, 32, 1)
#
# type(X_test[ i ]): <class 'numpy.ndarray'>
# X_test[ i ].dtype: float32
# X_test[ i ].min(): 0.0
# X_test[ i ].max(): 1.0
# X_test[ i ].shape = (HEIGHT, WIDTH, CHANNEL): (reshape=False),  (32, 32, 1)
#
# type(Y_test):  <class 'numpy.ndarray'>
# Y_test.dtype: float32
# Y_test.shape: (one_hot=True),  (20000, 10)
#
# type(Y_test[ i ]): <class 'numpy.ndarray'>
# Y_test[ i ].dtype: float32
# Y_test[ i ].min(): 0.0
# Y_test[ i ].max(): 1.0
# Y_test[ 0 ]: (one_hot=True),  [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print('Reading test dataset (Test 20000.cdb)...')
X_test, Y_test = read_hoda_dataset(dataset_path='./DigitDB/Test 20000.cdb',
                              images_height=32,
                              images_width=32,
                              one_hot=True,
                              reshape=False)


# type(X_remaining):  <class 'numpy.ndarray'>
# X_remaining.dtype: float32
# X_remaining.shape: (reshape=True),  (22352, 1024)
#
# type(X_remaining[ i ]): <class 'numpy.ndarray'>
# X_remaining[ i ].dtype: float32
# X_remaining[ i ].min(): 0.0
# X_remaining[ i ].max(): 1.0
# X_remaining[ i ].shape = (HEIGHT*WIDTH,): (reshape=True),  (1024,)
#
# type(Y_remaining):  <class 'numpy.ndarray'>
# Y_remaining.dtype: float32
# Y_remaining.shape: (one_hot=True),  (22352, 10)
#
# type(Y_remaining[ i ]): <class 'numpy.ndarray'>
# Y_remaining[ i ].dtype: float32
# Y_remaining[ i ].min(): 0.0
# Y_remaining[ i ].max(): 1.0
# Y_remaining[ 0 ]: (one_hot=True),  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
print('Reading remaining samples dataset (RemainingSamples.cdb)...')
X_remaining, Y_remaining = read_hoda_dataset('./DigitDB/RemainingSamples.cdb',
                                             images_height=32,
                                             images_width=32,
                                             one_hot=True,
                                             reshape=True)
```

![Figure 2](Figure_2.png)

# Running Sample Code
To run sample code, type the following command at the command prompt:
```
python3 ./main.py
```

# Dependencies
* Python 3
* numpy
* python-opencv
* matplotlib (for `main.py`)

# Links
* http://farsiocr.ir/مجموعه-داده/مجموعه-ارقام-دستنویس-هدی
* http://dadegan.ir/catalog/hoda
* https://github.com/amir-saniyan/HodaDatasetReader
