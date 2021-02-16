# ssh client

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.load_system_host_keys()
ssh.connect(hostname='75.68.208.161', username='ucspe', password='ucspe')
print('*')
stdin, stdout, stderr = ssh.exec_command('a')

print(stdout.read())
for line in stdout.read().splitlines():
    print(line)

ssh.close()