import platform
import os

system_type = platform.system()
if system_type == "Windows":
    os.system("del config.pkl")
    os.system("copy defaultConfig.pkl .\config.pkl")
if system_type == "Linux":
    os.system("rm -rf config.pkl")
    os.system("cp defaultConfig.pkl .\config.pkl")