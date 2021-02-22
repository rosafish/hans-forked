var_type_subtypes={
    "N": ["Np", "Ns", "Nlocation"],
    "V": ["Vt", "Vi", "Vunderstand", "Vpp", "Vnpz", "Vnps", "Vconstquotentailed", "Vnonentquote"],
    "Adj": [],
    "Adv": ['Advoutent', 'Advent', 'Advembent', 'Advoutnent', 'Advnonent', 'Advembnent'],
    "Be": ['BePast'],
    "P": [],
    "Rels": [],
    "O": [],
    "Conj": [],
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

Rels = ["that", "who"]

Vunderstand = ["paid", "explored", "won", "wrote", "left", "read", "ate"]
called_objects = ["coward", "liar", "hero", "fool"]
told_objects = ["story", "lie", "truth", "secret"]
food_words = ["fruit", "salad", "broccoli", "sandwich", "rice", "corn", "ice cream"]
location_nouns = ["neighborhood", "region", "country", "town", "valley", "forest", "garden", "museum", "desert", "island", "town"]
location_nouns_b = ["museum", "school", "library", "office","laboratory"]
won_objects = ["race", "contest", "war", "prize", "competition", "election", "battle", "award", "tournament"]
read_wrote_objects = ["book", "column", "report", "poem", "letter", "novel", "story", "play", "speech"]
Vunderstand_object_dict = {}
Vunderstand_object_dict["called"] = called_objects
Vunderstand_object_dict["told"] = told_objects
Vunderstand_object_dict["brought"] = food_words
Vunderstand_object_dict["made"] = food_words
Vunderstand_object_dict["saved"] = food_words
Vunderstand_object_dict["offered"] = food_words
Vunderstand_object_dict["explored"] = location_nouns
Vunderstand_object_dict["won"] = won_objects
Vunderstand_object_dict["wrote"] = read_wrote_objects
Vunderstand_object_dict["left"] = location_nouns
Vunderstand_object_dict["read"] = read_wrote_objects
Vunderstand_object_dict["ate"] = food_words
Vunderstand_object_dict["paid"] = N

Vpp = ["studied", "paid", "helped","investigated", "presented"]
Nlocation = ["museum", "school", "library", "office","laboratory"]

Conj = ["while", "after", "before", "when", "although", "because", "since"]
Vnpz = ["hid", "moved", "presented", "paid","studied","stopped", "fought"]
Vnps = ["believed", "knew", "heard"]
Vconstquotentailed = ["forgot", "learned", "remembered", "knew"]

Advoutent = ["after", "before", "because", "although", "though", "since", "while"]
Advent = ["certainly", "definitely", "clearly", "obviously", "suddenly"]
Advembent = ["after", "before", "because", "although", "though", "since", "while"]
Advoutnent = ["if", "unless"]
Vnonentquote = ["hoped", "claimed", "thought", "believed", "said", "assumed"]
Advnonent = ["supposedly", "probably", "maybe", "hopefully"]
Advembnent = ["if","unless"]

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
    "Rels": Rels,
    "Vunderstand": Vunderstand,
    "VunderstandO": Vunderstand_object_dict,
    "Vpp": Vpp,
    "Vnonentquote": Vnonentquote,
    "Nlocation": Nlocation,
    "Conj": Conj,
    "Vnpz": Vnpz,
    "Vnps": Vnps,
    "Vconstquotentailed": Vconstquotentailed,
    "Advoutent": Advoutent,
    "Advent": Advent,
    "Advembent": Advembent,
    "Advoutnent": Advoutnent,
    "Advnonent": Advnonent,
    "Advembnent": Advembnent,
}
