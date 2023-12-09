import pygame
from tkinter import filedialog
import librosa , wave
import os.path



pygame.font.init()

#=============================================================   Set up   ==========================================================================================
WIDTH , HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH , HEIGHT))

#set color
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
grey = (97,97,97)
darker_grey = (52,52,52)
transparent = (0,0,0,0)

#Set Window name
pygame.display.set_caption("Key Tap")

#defult font
font = pygame.font.Font('./Roboto.ttf',30)

#default button animation
BUTTON_DYNAMIC = 5

#default tile speed
SPEED = 2

#song wav file open
file_name = filedialog.askopenfilename(title="Choose a song", filetypes=(("wav files", "*.wav"), ("all files", "*.*")))

#song setup
f = wave.open(file_name, 'rb')
frequency = f.getframerate()

cool = pygame.image.load("./cool.png").convert()
blank = pygame.image.load("./blank.png").convert()
perfect = pygame.image.load("./perfect.png").convert()
miss = pygame.image.load("./miss.png").convert()


#=============================================================    Classes    ========================================================================================
#difficulty selecting button
class set_font:
    def __init__(self,font,size,text = '',color = white):
        self.main_font = pygame.font.SysFont(font , size)
        self.with_text = self.main_font.render(text , True , color)
        self.color = color
    
    def get_font(self):
        return self.main_font
    
    def get_text(self):
        return self.with_text
    
    def update_text(self,text):
        self.with_text = self.main_font.render(text , True , self.color)


class musicblock():
    def __init__(self,image,block):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image_rect = self.image.get_rect()
        self.block = block.get_rect()
        self.block.y = 735
    
    
    def draw(self):
        
        WINDOW.blit(self.image , (self.x, self.y))
        
    
    def move(self):
        global miss_time
        self.image_rect.top = self.y
        if self.y <= 800 or self.x == 1000:
            self.y += SPEED
        else:
            self.image.fill(transparent)
            miss_time = 10
            return True
        if self.x == 1000:
            return True
    
    def printin(self):
        return self.y

class yellownote(musicblock):
    def __init__(self, image, block):
        super().__init__(image, block)
        self.x = (yellow_rect.right + yellow_rect.left)/2
        self.y = 100
    
    def check_colide(self,key):
        
        global perfect_time
        global cool_time
        global score
        
        
        if key == "d" and abs(self.y - self.block.y) <= 50:
            self.y = 3000
            self.x = 1000
            perfect_time = 20
            score += 300
        if key == "d" and abs(self.y - self.block.y) <= 100:
            self.y = 3000
            self.x = 1000
            cool_time = 20
            score += 100


class greennote(musicblock):
    
    def __init__(self, image, block):
        super().__init__(image, block)
        self.x = (green_rect.right + green_rect.left)/2
        self.y = 100
    
    def check_colide(self,key):
        global perfect_time
        global cool_time
        global score
        
        if key == "f" and abs(self.y - self.block.y) <= 50:
            self.y = 3000
            self.x = 1000
            perfect_time = 20
            score += 300
        if key == "f" and abs(self.y - self.block.y) <= 100:
            self.y = 3000
            self.x = 1000
            cool_time = 20
            score += 100
        
        


class bluenote(musicblock):
    def __init__(self, image, block):
        super().__init__(image, block)
        self.x = (blue_rect.right + blue_rect.left)/2
        self.y = 100
    
    def check_colide(self,key):
        global perfect_time
        global cool_time
        global score
        
        if key == "j" and abs(self.y - self.block.y) <= 50:
            self.y = 3000
            self.x = 1000
            perfect_time = 20
            score += 300
        if key == "j" and abs(self.y - self.block.y) <= 100:
            self.y = 3000
            self.x = 1000
            cool_time = 20
            score += 100


class orangenote(musicblock):
    def __init__(self, image, block):
        super().__init__(image, block)
        self.x = (orange_rect.right + orange_rect.left)/2
        self.y = 100
    
    def check_colide(self,key):
        global perfect_time
        global cool_time
        global score
        
        if key == "k" and abs(self.y - self.block.y) <= 50:
            self.y = 3000
            self.x = 1000
            perfect_time = 20
            score += 300
        if key == "k" and abs(self.y - self.block.y) <= 100:
            self.y = 3000
            self.x = 1000
            cool_time = 20
            score += 100




        

