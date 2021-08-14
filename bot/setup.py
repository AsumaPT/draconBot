print("Checking required packages")
pkgs = ['websocket-client', 'Pillow', 'requests', 'colorama', 'pypresence', ]

import pip

try:
    for package in pkgs:
        try:
            import package
        except ImportError as e:
                pip.main(['install', package])

    print("OK")
except AttributeError as e:
    print("It seems you pip version is over 10.0, please install the required packages manually, "
          "by executing following command:\n"
          "pip install websocket-client Pillow requests pyqrcode pypng six")
