import pytest
import os


"""
    Our model should run in the following way:
     src/predictor/main.py -device cpu -batch 8 --load_to_ram
"""
@pytest.mark.parametrize("device,batch,load_to_ram", [
    ("cpu", 8, True),
    ("cpu", 8, False),
    ("cuda:0", 8, True),
    ("cuda:0", 8, False),
])
def test_model_run(device, batch, load_to_ram):
    """
    :param device: cpu or number of gpu
    :param batch: batch size
    :param load_to_ram: if true will load to ram
    :return:
    """
    main_path = "/home/rrubin/PycharmProjects/test-examples/src/predictor/main.py"
    command = "python " + main_path + " -device " + device + " -batch " + str(batch)
    if load_to_ram:
        command = command + " --load_to_ram"
    os.system(command)
