import random 

Ns = []
Np = []
N = []
Vt = []
Vi = []
V = []
P = []
Adj = []
Adv = []
Rels = []
Vunderstand = []
called_objects = []
told_objects = []
food_words = []
location_nouns = []
location_nouns_b = []
won_objects = []
read_wrote_objects = []
Vpp = []
Nlocation = []
Conj = []
Vnpz = []
Vnps = []
Vconstquotentailed = []
Advoutent = []
Advent = []
Advembent = []
Advoutnent = []
Vnonentquote = []
Advnonent = []
Advembnent = []
var_of_string = None

Ns_ind = []
Np_ind = []
N_ind = []
Vt_ind = []
Vi_ind = []
V_ind = []
P_ind = []
Adj_ind = []
Adv_ind = []
Rels_ind = []
Vunderstand_ind = []
called_objects_ind = []
told_objects_ind = []
food_words_ind = []
location_nouns_ind = []
location_nouns_b_ind = []
won_objects_ind = []
read_wrote_objects_ind = []
Vpp_ind = []
Nlocation_ind = []
Conj_ind = []
Vnpz_ind = []
Vnps_ind = []
Vconstquotentailed_ind = []
Advoutent_ind = []
Advent_ind = []
Advembent_ind = []
Advoutnent_ind = []
Vnonentquote_ind = []
Advnonent_ind = []
Advembnent_ind = []

Ns_ood = []
Np_ood = []
N_ood = []
Vt_ood = []
Vi_ood = []
V_ood = []
P_ood = []
Adj_ood = []
Adv_ood = []
Rels_ood = []
Vunderstand_ood = []
called_objects_ood = []
told_objects_ood = []
food_words_ood = []
location_nouns_ood = []
location_nouns_b_ood = []
won_objects_ood = []
read_wrote_objects_ood = []
Vpp_ood = []
Nlocation_ood = []
Conj_ood = []
Vnpz_ood = []
Vnps_ood = []
Vconstquotentailed_ood = []
Advoutent_ood = []
Advent_ood = []
Advembent_ood = []
Advoutnent_ood = []
Vnonentquote_ood = []
Advnonent_ood = []
Advembnent_ood = []

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

Ns_all=["professor", "student", "president","judge","senator","programmer","doctor","lawyer","scientist","banker","tourist","manager","artist","author","actor","athlete", \
    "designer", "animator", "architect", "administrator", "artisan", "therapist", "baker", "artist", "officer", \
    "colorist", "curator", "dancer", "director", "strategist", "essayist", "planner", "stylist", "illustrator", "lyricist", \
    "musician", "penciller", "photographer", "photojournalist", "potter", "sculptor", "singer", "writer", \
    "chaplain", "analyst", "counselor", "nurse", "psychiatrist", "psychologist", "psychotherapist", "worker", "engineer", \
    "technologist", "technician"]
Np_all=["professors", "students", "presidents","judges","senators","programmers","doctors","lawyers","scientists","bankers","tourists","managers","artists","authors","actors","athletes", \
    "designers", "animators", "architects", "administrators", "artisans", "therapists", "bakers", "artists", "officers", \
    "colorists", "curators", "dancers", "directors", "strategists", "essayists", "planners", "stylists", "illustrators", "lyricists", \
    "musicians", "pencillers", "photographers", "photojournalists", "potters", "sculptors", "singers", "writers", \
    "chaplains", "analysts", "counselors", "nurses", "psychiatrists", "psychologists", "psychotherapists", "workers", "engineers", \
    "technologists", "technicians"]
N_all=Np_all+Ns_all

Vt_all=["recommended", "called", "helped","supported","contacted","avoided","advised","saw","introduced","mentioned","encouraged","thanked", \
    "recognized","admired", "addressed", "needed", "brought", "disturbed", "deceived", "offended", "affected", "found", "expected"]
Vi_all=["slept", "danced", "ran","shouted","resigned","waited", "arrived", "performed", \
    "voted", "sat", "laughed", "agreed", "appeared", "continued", "cried", "died", "existed", "grew", "lay", "listened", "panicked", "smiled", \
    "talked", "worked", "yelled"]
V_all=Vi_all+Vt_all

P_all=["near", "behind", "by", "in front of", "next to"]

Adj_all = ["important", "popular", "famous", "young", "happy", "helpful", "serious", "angry", \
       "ambitious", "agreeable", "angry", "thoughtless", "obedient", "reliable", "witty", "silly", "gentle", "compassionate", "lazy", "nervous"]

Adv_all = ["quickly", "slowly", "happily", "easily", "quietly", "thoughtfully", \
       "anxiously", "arrogantly", "awkwardly", "bashfully", "bitterly", "blindly", "blissfully", "boastfully", "boldly", "bravely", "briefly", "brightly", "briskly", \
       "broadly", "busily", "calmly", "carefully", "carelessly", "cautiously", "certainly", "cheerfully"]

Rels_all = ["that", "who"]

