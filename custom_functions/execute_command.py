
import subprocess
def execute_command(command):
  process = subprocess.Popen(
    command, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    shell=True)
  output, error = process.communicate()
  return process.returncode, output.decode('utf-8'), error.decode('utf-8')