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
import pickle

from PySide6 import QtCore

logger = logging.getLogger(__name__)

class MyDataBase(QtCore.QObject):
    """
        This is where the abstract model lives. This could be a database with some added
        functionality, or a physics enginge which continually calculates the positions of the
        bodies in a planetary system. This is the core of the app if you will, what the app
        is about. Making visual sense of the abstract data in the Model object is the job of
        the View and Presenter objects. 
    """

    def __init__(self):
        super(MyDataBase, self).__init__()
        # We will use a dictionary to save all edited text.
        self.textDB = {}


    def quit(self):
        """
            This method gets called before the app exits, to give us a chance to exit cleanly
            if this is deemed necessary.
        """
        pass


    def storeTextInMemory(self, date, text):
        if text != '':
            self.textDB[date] = text
            logger.debug('Saved post to database. Key: %s' % date)
            logger.debug('Saved string: "%s".' % text)
        elif date in self.textDB:
            # Storing an empty string is the same as deleting the existing post.
            del self.textDB[date]
            logger.debug('Deleted post from database. Key: %s' % date)


    def getTextFromMemory(self, date):
        if date in self.textDB:
            text = self.textDB[date]
            logger.debug('Retreived post from database. Key: %s' % date)
            logger.debug('Retreived string: "%s".' % text)
        else:
            text = ''
        return text


    def loadDatabaseFromDisk(self, database_file_path):
        f = open(database_file_path, 'rb')
        self.textDB = pickle.load(f)
        f.close()
        # Nope
        

    def saveDatabaseToDisk(self, database_file_path):
        f = open(database_file_path, 'wb')
        pickle.dump(self.textDB, f)
        f.close()