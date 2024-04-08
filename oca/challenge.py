class Challenge:
    def __init__(
                self, name:str="", url:str="", score:int=0, id:int=0,
                categories:list[str]=[],
                urls:list[str]=[], files:list[dict]=[], hosts:list[tuple[str,int]]=[],
                writeup:str="", description:str=""
                ):
        self.name=name
        self.score=score
        self.id=id
        self.url=url
        self.categories=categories
        self.urls=urls
        self.files=files
        self.hosts=hosts
        self.writeup=writeup
        self.description=description