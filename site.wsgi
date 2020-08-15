import os, sys
activate_this = '/home/a0218470/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a0218470/domains/mlstmarket.com/public_html/'))
from myapp import app as application
if __name__ == "__main__":
    application.run()