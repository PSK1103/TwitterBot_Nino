import os

imgname = open('images.txt','r')
imgs = imgname.read().splitlines()

imgnos = open('imgnum.txt','r')
imgnos = imgnos.read().splitlines()
cum = 0
fin = []
for i in imgnos:
    fin.append(" ".join(imgs[cum:cum+int(i)]) + "\n")
    cum = cum+int(i)

# os.remove('images.txt')
file = open('images1.txt','w')

for line in fin:
    file.write(line)