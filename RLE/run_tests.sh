
/usr/local/bin/python -mpip install -U pip
/usr/local/bin/python -mpip install -U virtualenv 


/usr/local/bin/virtualenv testvenv

. testvenv/bin/activate

python -mpip install -r RLE/requirements.txt
pytest RLE

