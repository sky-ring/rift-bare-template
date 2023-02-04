from rift import *

# You can import from contracts here
from contracts.bare_template import BaseContract


def deploy():
    init_data = Cell()
    msg, addr = BaseContract.deploy(init_data, amount=2 * 10 ** 8)
    return msg, False
