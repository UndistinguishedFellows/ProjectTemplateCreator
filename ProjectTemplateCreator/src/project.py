#import templates

import os, sys, shutil
import urllib.request

P5_PATH = "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js-Template"
P5_TENSORFLOW_PATH = "F:\Documents\GitHub\ProjectTemplateCreator\ProjectTemplateCreator\p5.js&Tensorflow.js-Template"

def CreateTemplate(src):

    pwd = os.getcwd()
    print("Will create the template copy into: " + pwd)

    for file_name in os.listdir(src):
        file = os.path.join(src, file_name)
        if(os.path.isfile(file)):
            dst_file = os.path.join(pwd, file_name)
            print("\t - Copying [" + file + "] into [" + dst_file + "].")
            shutil.copy(file, dst_file)

def Help():
    print(" - Help: This script will create a copy of a template into your current directory. \nArguments:")
    print("\t[-p5]: Creates a full p5.js template.")
    print("\t[-t]: Creates a full p5.js template with tensorflow.js.")
    print("\t[-h]: Help.")
    print("\t[<none>]: Will use -p5 as default.")

def GetTemplateFromURL(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        #print("URL: " + url)
        #print("file_name: " + file_name)
        print(response)
        shutil.copyfileobj(response, out_file)


if __name__ == "__main__":

    #GetTemplateFromURL("https://bitbucket.org/Josef21296/various-resources/raw/master/Templates/p5.js-Template/index.html", "index.html")
    #sys.exit()

    try:
        arg = sys.argv[1]
    except IndexError:
        print("WARNING: No template type argument passed, will use default one instead [-p5].")
        arg = "-p5"

    template = ""
    if arg == "-p5":
        template = P5_PATH
    elif arg == "-t":
        template = P5_TENSORFLOW_PATH
    elif arg == "-h":
        Help()
        sys.exit()
    else:
        print("ERROR: Invalid argument.")
        sys.exit()

    CreateTemplate(template)