Vunderstand_all = ["paid", "explored", "won", "wrote", "left", "read", "ate"]
called_objects_all = ["coward", "liar", "hero", "fool"]
told_objects_all = ["story", "lie", "truth", "secret"]
food_words_all = ["fruit", "salad", "broccoli", "sandwich", "rice", "corn", "ice cream"]
location_nouns_all = ["neighborhood", "region", "country", "town", "valley", "forest", "garden", "museum", "desert", "island", "town"]
location_nouns_b_all = ["museum", "school", "library", "office","laboratory"]
won_objects_all = ["race", "contest", "war", "prize", "competition", "election", "battle", "award", "tournament"]
read_wrote_objects_all = ["book", "column", "report", "poem", "letter", "novel", "story", "play", "speech"]

Vunderstand_object_dict = {}
Vunderstand_object_dict["called"] = called_objects_all
Vunderstand_object_dict["told"] = told_objects_all
Vunderstand_object_dict["brought"] = food_words_all
Vunderstand_object_dict["made"] = food_words_all
Vunderstand_object_dict["saved"] = food_words_all
Vunderstand_object_dict["offered"] = food_words_all
Vunderstand_object_dict["explored"] = location_nouns_all
Vunderstand_object_dict["won"] = won_objects_all
Vunderstand_object_dict["wrote"] = read_wrote_objects_all
Vunderstand_object_dict["left"] = location_nouns_all
Vunderstand_object_dict["read"] = read_wrote_objects_all
Vunderstand_object_dict["ate"] = food_words_all
Vunderstand_object_dict["paid"] = N_all

Vpp_all = ["studied", "paid", "helped","investigated", "presented"]
Nlocation_all = ["museum", "school", "library", "office","laboratory"]

Conj_all = ["while", "after", "before", "when", "although", "because", "since"]
Vnpz_all = ["hid", "moved", "presented", "paid","studied","stopped", "fought"]
Vnps_all = ["believed", "knew", "heard"]
Vconstquotentailed_all = ["forgot", "learned", "remembered", "knew"]

Advoutent_all = ["after", "before", "because", "although", "though", "since", "while"]
Advent_all = ["certainly", "definitely", "clearly", "obviously", "suddenly"]
Advembent_all = ["after", "before", "because", "although", "though", "since", "while"]
Advoutnent_all = ["if", "unless"]
Vnonentquote_all = ["hoped", "claimed", "thought", "believed", "said", "assumed"]
Advnonent_all = ["supposedly", "probably", "maybe", "hopefully"]
Advembnent_all = ["if","unless"]


def split_in_half(alist):
    random.shuffle(alist)
    desired_length = int(len(alist)/2)
    return alist[:desired_length], alist[desired_length:]


def ind_ood_split():
    global Ns_ind
    global Np_ind
    global N_ind
    global Vt_ind
    global Vi_ind
    global V_ind
    global P_ind
    global Adj_ind
    global Adv_ind
    global Rels_ind
    global Vunderstand_ind
    global called_objects_ind
    global told_objects_ind
    global food_words_ind
    global location_nouns_ind
    global location_nouns_b_ind
    global won_objects_ind
    global read_wrote_objects_ind
    global Vpp_ind
    global Nlocation_ind
    global Conj_ind
    global Vnpz_ind
    global Vnps_ind
    global Vconstquotentailed_ind
    global Advoutent_ind
    global Advent_ind
    global Advembent_ind
    global Advoutnent_ind
    global Vnonentquote_ind
    global Advnonent_ind
    global Advembnent_ind

    global Ns_ood
    global Np_ood
    global N_ood
    global Vt_ood
    global Vi_ood
    global V_ood
    global P_ood
    global Adj_ood
    global Adv_ood
    global Rels_ood
    global Vunderstand_ood
    global called_objects_ood
    global told_objects_ood
    global food_words_ood
    global location_nouns_ood
    global location_nouns_b_ood
    global won_objects_ood
    global read_wrote_objects_ood
    global Vpp_ood
    global Nlocation_ood
    global Conj_ood
    global Vnpz_ood
    global Vnps_ood
    global Vconstquotentailed_ood
    global Advoutent_ood
    global Advent_ood
    global Advembent_ood
    global Advoutnent_ood
    global Vnonentquote_ood
    global Advnonent_ood
    global Advembnent_ood

    Ns_ind, Ns_ood = split_in_half(Ns_all)
    Np_ind = [elt+"s" for elt in Ns_ind] #add s to words in nouns_sg_train
    Np_ood = [elt+"s" for elt in Ns_ood] #add s to words in nouns_sg_test
    N_ind= Ns_ind + Np_ind
    N_ood = Ns_ood + Np_ood

    Vt_ind, Vt_ood = split_in_half(Vt_all)
    Vi_ind, Vi_ood = split_in_half(Vi_all)
    V_ind = Vt_ind + Vi_ind
    V_ood = Vt_ood + Vi_ood

    P_ind, P_ood = split_in_half(P_all)
    Adj_ind, Adj_ood = split_in_half(Adj_all)
    Adv_ind, Adv_ood = split_in_half(Adv_all)

    Rels_ind, Rels_ood = split_in_half(Rels_all)
    Vunderstand_ind, Vunderstand_ood = split_in_half(Vunderstand_all)
    called_objects_ind, called_objects_ood = split_in_half(called_objects_all)
    told_objects_ind, told_objects_ood = split_in_half(told_objects_all)
    food_words_ind, food_words_ood = split_in_half(food_words_all)
    location_nouns_ind, location_nouns_ood = split_in_half(location_nouns_all)
    location_nouns_b_ind, location_nouns_b_ood = split_in_half(location_nouns_b_all)
    won_objects_ind, won_objects_ood = split_in_half(won_objects_all)
    read_wrote_objects_ind, read_wrote_objects_ood = split_in_half(read_wrote_objects_all)
    Vpp_ind, Vpp_ood = split_in_half(Vpp_all)
    Nlocation_ind, Nlocation_ood = split_in_half(Nlocation_all)
    Conj_ind, Conj_ood = split_in_half(Conj_all)
    Vnpz_ind, Vnpz_ood = split_in_half(Vnpz_all)
    Vnps_ind, Vnps_ood = split_in_half(Vnps_all)
    Vconstquotentailed_ind, Vconstquotentailed_ood = split_in_half(Vconstquotentailed_all)
    Advoutent_ind, Advoutent_ood = split_in_half(Advoutent_all)
    Advent_ind, Advent_ood = split_in_half(Advent_all)
    Advembent_ind, Advembent_ood = split_in_half(Advembent_ood)
    Advoutnent_ind, Advoutnent_ood = split_in_half(Advoutnent_all)
    Vnonentquote_ind, Vnonentquote_ood = split_in_half(Vnonentquote_all)
    Advnonent_ind, Advnonent_ood = split_in_half(Advnonent_all)
    Advembnent_ind, Advembnent_ood = split_in_half(Advembnent_all)

    
