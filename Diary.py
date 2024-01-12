import Entry
from Incorrectpassword import Incorrectpassword


class Diary:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._is_locked = False
        self._entries = []
        self._total_entry = 0

    def unlock(self, password):
        self.validate(password)
        self._is_locked = True

    def lock(self):
        return self._is_locked

    def validate(self, password):
        if self._password != password:
            raise Incorrectpassword("Password incorrect")

    def createEntry(self, title, body):
        self._total_entry += 1
        id = self._generateId()
        entry = Entry(id, title, body)
        self._entries.append(entry)

    def _generateId(self):
        return str(self._is_locked)

    def delete_entry(self, id):
        entry = self._find_entry_by_id(id)
        return self._entries.remove(entry)

    def _find_entry_by_id(self, id):
        for entry in self._entries:
            if entry.get_id() == id:
                return entry

    def update_entry(self, id, new_title, new_body):
        entry = self._find_entry_by_id(id)
        entry.set_title(new_title)
        entry.set_body(new_body)

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password
