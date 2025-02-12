
class Player:
    _name : str
    _score : int

    def init(self, name):
        self._name = name
        self._score = 0

    def getName(self) -> str:
        return self._name

    def getScore(self) -> int:
        return self._score

    def setScore(self,new_score) -> None:
        self._score = new_score
