class ChanceAttendingConstants():
    #data source options
    NOT_RESPONDED=  (-1, "na")
    DEFINITE     =  (0, "definitely")
    MAYBE        =  (1, "maybe")
    PROBABLY_NOT =  (2, "probably not")
    NOT          =  (3, "nope")
    
    @classmethod
    def choices_for_model(cls):
        return (cls.NOT_RESPONDED, cls.DEFINITE, cls.MAYBE, cls.PROBABLY_NOT, cls.NOT)
    
    


