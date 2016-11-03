import Config
import Validator
import Updater


if __name__ == '__main__':
    """
    AutoUpdater Client
    """
    config = Config.Config()
    validator = Validator.Validator(config.get_checksum_list())
    updater = Updater.Updater(config.get_channel(), validator, config.get_current_version())
    print(updater.has_new_version())