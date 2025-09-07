import random

class Computer:

    def __init__(self, processor, cpu_speed, pc_case = 'black' ):
        self.processor = processor
        self.color = pc_case
        self.cpu_speed = cpu_speed

    def check_speed(self):
        if self.cpu_speed < 6:
            return 'slow'
        elif self.cpu_speed > 10:
            return 'fast'
        else:
            return 'midrange'

    def compliment_pc(self):
        return f'A {self.check_speed()} speed for an {self.processor} processor. Youre rocking that {self.color} case with {self.processor}!!'

class GamingPC(Computer):

    def __init__(self,processor,cpu_speed, gpu, case_color = 'black'):
        self.gpu = gpu
        super().__init__(processor, cpu_speed, case_color)

    def how_good_is_the_gaming(self):
        if self.gpu == 'Nvidia' or self.gpu == 'Amd':
            return f'Gaming is good with {self.gpu}'
        else:
            return f"You're amazing for gaming on an {self.gpu}"

computers = []
cpus = ['Intel', 'Amd', 'Arduino']
case_clr = ['black', 'red', 'yellow', 'lavender', '']
gpus = ['Nvidia', 'Amd', 'Arduino']
for x in range(60):
    cpu = cpus[random.randint(0,2)]
    color = case_clr[random.randint(0,4)]
    if color == '':
        computers.append(Computer(cpu, random.randint(4, 12)))
    else:
        computers.append(Computer(cpu, random.randint(4, 12), color))

for x in range(40):
    cpu = cpus[random.randint(0, 2)]
    color = case_clr[random.randint(0, 4)]
    graphic = gpus[random.randint(0,2)]
    if color == '':
        computers.append(GamingPC(cpu, random.randint(4, 12), graphic))
    else:
        computers.append(GamingPC(cpu, random.randint(4, 12), graphic, color))

for x in computers:
    print(x.compliment_pc())
    if isinstance(x, GamingPC):
        print(x.how_good_is_the_gaming())
    print('')