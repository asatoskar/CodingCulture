from PIL import Image
import imagehash


def get_image_hash(image_url):
	return imagehash.phash(Image.open(image_url))


def get_hash_diff(hash1, hash2):
	return hash1 - hash2
