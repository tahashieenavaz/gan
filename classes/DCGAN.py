from homa import get_device, settings


class DGGAN:
    def __init__(self):
        self.discriminator = Discriminator().to(get_device())
        self.generator = Generator().to(get_device())
