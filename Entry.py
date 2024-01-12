class Entry:
    def __init__(self, entryId, entryTitle, entryBody):
        self._entryId = entryId
        self._entryTitle = entryTitle
        self._entryBody = entryBody

    def get_id(self):
        return self._entryId

    def set_title(self, title):
        self._entryTitle = title

    def set_body(self, body):
        self._entryBody += " " + body

    def get_body(self):
        return self._entryBody





