from pywinauto.application import Application
#start the application
app = Application().start("notepad")

#select the menu item
app.UntitledNotepad.menu_select("Help->About Notepad")
#click the OK button
app.AboutNotepad.OK.click()
#type some text
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
