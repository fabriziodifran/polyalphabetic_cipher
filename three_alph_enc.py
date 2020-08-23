from random import sample
from collections import deque

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
			'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def _getKeys(alphabet):
	pos_keys = list(range(1, len(alphabet)))
	neg_keys = list(range(-len(alphabet)+1, 0))
	possible_keys_list = pos_keys + neg_keys

	return sample(possible_keys_list, 2)


def encrypt(message, alphabet=alpha):


	keys = _getKeys(alphabet)
	alpha2 = deque(alphabet)
	alpha3 = deque(alphabet)

	alpha2.rotate(keys[0])
	alpha3.rotate(keys[1])

	alpha2 = list(alpha2)
	alpha3 = list(alpha3)

	message_words = message.lower().rsplit()
	message_words_enc = []
	parity = 0

	for word in message_words:
		words_enc = []
		for i, char in enumerate(word):
		
			if parity%2 == 0:
				char_enc = alpha2[alphabet.index(char)]
		
			else:
				char_enc = alpha3[alphabet.index(char)]
		
			words_enc.append(char_enc)
			parity += 1
		
		message_words_enc.append("".join(words_enc))

	message_encrypted = " ".join(message_words_enc)

	return message_encrypted, keys



def decrypt(message, keys, alphabet=alpha):

	alpha2 = deque(alphabet)
	alpha3 = deque(alphabet)

	alpha2.rotate(-keys[0])
	alpha3.rotate(-keys[1])

	alpha2 = list(alpha2)
	alpha3 = list(alpha3)

	message_words = message.lower().rsplit()
	message_words_dec = []
	parity = 0

	for word in message_words:
		words_dec = []
		for i, char in enumerate(word):
		
			if parity%2 == 0:
				char_dec = alpha2[alphabet.index(char)]
		
			else:
				char_dec = alpha3[alphabet.index(char)]
		
			words_dec.append(char_dec)
			parity += 1
		
		message_words_dec.append("".join(words_dec))

	message_decrypted = " ".join(message_words_dec)

	return message_decrypted