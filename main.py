import pygame
import sys
import random


class ball:
    def __init__(self, x, y, color, radius):
        #Topların özelliklerini barındıran class
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

        self.hiz_carpan = 1.0

        #Topların başlangıç kordinatlarını rastgele ayarlayan kodlar
        self.hareket_x = random.choice([-3, -2, 2, 3])
        self.hareket_y = random.choice([-3, -2, 2, 3])

    def move(self):
        #Topların hareket etmesini sağlayan kod
        self.x += self.hareket_x * self.hiz_carpan
        self.y += self.hareket_y * self.hiz_carpan

    def draw(self, screen):
        #Ekrana topları çizdiren kod
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)

    def yon_degistir(self):
        global tv_rect

        # X ekseninde çarpma kontrolü
        if self.x - self.radius <= tv_rect.left or self.x + self.radius >= tv_rect.right:
            self.hareket_x *= -1

        # Y ekseninde çarpma kontrolü
        if self.y - self.radius <= tv_rect.top or self.y + self.radius >= tv_rect.bottom:
            self.hareket_y *= -1


pygame.init()

#Pencere boyutu
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TV ve Kumanda")

#Renkler
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
DarkGray = (100, 100, 100)
BLUE = (0, 120, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)

#TV ekran oranı 16:9
ekran_orani = 16 / 9

#TV boyutunu ayarlayan kodlar
tv_width = SCREEN_WIDTH * 0.65
tv_height = tv_width / ekran_orani

if tv_height > SCREEN_HEIGHT * 0.9:
    tv_height = SCREEN_HEIGHT * 0.9
    tv_width = tv_height * ekran_orani

#TV konumunu ayarlayan kodlar
tv_x = (SCREEN_WIDTH - tv_width) / 2 - 100
tv_y = (SCREEN_HEIGHT - tv_height) / 2
tv_rect = pygame.Rect(tv_x, tv_y, tv_width, tv_height)

#Görselleri yükle
remote_img = pygame.image.load("KUMANDA.png").convert_alpha()
reader_img = pygame.image.load("reader.png").convert_alpha()
dvd_img = pygame.image.load("Dvd_logo.png").convert_alpha()

dvd_img = pygame.transform.scale(dvd_img, (100, 60))


#Kumanda boyutunu ayarla
remote_height = tv_height * 2.0
remote_width = remote_img.get_width() * (remote_height / remote_img.get_height())
remote_img = pygame.transform.smoothscale(remote_img, (int(remote_width), int(remote_height)))

reader_height = tv_height * 0.3
reader_width = reader_img.get_width() * (reader_height / reader_img.get_height())
reader_img = pygame.transform.smoothscale(reader_img, (int(reader_width), int(reader_height)))

#Kumanda konumunu ayarla
remote_x = tv_rect.right - 50
remote_y = tv_rect.centery - 100

reader_x = tv_rect.centery
reader_y = tv_rect.centery + 180

#Topun renk seçimini
selected_color = None


hareket_aktif = False  # Topların hareket edip etmediğini kontrol eder


#Renk Seçim Fonksiyonu
def ball_color(color):
    global selected_color
    selected_color = color
    print("Seçilen renk:", selected_color)


#Start Fonksiyonu
def start_animation():
    global hareket_aktif
    if not nesneler:
        print("Lütfen önce bir top oluşturun!")
        return
    hareket_aktif = True
    print("Animasyon BAŞLADI.")


#Stop Fonksiyonu
def stop_animation():
    global hareket_aktif
    hareket_aktif = False
    print("Animasyon DURDU.")


#Reset Fonksiyonu
def reset_animation():
    global nesneler, hareket_aktif
    nesneler = []  # Tüm topları sil
    hareket_aktif = False  # Hareketi durdur
    print("Animasyon SIFIRLANDI.")


#Hızlan Fonksiyonu
def speed_up():
    for b in nesneler:
        if b.hiz_carpan == 8.0:
            return
        else:
            b.hiz_carpan += 0.5


        current_hiz = nesneler[0].hiz_carpan if nesneler else 1.0
        print(f"Hız Arttırıdı. Yeni Çarpan: {current_hiz}")

