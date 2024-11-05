from flask import Flask, render_template
from artistas import Artista
from categorias import Categoria
from comentarios import Comentario
from leiloes import Leilao
from obras import Obra
from exibições import Exibicao

app = Flask(__name__)

lista_artistas = [
    Artista(1,"William-Adolphe Bouguereau","William_Bouguereau.jpg","William-Adolphe Bouguereau (30 November 1825 – 19 August 1905) was a French academic painter. In his realistic genre paintings, he used mythological themes, making modern interpretations of classical subjects, with an emphasis on the female human body. During his life, he enjoyed significant popularity in France and the United States, was given numerous official honors, and received top prices for his work. As the quintessential salon painter of his generation, he was reviled by the Impressionist avant-garde. By the early twentieth century, Bouguereau and his art fell out of favor with the public, due in part to changing tastes. In the 1980s, a revival of interest in figure painting led to a rediscovery of Bouguereau and his work. He finished 822 known paintings, but the whereabouts of many are still unknown."),
    Artista(2,"Michelangelo","Michelangelo.webp","...")
]

lista_obras = [
    Obra(1,"song_of_the_angels.jpg", "William-Adolphe Bouguereau", "The Virgin with the Angels", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white. "),
    Obra(2,"Pieta_(1876).jpg", "William-Adolphe Bouguereau", "Pieta - (1876)", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white. "),
    Obra(3,"The_First_Mourning_(1888).jpg", "William-Adolphe Bouguereau", "The First Mourning", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white. "),
    Obra(4,"The_Creation_of_Adam.webp", "Michelangelo", "The Creation of Adam", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white."),
    Obra(5,"creation_of_eve.jpg", "Michelangelo", "The Creation of Eve", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white."),
    Obra(6,"the_fall_of_man.jpg", "Michelangelo", "The Fall of Man", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white."),
    Obra(7,"Coronation_of_the_virgin.jpg", "Diego Velázquez", "The Coronation of the Virgin", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white."),
    Obra(8,"Cristo_crucificado.jpg", "Diego Velázquez", "Christ Crucified", "Legend has it that he searched for a model for the painting's figures and found them in his first wife, Nelly Monochablon, who posed for the angels, one by one, and at last, with a child in her arms. The painting shows the Virgin Mary holding the baby Jesus Christ, who is calmly asleep in a pastoral setting, while a trio of angels hovers nearby. It highlights Bouguereau's ability to render realistic flesh tones and subtle gradations of white."),
]

lista_categorias = [
    Categoria(1, "Renascentista"),
]


@app.route('/')
def home():
    return render_template("index.html", lista_artistas = lista_artistas, lista_categorias = lista_categorias, lista_obras = lista_obras)