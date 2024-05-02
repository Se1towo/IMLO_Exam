import torch
import torchvision
import numpy as np
import pandas as pd
from torch.utils.data.dataloader import dataloader
from torch.utils.data import Dataset

flowers_102 = torchvision.datasets.Flowers102(root: Union[str, Path], split: str = 'train', download= False)
print(flowers_102)