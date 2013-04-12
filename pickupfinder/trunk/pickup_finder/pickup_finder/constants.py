class Constants():    
    @classmethod
    def get_verbose(cls, key):
        for choice in cls.choices_for_model():
            if choice[0] == key:
                return choice[1]

class FormattingConstants():
    DATE_FORMAT = '%m/%d/%Y %I:%M%p';

class ChanceAttendingConstants(Constants):
    #data source options
    NOT_RESPONDED=  (-1, "not responded")
    DEFINITE     =  (0, "definitely")
    MAYBE        =  (1, "maybe")
    PROBABLY_NOT =  (2, "probably not")
    NOT          =  (3, "nope")
    
    @classmethod
    def choices_for_model(cls):
        return (cls.NOT_RESPONDED, cls.DEFINITE, cls.MAYBE, cls.PROBABLY_NOT, cls.NOT)
            
class GameTypeConstants(Constants):
    SOCCER = (0, "soccer")
    FOOTBALL = (1, "tennis")
    BASKETBALL = (2, "basketball")
    SOFTBALL = (3, "softball")
    BASEBALL = (4, "baseball")
    WIFFLE_BALL = (5, "wiffle ball")
    VOLLEYBALL = (6, "volleyball")
    OTHER = (7, "other")

    @classmethod
    def choices_for_model(cls):
        return (cls.SOCCER, cls.FOOTBALL, cls.BASKETBALL, cls.SOFTBALL, cls.BASEBALL, cls.WIFFLE_BALL, cls.VOLLEYBALL, cls.OTHER)
    
            
class NotificationTypeConstants(Constants):
    PLAYER_JOINED = (0, lambda player_game,game: "%s\'s status is now %s for the %s game at %s" % (player_game.player.name, player_game.verbose_status, game.verbose_game_type, game.normalized_location))
    GAME_CREATED = (1, lambda player_game,game: "A new public game taking place %s at %s created" % (game.starts_at, game.normalized_location))

    @classmethod
    def choices_for_model(cls):
        return (cls.PLAYER_JOINED,cls.GAME_CREATED)


class APIKeys():
    FACEBOOK_DEV = "552967234734621"
    FACEBOOK_PROD = "154899554671199"
    GOOGLE = "AIzaSyB9hdim8sfFqodjXTmBsSZ2cpfqaZeSC7Y"
    

        
    
    


