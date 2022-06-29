import os
from zipfile import ZipFile, ZIP_BZIP2
from pathlib import Path
from argparse import ArgumentParser


class FileCompresser:
    def __init__(self):
        """
          This is the constructor for these class
        """
        self.argument_parser = ArgumentParser()
        self.argument_parser.add_argument('-d', '--directory', required=False,
                                          help="""Path to director/folder you want to compress
                                          e.g ./compressor.py -d directory_path
                                          """)
        self.args = vars(self.argument_parser.parse_args())
        self.file_name = ""
        self.destination = ""
        self.path = os.getcwd()

    def compresser(self):
        try:
            src_directory = Path(self.args['directory']).expanduser().resolve()
            self.file_name = f"{src_directory}.zip"
            with ZipFile(self.file_name, mode='w', compression=ZIP_BZIP2,
                         allowZip64=True) as zipIT:
                for filepath in src_directory.rglob("*"):
                    zipIT.write(filepath, arcname=filepath.relative_to(src_directory))

            self.destination = src_directory
            zipIT.close()
            return f"Successfully compressed File Saved to: {self.destination}"

        except TypeError:
            return "Path to folder not specified. Try Again Passing directory/folder name as an Argument."


if __name__ == '__main__':
    compress = FileCompresser()
    result = compress.compresser()
    print(result)

