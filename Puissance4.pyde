from pion import Pion
gri = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
pion = Pion("Rouge",0,0)

def setup():
    size(800,900)
    dessiner_grille()

def draw():
    if pion_gagnant() :
        print("toto")
        if pion.changer_couleur == "Rouge" :
            textAlign(CENTER)
            fill(0,0,0)
            text("PARTIE GAGNEE PAR LE JOUEUR JAUNE",400,680)
        else :
            textAlign(CENTER)
            fill(0,0,0)
            text("PARTIE GAGNEE PAR LE JOUEUR ROUGE",400,680)
            
            
def mousePressed():
    global gri
    x = mouseX
    y = mouseY
    if not fin_partie() :
        if clic_valid(x,y):
            if case_vide(x,y):
                descendre_pion(x,y)
                maj_grille(x,y)
                print(gri)
                pion.changer_couleur()
                if pion_gagnant() :
                    print("toto")
                
                    
        
        
                
def dessiner_grille():
    fill(0,50,255)
    stroke(0,50,255)
    rect(50,50,700,600)
    n = 1
    for k in range(1,8):
        for n in range(1,7):
            fill(255,255,255)
            ellipse(k*100,n*100,85,85)

def maj_grille(x,y):
    indice = descendre_pion(x,y)
    if pion.couleur == "Rouge":
        gri[indice] = 'R'
    else:
        gri[indice] = 'J'

def fin_partie():
    if '' in gri or not pion_gagant():
        return False
    else :
        return True

def clic_valid(x,y):
    if 50 < x < 750 and 50 < y < 650 :
        return True
    else :
        return False

def case_vide(x,y):
    a = convertir_les_coord_en_ind(x,y)
    if gri[a] == '':
        return True
   
