def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Function sorts a package based on it's dimensions( width, height, lenght)
    and weight (mass).
    A package is considered bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ 
    or when one of its dimensions is greater or equal to 150 cm.
    A package is heavy when its mass is greater or equal to 20 kg.
    if the package is heavy and bulky it is REJECTED,
    if it's only bulky or heavy is marked as SPECIAL,
    otherwise is STANRDAD.
    """
    if (width*height*length >= 1000000 or width >= 150 or height >= 150 or length >= 150) and mass >= 20:
        return "REJECTED"
    elif (width*height*length >= 1000000 or width >= 150 or height >= 150 or length >= 150) or mass >= 20:
        return "SPECIAL"
    else:
        return "STANDARD"
    
