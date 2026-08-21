import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
}

def open_application(app_name):
    executable = APPLICATIONS.get(app_name)

    if executable is None:
        return False

    subprocess.Popen([executable])
    return True