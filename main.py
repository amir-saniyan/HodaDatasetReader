# *-* coding: utf-8 *-*

from matplotlib import pyplot as plt
from HodaDatasetReader import read_hoda_cdb, read_hoda_dataset

print('################################################################################')
print()

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

print()

# ******************************************************************************

print('type(train_images): ', type(train_images))
print('len(train_images): ', len(train_images))
print()

print('type(train_labels): ', type(train_labels))
print('len(train_labels): ', len(train_labels))
print()

fig = plt.figure(figsize=(15, 4))
for i in range(4):

    print('----------------------------------------')
    print()

    print('type(train_images[', i, ']):', type(train_images[i]))
    print('train_images[', i, '].dtype:', train_images[i].dtype)
    print('train_images[', i, '].min():', train_images[i].min())
    print('train_images[', i, '].max():', train_images[i].max())
    print('train_images[', i, '].shape = (HEIGHT, WIDTH):', train_images[i].shape)
    print()

    print('type(train_labels[', i, ']):', type(train_labels[i]))
    print('train_labels[', i, ']:', train_labels[i])
    print()

    fig.add_subplot(1, 4, i + 1)
    plt.title('train_labels[' + str(i) + '] = ' + str(train_labels[i]))
    plt.imshow(train_images[i], cmap='gray')

plt.show()

print('################################################################################')
print()

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

print()

# ******************************************************************************

print('type(X_train): ', type(X_train))
print('X_train.dtype:', X_train.dtype)
print('X_train.shape: (reshape=True), ', X_train.shape)
print()

print('type(Y_train): ', type(Y_train))
print('Y_train.dtype:', Y_train.dtype)
print('Y_train.shape: (one_hot=False), ', Y_train.shape)
print()

print('type(X_test): ', type(X_test))
print('X_test.dtype:', X_test.dtype)
print('X_test.shape: (reshape=False), ', X_test.shape)
print()

print('type(Y_test): ', type(Y_test))
print('Y_test.dtype:', Y_test.dtype)
print('Y_test.shape: (one_hot=True), ', Y_test.shape)
print()

print('type(X_remaining): ', type(X_remaining))
print('X_remaining.dtype:', X_remaining.dtype)
print('X_remaining.shape: (reshape=True), ', X_remaining.shape)
print()

print('type(Y_remaining): ', type(Y_remaining))
print('Y_remaining.dtype:', Y_remaining.dtype)
print('Y_remaining.shape: (one_hot=True), ', Y_remaining.shape)
print()

fig = plt.figure(figsize=(16, 3))

print('----------------------------------------')
print()

print('type(X_train[ 0 ]):', type(X_train[0]))
print('X_train[ 0 ].dtype:', X_train[0].dtype)
print('X_train[ 0 ].min():', X_train[0].min())
print('X_train[ 0 ].max():', X_train[0].max())
print('X_train[ 0 ].shape = (HEIGHT*WIDTH,): (reshape=True), ', X_train[0].shape)
print()

print('type(Y_train[ 0 ]):', type(Y_train[0]))
print('Y_train[ 0 ].dtype:', Y_train[0].dtype)
print('Y_train[ 0 ]: (one_hot=False), ', Y_train[0])
print()

fig.add_subplot(1, 3, 1)
plt.title('Y_train[ 0 ] = ' + str(Y_train[0]))
plt.imshow(X_train[0].reshape([32, 32]), cmap='gray')

print('----------------------------------------')
print()

print('type(X_test[ 0 ]):', type(X_test[0]))
print('X_test[ 0 ].dtype:', X_test[0].dtype)
print('X_test[ 0 ].min():', X_test[0].min())
print('X_test[ 0 ].max():', X_test[0].max())
print('X_test[ 0 ].shape = (HEIGHT, WIDTH, CHANNEL): (reshape=False), ', X_test[0].shape)
print()

print('type(Y_test[ 0 ]):', type(Y_test[0]))
print('Y_test[ 0 ].dtype:', Y_test[0].dtype)
print('Y_test[ 0 ].min():', Y_test[0].min())
print('Y_test[ 0 ].max():', Y_test[0].max())
print('Y_test[ 0 ]: (one_hot=True), ', Y_test[0])
print()

fig.add_subplot(1, 3, 2)
plt.title('Y_test[ 0 ] = ' + str(Y_test[0]))
plt.imshow(X_test[0].reshape([32, 32]), cmap='gray')

print('----------------------------------------')
print()

print('type(X_remaining[ 0 ]):', type(X_remaining[0]))
print('X_remaining[ 0 ].dtype:', X_remaining[0].dtype)
print('X_remaining[ 0 ].min():', X_remaining[0].min())
print('X_remaining[ 0 ].max():', X_remaining[0].max())
print('X_remaining[ 0 ].shape = (HEIGHT*WIDTH,): (reshape=True), ', X_remaining[0].shape)
print()

print('type(Y_remaining[ 0 ]):', type(Y_remaining[0]))
print('Y_remaining[ 0 ].dtype:', Y_remaining[0].dtype)
print('Y_remaining[ 0 ].min():', Y_remaining[0].min())
print('Y_remaining[ 0 ].max():', Y_remaining[0].max())
print('Y_remaining[ 0 ]: (one_hot=True), ', Y_remaining[0])
print()

fig.add_subplot(1, 3, 3)
plt.title('Y_remaining[ 0 ] = ' + str(Y_remaining[0]))
plt.imshow(X_remaining[0].reshape([32, 32]), cmap='gray')

plt.show()

print('################################################################################')
print()
