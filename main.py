from config.config import GlobalConfig

CONFIG = GlobalConfig()


def main():
    print('start project')
    print("CONFIG", CONFIG.email_info)


if __name__ == '__main__':
    main()
