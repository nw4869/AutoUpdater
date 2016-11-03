class Updater:
    def __init__(self, channel, validator, current_version):
        self.validator = validator
        self.channel = channel
        self.currentVersion = current_version

    def update(self):
        """
        validate files and update
        :return:
        """
        version = self.get_latest_version()
        result, error_files = self.validator.validate_all()
        return self._to_version(version, error_files)

    def get_latest_version(self):
        # TODO
        return '0.0.1'

    def has_new_version(self):
        """
        :return: whether has new version (latest version != current version)
        """
        return self.get_latest_version() != self.currentVersion

    def revert(self, version):
        """
        revert old version
        :param version:
        :return:
        """
        result, error_files = self.validator.validate_all()
        return self._to_version(version, error_files)

    def _to_version(self, version, error_files):
        """
        send version and error_files to server, and server return operations (download a file or a patch)
        and file download urls, then apply to the local file system (create/patch/delete)
        :param version:
        :param error_files:
        :return:
        """
        # TODO
        pass

    # def _download_file(self, file):
    #     # TODO
    #     pass
    #
    # def _update_files(self, file_list):
    #     for file in file_list:
    #         self._update_file(file, )
    #
    # def _update_file(self, file, operate):
    #     pass

    def _patch_file(self, file):
        # TODO
        pass

    def _create_file(self, file):
        # TODO
        pass

    def _delete_file(self, file):
        # TODO
        pass