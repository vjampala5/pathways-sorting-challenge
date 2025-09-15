def sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    bulky = True if (volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150) else False
    heavy = True if mass >= 20 else False
    return "REJECTED" if bulky and heavy else "SPECIAL" if bulky or heavy else "STANDARD"



# Example runs
if __name__ == "__main__":
    print(sort(100, 100, 100, 10))   # STANDARD
    print(sort(200, 50, 50, 10))     # SPECIAL
    print(sort(100, 100, 100, 25))   # SPECIAL
    print(sort(200, 200, 200, 25))   # REJECTED
