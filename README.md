# Hencoder

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python](https://img.shields.io/badge/Python-v3.0+-BLUE.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/badge/release-v1.0-BLUE.svg)](https://github.com/Akashtyagi08/Hencoder/releases)
![Build Status](https://travis-ci.org/anfederico/Clairvoyant.svg?branch=master)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

------------------------------------------------
### Hencoder is a simple encoder based on greedy algorithim [Hauffman encoding](https://en.wikipedia.org/wiki/Huffman_coding).


### ```pip install Hencoder```

#### This package can be used to:

* Encode/Decode any given text
* Encode/Decode any given file. 

This file can be
* Any plain text file.
* Source code along with indentations.
* Any other text that is readable by python.

------------------------------------------------

# Whats Great about Hencoder ? :star2:	

> Hencoder makes sure that nobody else can decode your text other than you. :superhero:

Hencoder provides a feature to encode your input using a ```secret key```.

This ```secret key``` ensures that no-one else can decode your encoded text until they know the key used for encoding the text.

This secret key gets added to your original text, therefore correct decoding is only possible when user enters same key that was used while encoding.

This key can be any value in range of `key = 1-100 ` .

> Geek fact:
>
>   You can super encode your already encoded file with another key to make it even more difficult for someone to crack it.


# How to Use Hencoder ? :book:


It's as smooth as butter.

* Encoding/Decoding can be done in 2 ways:
	1. Encoding/Decoding a **text**
	2. Encoding/Decoding a **file**


```python
Hencoder.encode(text="", key=0, path=None, inplace=False)
Hencoder.decode(text="", key=0, path=None, inplace=False)

* text: Text that needs to be encoded.
		{Default=''} {Optional}

* key: Encoding: Secure your data by adding a secret value.
	   Decoding: When decoding, you need to enter same key.
	    {Default=0}  {Optional}

* path: If want to convert any file, enter its complete path.
		{Default=None} (Optional)

* inplace: When coverting file, modify file inplace. 
		{Default= False} (Optional)
```
