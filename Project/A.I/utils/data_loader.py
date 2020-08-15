from torch.utils.data.dataset import Dataset
from torchvision import transforms
import pandas as pd
import numpy as np
from PIL import Image
import torch
from torch.utils.data.sampler import SubsetRandomSampler


class NkDataSet(Dataset):

    def __init__(self, file_path):
        self.trans = transforms.Compose([transforms.RandomHorizontalFlip(),
                                         transforms.RandomCrop(128, 4),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                              std=[0.229, 0.224, 0.225])])
        self.to_tensor = transforms.ToTensor()
        self.data_info = pd.read_csv(file_path, header=None)
        self.image_arr = np.asarray(self.data_info.iloc[:, 0][1:])
        self.label_arr = np.asarray(self.data_info.iloc[:, 1][1:])
        self.label_arr = self.label_arr.astype(np.long) - 1
        self.label_arr = torch.from_numpy(self.label_arr)
        self.data_len = len(self.data_info.index)
        self.img_path = "/tmp/pycharm_project_917/img/faces_images/"

    def __getitem__(self, index):
        img_name = self.img_path + self.image_arr[index - 1]
        img_as_img = Image.open(img_name)
        img_as_tensor = self.trans(img_as_img)
        img_label = self.label_arr[index - 1]

        return img_as_tensor, img_label, img_name

    def __len__(self):
        return self.data_len


def get_data_loader(args):
    validation_split = 2
    random_seed = 42

    csv_path = "/tmp/pycharm_project_917/files/train_vision.csv"
    custom_dataset = NkDataSet(csv_path)

    test_csv_path = "/tmp/pycharm_project_917/files/test_vision.csv"
    test_custom_dataset = NkDataSet(test_csv_path)

    dataset_size = len(custom_dataset)
    indices = list(range(dataset_size))
    split = int(np.floor(validation_split * dataset_size))
    np.random.seed(random_seed)
    np.random.shuffle(indices)

    train_indices, val_indices = indices[split:], indices[:split]

    train_sampler = SubsetRandomSampler(train_indices)
    valid_sampler = SubsetRandomSampler(val_indices)

    train_loader = torch.utils.data.DataLoader(custom_dataset, batch_size=64,
                                               sampler=train_sampler)

    val_loader = torch.utils.data.DataLoader(custom_dataset, batch_size=64,
                                             sampler=valid_sampler)

    test_loader = torch.utils.data.DataLoader(dataset=test_custom_dataset, batch_size=1, shuffle=False)

    print("data set length = %d" % len(test_loader))

    return train_loader, val_loader, test_loader