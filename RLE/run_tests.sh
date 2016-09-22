
export PATH=/usr/local/bin:$PATH
# python -mpip install -U pip
# python -mpip install -U virtualenv 


virtualenv testvenv

. testvenv/bin/activate

pip install -r RLE/requirements.txt
pytest RLE

