import json

set1 = {card['cardCode']: card['name']
        for card in json.load(open('set1-en_us.json', encoding='utf8'))}
set2 = {card['cardCode']: card['name']
        for card in json.load(open('set2-en_us.json', encoding='utf8'))}
set3 = {card['cardCode']: card['name']
        for card in json.load(open('set3-en_us.json', encoding='utf8'))}

cards = {**set1, **set2, **set3}

# just using this to shirnk the .json for cards.
f = open('card_names.json', 'w')
f.write(json.dumps(cards))
f.close()
