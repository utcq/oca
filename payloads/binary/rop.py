from ropper import RopperService

from core.challenge import Challenge

options = {'color' : False,
            'badbytes': '00',
            'all' : False,
            'inst_count' : 6,
            'type' : 'all',
            'detailed' : False}



class Rop():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()

    def analyze(self)->None:
        rs = RopperService(options)
        for file in self.challenge.files:
            if "." not in file['name']:
                rs.addFile(file['path'])
                rs.loadGadgetsFor()
                pprs = rs.searchJmpReg()
                pprs.update(rs.searchPopPopRet())
                for file, ppr in pprs.items():
                    for p in ppr:
                        print(p)