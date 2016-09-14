import sys
from SvrApplication import Application

def main(app):
    ServerApplication = Application()
    ServerApplication.start()

if __name__ == "__main__":
    main(sys.argv)


