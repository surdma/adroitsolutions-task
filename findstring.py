import os


class FindString:
    def __init__(self):
        """findstring class construtor"""
        self.path = os.getcwd()
        self.filepath = ""
        self.file_extension = ""
        self.sub_folder = ""

    def searchstring(self, folder_name, text):
        if folder_name == "":
            walker = os.walk(self.path, folder_name)
        else:
            walker = os.walk(folder_name)
        if walker:
            for (base_folder, sub_folders, files) in walker:
                self.sub_folder = sub_folders
                for file in files:
                    self.filepath = os.path.join(base_folder, file)
                    self.file_extension = os.path.splitext(self.filepath)[-1].lower()

                    if self.file_extension == ".txt":
                        with open(self.filepath, 'r') as test_file:
                            for line_number, line in enumerate(test_file):
                                line = line.lower()
                                if word in line:
                                    print(f"{text} text found in: {self.filepath} file on line number {line_number}")


if __name__ == '__main__':
    test = FindString()
    word = input("input text: ").lower()
    while word == "" or word.isspace():
        print("Invalid input")
        word = input("input text: ").lower()

    print("default directory is the current working directory.")
    folder = input("Input folder search path: ")
    if folder:
        test.searchstring(folder_name=folder, text=word)
    else:
        print("Directory not found")
