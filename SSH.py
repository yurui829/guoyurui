import paramiko
import os


class SSHServer():
    
    def __init__(self,host, username, password):
        self.server_conn = paramiko.SSHClient()
        self.server_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.server_conn.connect(host, username = username, password = password)        

    def open_ssh(self,host, username, password):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(host, username = username, password = password)
        
        return s

    def close(self):
        self.server_conn.close() 
    
    def execute_command(self, command):
        stdin, stdout, stderr = self.server_conn.exec_command(command)

    def copy_file_to_server(self,host, user, source, destination):
        scp_cmd = 'scp -r %s %s@%s:%s' %(source, user, host, destination)
            
        self.exec_local_cmd(scp_cmd)              

    def copy_file_to_checkout(self,host, user, source, destination):
        command = ''' scp %s@%s:%s %s''' %(user, host, source, destination)
        self.exec_local_cmd(command)
    def exec_local_cmd(self,cmd):
    
        os.system(cmd)

class SFTPServer():
    
    def __init__(self,host, username, password):
        self.t = paramiko.Transport((host,22))
        self.t.connect(username = username, password = password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)

    def close(self):
        self.t.close()
    
    def download_file(self, remotepath,localpath):
        self.sftp.get(remotepath, localpath)
 