import os
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QHBoxLayout, QListWidget, QFileDialog

class image_process():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def image_load(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def image_show(self, path):
        image_picture.hide()
        pixmapimage = QPixmap(path)
        w, h = image_picture.width(), image_picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image_picture.setPixmap(pixmapimage)
        image_picture.show()
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def left_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def right_90(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def enhance(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(1.5)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def bandw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.image_show(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)            

image_app = QApplication([])
image_main = QWidget()
image_main.resize(700, 500) 

image_folder = QPushButton('Папка')
image_left90 = QPushButton('Лево')
image_right90 = QPushButton('Право')
image_mirror = QPushButton('Зеркально')
image_enhance = QPushButton('Резкость')
image_bandw = QPushButton('Ч/Б')
image_blur = QPushButton('Размытие')
image_picture = QLabel('Image may be here')
image_folder_list = QListWidget()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1.addLayout(v1)
h1.addLayout(v2)
v2.addLayout(h2)
v2.addLayout(h3)
v1.addWidget(image_folder)
v1.addWidget(image_folder_list)
h2.addWidget(image_picture)
h3.addWidget(image_left90)
h3.addWidget(image_right90)
h3.addWidget(image_mirror)
h3.addWidget(image_enhance)
h3.addWidget(image_bandw)
h3.addWidget(image_blur)
image_main.setLayout(h1)

image_workdir = ''
def filter(files,image_extensions):
    result = []
    for filename in files:
        for ext in image_extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
def chooseWorkdir():
    global image_workdir
    image_workdir = QFileDialog.getExistingDirectory()
def showFilenamesList():
    image_extensions = ['.jpg','.jpeg','.png','.gif','.tif','.tiff','.bmp','.dib','.webp']
    chooseWorkdir()
    try:
        filenames = filter(os.listdir(image_workdir), image_extensions)
        image_folder_list.clear()
        for filename in filenames:
            image_folder_list.addItem(filename)
    except:
        pass
image_folder.clicked.connect(showFilenamesList)

def showImage():
    filename = image_folder_list.currentItem().text()
    wandImage.image_load(image_workdir, filename)
    image_path = os.path.join(wandImage.dir, wandImage.filename)
    wandImage.image_show(image_path)
wandImage = image_process()
image_folder_list.currentRowChanged.connect(showImage)
image_mirror.clicked.connect(wandImage.mirror)
image_left90.clicked.connect(wandImage.left_90)
image_right90.clicked.connect(wandImage.right_90)
image_enhance.clicked.connect(wandImage.enhance)
image_bandw.clicked.connect(wandImage.bandw)
image_blur.clicked.connect(wandImage.blur)

image_main.show()
image_app.exec_()