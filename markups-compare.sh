python markups-extract.py index.html > /tmp/markups-extract-index
python markups-extract.py el.html > /tmp/markups-extract-el

diff /tmp/markups-extract-index /tmp/markups-extract-el
