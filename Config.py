class Config:
    """
    version, channel information and file checksum list
    """
    def __init__(self):
        self.checksumList = []

    def set_checksum_list(self, checksum_list):
        self.checksumList = checksum_list

    def get_checksum_list(self):
        return self.checksumList

    def get_current_version(self):
        return '0.0.1'

    def set_current_version(self, version):
        pass

    def get_channel(self):
        return 'stable'

    def set_channel(self, channel):
        pass
