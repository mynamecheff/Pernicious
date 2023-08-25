# Programme is deleted from the computer once it runs, shielding it from detection or analysis.
import os
import tempfile
import subprocess
import time

def main():
    batch_file = os.path.join(tempfile.gettempdir(), next(tempfile._get_candidate_names()) + ".bat")
    current_process_path = os.path.abspath(__file__)

    with open(batch_file, "w") as batch:
        batch.write(f'ping 127.0.0.1 -n 2 > nul && del /f "{current_process_path}" && del "{batch_file}"')

    subprocess.Popen(['cmd.exe', '/C', batch_file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    time.sleep(1)  # Allow some time for the batch file to take effect before exiting
    os._exit(0)  # Terminate the script

if __name__ == "__main__":
    main()
