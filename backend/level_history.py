from datetime import datetime, timedelta

from const import N


class LevelHistory:
    level = {}
    def addLevel(self, level):
        # add with timestamp
        self.level[datetime.now()] = level
    def getLevels(self):
        # clean the dict removin values older than N minutes
        dicNew = {}
        for key in self.level.keys():
            if not (key < datetime.now() - timedelta(minutes=N)):
                dicNew[key] = self.level[key]
        self.level = dicNew
        # return the list of values ordered by timestamp
        ret =  sorted(self.level.items(), key=lambda x: x[0])
        ret = [x[1] for x in ret]
        return ret