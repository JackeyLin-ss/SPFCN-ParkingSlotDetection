import torch
from torch.backends import cudnn

from .dataset import get_training_set, get_validating_set
from .model.network import SlotNetwork
from .train import auto_train, auto_validate


def setup(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    cudnn.benchmark = True
    cudnn.deterministic = True


def slot_network_training(device_id=1):
    # Initial
    setup(19960229)
    net = SlotNetwork([32, 44, 64, 92, 128], device_id=device_id)

    # Train
    auto_train(get_training_set(6535, 50, 224, device_id), net, device_id=device_id,
               epoch_limit=1000, save_path="parameters/")
