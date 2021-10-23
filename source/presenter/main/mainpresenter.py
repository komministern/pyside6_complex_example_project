"""
Copyright (C) 2021 Oscar Franzén <oscarfranzen@protonmail.com>

This file is part of PySide6 Complex Example Project.

PySide6 Complex Example Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySide6 Complex Example Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySide6 Complex Example Project.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
import os.path

from PySide6 import QtCore, QtGui, QtWidgets

logger = logging.getLogger(__name__)

class MainPresenter(QtCore.QObject):
    """
        The Presenter object contains the intelligence of the GUI. That is, here
        resides the interactions between the widgets in the View object. The Presenter
        acts upon signals sent from both the View and the Model.

        The Presenter object has access to both the View and Model objects, so its
        actions takes the form of method calls to these.
    """

    update_calendar = QtCore.Signal(list)

    def __init__(self, model, view, app):
        super(MainPresenter, self).__init__()

        # Store view, model and app.
        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

        # # We must have a record of the previously selected date, when a new date is clicked on.
        self.prieviously_selected_date = self.selected_date

        self.changes_made_to_current_post = False
        self.changes_made_to_database = False

    @property
    def selected_date(self):
        return self.view.mainwindow.calendarWidget.selectedDate()


    def connectSignals(self):
        """
            Here we connect the signals from both Model and View to methods in the
            Presenter object.
        """
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.pushButton_LoadDB.pressed.connect(self.loadDatabase)
        self.view.mainwindow.pushButton_SaveDB.pressed.connect(self.saveDatabase)
        self.view.mainwindow.pushButton_Commit.pressed.connect(self.commitPost)
        self.view.mainwindow.textEdit_Post.textChanged.connect(self.textChanged)
        self.view.mainwindow.calendarWidget.clicked.connect(self.newDateSelected)


    def textChanged(self):
        self.changes_made_to_current_post = True
        self.updateStates()
        self.updateCharacterInPostCounter()


    def commitPost(self):
        # Get the text from the text editor...
        selected_date_text = self.view.mainwindow.textEdit_Post.toPlainText()

        # ... and save it to the database.
        self.model.database.storeTextInMemory(self.selected_date, selected_date_text)

        # self.model.database.changes_made_to_database_in_memory = True
        self.changes_made_to_database = True
        self.changes_made_to_current_post = False

        self.updateCalendar()
        self.updatePostCounter()
        self.updateStates()
    

    def newDateSelected(self, new_date):
        """
            This method is called when the calendarwidget sends the clicked signal. And this 
            happens when the user has clicked on a valid date. The date is sent as an argument 
            with the signal.
        """

        if self.changes_made_to_current_post:
            button = QtWidgets.QMessageBox.warning(self.view.mainwindow, 'Unsaved changes in post', 'There are changes made to this post that will be lost. Proceed anyway?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if button == QtWidgets.QMessageBox.StandardButton.Yes:
                new_text = self.model.database.getTextFromMemory(new_date)
                self.view.mainwindow.textEdit_Post.setPlainText(new_text)
                # Move the cursor to the end of the text for good measure.
                self.view.mainwindow.textEdit_Post.moveCursor(QtGui.QTextCursor.End)
                self.prieviously_selected_date = new_date
                self.changes_made_to_current_post = False
            else:
                self.view.mainwindow.calendarWidget.setSelectedDate(self.prieviously_selected_date)
                self.changes_made_to_current_post = True
        else:
            new_text = self.model.database.getTextFromMemory(new_date)
            self.view.mainwindow.textEdit_Post.setPlainText(new_text)
            # Move the cursor to the end of the text for good measure.
            self.view.mainwindow.textEdit_Post.moveCursor(QtGui.QTextCursor.End)
            self.prieviously_selected_date = new_date
            self.changes_made_to_current_post = False
        self.updateCharacterInPostCounter()
        self.updateStates()


    def updateStates(self):
        self.view.mainwindow.label_ChangesMadeToCurrentPost.setText(str(self.changes_made_to_current_post))
        self.view.mainwindow.label_ChangesMadeToDatabase.setText(str(self.changes_made_to_database))


    def updateCalendar(self):
        dates_with_content = list(self.model.database.textDB.keys())
        self.view.mainwindow.calendarWidget.setGreenDates(dates_with_content)
        self.view.mainwindow.calendarWidget.updateCell(self.selected_date)


    def updateCharacterInPostCounter(self):
        number_of_characters_in_current_post = len(self.view.mainwindow.textEdit_Post.toPlainText())
        self.view.mainwindow.label_NumberOfChars.setNum(number_of_characters_in_current_post)


    def updatePostCounter(self):
        number_of_posts_in_database = len(self.model.database.textDB)
        self.view.mainwindow.label_NumberOfPosts.setNum(number_of_posts_in_database)


    def loadDatabase(self):
        if self.changes_made_to_current_post and self.changes_made_to_database:
            text = 'There are changes made to both this post and the database that will be lost. Proceed anyway?'
        elif self.changes_made_to_current_post and not self.changes_made_to_database:
            text = 'There are changes made to both this post that will be lost. Proceed anyway?'
        elif not self.changes_made_to_current_post and self.changes_made_to_database:
            text = 'There are changes made to the database that will be lost. Proceed anyway?'
        
        proceed = True
        if self.changes_made_to_database or self.changes_made_to_current_post:
            button = QtWidgets.QMessageBox.warning(self.view.mainwindow, 'Unsaved changes', text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if button == QtWidgets.QMessageBox.StandardButton.No:
                proceed = False
        
        if proceed:
            database_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.view.mainwindow, 'Open Database File', os.path.expanduser('~'), 'Database (*.db)')
            if database_file_path:
                try:
                    self.model.database.loadDatabaseFromDisk(database_file_path)
                    current_text_from_new_database = self.model.database.getTextFromMemory(self.selected_date)
                    self.view.mainwindow.textEdit_Post.setPlainText(current_text_from_new_database)

                    self.changes_made_to_current_post = False
                    self.changes_made_to_database = False

                    self.updateCalendar()
                    self.updatePostCounter()
                    self.updateCharacterInPostCounter()
                    self.updateStates()

                except Exception as e:
                    QtWidgets.QMessageBox.critical(self.view.mainwindow, 'Unable to load database', repr(e))


    def saveDatabase(self):
        proceed = True
        if self.changes_made_to_current_post:
            button = QtWidgets.QMessageBox.warning(self.view.mainwindow, 'Unsaved changes', 'The changes made to the current post will not be saved to disk if not committed first. Proceed anyway?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            
            if button == QtWidgets.QMessageBox.StandardButton.No:
                proceed = False

        if proceed:
            database_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.view.mainwindow, 'Save Database File', os.path.expanduser('~'), 'Database (*.db)')
            if database_file_path:
                try:
                    self.model.database.saveDatabaseToDisk(database_file_path)
                    self.changes_made_to_database = False
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self.view.mainwindow, 'Unable to save database', repr(e))

    
    def quit(self):
        """
            This method should always be called when exiting the app. If data needs
            to be saved, or the user needs to be asked for some action prior to exiting,
            here is where it should happen.
        """

        if self.changes_made_to_current_post and self.changes_made_to_database:
            text = 'There are changes made to both this post and the database that will be lost. Proceed anyway?'
        elif self.changes_made_to_current_post and not self.changes_made_to_database:
            text = 'There are changes made to both this post that will be lost. Proceed anyway?'
        elif not self.changes_made_to_current_post and self.changes_made_to_database:
            text = 'There are changes made to the database that will be lost. Proceed anyway?'

        proceed = True

        if self.changes_made_to_current_post or self.changes_made_to_database:
            button = QtWidgets.QMessageBox.warning(self.view.mainwindow, 'Unsaved changes', text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if button == QtWidgets.QMessageBox.StandardButton.No:
                proceed = False

        if proceed:
            # Give the model a chance to make a clean exit.
            self.model.quit()

            # This line exits the application.
            QtWidgets.QApplication.quit()
