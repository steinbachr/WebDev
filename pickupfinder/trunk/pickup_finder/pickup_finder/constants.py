class FormattingConstants():
    DATE_FORMAT = '%m/%d/%Y %I:%M%p';

class ChanceAttendingConstants():
    #data source options
    NOT_RESPONDED=  (-1, "not responded")
    DEFINITE     =  (0, "definitely")
    MAYBE        =  (1, "maybe")
    PROBABLY_NOT =  (2, "probably not")
    NOT          =  (3, "nope")
    
    @classmethod
    def choices_for_model(cls):
        return (cls.NOT_RESPONDED, cls.DEFINITE, cls.MAYBE, cls.PROBABLY_NOT, cls.NOT)
    
    @classmethod
    def get_verbose(cls, key):
        for choice in cls.choices_for_model():
            if choice[0] == key:
                return choice[1]
            
class GameTypeConstants():
    SOCCER = (0, "soccer")
    FOOTBALL = (1, "tennis")
    BASKETBALL = (2, "basketball")
    SOFTBALL = (3, "softball")
    BASEBALL = (4, "baseball")
    WIFFLE_BALL = (5, "wiffle ball")
    OTHER = (6, "other")


    @classmethod
    def choices_for_model(cls):
        return (cls.SOCCER, cls.FOOTBALL, cls.BASKETBALL, cls.SOFTBALL, cls.BASEBALL, cls.WIFFLE_BALL, cls.OTHER)

    @classmethod
    def get_verbose(cls, key):
        for choice in cls.choices_for_model():
            if choice[0] == key:
                return choice[1]


class APIKeys():
    FACEBOOK_DEV = "552967234734621"
    FACEBOOK_PROD = "154899554671199"
    GOOGLE = "AIzaSyB9hdim8sfFqodjXTmBsSZ2cpfqaZeSC7Y"
    

        
    
    


