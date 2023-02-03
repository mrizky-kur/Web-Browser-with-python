import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QAction, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Browser')
        self.setGeometry(100, 100, 800, 600)

        # Add URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)

        # Add web engine view
        self.web_view = QWebEngineView()
        self.web_view.loadFinished.connect(self.update_url_bar)

        # Create navigation actions
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.web_view.back)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.web_view.forward)

        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.web_view.reload)

        # Add navigation actions to the tool bar
        nav_bar = self.addToolBar("Navigation")
        nav_bar.setMovable(False)
        nav_bar.addAction(back_action)
        nav_bar.addAction(forward_action)
        nav_bar.addAction(reload_action)

        # Add URL bar and web engine view to the central widget
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def navigate(self):
        url = QUrl(self.url_bar.text())
        self.web_view.setUrl(url)

    def update_url_bar(self):
        self.url_bar.setText(self.web_view.url().toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