#Yavaşla Fonksiyonu
def speed_down():
    for b in nesneler:
        if b.hiz_carpan == 1.0:
            return
        else:
            b.hiz_carpan -= 0.5


    current_hiz = nesneler[0].hiz_carpan if nesneler else 1.0
    print(f"Hız Azaltıldı. Yeni Çarpan: {current_hiz}")


#Top Oluşturma Fonksiyonları
def smallBall(): #Küçük Top oluşturmak için
    global selected_color
    if selected_color is None:
        print("Lütfen önce bir renk seçin!")
        return
    x = random.randint(int(tv_rect.left + 10), int(tv_rect.right - 10))
    y = random.randint(int(tv_rect.top + 10), int(tv_rect.bottom - 10))
    nesnem = ball(x, y, selected_color, 10)
    nesneler.append(nesnem)
    print("Küçük Top Eklendi.")


def middleBall(): #Orta Top oluşturmak için
    global selected_color
    if selected_color is None:
        print("Lütfen önce bir renk seçin!")
        return
    x = random.randint(int(tv_rect.left + 22), int(tv_rect.right - 22))
    y = random.randint(int(tv_rect.top + 22), int(tv_rect.bottom - 22))
    nesnem = ball(x, y, selected_color, 22)
    nesneler.append(nesnem)
    print("Orta Top Eklendi.")


def bigBall(): #Büyük Top oluşturmak için
    global selected_color
    if selected_color is None:
        print("Lütfen önce bir renk seçin!")
        return
    x = random.randint(int(tv_rect.left + 41), int(tv_rect.right - 41))
    y = random.randint(int(tv_rect.top + 41), int(tv_rect.bottom - 41))
    nesnem = ball(x, y, selected_color, 41)
    nesneler.append(nesnem)
    print("Büyük Top Eklendi.")


#EasterEgg kodları
dvd_x = tv_rect.centerx
dvd_y = tv_rect.centery
hareket_x = 2
hareket_y = 2
dvd_uzunluk_x = 100
dvd_uzunluk_y = 60

def dvdplay():
    global dvd_x, dvd_y, hareket_x, hareket_y

    #DVD logosunu çiz
    screen.blit(dvd_img, (dvd_x, dvd_y))

    #Konumu güncelle
    dvd_x += hareket_x
    dvd_y += hareket_y

    #X ve Y ekseninde çarpma kontrolü kodları
    if dvd_x <= tv_rect.left or dvd_x + dvd_uzunluk_x >= tv_rect.right:
        hareket_x *= -1

    if dvd_y <= tv_rect.top or dvd_y + dvd_uzunluk_y >= tv_rect.bottom:
        hareket_y *= -1


#Buton listesi
buttons = [
    #Exit tuşu
    {"type": "circle", "center": (remote_x + 270, remote_y + 78), "radius": 22, "color": RED, "action": "exit"},

    #Top boyut seçme tuşları
    {"type": "circle", "center": (remote_x + 148, remote_y + 155), "radius": 22, "color": GREEN, "action": "smallBall"},
    {"type": "circle", "center": (remote_x + 207, remote_y + 155), "radius": 22, "color": YELLOW,
     "action": "middleBall"},
    {"type": "circle", "center": (remote_x + 266, remote_y + 155), "radius": 22, "color": YELLOW, "action": "bigBall"},

    #hareket, durdur, devam et, başlat ve reset tuşları:
    {"type": "rect", "rect": pygame.Rect(remote_x + 183, remote_y + 210, 47, 30), "color": (0, 255, 255),
     "action": "start_animation"},  # PLAY (START)
    {"type": "rect", "rect": pygame.Rect(remote_x + 183, remote_y + 255, 47, 30), "color": (0, 255, 255),
     "action": "stop_animation"},  # KARE (STOP)
    {"type": "rect", "rect": pygame.Rect(remote_x + 183, remote_y + 300, 47, 30), "color": (0, 255, 255),
     "action": "reset_animation"},  # KÜÇÜK TUŞ (RESET)

    #Hız ayarlama tuşları
    {"type": "rect", "rect": pygame.Rect(remote_x + 240, remote_y + 200, 50, 65), "color": (0, 255, 255),
     "action": "speed_up"},

    {"type": "rect", "rect": pygame.Rect(remote_x + 240, remote_y + 270, 50, 65), "color": (0, 255, 255),
     "action": "speed_down"},

    #Renk seçim tuşları
    {"type": "circle", "center": (remote_x + 148, remote_y + 375), "radius": 22, "color": RED,
     "action": "ball_color(RED)"},
    {"type": "circle", "center": (remote_x + 207, remote_y + 375), "radius": 22, "color": BLUE,
     "action": "ball_color(BLUE)"},
    {"type": "circle", "center": (remote_x + 266, remote_y + 375), "radius": 22, "color": YELLOW,
     "action": "ball_color(YELLOW)"},

    #EasterEgg tuşları
    {"type": "circle", "center": (remote_x + 148, remote_y + 78), "radius": 22, "color": YELLOW, "action": "sources"},
    {"type": "circle", "center": (reader_x + 22, reader_y + 50), "radius": 8, "color": YELLOW, "action": "easterbutton"},

]

