import subprocess
import os
import sys

def main():
    install_dir = sys.argv[1]
    exe_path = os.path.join(install_dir, "QRScanner.exe")
    subprocess.Popen([exe_path], shell=True)

if __name__ == "__main__":
    main()
