import templates, sys, os
from PyQt5.QtWidgets import QDialog, QFileDialog
from ui_projtmpl import Ui_ProjTempl

class Application(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProjTempl()
        self.ui.setupUi(self)

        self.templates = templates.Templates(warn_if_empty=False)
        self.setupConnects()

        self.show()

    def setupConnects(self):
        self.infoLocationChanged(0)
        self.ui.infoLocation_comboBox.currentIndexChanged.connect(self.infoLocationChanged)

        self.ui.infoLocationPath.setText("")
        self.ui.templatesInfoPath_btn.clicked.connect(self.infoLocationBtn)

        self.ui.loadData_btn.clicked.connect(self.loadTemplatesInfoBtn)

        self.ui.create_btn.clicked.connect(self.createCopyBtn)

    def infoLocationChanged(self, index):
        if index == 0:
            self.location = "url"
            self.ui.templatesInfoPath_btn.hide()
            self.ui.loadData_btn.show()
        elif index == 1:
            self.location = "local"
            self.ui.templatesInfoPath_btn.show()
            self.ui.loadData_btn.hide()

    def infoLocationBtn(self):
        fileName = QFileDialog.getOpenFileName(self, filter="json(*.json)")[0]
        self.ui.infoLocationPath.setText(fileName)
        self.loadTemplatesInfoBtn()

    def loadTemplatesInfoBtn(self):
        path = str(self.ui.infoLocationPath.text())
    #TODO: Handle errors!!!
        if path != "":
            if self.location == "url":
                self.templates.LoadDataFromUrl(path)
            elif self.location == "local":
                self.templates.LoadLocalData(path)

            self.fillProjectsCombo()


    def fillProjectsCombo(self):
        self.ui.project_comboBox.clear()

        for proj, data in self.templates.data.items():
            self.ui.project_comboBox.addItem(proj)

    def createCopyBtn(self):
        if self.templates.IsTemplateDataLoaded():

            proj = str(self.ui.project_comboBox.currentText())
            dst = str(QFileDialog.getExistingDirectory(self))

            if not dst:
                return

            origin = 0

            if self.ui.url_check.isChecked():
                origin |= templates.URLS
            if self.ui.localFiles_check.isChecked():
                origin |= templates.LOCAL_FILES
            if self.ui.localDir_check.isChecked():
                origin |= templates.LOCAL_DIRS

            self.templates.CopyTemplate(proj, dst, origin)

        else:
            print("Can't create copy. Load template data before.")
