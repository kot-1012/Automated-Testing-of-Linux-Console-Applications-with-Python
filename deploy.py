from sshcheckers import ssh_checkout, upload_files


def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "A123B456!!", "tests/google-chrome-stable_current_amd64.deb", "/home/user2/google-chrome-stable_current_amd64.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "A123B456!!", "echo 'A123B456!!' | sudo -S dpkg -i /home/user2/google-chrome-stable_current_amd64.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "A123B456!!", "echo 'A123B456!!' | sudo -S dpkg -s google-chrome-stable_current_amd64",
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
