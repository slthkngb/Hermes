import torch
import logging

def setup_device(prefer_gpu: bool = True):
    if prefer_gpu and torch.cuda.is_available():
        logging.info("Using GPU: " + torch.cuda.get_device_name(0))
        return torch.device("cuda")
    else:
        logging.info("Using CPU")
        return torch.device("cpu")

def check_libraries():
    # Optional: check if certain libraries are installed
    pass
