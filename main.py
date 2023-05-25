import sys
import time
import pyautogui
import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from ui.main_ui import Ui_MainWindow
from selenium import webdriver
import GState

global driver


def on_press():
    print('按键 {} 被按下了。')


class MainWindows(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.driver = None
        self.option = None
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.log_button.clicked.connect(self.log_in)
        self.update_button.clicked.connect(self.load_pack)
        self.web_button.clicked.connect(self.open_web)
        self.restart_button.clicked.connect(self.restart)

        self.account_edit.setText(GState.user_name)
        self.passwor_edit.setText(GState.password)
        self.url_edit.setText(GState.global_url)
        self.addr_edit.setText(GState.firmware_path)
        self.show()

    def open_web(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.option.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.maximize_window()
        self.driver.get(self.url_edit.text())

    def log_in(self):
        try:
            text_label = self.driver.find_element(By.ID, 'account')
            text_label.clear()
            text_label.send_keys(self.account_edit.text())
            text_label = self.driver.find_element(By.ID, 'loginPwd')
            text_label.clear()
            text_label.send_keys(self.passwor_edit.text())
            self.click_button('btLogin')
        except:
            print('error')

    def click_button(self, find_id):
        time.sleep(0.1)
        try:
            button = self.driver.find_element(By.ID, find_id)
            button.click()
        except:
            print("click button error")
        time.sleep(0.1)

    def restart(self):
        self.click_button('navIbmcManager')
        self.click_button('leftUpgradeConfig')
        self.click_button('restBut')
        self.click_button('resetOpen_ok_btn')

    def load_pack(self):
        self.click_button('navIbmcManager')
        self.click_button('leftUpgradeConfig')
        self.click_button('firmwareTabs_upgradeManual_a')
        # file_input = self.driver.find_element(By.ID, 'uploadConfig_list')
        # file_input.send_keys(self.addr_edit.text())
        self.click_button('uploadConfig_select')
        time.sleep(1)
        pyperclip.copy(GState.firmware_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter', presses=1)
        time.sleep(0.5)
        self.click_button('modeButton')
        self.click_button('startUp_ok_btn')
        self.click_button('navSystemManager')
        self.click_button('systemInfoOthers')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_windows = MainWindows()
    sys.exit(app.exec_())
