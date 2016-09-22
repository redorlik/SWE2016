
pip install -r requirements.txt

virtualenv testvenv

. testenv/bin/activate

pytest RLE

