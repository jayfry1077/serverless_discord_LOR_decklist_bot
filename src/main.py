from lor_deckcodes import LoRDeck, CardCodeAndCount
import json


def main(event, context):

    deck_code = event['deck_code']
    deck = LoRDeck.from_deckcode(deck_code)
    card_names = json.load(open('card_names.json'))

    faction_1 = ''
    faction_2 = ''
    faction_1_cards = []
    faction_2_cards = []

    message = f'```fix \n#Deck Code: {deck_code}```\n'

    region_list = []
    [region_list.append(card.faction)
     for card in deck.cards if card.faction not in region_list]

    for card in deck.cards:
        qty = str(card).split(':')[0]
        card_name = card_names[str(card).split(':')[1]]

        if faction_1 == '':
            faction_1 = card.faction
        elif faction_2 == '' and card.faction != faction_1:
            faction_2 = card.faction

        if card.faction == faction_1:
            faction_1_cards.append(f'{qty}:{card_name}\n')
        else:
            faction_2_cards.append(f'{qty}:{card_name}\n')

    message += f'Faction: {faction_1}\n```{"".join(faction_1_cards)}```\n'

    if len(region_list) > 1:
        message += f'Faction: {faction_2}\n```{"".join(faction_2_cards)}```'

    print(message)


# main({'deck_code': 'CEBQIAICAYNCIKYHAEBQODYUEUTCQNYBAMBAWAADAIAQGGZTAEAQEMIBAIBAO'}, 'hmm')
