from PIL import Image
import imagehash


def hasher(imageurl):
	hash = imagehash.phash(Image.open(imageurl))
	return hash

def comparehash(hash1, hash2):
	return(hash1 - hash2)


if __name__== "__main__":
	hash = hasher('/home/ananya/Pictures/420238.jpg');
	print(hash)