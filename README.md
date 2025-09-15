# pathways-sorting-challenge
Python solution for Pathways Backend Debugging Challenge (Package Sorting).
# Pathways Sorting Challenge 

This repository contains my solution for the Pathways Backend Debugging Challenge.  
The task is to implement a function that classifies packages into the correct stack (`STANDARD`, `SPECIAL`, or `REJECTED`) based on their dimensions and mass.

Packages are classified as follows:

- A package is bulky if:
  - Its volume (Width × Height × Length) ≥ 1,000,000 cm³, OR
  - Any of its dimensions ≥ 150 cm
- A package is heavy if:
  - Its mass ≥ 20 kg

### Stacks
- STANDARD → not bulky and not heavy  
- SPECIAL → bulky OR heavy  
- REJECTED → bulky AND heavy  


Implemented in `challenge.py`:
def sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    bulky = True if (volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150) else False
    heavy = True if mass >= 20 else False
    return "REJECTED" if bulky and heavy else ("SPECIAL" if bulky or heavy else "STANDARD")
