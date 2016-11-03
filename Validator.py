import hashlib


class Validator:
    """
    validator files checksum thought given checksum list
    """

    def __init__(self, checksum_list):
        self.checksumList = checksum_list

    def validate_all(self):
        """
        validator files checksum
        :return: tuple: (pass or not, error file list)
        """
        error_files = []
        for file, checksum in self.checksumList:
            if not self._validate(file, checksum):
                error_files.append(file)
        return len(error_files) == 0, error_files

    def _validate(self, file, checksum):
        try:
            return self.__md5(file) == checksum
        except:
            return False

    @staticmethod
    def __md5(file, block_size=64 * 1024):
        with open(file, 'rb') as f:
            md5 = hashlib.md5()
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
        return md5.hexdigest()

if __name__ == '__main__':
    checksum_list = [('test.txt', '5eb63bbbe01eeed093cb22bb8f5acdc3')]
    validator = Validator(checksum_list)
    print(validator.validate_all())