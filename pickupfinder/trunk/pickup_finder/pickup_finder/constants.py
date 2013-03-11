class DataSourceConstants():
    #data source options
    CROWD = (0, "crowdsourced")
    SCRAPED = (1, "scraped")
    
    @classmethod
    def choices_for_model(cls):
        return (cls.CROWD, cls.SCRAPED)
    
    


