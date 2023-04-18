import numpy as np
import matplotlib.pyplot as plt

import torch, torchvision, pathlib, time, os, glob
from torch.utils.data import DataLoader, Dataset, Subset
from torchvision import transforms
from torchsummary import summary
import torch.nn as nn
import torch.nn.functional as F

from collections import defaultdict
from tqdm.auto import tqdm

from google.colab import drive
from PIL import Image

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
