import os
import hashlib


class DuplicateRemover:
    def __init__(self):
        """Duplicate remover constructor."""
        self.path = os.getcwd()
        self.walk = os.walk(self.path)
        self.uniqueFiles = dict()
        self.deletefiles = ""
        self.sub_folder = ""

    def deleteduplicate(self):
        for (folder, sub_folders, files) in self.walk:
            self.sub_folder = sub_folders
            for file in files:
                filepath = os.path.join(folder, file)
                hashfile = hashlib.sha256(open(filepath, 'rb').read()).hexdigest()
                if hashfile in self.uniqueFiles:
                    print(f"{filepath} has been deleted")
                    os.remove(filepath)
                    self.deletefiles = hashfile
                else:
                    self.uniqueFiles[hashfile] = self.path

        if len(self.deletefiles) < 1:
            print("No file deleted")
            print(f"{len(self.uniqueFiles)} files currently in {self.path}")
        else:
            print(f"{len(self.deletefiles)} files deleted")


if __name__ == '__main__':
    test = DuplicateRemover()
    test.deleteduplicate()
