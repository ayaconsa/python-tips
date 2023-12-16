from enum import Enum

class ForceType(Enum):
    NONE = 0
    TRANSMUTER = 1
    SPECIALIST = 2

class MindForce():
    force_type = ""
    force_type_flag = ForceType.NONE

    def __init__(self, name):
        self.name = name
    
    def view_force_type(self):
        print(self.force_type)


class Transmuter(MindForce):

    def __init__(self, name):
        self.force_type_flag = ForceType.TRANSMUTER
        super().__init__(name)
    
    def view_force_type(self):
        print('変化系')


class Specialist(MindForce):

    def __init__(self, name):
        self.force_type_flag = ForceType.SPECIALIST
        super().__init__(name)
    
    def view_force_type(self):
        print('特質系')

def main():
    lstMindForcer: list[MindForce] = []

    hisoka = Transmuter('ヒソカ')
    kirua = Transmuter('キルア')
    machi = Transmuter('マチ＝コマネチ')
    qworf = Specialist('クロロ＝ルシルフル')


    lstMindForcer.append(hisoka)
    lstMindForcer.append(kirua)
    lstMindForcer.append(machi)
    lstMindForcer.append(qworf)

    for mf in lstMindForcer:
        if mf.force_type_flag == ForceType.SPECIALIST: #マジックナンバーよりはマシだけど、フラグの代わりに文字列も最適でない→enum
            print(mf.name)
            mf.view_force_type()



if __name__=="__main__":
    main()