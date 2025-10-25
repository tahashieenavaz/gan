from homa import get_device
from .Discriminator import Discriminator
from .Generator import Generator


class DGGAN:
    def __init__(self):
        self.discriminator = Discriminator().to(get_device())
        self.generator = Generator().to(get_device())
