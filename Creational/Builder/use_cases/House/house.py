class House:
    def __init__(self):
        self.walls: str | None = None
        self.roof: str | None = None
        self.doors: str | None = None
        self.windows: str | None = None
        self.finish: bool | None = False

    def __setattr__(self, name, value):
        """
        When any attribute is set, we loop over all attributes in the __dict__
        dictionary and check if any of them are None. If so, we set the finish
        attribute to False and return immediately. Otherwise, we set the finish
        attribute to True. Note that we also initialize finish to False in the
        constructor, which is a good practice.
        """
        super().__setattr__(name, value)
        finished: bool = True
        for v in self.__dict__.values():
            if v is None:
                finished = False
                break
        super().__setattr__('finish', finished)