#=============================================================    Methods    =====================================================================================================
#Draw background funtion
def Draw_main_screen(bool):
    WINDOW.fill(white)

    if bool:
        WINDOW.blit(starttext , textRect) # Write 'Click to play'
        WINDOW.blit(titletext , titleRect) # Write Game name
        WINDOW.blit(songtext , songRect) # Write song name

def maingame_state(start):
    
    
    
    for k in range(len(note_info_list)):
        
        if (get_current_time() - start)/1000 >= float(note_info_list[k][0]) - 5 and not note_info_list[k][2]:
            note_info_list[k][1].draw()
            
            if note_info_list[k][1].move():
                note_info_list[k][2] = True
            
            
        
    

def draw_keys():
    WINDOW.blit(d , (135 , 705))
    WINDOW.blit(f , (285 , 705))
    WINDOW.blit(j , (435 , 705))
    WINDOW.blit(k , (585 , 705))

def del_keys():
    d.fill(transparent)
    f.fill(transparent)
    j.fill(transparent)
    k.fill(transparent)


def get_current_time():
    return pygame.time.get_ticks()

def Draw_end_screen():
    WINDOW.fill(black)

def conclusion_screen():
    
    scorefont.update_text("Your score is : " + str(score))
    WINDOW.blit(scorefont.get_text() , (300,400))
    WINDOW.blit(endtext , endrect)
    
    

def save_score():
    print("Tried")
    try:
        print("created")
        save_file = open("Project/" + os.path.basename(file_name)[:-4] + "_Score.txt" , "x")
        save_file.close()
        saving_file = open("Project/" + os.path.basename(file_name)[:-4] + "_Score.txt" , "a")
        saving_file.write(str(score))
        saving_file.close()
    except:
        print("append")
        append_file = open("Project/" + os.path.basename(file_name)[:-4] + "_Score.txt" , "a")
        append_file.write("\n" + str(score))
        append_file.close()


    

    



#=================================================== Setting up / Initialize stuff ===============================================================================================

