# *-* coding: utf-8 *-*

from matplotlib import pyplot as plt
from HodaDatasetReader import read_hoda_cdb

################################################################################

print('Reading Hoda dataset (Train)...')
train_images, train_labels = read_hoda_cdb('DigitDB/Train 60000.cdb')

print('Reading Hoda dataset (Test)...')
test_images, test_labels = read_hoda_cdb('DigitDB/Test 20000.cdb')

print('Reading Hoda dataset (RemainingSamples)...')
remaining_images, remaining_labels = read_hoda_cdb('DigitDB/RemainingSamples.cdb')

print()

################################################################################

print('type(train_images): ', type(train_images))
print('type(train_labels): ', type(train_labels))
print()

print('len(train_images): ', len(train_images))
print('len(train_labels): ', len(train_labels))
print()

fig = plt.figure(figsize=(15, 4))
for i in range(4):

    print('----------------------------------------')
    print()

    print('type(train_images[', i, ']):', type(train_images[i]))
    print('type(train_labels[', i, ']):', type(train_labels[i]))
    print()

    print('train_images[', i, '].shape:', train_images[i].shape)
    print('train_images[', i, '].shape[0] = HEIGHT:', train_images[i].shape[0])
    print('train_images[', i, '].shape[1] = WIDTH:', train_images[i].shape[1])
    print('train_labels[', i, ']:', train_labels[i])
    print()

    fig.add_subplot(1, 4, i + 1)
    plt.title('train_labels[' + str(i) + '] = ' + str(train_labels[i]))
    plt.imshow(train_images[i], cmap='gray')

plt.show()
