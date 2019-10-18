from base.base_data_loader import BaseDataLoader
from keras.preprocessing.image import ImageDataGenerator

class DataLoader(BaseDataLoader):
    def __init__(self, config):
        super(DataLoader, self).__init__(config)
        # self.labels = labels  # array of labels
        # self.images_paths = images_paths  # array of image paths
        # self.dim = image_dimensions  # image dimensions
        # self.batch_size = batch_size  # batch size
        # self.shuffle = shuffle  # shuffle bool
        # self.augment = augment  # augment data bool
        # self.on_epoch_end()


    def get_train_generator(self):
        train_datagen = ImageDataGenerator()

        train_generator = train_datagen.flow_from_directory(
            'data/train/',
            class_mode='binary'
        )

        return train_generator
    # def get_test_generator(self):
    #     return self.X_test, self.y_test
