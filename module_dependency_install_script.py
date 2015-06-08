def install_module(package):
    """
    Installs matplotlib for graphing results
    of timing message creation in gone_fishin.py
    """
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
# install 'six' dependency
install_module('six')
install_module('dateutils')
install_module('pyparsing')
install_module('numpy')
install_module('matplotlib')
# refresh sys.path
imp.reload(site)
# import matplotlib after install
import matplotlib.pyplot as plt