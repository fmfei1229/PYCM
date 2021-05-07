from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5.QtCore import Qt
from .SendMessageGroupUI import Ui_SendMessageGroupDialog


class SendMessageGroupForm(QDialog):
    def __init__(self, parent=None):
        super(SendMessageGroupForm, self).__init__(parent)
        self.ui = Ui_SendMessageGroupDialog()
        self.parent = parent
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.ui.send_to_selected.setChecked(True)
        self.ui.target_select.show()
        self.ui.send_message_input.clear()
        self.ui.target_list.clear()
        for ip in self.parent.clients.keys():
            new_item = QListWidgetItem(self.parent.get_client_label_by_ip(ip))
            new_item.setData(Qt.UserRole, ip)
            self.ui.target_list.addItem(new_item)
