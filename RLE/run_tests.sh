
python -mpip install -U pip
python -mpip install -U virtualenv 

python -mpip install -r RLE/requirements.txt

virtualenv testvenv

. testenv/bin/activate

pytest RLE

