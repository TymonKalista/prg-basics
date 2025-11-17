def hide(card_number):
    card_number = str(card_number)
    result = card_number[0:2] + ('**********') + card_number[-4:]
    return result

