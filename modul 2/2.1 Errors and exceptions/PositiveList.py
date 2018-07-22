class PositiveList(list):
    def append(self, arg):
        if arg > 0:
            list.append(self, arg)
        else:
            raise NonPositiveError


class NonPositiveError(Exception):
    pass
