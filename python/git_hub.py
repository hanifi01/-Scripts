import subprocess


commit_message = "this is my first push file"
branch = "main"


subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', commit_message])
subprocess.run(['git', 'push', 'origin', branch])
