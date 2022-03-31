class Pion :
    def __init__(self,couleur,x,y):
        self.couleur = couleur
        self.x = x
        self.y = y
    
    def afficher_pion(self,x,y):
        if self.couleur == "Rouge":
            fill(250,0,0)
            ellipse(((x+50)//100*100),((y+50)//100*100),85,85)
        else :
            fill(250,250,0)
            ellipse(((x+50)//100*100),((y+50)//100*100),85,85)
    
    def changer_couleur(self):
        if self.couleur == "Rouge":
            self.couleur = "Jaune"
        else :
            self.couleur = "Rouge"
            
            
