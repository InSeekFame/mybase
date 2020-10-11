
# 安装PySide2 : pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyside2
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class MyBase:
    def __init__(self):
        # 从文件中加载UI定义
        qfile_base = QFile('ui/第一个小说界面.ui')
        qfile_base.open(QFile.ReadOnly)
        qfile_base.close()

        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如self.ui.button, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_base)
        self.ui.searchBtn.clicked.connect(self.searchBtnClick)

    def searchBtnClick(self):
        print('search Btn Click...')


if __name__ == "__main__":
    app = QApplication([])
    mybase1 = MyBase()
    mybase1.ui.show()
    mybase1.searchBtnClick()
    app.exec_()
