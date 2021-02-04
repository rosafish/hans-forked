var_type_subtypes={
    "N": ["Np", "Ns"],
    "V": ["Vt", "Vi"],
    "Adj": [],
    "Adv": [],
    "Be": [],
    "P": [],
}

Ns=["professor", "student", "president","judge","senator","programmer","doctor","lawyer","scientist","banker","tourist","manager","artist","author","actor","athlete", \
    "designer", "animator", "architect", "administrator", "artisan", "therapist", "baker", "artist", "officer", \
    "colorist", "curator", "dancer", "director", "strategist", "essayist", "planner", "stylist", "illustrator", "lyricist", \
    "musician", "penciller", "photographer", "photojournalist", "potter", "sculptor", "singer", "writer", \
    "chaplain", "analyst", "counselor", "nurse", "psychiatrist", "psychologist", "psychotherapist", "worker", "engineer", \
    "technologist", "technician"]
Np=["professors", "students", "presidents","judges","senators","programmers","doctors","lawyers","scientists","bankers","tourists","managers","artists","authors","actors","athletes", \
    "designers", "animators", "architects", "administrators", "artisans", "therapists", "bakers", "artists", "officers", \
    "colorists", "curators", "dancers", "directors", "strategists", "essayists", "planners", "stylists", "illustrators", "lyricists", \
    "musicians", "pencillers", "photographers", "photojournalists", "potters", "sculptors", "singers", "writers", \
    "chaplains", "analysts", "counselors", "nurses", "psychiatrists", "psychologists", "psychotherapists", "workers", "engineers", \
    "technologists", "technicians"]
N=Np+Ns

Vt=["recommended", "called", "helped","supported","contacted","avoided","advised","saw","introduced","mentioned","encouraged","thanked", \
    "recognized","admired", "addressed", "needed", "brought", "disturbed", "deceived", "offended", "affected", "found", "expected"]
Vi=["slept", "danced", "ran","shouted","resigned","waited", "arrived", "performed", \
    "voted", "sat", "laughed", "agreed", "appeared", "continued", "cried", "died", "existed", "grew", "lay", "listened", "panicked", "smiled", \
    "talked", "worked", "yell"]
V=Vi+Vt

P=["near", "behind", "by", "in front of", "next to"] 

Adj = ["important", "popular", "famous", "young", "happy", "helpful", "serious", "angry", \
       "ambitious", "agreeable", "angry", "thoughtless", "obedient", "reliable", "witty", "silly", "gentle", "compassionate", "lazy", "nervous"] 

Adv = ["quickly", "slowly", "happily", "easily", "quietly", "thoughtfully", \
       "anxiously", "arrogantly", "awkwardly", "bashfully", "bitterly", "blindly", "blissfully", "boastfully", "boldly", "bravely", "briefly", "brightly", "briskly", \
       "broadly", "busily", "calmly", "carefully", "carelessly", "cautiously", "certainly", "cheerfully"] 

var_of_string={
    "N": N,
    "Ns": Ns,
    "Np": Np,
    "V": V,
    "Vt": Vt,
    "Vi": Vi,
    "Adj": Adj,
    "Adv": Adv,
    "P": P,
}