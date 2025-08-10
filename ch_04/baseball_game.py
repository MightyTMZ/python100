def baseball_game(inning, half, first, second, third, balls, strikes, home, away):
    # inning with ordinal suffix
    def ordinal(n):
        return f"{n}{'th' if 11<=n%100<=13 else {1:'st',2:'nd',3:'rd'}.get(n%10, 'th')}"
    
    # half inning word
    half_str = "Top" if half.lower() == "top" else "Bottom"

    # bases occupied
    bases = []
    if first:
        bases.append("first")
    if second:
        bases.append("second")
    if third:
        bases.append("third")

    bases_str = "no runners on base" if not bases else "runner" + ("s" if len(bases) > 1 else "") + " on " + ", ".join(bases)

    # balls and strikes
    balls_str = f"{balls} ball{'s' if balls != 1 else ''}"
    strikes_str = f"{strikes} strike{'s' if strikes != 1 else ''}"

    # score summary
    score_str = f"Score — Home: {home}, Away: {away}"

    # final result string
    result = (f"{half_str} of the {ordinal(inning)} inning. "
              f"There are {balls_str} and {strikes_str}. "
              f"There {'is' if len(bases) == 1 else 'are'} {bases_str}. "
              f"{score_str}.")

    return result

