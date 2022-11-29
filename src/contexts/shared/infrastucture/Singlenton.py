class Singlenton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singlenton, cls).__new__(cls)
        return cls.instance
