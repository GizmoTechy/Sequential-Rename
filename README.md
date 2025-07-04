# Sequentially Rename Files

A small rename function I created to handle documents that have the same 
file name during automated copy jobs. This function will allow the files 
to be copied by just appending a (#) to the end of the file name similar 
to how file systems do so. You need to pass the new directory, current 
file name, and the files extension and the function will return the new 
name with (#) if no file with the same name already exists.

If 'test.csv' exists, then the new name would become 'test (1).csv'. This
would also continue increasing the number if the new names already exist:
'test (1).csv', 'test (2).csv', 'test (3).csv', etc. 

### seq_rename(new_directory, current_file_name, file_extension):

Sequentially rename documents on your local or networked file system.  

### pysftp_seq_rename(pysftp.Connection, new_directory, current_file_name, file_extension):

Sequentially rename documents on an FTP/SFTP site using your pysftp 
Connection.

### paramiko_seq_rename(paramiko.SFTPClient, new_directory, current_file_name, file_extension):

Sequentially rename documents on an FTP/SFTP site using your paramiko 
SFTPClient connection.
