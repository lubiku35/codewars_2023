def rain_amount(mm):
    return "Your plant has had more than enough water for today!" if mm >= 40 else f"You need to give your plant {40 - mm}mm of water"