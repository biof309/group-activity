# %% Imports
import difflib
import pathlib

#%% names: interests dictionary
d = {
    "Abudi, Shachar": "Fill in interest here",
    "Ajaj, Yasmeen": "Fill in interest here",
    "Ben-Omran, Munder": "Fill in interest here",
    "Bruno, Melissa": "epidemiology",
    "Cahill, Eileen": "Fill in interest here",
    "Callies, Katelyn": "Fill in interest here",
    "Cavazos Saldana, Alejandra": "Fill in interest here",
    "Cohen, Matan": "Fill in interest here",
    "Deveau, Ciana": "Fill in interest here",
    "Dou, Tongyi": "Fill in interest here",
    "Duarte, Danielle": "Fill in interest here",
    "Fadl, Benjamin": "Fill in interest here",
    "Farkasova, Helena": "Fill in interest here",
    "Fletcher, Colin": "Fill in interest her0e",
    "Gardner, Danielle": "Fill in interest here",
    "Geller, Alicia": "Fill in interest here",
    "Ghosh, Banani": "Fill in interest here",
    "Gupta, Neha": "Fill in interest here",
    "Hall, Austin": "Plant Pathology",
    "Jackson, Samantha": "Fill in interest here",
    "Jaeger, Catherine": "Fill in interest here",
    "Kashyap, Anuj": "Going to BIOF309 class",
    "Kim, Ji Hyun": "Fill in interest here",
    "Kirwan, Stuart": "Fill in interest here",
    "Kulam Najmudeen, Magdoom Mohamed": "Fill in interest here",
    "Lai, Yi Ling": "Fill in interest here",
    "Lehmann, Michael": "Fill in interest here",
    "Liu, Poching": "Fill in interest here",
    "Lott, Nathaniel": "Fill in interest here",
    "Magaziner, Samuel": "Fill in interest here",
    "Mehani, Bharati": "Fill in interest here",
    "Meng, Yiran": "Fill in interest here",
    "Miyazaki, Nanami": "Fill in interest here",
    "Mondal Laha, Satarupa": "Fill in interest here",
    "Neureiter, Elizabeth": "Fill in interest here",
    "Nicoli, Elena-Raluca": "Fill in interest here",
    "Nie, Zuqin": "Fill in interest here",
    "O'Callaghan, Georgia": "Fill in interest here",
    "Pakhchanian, Haig": "Fill in interest here",
    "Reynolds, Hayley": "Fill in interest here",
    "Sepe-Forrest, Linnea": "Fill in interest here",
    "Skarzynski, Martin": "epidemiology",
    "Steenackers, Agata": "Fill in interest here",
    "Szabo, Roman": "Fill in interest here",
    "Tan, Vee": "Fill in interest here",
    "Tiwary, Shweta": "Fill in interest here",
    "Trevino, Melissa": "Fill in interest here",
    "Ullah, Ehsan": "Fill in interest here",
    "Verma, Subhash": "Fill in interest here",
    "Wang, Yiran": "Structural Biology",
    "Wigerblad, Gustaf": "Fill in interest here",
    "Yau, Jessica": "Fill in interest here",
    "Zhang, Shu": "Fill in interest here",
    "Zhang, Yaqiu": "Fill in interest here",
}


#%% Search dictionary for close matches
def search_dict(query, dictionary, cutoff=0.8):
    return [
    (key, value) for key, value
    in dictionary.items()
    if value in difflib.get_close_matches(
           query,
           dictionary.values(),
           cutoff=cutoff
           )
    ]

matches = search_dict('epi', d, cutoff=0.15)

#%% Save dictionary to file
pathlib.Path(
    'interested_in_.txt'
).write_text('\n'.join(f'{x[0]}: {x[1]}' for x in matches))
matches

#%%
