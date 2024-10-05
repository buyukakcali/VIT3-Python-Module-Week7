from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QApplication, QMessageBox, QLineEdit
from PyQt6.QtWidgets import QWidget

from UI_Files.settings_ui import Ui_FormSettings
import my_functions as myf
from my_classes import Config


class SettingsPage(QWidget):
    def __init__(self, current_user):
        super().__init__()
        self.current_user = current_user

        self.form_settings = Ui_FormSettings()
        self.form_settings.setupUi(self)

        # Persistent form settings activated at startup:

        # Initial load view settings:
        self.form_settings.gridFrameUserInfo.close()
        self.form_settings.gridFrameChangePassword.close()

        # Connect signals to slots
        self.form_settings.pushButtonChangeAInfo.clicked.connect(self.change_account_information_menu)
        self.form_settings.pushButtonChangePassword.clicked.connect(self.change_password_menu)
        self.form_settings.pushButtonCAIApprove.clicked.connect(self.change_account_information)
        self.form_settings.pushButtonCAICancel.clicked.connect(self.back_to_options)
        self.form_settings.pushButtonCPApprove.clicked.connect(self.change_password)
        self.form_settings.pushButtonCPCancel.clicked.connect(self.back_to_options)
        self.form_settings.pushButtonExit.clicked.connect(self.app_exit)

    def change_account_information_menu(self):
        try:
            self.form_settings.frameOptions.close()
            self.form_settings.gridFrameChangePassword.close()
            self.form_settings.gridFrameUserInfo.show()

            self.form_settings.lineEditUser.setPlaceholderText('Username :   '+ self.current_user[0])
            self.form_settings.lineEditAccountType.setPlaceholderText('Authority :   ' + self.current_user[2])
            self.form_settings.lineEditUserName.setPlaceholderText('Name      :   ' + self.current_user[3])
            self.form_settings.lineEditUserSurname.setPlaceholderText('Surname :   ' + self.current_user[4])
            self.form_settings.lineEditUserName.setEnabled(True)
            self.form_settings.lineEditUserSurname.setEnabled(True)

            # Event filter'i aktif ediyoruz
            # QLineEdit widget'larını bulma ve eventFilter ekleme
            for widget in self.findChildren(QLineEdit):
                widget.installEventFilter(self)
        except Exception as e:
            raise Exception(f"Error occurred in change_account_information_menu method: {e}")

    def change_account_information(self):
        try:
            cnf = Config()
            data_to_update = {
                "UName": self.form_settings.lineEditUserName.text().strip(),
                "USurname": self.form_settings.lineEditUserSurname.text().strip()
            }

            # Boş olmayan alanları alıyoruz
            non_empty_fields = {key: value for key, value in data_to_update.items() if value}

            # Eğer güncellenecek veri yoksa işlemi bitiriyoruz
            if not non_empty_fields:
                header = 'Bilgi:'
                message_text = 'Herhangi bir verinizi degistirmediniz!'
                myf.set_info_dialog(self, header, message_text)
                self.back_to_options()
                print("No data to update!")
                return

            reply = QMessageBox.question(self, 'Hesap Bilgileri Guncelleme', 'Veri degisikliklerini onayliyor musunuz?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                # Dinamik sorgu oluşturma
                set_clause = ", ".join([f"{key} = %s" for key in non_empty_fields])
                values = list(non_empty_fields.values())
                values.append(self.current_user[0])

                q1 = f"UPDATE users SET {set_clause} WHERE Username = %s"

                # Sorguyu çalıştırma
                try:
                    result = myf.execute_write_query(cnf.open_conn(), q1, tuple(values))
                    if result:
                        header = "Bilgi:"
                        message_text = "Bilgileriniz basariyla guncellenmistir!"
                        myf.set_info_dialog(self, header, message_text)
                        if data_to_update['UName']:
                            self.current_user[3] = data_to_update['UName']
                        if data_to_update['USurname']:
                            self.current_user[4] = data_to_update['USurname']
                        self.form_settings.lineEditUserName.setText('')
                        self.form_settings.lineEditUserSurname.setText('')
                        self.form_settings.lineEditUserName.setPlaceholderText('User Name      :   ' + self.current_user[3])
                        self.form_settings.lineEditUserSurname.setPlaceholderText('User Surname :   ' + self.current_user[4])


                except Exception as e:
                    raise  Exception(f"Error updating user information: {e}")
            self.back_to_options()
        except Exception as e:
            raise Exception(f"Error occurred in change_account_information method: {e}")

    def change_password_menu(self):
        try:
            self.form_settings.frameOptions.close()
            self.form_settings.gridFrameUserInfo.close()
            self.form_settings.gridFrameChangePassword.show()

            # Parolaların gizlenmesi için EchoMode.Password ayarlanıyor
            self.form_settings.lineEditCurrentPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.form_settings.lineEditNewPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.form_settings.lineEditNewPass2.setEchoMode(QLineEdit.EchoMode.Password)

            # textChanged sinyalini bir fonksiyona bağlıyoruz
            self.form_settings.lineEditNewPass.textChanged.connect(self.check_password_match)
            self.form_settings.lineEditNewPass2.textChanged.connect(self.check_password_match)
        except Exception as e:
            raise Exception(f"Error occurred in change_password_menu method: {e}")

    def check_password_match(self):
        try:
            # Yeni parola ile doğrulama parolasını karşılaştırıyoruz
            new_pass = self.form_settings.lineEditNewPass.text().strip()
            new_pass2 = self.form_settings.lineEditNewPass2.text().strip()

            if len(new_pass2) == 0:
                self.form_settings.lineEditNewPass.setStyleSheet("""
                                        QLineEdit { color: rgb(255, 255, 255);
                                                    border: 2px solid rgba(38, 38, 48,20);
                                                    border-radius: 15px;
                                                    padding-left: 15px;
                                                    background-color: rgba(36, 36, 36,0);
                                                    background-color: rgb(170, 170, 127); 
                                        }
                                        """)
            elif len(new_pass) != 0 and new_pass == new_pass2:
                self.form_settings.lineEditNewPass.setStyleSheet("""
                            QLineEdit { color: green;
                                        border: 2px solid rgba(38, 38, 48,20);
                                        border-radius: 15px;
                                        padding-left: 15px;
                                        background-color: rgba(36, 36, 36,0);
                                        background-color: rgb(170, 170, 127); 
                            }
                            """)
                self.form_settings.lineEditNewPass2.setStyleSheet("""
                            QLineEdit { color: green;
                                        border: 2px solid rgba(38, 38, 48,20);
                                        border-radius: 15px;
                                        padding-left: 15px;
                                        background-color: rgba(36, 36, 36,0);
                                        background-color: rgb(170, 170, 127); 
                            }
                            """)
            else:
                self.form_settings.lineEditNewPass.setStyleSheet("""
                            QLineEdit { color: red;
                                        border: 2px solid rgba(38, 38, 48,20);
                                        border-radius: 15px;
                                        padding-left: 15px;
                                        background-color: rgba(36, 36, 36,0);
                                        background-color: rgb(170, 170, 127);
                            }
                            """)
                self.form_settings.lineEditNewPass2.setStyleSheet("""
                            QLineEdit { color: red;
                                        border: 2px solid rgba(38, 38, 48,20);
                                        border-radius: 15px;
                                        padding-left: 15px;
                                        background-color: rgba(36, 36, 36,0);
                                        background-color: rgb(170, 170, 127); 
                            }
                            """)
        except Exception as e:
            raise Exception(f"Error occurred in check_password_match method: {e}")

    def change_password(self):
        try:
            cnf = Config()

            current_pass = self.form_settings.lineEditCurrentPass.text().strip()
            new_pass = self.form_settings.lineEditNewPass.text().strip()
            new_pass2 = self.form_settings.lineEditNewPass2.text().strip()

            if not myf.check_password(current_pass, self.current_user[1].encode('utf-8')):
                header = "Hata:"
                message_text = "Eski parolanizi dogru giriniz!"
                myf.set_info_dialog(self, header, message_text)
            else:
                if new_pass == new_pass2:
                    header = "Bilgi:"
                    message_text = "Parolaniz basariyla degistirildi."

                    reply = QMessageBox.question(self, 'Hesap Bilgileri Guncelleme',
                                                 'Veri degisikliklerini onayliyor musunuz?',
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                 QMessageBox.StandardButton.No)

                    if reply == QMessageBox.StandardButton.Yes:
                        q1 = "UPDATE users SET Password = %s WHERE Username = %s"
                        parameters = (myf.hash_password(new_pass), self.current_user[0])

                        try:
                            result = myf.execute_write_query(cnf.open_conn(), q1, parameters)
                            if result:
                                myf.set_info_dialog(self, header, message_text)

                                self.form_settings.lineEditCurrentPass.setText('')
                                self.form_settings.lineEditNewPass.setText('')
                                self.form_settings.lineEditNewPass2.setText('')
                                self.form_settings.lineEditCurrentPass.setPlaceholderText('Current Password')
                                self.form_settings.lineEditNewPass.setPlaceholderText('New Password')
                                self.form_settings.lineEditNewPass2.setPlaceholderText('New Password (Again)')
                                self.back_to_options()
                        except Exception as e:
                            raise Exception(f"Error changing the password: {e}")
                    else:
                        self.back_to_options()

                else:
                    header = "Hata:"
                    message_text = "Yeni girilen parolalar eslesmiyor!"
                    myf.set_info_dialog(self, header, message_text)
        except Exception as e:
            raise Exception(f"Error occurred in change_password method: {e}")

    def back_to_options(self):
        self.form_settings.gridFrameUserInfo.close()
        self.form_settings.gridFrameChangePassword.close()
        self.form_settings.frameOptions.show()

    def eventFilter(self, source, event):
        # FocusIn olayını yakalama
        if event.type() == QEvent.Type.FocusIn:
            if isinstance(source, QLineEdit):  # Eğer source bir QLineEdit ise
                if source == self.form_settings.lineEditUserName:
                    self.form_settings.lineEditUserName.setPlaceholderText('')
                elif source == self.form_settings.lineEditUserSurname:
                    self.form_settings.lineEditUserSurname.setPlaceholderText('')
        return super().eventFilter(source, event)

    def app_exit(self):
        try:
            self.close()
        except Exception as e:
            raise Exception(f"Error occurred in app_exit method: {e}")

if __name__ == "__main__":
    app = QApplication([])
    main_window = SettingsPage(['a', '$2b$12$U67LNgs5U7xNND9PYczCZeVtQl/Hhn6vxACCOxNpmSRjyD2AvKsS2', 'admin', 'Fatih', 'BUYUKAKCALI'])
    main_window.show()
    app.exec()
