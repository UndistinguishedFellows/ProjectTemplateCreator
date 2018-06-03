import os, sys, shutil, json
import urllib.request as req

URLS = 1 << 0
LOCAL_FILES = 1 << 1
LOCAL_DIRS = 1 << 2
ALL = URLS | LOCAL_FILES | LOCAL_DIRS

DEFAULT_JSON_URL = "https://bitbucket.org/Josef21296/various-resources/raw/55ac88d9f8d97a4649b67cf70596f8bcd16af066/Templates/templates_source.json"
DEFAULT_JSON_NAME = "templates_source.json"

class Templates:
# Creates the Templates object. Templates origin can be passed as parameter; if both local and hosted are provided, hosted one will be used.
    def __init__(self, data_path="", data_url="", warn_if_empty=True):

        # Will priorize online hosted one
        if data_url != "":
            self.LoadDataFromUrl(data_url)
        elif data_path != "":
            self.LoadLocalData(data_path)
        else:
            if warn_if_empty == True:
                print("WARNING: No template info provided.")
            self.data = 0


# Loads the templates data from a local json file.
    def LoadLocalData(self, path):
        print("Loading templates data from local json: " + path);
        with open(path) as file_data:
            self.data = json.load(file_data)

# Loads the templates data from a hosted json file.
    def LoadDataFromUrl(self, url):
        print("Loading templates data from hosted json: " + url);
        with req.urlopen(url) as res:
            self.data = json.loads(res.read())

    def IsTemplateDataLoaded(self):
        return self.data != 0


# Copy a template project. Origin determines from where
#   (ALL: tries to get all the sources available),
#   (URLS: only search for files hoested online),
#   (LOCAL_FILES: only searches for defined local single files),
#   (LOCAL_DIRS: only searches for defined local dirs and copes all files in there)
    def CopyTemplate(self, project, destination=os.getcwd(), origin=ALL):

        if not self.data:
            print("ERROR: Templates data not loaded!")
            return

        if project == "default":
            try:
                project = self.data['default']
            except KeyError:
                print("ERROR: Default key not setted.")
                return

        if project in self.data:
            print("Creating project from template: " + project)

            template = self.data[project]

            if origin & URLS and 'urls' in template:
                print("Getting templates from URLS")
                for file, url in template['urls'].items():
                    self.CopyFileFromUrl(url, file, destination)

            if origin & LOCAL_FILES and 'local_files' in template:
                print("Getting templates from LOCAL_FILES")
                for file, dir in template['local_files'].items():
                    self.CopyFileFromLocal(file, dir, destination)

            if origin & LOCAL_DIRS and 'local_dirs' in template:
                print("Getting templates from LOCAL_DIRS")
                for dir in template['local_dirs']:
                    self.CopyFilesFromDir(dir, destination)

        else:
            print("ERROR: Project not found... [" + project + "].")

# Copy a single file from the url
    def CopyFileFromUrl(self, url, dst_file, dst_dir):
        with req.urlopen(url) as response, open(os.path.join(dst_dir, dst_file), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

# Copy a single src file from local src directory to a dst directory
    def CopyFileFromLocal(self, src_file, src_dir, dst_dir):
        if os.path.isfile(os.path.join(src_dir, src_file)):
            shutil.copy(os.path.join(src_dir, src_file), os.path.join(dst_dir, src_file))

# Copy all files from a src directory into the des directory
    def CopyFilesFromDir(self, src_dir, dst_dir):
        for file_name in os.listdir(src_dir):
            file = os.path.join(src_dir, file_name)
            if os.path.isfile(file):
                shutil.copy(file, os.path.join(dst_dir, file_name))

# Displays the help info about the application and list all the templates abailable
    def Help(self):
        print(" - Help: This script will create a copy of a template into your current directory. \nArguments:")
        print("\t-h: Help.")
        print("\t<none>: Will use p5.js as default.")

        print("--------------------------------------------")

        for proj, data in self.data.items():
            if proj == "default":
                print("\tDefault: " + str(data))
            else:
                print("\t" + proj + ": ")
                print("\t \t-Have urls: " + str('urls' in data))
                print("\t \t-Have local files: " + str('local_files' in data))
                print("\t \t-Have local dirs: " + str('local_dirs' in data))

            print("--------------------------------------------")
