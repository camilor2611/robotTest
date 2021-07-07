from RPA.FileSystem import FileSystem

class CopyInWorkSpace():
    def __init__(self, path_root) -> None:
        self.path_root = path_root
        self.path_input = self.path_root + '/input/'
        self.path_output  = self.path_root + '/output/'
        self.file_system = FileSystem()

    def get_main_folders(self):
        return self.path_input, self.path_output

    def copy_files_input_to_output(self) -> None:
        list_files = self.file_system.list_files_in_directory(self.path_input)
        for file in list_files:
            self.file_system.copy_file(file, self.path_output + self.file_system.get_file_name(file))