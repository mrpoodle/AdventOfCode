import os
import importlib

globals()["day"] = {}
# import all the scripts
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and not file.startswith("__"):
        globals()["day"][file[3:5]] = {}
        module = importlib.import_module(f"scripts.{file[:-3]}")
        if hasattr(module, "part_1"):
            part_1_func = getattr(module, "part_1")
            globals()["day"][file[3:5]]["1"] = part_1_func
        if hasattr(module, "part_2"):
            part_2_func = getattr(module, "part_2")
            globals()["day"][file[3:5]]["2"] = part_2_func
