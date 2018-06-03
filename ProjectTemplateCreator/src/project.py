import templates, Application, sys, os
from PyQt5.QtWidgets import QApplication

def ConsoleVersion(arg):

    local_json = os.path.join(os.path.dirname(os.path.realpath(__file__)), templates.DEFAULT_JSON_NAME)
    tmpl = templates.Templates(data_path=local_json, data_url=templates.DEFAULT_JSON_URL)

    if arg == "-h":
        tmpl.Help()
        return

    try:
        proj = sys.argv[2]
    except IndexError:
        print("WARNING: No project template passed, will use default one instead.")
        proj = "default"

    tmpl.CopyTemplate(proj)

def GUIVersion():
    app = QApplication(sys.argv)
    w = Application.Application()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    try:
        arg = sys.argv[1]
    except IndexError:
        arg = ""

    if arg == "-c":
        ConsoleVersion()
    else:
        GUIVersion()