#Set "Click to play font
startfont = set_font('Roboto.ttf',52,"Press Return to start!",black)
starttext = startfont.get_text()
textRect = starttext.get_rect()
textRect.center = (WIDTH//2,HEIGHT//1.35)

#Set title font
titlefont = set_font('Roboto.ttf', 80,"Key Tap", black)
titletext = titlefont.get_text()
titleRect = titletext.get_rect()
titleRect.center = (WIDTH//2,HEIGHT//5)

#Set song name
songfont = set_font('Roboto.ttf' , 60 , "Song Name : " + os.path.basename(file_name)[:-4] , black)
songtext = songfont.get_text()
songRect = songtext.get_rect()
songRect.center = (WIDTH//2,HEIGHT//3.5)

#Set score
score = 0
scorefont = set_font("Roboto.ttf" , 40 ,"Score : " + str(score) , black)
scoretext = scorefont.get_text()
scoreRect = scoretext.get_rect()
scoreRect.top = 0
scoreRect.left = 0

#End screen
endfont = set_font("Roboto.ttf" , 60 , "Game End" , black)
endtext = endfont.get_text()
endrect = endtext.get_rect()
endrect.center = (400,200)

#Set limit FPS
FPS = 60

#block set up
yellowbg = pygame.image.load('./yellowbg.png')
yellowbg = pygame.transform.scale(yellowbg, (125, 70))
yellow_rect = yellowbg.get_rect()
yellow_rect.top = 700
yellow_rect.left = 100

greenbg = pygame.image.load('./greenbg.png')
greenbg = pygame.transform.scale(greenbg, (125, 70))
green_rect = greenbg.get_rect()
green_rect.top = 700
green_rect.left = 250

bluebg = pygame.image.load('./bluebg.png')
bluebg = pygame.transform.scale(bluebg, (125, 70))
blue_rect = bluebg.get_rect()
blue_rect.top = 700
blue_rect.left = 400

orangebg = pygame.image.load('./orangebg.png')
orangebg = pygame.transform.scale(orangebg, (125, 70))
orange_rect = orangebg.get_rect()
orange_rect.top = 700
orange_rect.left = 550

d = pygame.image.load('./d.png')
d = pygame.transform.scale(d, (50, 50))
f = pygame.image.load('./f.png')
f = pygame.transform.scale(f, (50, 50))
j = pygame.image.load('./j.png')
j = pygame.transform.scale(j, (50, 50))
k = pygame.image.load('./k.png')
k = pygame.transform.scale(k, (50, 50))


#librosa setup
x , sr = librosa.load(file_name)
onset_frames = librosa.onset.onset_detect(y=x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
onset_times = librosa.frames_to_time(onset_frames)
t = open("./" + os.path.basename(file_name)[:-4] + ".txt" , "r")
notelist = t.read().split("\n")
note_info_list = []

for i in notelist:
    try:
        note_info = i.split(";")
        note_info.append(bool(False))
        if note_info[1] == "1":
            note_info[1] = yellownote("./yellowcir.png",yellowbg)
        if note_info[1] == "2":
            note_info[1] = greennote("./greencir.png",greenbg)
        if note_info[1] == "3":
            note_info[1] = bluenote("./bluecir.png",bluebg)
        if note_info[1] == "4":
            note_info[1] = orangenote("./orangecir.png",orangebg)
        note_info_list.append(note_info)
    except:
        print("note file is incorrect at line " , i)
    
    

#=============================================================== Main ==============================================================================================================
#Main function
def main():
    global start_time
    global status
    global perfect_time
    global cool_time
    global score
    global miss_time


    status = blank
    score = 0
    clock = pygame.time.Clock()

    conclusion = False
    run = True
    mainscreen = True # check for main screen title
    maingame = False
    start_time = 0

    perfect_time = 0
    cool_time = 0
    miss_time = 0
    saved = False
    

    while run:
        clock.tick(FPS) # Limit FPS
       
        Draw_main_screen(mainscreen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not maingame:
                    mainscreen = False
                    maingame = True
                    start_time = get_current_time()
                    pygame.mixer.init(frequency=frequency)
                    pygame.mixer.music.load(file_name)
                    pygame.mixer.music.play(1)
                    
                for i in note_info_list:
                    if event.key == pygame.K_d:
                        i[1].check_colide("d")
                    if event.key == pygame.K_f:
                        i[1].check_colide("f")
                    if event.key == pygame.K_j:
                        i[1].check_colide("j")
                    if event.key == pygame.K_k:
                        i[1].check_colide("k")
            
            
        

       
        
           

        if maingame:
            
            WINDOW.blit(bluebg , blue_rect)
            WINDOW.blit(greenbg , green_rect)
            WINDOW.blit(orangebg , orange_rect)
            WINDOW.blit(yellowbg , yellow_rect)
            WINDOW.blit(scorefont.get_text() , scoreRect)
            scorefont.update_text("Score : " + str(score))
            if perfect_time > 0:
                WINDOW.blit(perfect , (200,200))
                perfect_time -= 1
            if cool_time > 0:
                WINDOW.blit(cool , (200,200))
                cool_time -= 1
            if miss_time > 0:
                WINDOW.blit(miss , (200 ,200))
                miss_time -= 1
            if miss_time == 0 and cool_time == 0 and perfect_time == 0:
                WINDOW.blit(blank , (200,200))
                
            
            maingame_state(start_time)

            if (get_current_time() - start_time)/1000 > 5:
                del_keys() 
            else:
                draw_keys()

            

            if note_info_list[len(note_info_list)-1][2]:
                print("song ended")
                maingame = False
                conclusion = True
            
            
        
        if conclusion:
            if not saved:
                save_score()
                saved = True
            conclusion_screen()

        pygame.display.flip() # update display every loop
    
    pygame.quit() # End

#Just make sure
if __name__ == "__main__":
    main()