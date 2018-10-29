# Initialize a dummy list of students

class ScoreCard:
    """
    This class defines the EPIC scores of a
    user.
    """

    def __init__(self, name, e_score, p_score, i_score, c_score):
        self.name
        self.e_score
        self.p_score
        self.i_score
        self.c_score

    def get_score(self):
        return self.score

    def __str__(self):
        return "ScoreCard[name=" + self.name + \
                         "epic=" + self.e_score + \
                         "passion" + self.p_score + \
                         "integrity" + self.i_score + \
                         "collaboration" + self.c_score + \
                         "]"


def add_score():
    name = input("Enter students name: ")
    epic_score = input("Enter student epic score: ")
    passion_score = input("Enter student passion score: ")
    interity_score = input("Enter student integrity score: ")
    collaboration_score = input("Enter student collaboration score: ")
    return ScoreCard(name, e_score, p_score, i_score, c_score)

def main():
    scores = []
    scores.append(add_score())
    print(scores)