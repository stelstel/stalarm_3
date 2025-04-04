README

Most of the files in Dist and Build-folders were to big to imclude in the GIT repository.

Run in VS Code stalarm_2-folder to create app.exe in the dist folder
    pyinstaller --clean --onefile --add-data "app/templates;templates" --add-data "app/static;static" app/app.py



In command run app.exe from dist