#EasterEgg Switchleri
control_switch = False
source_switch = False

def easterbutton():
    global control_switch
    control_switch = not control_switch  # True <-> False arasında geçiş yapar

def sources():
    global control_switch
    global source_switch
    source_switch = not source_switch





#TV rengi
tv_color = DarkGray

#Topları tutan liste
nesneler = []

#Pygame Ana döngü
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Fare tıklama
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for btn in buttons:
                action = None
                if btn["type"] == "circle":
                    dist = ((mouse_pos[0] - btn["center"][0]) ** 2 + (mouse_pos[1] - btn["center"][1]) ** 2) ** 0.5
                    if dist <= btn["radius"]:
                        action = btn["action"]
                elif btn["type"] == "rect":
                    if btn["rect"].collidepoint(mouse_pos):
                        action = btn["action"]

                if action:
                    #Buton eylemleri
                    if action == "exit":
                        pygame.quit()
                        sys.exit()

                    elif action == "start_animation":
                        start_animation()

                    elif action == "stop_animation":
                        stop_animation()

                    elif action == "reset_animation":
                        reset_animation()

                    elif action == "speed_up":
                        speed_up()

                    elif action == "speed_down":
                        speed_down()

                    elif action == "ball_color(RED)":
                        ball_color(RED)

                    elif action == "ball_color(BLUE)":
                        ball_color(BLUE)

                    elif action == "ball_color(YELLOW)":
                        ball_color(YELLOW)

                    elif action == "smallBall":
                        smallBall()

                    elif action == "middleBall":
                        middleBall()

                    elif action == "bigBall":
                        bigBall()

                    elif action == "easterbutton":
                        easterbutton()

                    elif action == "sources":
                        sources()

    #Arka plan rengi
    screen.fill(BLACK)

    #TV çerçevesi ve ekran
    pygame.draw.rect(screen, GRAY, tv_rect.inflate(20, 20))
    pygame.draw.rect(screen, tv_color, tv_rect)

    #Kumandayı çiz
    screen.blit(remote_img, (remote_x, remote_y))
    screen.blit(reader_img, (reader_x, reader_y))


    #Topları çiz
    for b in nesneler:
        b.draw(screen)
        #Hareket kontrolü
        if hareket_aktif:
            b.move()
            b.yon_degistir()

    #EasterEgg dvd kutusu kontrol ışığı
    if control_switch:
        pygame.draw.circle(screen, GREEN, (reader_x + 41, reader_y + 52), 4)

    else:
        pygame.draw.circle(screen, BLACK, (reader_x + 41, reader_y + 52), 4)


    if control_switch & source_switch:
        pygame.draw.rect(screen, BLACK, tv_rect)
        dvdplay()

    if control_switch == False and source_switch == True:
        pygame.draw.rect(screen, BLACK, tv_rect)
        font = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 18)
        text1 = font.render("HDMI cihazına bağlanılamıyor", True, (255, 255, 255))
        text2 = font2.render("Lütfen cihazın gücünün açık olduğunu ve kabloların bağlı olduğunu doğrulayınız", True, (150, 150, 150))
        screen.blit(text1, (tv_rect.left + 150, tv_rect.y + 150))
        screen.blit(text2, (tv_rect.left + 100, tv_rect.y + 200))

    pygame.display.update()
    clock.tick(60)