def set_vocab_by_type(data_type):
    # data_type can be either "ind" or "ood" 
    global Ns
    global Np
    global N
    global Vt
    global Vi
    global V
    global P 
    global Adj 
    global Adv 
    global Rels 
    global Vunderstand 
    global called_objects 
    global told_objects 
    global food_words
    global location_nouns 
    global location_nouns_b 
    global won_objects
    global read_wrote_objects 
    global Vpp 
    global Nlocation 
    global Conj 
    global Vnpz 
    global Vnps 
    global Vconstquotentailed 
    global Advoutent 
    global Advent 
    global Advembent 
    global Advoutnent 
    global Vnonentquote 
    global Advnonent 
    global Advembnent 
    global Vunderstand_object_dict
    global var_of_string

    if data_type == "ind":
        Ns = Ns_ind
        Np = Np_ind
        N = N_ind
        print('N: ', N)
        print('N_ind: ', N_ind)
        Vt = Vt_ind
        Vi = Vi_ind
        V = V_ind
        P = P_ind
        Adj = Adj_ind
        Adv = Adv_ind
        Rels = Rels_ind
        Vunderstand = Vunderstand_ind
        called_objects = called_objects_ind
        told_objects = told_objects_ind
        food_words = food_words_ind
        location_nouns = location_nouns_ind
        location_nouns_b = location_nouns_b_ind
        won_objects = won_objects_ind
        read_wrote_objects = read_wrote_objects_ind
        Vpp = Vpp_ind
        Nlocation = Nlocation_ind
        Conj = Conj_ind
        Vnpz = Vnpz_ind
        Vnps = Vnps_ind
        Vconstquotentailed = Vconstquotentailed_ind
        Advoutent = Advoutent_ind
        Advent = Advent_ind
        Advembent = Advembent_ind
        Advoutnent = Advoutnent_ind
        Vnonentquote = Vnonentquote_ind
        Advnonent = Advnonent_ind
        Advembnent = Advembnent_ind

        # update Vunderstand_object_dict
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

    elif data_type == "ood":
        Ns = Ns_ood
        Np = Np_ood
        N = N_ood
        Vt = Vt_ood
        Vi = Vi_ood
        V = V_ood
        P = P_ood
        Adj = Adj_ood
        Adv = Adv_ood
        Rels = Rels_ood
        Vunderstand = Vunderstand_ood
        called_objects = called_objects_ood
        told_objects = told_objects_ood
        food_words = food_words_ood
        location_nouns = location_nouns_ood
        location_nouns_b = location_nouns_b_ood
        won_objects = won_objects_ood
        read_wrote_objects = read_wrote_objects_ood
        Vpp = Vpp_ood
        Nlocation = Nlocation_ood
        Conj = Conj_ood
        Vnpz = Vnpz_ood
        Vnps = Vnps_ood
        Vconstquotentailed = Vconstquotentailed_ood
        Advoutent = Advoutent_ood
        Advent = Advent_ood
        Advembent = Advembent_ood
        Advoutnent = Advoutnent_ood
        Vnonentquote = Vnonentquote_ood
        Advnonent = Advnonent_ood
        Advembnent = Advembnent_ood

        # update Vunderstand_object_dict
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

    else:
        print("Wrong data type!")

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
