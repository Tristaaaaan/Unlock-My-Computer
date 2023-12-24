import paramiko
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
import threading

class MyApp(MDApp):
    def build(self):
        button = MDRoundFlatButton(text='Unlock My Computer!')
        button.bind(on_press=self.unlock_computer)
        return button

    def unlock_computer(self, instance):
    	
    	thread = threading.Thread(target=self.unlock)
    	thread.start()
    
    def unlock(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="192.168.1.199", username="q", password="P@ssW0rd")
        ssh.exec_command('cinnamon-screensaver-command -d')
        ssh.close()

if __name__ == '__main__':
    MyApp().run()

