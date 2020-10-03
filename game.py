import random

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'


class person:
    def __init__(self,hp,np,atk,df,magic):
        self.maxhp=hp
        self.hp=hp
        self.maxnp=np
        self.np=np
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.actions=["Attack","Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    
    def generate_spell_damage(self, i):
        ngl = self.magic[i]["dmg"]-5
        ngh = self.magic[i]["dmg"]+5
        return random.randrange(ngl,ngh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_np(self):
        return self.np
    
    def grt_max_np(self):
        return self.maxnp
    
    def reduce_mp(self, cost):
        self.np -= cost
        
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    def get_spell_np_cost(self, i):
        return self.magic[i]["cost"]
    
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + "i",item)
            i += 1
            
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + "i",spell["name"],"(cost:",str(spell["np"])+")")
            i += 1
