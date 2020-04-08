"""

CUDA
https://www.google.com/search?q=cuda+nvidia

"""

# Check if device/machine supports CUDA
import torch

# If GPU support is available
print(torch.cuda.is_available())

# In case CUDA is available on your machines :)

device = torch.device("cuda")
X = torch.ones(5)

# Use GPU Capabilities to process the data :)
Y = torch.ones_like(X, device=device)