README

Author: Stefan Elmgren
Date: 2025-03-21 - 2025-04-05

Most of the files in Dist and Build-folders were to big to imnlude in the GIT repository.

Run in VS Code stalarm_2-folder to create app.exe in the dist folder
    pyinstaller --clean --onefile --add-data "app/templates;templates" --add-data "app/static;static" app/app.py

app.exe is uploaded to elmgren.nu
