import os, sys, shutil
import urllib.request as req

URLS = 1 << 0
LOCAL_FILES = 1 << 1
LOCAL_DIRS = 1 << 2
ALL = URLS | LOCAL_FILES | LOCAL_DIRS

class Templates:
    def __init__(self):
        self.data = {
            'p5.js':
            {
            'urls': {
            'index.html': "https://bitbucket.org/Josef21296/various-resources/raw/master/Templates/p5.js-Template/index.html",
            'sketch.js': "https://bitbucket.org/Josef21296/various-resources/raw/master/Templates/p5.js-Template/sketch.js"
                },
            'local_files': {
                'index.html': "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js-Template",
                'sketch.js': "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js-Template"
                },
            'local_dirs': ["F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js-Template"]
            },
            'p5.js-tensorflow.js':
            {
                'urls': {
                'index.html': "https://bitbucket.org/Josef21296/various-resources/raw/39d6cd13f1fd27ec716360ad391d4f758cb0a269/Templates/p5.js%26Tensorflow.js-Template/index.html",
                'sketch.js': "https://bitbucket.org/Josef21296/various-resources/raw/master/Templates/p5.js%26Tensorflow.js-Template/sketch.js"
                    },
                'local_files': {
                    'index.html': "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js&Tensorflow.js-Template",
                    'sketch.js': "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js&Tensorflow.js-Template"
                    },
                'local_dirs': ["F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js&Tensorflow.js-Template"]
            }
            }

    # Copy a template project. Origin determines from where
    #   (ALL: tries to get all the sources available),
    #   (URLS: only search for files hoested online),
    #   (LOCAL_FILES: only searches for defined local single files),
    #   (LOCAL_DIRS: only searches for defined local dirs and copes all files in there)
    def CopyTemplate(self, project, destination=os.getcwd(), origin=ALL):

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

    def Help(self):
        print(" - Help: This script will create a copy of a template into your current directory. \nArguments:")
        print("\t-h: Help.")
        print("\t<none>: Will use p5.js as default.")

        for proj, data in self.data.items():
            print("\t" + proj + ": ")
            print("\t \t-Have urls: " + str('urls' in data))
            print("\t \t-Have local files: " + str('local_files' in data))
            print("\t \t-Have local dirs: " + str('local_dirs' in data))
