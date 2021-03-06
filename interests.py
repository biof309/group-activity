# %% Imports
import difflib
import pathlib

# %% names: interests dictionary
d = {
    "Abudi, Shachar": "Genetics",
    "Ajaj, Yasmeen": "molecular biology",
    "Ben-Omran, Munder": "Fill in interest here",
    "Bruno, Melissa": "Fill in interest here",
    "Cahill, Eileen": "hiking",
    "Callies, Katelyn": "Fill in interest here",
    "Cavazos Saldana, Alejandra": "Fill in interest here",
    "Cohen, Matan": "Fill in interest here",
    "Deveau, Ciana": "Fill in interest here",
    "Dou, Tongyi": "structural biology",
    "Duarte, Danielle": "running",
    "Fadl, Benjamin": "Fill in interest here",
    "Farkasova, Helena": "Fill in interest here",
    "Fletcher, Colin": "Fill in interest here",
    "Gardner, Danielle": "Fill in interest here",
    "Geller, Alicia": "Fill in interest here",
    "Ghosh, Banani": "Fill in interest here",
    "Gupta, Neha": "Fill in interest here",
    "Hall, Austin": "Plant pathology",
    "Jackson, Samantha": "Fill in interest here",
    "Jaeger, Catherine": "Fill in interest here",
    "Kashyap, Anuj": "Going to BIOF309 class",
    "Kim, Ji Hyun": "Fill in interest here",
    "Kirwan, Stuart": "psychology",
    "Kulam Najmudeen, Magdoom Mohamed": "Fill in interest here",
    "Lai, Yi Ling": "Fill in interest here",
    "Lehmann, Michael": "Fill in interest here",
    "Liu, Poching": "Fill in interest here",
    "Lott, Nathaniel": "Fill in interest here",
    "Magaziner, Samuel": "Fill in interest here",
    "Mehani, Bharati": "Fill in interest here",
    "Meng, Yiran": "Fill in interest here",
    "Miyazaki, Nanami": "neuroscience",
    "Mondal Laha, Satarupa": "Fill in interest here",
    "Neureiter, Elizabeth": "Fill in interest here",
    "Nicoli, Elena-Raluca": "Fill in interest here",
    "Nie, Zuqin": "Fill in interest here",
    "O'Callaghan, Georgia": "Fill in interest here",
    "Pakhchanian, Haig": "Fill in interest here",
    "Reynolds, Hayley": "Fill in interest here",
    "Sepe-Forrest, Linnea": "Neuroscience",
    "Skarzynski, Martin": "French",
    "Reynolds, Hayley": "hiking",
    "Sepe-Forrest, Linnea": "Fill in interest here",
    "Skarzynski, Martin": "French music",
    "Steenackers, Agata": "Fill in interest here",
    "Szabo, Roman": "Genetics",
    "Tan, Vee": "Fill in interest here",
    "Tiwary, Shweta": "Fill in hereinterest here",
    "Trevino, Melissa": "Fill in interest here",
    "Ullah, Ehsan": "Fill in interest here",
    "Verma, Subhash": "Fill in interest here",
    "Wang, Yiran": "structural biology",
    "Wigerblad, Gustaf": "Fill in interest here",
    "Yau, Jessica": "Fill in interest here",
    "Zhang, Shu": "Fill in interest here",
    "Zhang, Yaqiu": "Ski ",
}


# %% Search dictionary for close matches

from typing import Dict

def search_dict(query: str, dictionary: Dict, cutoff: float = 0.5):
    return [
        (key, value) for key, value
        in dictionary.items()
        if value in difflib.get_close_matches(
            query,
            dictionary.values(),
            cutoff=cutoff
        )
    ]


matches = search_dict('iking', d, cutoff=0.5)
print(matches)


# %% Save dictionary to file
pathlib.Path(
    'interested_in_iking.txt'
).write_text('\n'.join(': '.join(x) for x in matches))

# %%
