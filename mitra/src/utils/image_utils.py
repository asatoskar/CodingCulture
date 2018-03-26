import PIL
from PIL import Image, ImageDraw
import numpy
import sklearn
from sklearn.cluster import KMeans
import imagehash


def get_image_hash(image_url):
	print(Image.open(image_url))
	return imagehash.phash(Image.open(image_url))


def get_hash_diff(hash1, hash2):
	return hash1 - hash2



def get_domcolors(ipfile,swatchsize=200,numcolors=5): #pass path of I/P image
    maxval = 150
    image = Image.open(ipfile)
    width,height=image.size
    resizeratio = min(maxval/width, maxval/height)
    image = image.resize((int(width*resizeratio), int(height*resizeratio)),Image.ANTIALIAS)


    pixels = numpy.array(image)
    h,w,d=pixels.shape
    flattened = pixels.reshape(h*w,d)

    kmeans = KMeans(n_clusters=numcolors, random_state=0).fit(flattened)
    centres=kmeans.cluster_centers_

    centres=centres.tolist()

    for centre in centres:
        for i in range(len(centre)):
            centre[i]=int(centre[i])
    return(','.join(str(centres)))

def diffbetweencolors(color1,color2): #pass colors as numpy array ONLY, returns sum of elements of matrix of distances

    distmatrix = (sklearn.metrics.pairwise.euclidean_distances(color1,color2))
    total= distmatrix[0]+distmatrix[1]+distmatrix[2]

    return(total)

# print(get_image_hash("/Users/mitrathakker/Downloads/WhatsApp Image 2017-10-07 at 12.46.53.jpeg"))
