import pytest
import os


@pytest.mark.parametrize("device,batch,load_to_ram", [
    ("cpu", 8, True),
    ("cpu", 8, False),
    ("cuda:0", 8, True),
    ("cuda:0", 8, False),
])
def test_model_run(device, batch, load_to_ram):
    main_path = "/src/predictor/main.py"
    command = "python " + main_path + " -device " + device + " -batch " + str(batch)
    if load_to_ram:
        command = command + " --load_to_ram"
    os.system(command)