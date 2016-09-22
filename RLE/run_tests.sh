
export PATH=/usr/local/bin:$PATH
python -mpip install -U pip
python -mpip install -U virtualenv 


virtualenv testvenv

. testvenv/bin/activate

python -mpip install -r RLE/requirements.txt
pytest RLE