def convertir_les_coord_en_ind(x,y):
    '''
    entrée :
        x = int
        y = int
    sortie :
        int : représentant l'indice de la case du pion
    '''
    x = ((x+50)//100*100)
    y = ((y+50)//100*100)
    
    if x == 100 and y == 600:
        return 0
    elif x == 100 and y == 500:
        return 1
    elif x == 100 and y == 400:
        return 2
    elif x == 100 and y == 300:
        return 3
    elif x == 100 and y == 200:
        return 4
    elif x == 100 and y == 100:
        return 5
    elif x == 200 and y == 600:
        return 6
    elif x == 200 and y == 500:
        return 7
    elif x == 200 and y == 400:
        return 8
    elif x == 200 and y == 300:
        return 9
    elif x == 200 and y == 200:
        return 10
    elif x == 200 and y == 100:
        return 11
    elif x == 300 and y == 600:
        return 12
    elif x == 300 and y == 500:
        return 13
    elif x == 300 and y == 400:
        return 14
    elif x == 300 and y == 300:
        return 15
    elif x == 300 and y == 200:
        return 16
    elif x == 300 and y == 100:
        return 17
    elif x == 400 and y == 600:
        return 18
    elif x == 400 and y == 500:
        return 19
    elif x == 400 and y == 400:
        return 20
    elif x == 400 and y == 300:
        return 21
    elif x == 400 and y == 200:
        return 22
    elif x == 400 and y == 100:
        return 23
    elif x == 500 and y == 600:
        return 24
    elif x == 500 and y == 500:
        return 25
    elif x == 500 and y == 400:
        return 26
    elif x == 500 and y == 300:
        return 27
    elif x == 500 and y == 200:
        return 28
    elif x == 500 and y == 100:
        return 29
    elif x == 600 and y == 600:
        return 30
    elif x == 600 and y == 500:
        return 31
    elif x == 600 and y == 400:
        return 32
    elif x == 600 and y == 300:
        return 33
    elif x == 600 and y == 200:
        return 34
    elif x == 600 and y == 100:
        return 35
    elif x == 700 and y == 600:
        return 36
    elif x == 700 and y == 500:
        return 37
    elif x == 700 and y == 400:
        return 38
    elif x == 700 and y == 300:
        return 39
    elif x == 700 and y == 200:
        return 40
    elif x == 700 and y == 100:
        return 41
    else :
        return -1

def conv_ind_coor(ind):
    if ind == 0 :
        return 100,600
    elif ind == 1:
        return 100,500
    elif ind == 2:
        return 100,400
    elif ind == 3:
        return 100,300
    elif ind == 4:
        return 100,200
    elif ind == 5 :
        return 100,100
    elif ind == 6 :
        return 200,600
    elif ind == 7 :
        return 200,500
    elif ind == 8 :
        return 200,400
    elif ind == 9 :
        return 200,300
    elif ind == 10 :
        return 200,200
    elif ind == 11 :
        return 200,100
    elif ind == 12 :
        return 300,600
    elif ind == 13 :
        return 300,500
    elif ind == 14 :
        return 300,400
    elif ind == 15 :
        return 300,300
    elif ind == 16 :
        return 300,200
    elif ind == 17 :
        return 300,100
    elif ind == 18 :
        return 400,600
    elif ind == 19:
        return 400,500
    elif ind == 20:
        return 400,400
    elif ind == 21 :
        return 400,300
    elif ind == 22 :
        return 400,200
    elif ind == 23 :
        return 400,100
    elif ind == 24 :
        return 500,600
    elif ind == 25 :
        return 500,500
    elif ind == 26 :
        return 500,400
    elif ind == 27 :
        return 500,300
    elif ind == 28 :
        return 500,200
    elif ind == 29 :
        return 500,100
    elif ind == 30 :
        return 600,600
    elif ind == 31 :
        return 600,500
    elif ind == 32 :
        return 600,400
    elif ind == 33 :
        return 600,300
    elif ind == 34 :
        return 600,200
    elif ind == 35 :
        return 600,100
    elif ind == 36 :
        return 700,600
    elif ind == 37:
        return 700,500
    elif ind == 38 :
        return 700,400
    elif ind == 39 :
        return 700,300
    elif ind == 40 :
        return 700,200
    elif ind == 41 :
        return 700,100
    
def pion_gagnant():
    '''teste les combinaisons gagantes a l'horizontale '''
    for i in range(0,6):
        if gri[i]==gri[i+6]==gri[i+12]==gri[i+18]==( 'R' or 'J'):
            return True
        elif gri[i+6]==gri[i+12]==gri[i+18]==gri[i+24]==( 'R' or 'J'):
            return True
        elif gri[i+12]==gri[i+18]==gri[i+24]==gri[i+30]==( 'R' or 'J'):
            return True
        elif gri[i+18]==gri[i+24]==gri[i+30]==gri[i+36]==( 'R' or 'J'):
            return True
        '''teste les combinaisons gagantes à la verticale '''
    for i in range(0,37,6):
        if gri[i]==gri[i+1]==gri[i+2]==gri[i+3]==( 'R' or 'J'):
            return True
        elif gri[i+1]==gri[i+2]==gri[i+3]==gri[i+4]==( 'R' or 'J'):
            return True
        elif gri[i+2]==gri[i+3]==gri[i+4]==gri[i+5]==( 'R' or 'J'):
            return True
        '''teste les combinaisons gagantes en diagonale'''
    for i in range(0,19,6):
        if gri[i]==gri[i+7]==gri[i+14]==gri[i+21]==( 'R' or 'J'):
            return True
    for i in range(36,17,-6):
        if gri[i]==gri[i-5]==gri[i-10]==gri[i-15]==( 'R' or 'J'):
            return True
    for i in range(1,20,6):
        if gri[i]==gri[i+7]==gri[i+14]==gri[i+21]==( 'R' or 'J'):
            return True
    for i in range(37,18,-6):
        if gri[i]==gri[i-5]==gri[i-10]==gri[i-15]==( 'R' or 'J'):
            return True
    for i in range(2,21,6):
        if gri[i]==gri[i+7]==gri[i+14]==gri[i+21]==( 'R' or 'J'):
            return True
    for i in range(38,19,-6):
        if gri[i]==gri[i-5]==gri[i-10]==gri[i-15]==( 'R' or 'J'):
            return True
    else :
        return False

def descendre_pion(x,y):
    ind = convertir_les_coord_en_ind(x,y)
    if 0<= ind <= 5 :
        while gri[ind-1] == '' and ind > 0 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 6<= ind <= 11 :
        while gri[ind-1] == '' and ind > 6 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 12<= ind <= 17 :
        while gri[ind-1] == '' and ind > 12 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 18<= ind <= 23 :
        while gri[ind-1] == '' and ind > 18 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 24<= ind <= 29 :
        while gri[ind-1] == '' and ind > 24 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 30<= ind <= 35 :
        while gri[ind-1] == '' and ind > 30 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    if 36<= ind <= 41 :
        while gri[ind-1] == '' and ind > 36 :
            ind -= 1
        a,b = conv_ind_coor(ind)
        pion.afficher_pion(a,b)
        return ind
    
     
