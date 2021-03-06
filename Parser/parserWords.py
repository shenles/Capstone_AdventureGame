from action import Action

# Class variables
verbDict = {
    "go": "move_user",
    "move": "move_user",
    "run": "move_user",
    "walk": "move_user",
    "head": "move_user",
    "hurry": "move_user",
    "sneak": "move_user",
    "stroll": "move_user",
    "sprint": "move_user",
    "jog": "move_user",
    "take": "take",
    "grab": "take",
    "get": "take",
    "pick": "take",
    "keep": "take",
    "stow": "take",
    "steal": "take",
    "acquire": "take",
    "collect": "take",
    "drop": "drop", 
    "abandon": "drop",
    "discard": "drop",
    "trash": "drop",
    "put": "drop",
    "place": "drop",
    "insert": "insert", 
    "sleep": "sleep",
    "rest": "sleep",
    "relax": "sleep",
    "talk": "talk_npc",
    "say": "talk_npc",
    "greet": "talk_npc",
    "ask": "talk_npc",
    "yell": "talk_npc",
    "scream": "talk_npc",
    "shout": "talk_npc",
    "tell": "talk_npc",
    "call": "talk_npc",
    "chat": "talk_npc",
    "speak": "talk_npc",
    "look": "look",
    "examine": "look",
    "x": "look",
    "l": "look",
    "study": "look",
    "find": "look",
    "touch": "look",
    "check": "look",
    "peer": "look",
    "peek": "look",
    "see": "look",
    "inspect": "look",
    "stare": "look",
    "gaze": "look",
    "glance": "look",
    "look_in": "search",
    "search": "search", 
    "read": "read",
    "listen": "listen",
    "eavesdrop": "listen",
    "hear": "listen", 
    "open": "open_thing",
    "unlock": "unlock_thing",
    "help": "show_help",
    "inventory": "show_inventory",
    "save": "save_game",
    "load": "load_game",
    "activate": "activate",
    "hit": "do_violence",
    "stab": "do_violence",
    "murder": "do_violence",
    "kill": "do_violence",
    "punch": "do_violence",
    "tackle": "do_violence",
    "wrestle": "do_violence",
    "fight": "do_violence",
    "harm": "do_violence", 
    "kick": "do_violence",
    "shoot": "do_violence",
    "break": "do_violence",
    "damage": "do_violence",
    "destroy": "do_violence"
}

verbListUnused = {
    "absorb",
    "accept",
    "accompany",
    "ache",
    "achieve",
    "act",
    "activate",
    "add",
    "address",
    "adjust",
    "admire",
    "admit",
    "advise",
    "afford",
    "agree",
    "allow",
    "animate",
    "announce",
    "answer",
    "apologize",
    "appear",
    "applaud",
    "apply",
    "approach",
    "approve",
    "argue",
    "arise",
    "arrange",
    "arrest",
    "assert",
    "assort",
    "astonish",
    "attack",
    "attend",
    "attract",
    "audit",
    "avoid",
    "awake",
    "bang",
    "banish",
    "bash",
    "bat",
    "be",
    "beat",
    "beautify",
    "become",
    "befall",
    "beg",
    "begin",
    "behave",
    "behold",
    "believe",
    "belong",
    "bend",
    "bereave",
    "beseech",
    "bet",
    "betray",
    "bid",
    "bind",
    "bite",
    "bleed",
    "bless",
    "blow",
    "boast",
    "boil",
    "bray",
    "break",
    "breathe",
    "breed",
    "bring",
    "broadcast",
    "build",
    "burn",
    "burst",
    "bury",
    "bust",
    "buy",
    "buzz",
    "calculate",
    "capture",
    "caress",
    "carry",
    "carve",
    "cash",
    "cast",
    "catch",
    "cause",
    "cease",
    "celebrate",
    "challenge",
    "change",
    "charge",
    "chase",
    "cheer",
    "chew",
    "chide",
    "chip",
    "choke",
    "choose",
    "classify",
    "clean",
    "cleave",
    "click",
    "climb",
    "cling",
    "close",
    "clothe",
    "clutch",
    "collapse",
    "colour",
    "come",
    "comment",
    "compare",
    "compel",
    "compete",
    "complain",
    "complete",
    "conclude",
    "conduct",
    "confess",
    "confine",
    "confiscate",
    "confuse",
    "congratulate",
    "connect",
    "connote",
    "conquer",
    "consecrate",
    "consent",
    "conserve",
    "consider",
    "consign",
    "consist",
    "console",
    "consort",
    "conspire",
    "constitute",
    "constrain",
    "construct",
    "construe",
    "consult",
    "contain",
    "contemn",
    "contend",
    "contest",
    "continue",
    "contract",
    "contradict",
    "contrast",
    "contribute",
    "contrive",
    "control",
    "convene",
    "converge",
    "converse",
    "convert",
    "convey",
    "convict",
    "convince",
    "coo",
    "cool",
    "co-operate",
    "cope",
    "copy",
    "correct",
    "correspond",
    "corrode",
    "corrupt",
    "cost",
    "cough",
    "counsel",
    "count",
    "course",
    "cover",
    "cower",
    "crack",
    "crackle",
    "crash",
    "crave",
    "create",
    "creep",
    "crush",
    "cry",
    "cure",
    "curve",
    "cut",
    "cycle",
    "damage",
    "damp",
    "dance",
    "dare",
    "dash",
    "dazzle",
    "deal",
    "decay",
    "decide",
    "declare",
    "decorate",
    "decrease",
    "dedicate",
    "delay",
    "delete",
    "deny",
    "depend",
    "deprive",
    "derive",
    "describe",
    "desire",
    "detach",
    "detect",
    "determine",
    "develop",
    "die",
    "differ",
    "dig",
    "digest",
    "dim",
    "diminish",
    "dine",
    "dip",
    "direct",
    "disappear",
    "discover",
    "discuss",
    "disobey",
    "display",
    "dispose",
    "distribute",
    "disturb",
    "disuse",
    "dive",
    "divide",
    "do",
    "donate",
    "download",
    "drag",
    "draw",
    "dream",
    "dress",
    "drill",
    "drink",
    "drive",
    "dry",
    "dump",
    "dwell",
    "dye",
    "earn",
    "eat",
    "educate",
    "empower",
    "empty",
    "encircle",
    "encourage",
    "encroach",
    "endanger",
    "endorse",
    "endure",
    "engrave",
    "enjoy",
    "enlarge",
    "enlighten",
    "enter",
    "envy",
    "erase",
    "escape",
    "evaporate",
    "exchange",
    "exclaim",
    "exclude",
    "exist",
    "expand",
    "expect",
    "explain",
    "explore",
    "express",
    "extend",
    "eye",
    "face",
    "fail",
    "faint",
    "fall",
    "fan",
    "fancy",
    "favour",
    "fax",
    "feed",
    "feel",
    "ferry",
    "fetch",
    "fight",
    "fill",
    "finish",
    "fish",
    "fit",
    "fix",
    "fizz",
    "flap",
    "flee",
    "fling",
    "float",
    "flop",
    "fly",
    "fold",
    "follow",
    "forbid",
    "force",
    "forecast",
    "foretell",
    "forget",
    "forgive",
    "forlese",
    "form",
    "forsake",
    "found",
    "frame",
    "free",
    "freeze",
    "frighten",
    "fry",
    "gag",
    "gain",
    "gainsay",
    "gash",
    "give",
    "glitter",
    "google",
    "govern",
    "grade",
    "grant",
    "grind",
    "grip",
    "grow",
    "guard",
    "guess",
    "guide",
    "handle",
    "hang",
    "happen",
    "hatch",
    "hate",
    "have",
    "heal",
    "heave",
    "help",
    "hew",
    "hide",
    "hinder",
    "hiss",
    "hoax",
    "hold",
    "hop",
    "hope",
    "horrify",
    "hug",
    "hum",
    "humiliate",
    "hunt",
    "hurl",
    "hurry",
    "hurt",
    "hush",
    "hustle",
    "hypnotize",
    "idealize",
    "identify",
    "idolize",
    "ignite",
    "ignore",
    "illuminate",
    "illustrate",
    "imagine",
    "imbibe",
    "imitate",
    "immerse",
    "impair",
    "impart",
    "impeach",
    "impede",
    "impel",
    "impend",
    "imperil",
    "impinge",
    "implant",
    "implicate",
    "implode",
    "implore",
    "imply",
    "import",
    "impose",
    "impress",
    "imprint",
    "imprison",
    "improve",
    "inaugurate",
    "incise",
    "include",
    "increase",
    "inculcate",
    "indent",
    "indicate",
    "induce",
    "indulge",
    "infect",
    "infest",
    "inflame",
    "inflate",
    "inflect",
    "inform",
    "infringe",
    "infuse",
    "ingest",
    "inhabit",
    "inhale",
    "inherit",
    "initiate",
    "inject",
    "injure",
    "inlay",
    "innovate",
    "input",
    "inquire",
    "inscribe",
    "inspire",
    "install",
    "insult",
    "insure",
    "integrate",
    "introduce",
    "invent",
    "invite",
    "join",
    "jump",
    "justify",
    "kid",
    "kill",
    "kiss",
    "kneel",
    "knit",
    "knock",
    "know",
    "latch",
    "laugh",
    "lead",
    "leak",
    "lean",
    "leap",
    "learn",
    "leer",
    "lend",
    "let",
    "lick",
    "lie",
    "lift",
    "like",
    "limp",
    "live",
    "lose",
    "love",
    "magnify",
    "maintain",
    "make",
    "manage",
    "march",
    "mark",
    "marry",
    "mash",
    "matter",
    "mean",
    "measure",
    "meet",
    "melt",
    "merge",
    "mew",
    "migrate",
    "milk",
    "mind",
    "mislead",
    "miss",
    "mistake",
    "misuse",
    "mix",
    "moan",
    "modify",
    "moo",
    "motivate",
    "mould",
    "moult",
    "move",
    "mow",
    "multiply",
    "murmur",
    "nail",
    "nap",
    "need",
    "neglect",
    "nip",
    "nod",
    "note",
    "notice",
    "notify",
    "nourish",
    "nurse",
    "obey",
    "oblige",
    "observe",
    "obstruct",
    "obtain",
    "occupy",
    "occur",
    "offer",
    "offset",
    "omit",
    "ooze",
    "operate",
    "opine",
    "oppress",
    "opt",
    "optimize",
    "order",
    "organize",
    "originate",
    "output",
    "overflow",
    "overtake",
    "owe",
    "own",
    "pacify",
    "pardon",
    "part",
    "partake",
    "participate",
    "pass",
    "paste",
    "pat",
    "patch",
    "pause",
    "pay",
    "peep",
    "perish",
    "permit",
    "persuade",
    "phone",
    "place",
    "plan",
    "play",
    "plead",
    "please",
    "plod",
    "plot",
    "pluck",
    "ply",
    "point",
    "polish",
    "pollute",
    "ponder",
    "pour",
    "pout",
    "practice",
    "praise",
    "pray",
    "preach",
    "prefer",
    "prepare",
    "prescribe",
    "present",
    "preserve",
    "preset",
    "preside",
    "press",
    "pretend",
    "prevent",
    "print",
    "proceed",
    "produce",
    "progress",
    "prohibit",
    "promise",
    "propose",
    "prosecute",
    "protect",
    "prove",
    "provide",
    "pull",
    "punish",
    "purify",
    "push",
    "qualify",
    "quarrel",
    "question",
    "race",
    "rattle",
    "reach",
    "read",
    "realize",
    "rebuild",
    "recall",
    "recast",
    "receive",
    "recite",
    "recognize",
    "recollect",
    "recur",
    "redo",
    "reduce",
    "refer",
    "reflect",
    "refuse",
    "regard",
    "regret",
    "relate",
    "rely",
    "remain",
    "remake",
    "remove",
    "rend",
    "renew",
    "renounce",
    "repair",
    "repeat",
    "replace",
    "reply",
    "report",
    "request",
    "resell",
    "resemble",
    "reset",
    "resist",
    "resolve",
    "respect",
    "restrain",
    "retain",
    "retch",
    "retire",
    "return",
    "reuse",
    "review",
    "rewind",
    "rid",
    "ride",
    "ring",
    "rise",
    "roar",
    "rob",
    "roll",
    "rot",
    "rub",
    "rule",
    "rush",
    "sabotage",
    "sacrifice",
    "sadden",
    "saddle",
    "sag",
    "sally",
    "salute",
    "salvage",
    "salve",
    "sample",
    "sanctify",
    "sanction",
    "saponify",
    "sashay",
    "sass",
    "sate",
    "satiate",
    "satirise",
    "satisfy",
    "saturate",
    "saunter",
    "savor",
    "savvy",
    "saw",
    "scab",
    "scald",
    "scale",
    "scam",
    "scan",
    "scant",
    "scar",
    "scare",
    "scarify",
    "scarp",
    "scat",
    "scatter",
    "scold",
    "scorch",
    "scowl",
    "scrawl",
    "screw",
    "scrub",
    "search",
    "seat",
    "secure",
    "seek",
    "seem",
    "seize",
    "select",
    "sell",
    "send",
    "sentence",
    "separate",
    "set",
    "sever",
    "sew",
    "shake",
    "shape",
    "share",
    "shatter",
    "shave",
    "shear",
    "shed",
    "shine",
    "shirk",
    "shit",
    "shiver",
    "shock",
    "shorten",
    "show",
    "shrink",
    "shun",
    "shut",
    "sight",
    "signal",
    "signify",
    "sing",
    "sip",
    "sit",
    "ski",
    "skid",
    "slam",
    "slay",
    "slide",
    "slim",
    "sling",
    "slink",
    "slip",
    "slit",
    "smash",
    "smile",
    "smite",
    "smooth",
    "smother",
    "snap",
    "snatch",
    "sneeze",
    "sniff",
    "soar",
    "sob",
    "solicit",
    "solve",
    "soothe",
    "sort",
    "sow",
    "sparkle",
    "speak",
    "speed",
    "spell",
    "spend",
    "spill",
    "spin",
    "spit",
    "split",
    "spoil",
    "spray",
    "spread",
    "spring",
    "sprout",
    "squeeze",
    "stand",
    "start",
    "state",
    "stay",
    "steep",
    "stem",
    "step",
    "sterilize",
    "stick",
    "stimulate",
    "sting",
    "stink",
    "stir",
    "stitch",
    "stoop",
    "stop",
    "store",
    "strain",
    "stray",
    "stress",
    "stretch",
    "strew",
    "stride",
    "strike",
    "string",
    "strive",
    "submit",
    "subscribe",
    "subtract",
    "succeed",
    "suck",
    "suffer",
    "suggest",
    "summon",
    "supply",
    "support",
    "suppose",
    "surge",
    "surmise",
    "surpass",
    "surround",
    "survey",
    "survive",
    "swallow",
    "sway",
    "swear",
    "sweat",
    "sweep",
    "swell",
    "swim",
    "swing",
    "tap",
    "taste",
    "tax",
    "teach",
    "tear",
    "tee",
    "tempt",
    "tend",
    "terminate",
    "terrify",
    "test",
    "thank",
    "think",
    "thrive",
    "throw",
    "thrust",
    "thump",
    "tie",
    "tire",
    "toss",
    "trample",
    "transfer",
    "transform",
    "translate",
    "trap",
    "travel",
    "tread",
    "treasure",
    "treat",
    "tree",
    "tremble",
    "triumph",
    "trust",
    "try",
    "turn",
    "type",
    "typeset",
    "understand",
    "undo",
    "uproot",
    "upset",
    "urge",
    "use",
    "utter",
    "value",
    "vanish",
    "vary",
    "verify",
    "vex",
    "vie",
    "view",
    "violate",
    "vomit",
    "wake",
    "wander",
    "want",
    "warn",
    "waste",
    "watch",
    "wax",
    "waylay",
    "wear",
    "weave",
    "wed",
    "weep",
    "weigh",
    "welcome",
    "wend",
    "wet",
    "whip",
    "whisper",
    "win",
    "wish",
    "withdraw",
    "work",
    "worry",
    "worship",
    "wring",
    "write",
    "yawn",
    "yield",
    "zoom"
}

directionDict = {
    "north": "n",
    "n": "n",
    "east": "e",
    "e": "e",
    "northeast": "ne",
    "ne": "ne",
    "south": "s",
    "s": "s",
    "west": "w",
    "w": "w",
    "northwest": "nw",
    "nw": "nw",
    "southeast": "se",
    "se": "se",
    "southwest": "sw",
    "sw": "sw", 
    "up": "u",
    "upstairs": "u",
    "u": "u",
    "down": "d",
    "downstairs": "d",
    "d": "d"
}

articlesList = ["the", "an", "a"]

pronounsList = ["that", "her", "it", "she", "he", "him", "his", "hers", "they", "them", "their",
                "you", "your", "yours", "me", "my", "mine", "myself", "yourself", "himself", "herself",
                "its", "itself", "we", "our", "ours", "ourselves", "yourselves", "theirs", "themselves",
                "this", "these", "those"]

conjunctionsList = ["and", "or", "nor", "but", "yet", "so", "whether", "neither", "either", "though", "although", "because", "while"] 

quantifiersList = ["all", "some", "few", "many", "several", "both", "every", "each", "first", "last", "next", "other", "same"]

# Two different kinds of prepositions...
# ...those recognized by the game
prepositionsListUnused = [
    "about", "above", "across", "after", "against", "along", "among", "around", "at",
    "before", "behind", "below", "beneath", "beside", "between", "by",
    "for", "from", "near", "of", "off", "onto", # "on",
    "through", "to", "toward", "towards", "under", "upon", "with", "within",
    "out"
] # removed 'down' - otherwise direction 'down' will be removed as preposition
# ...and those that are not
prepositionsListUsed = [
    "in", "inside", "into", "on"
] # removed 'down' - otherwise direction 'down' will be removed as preposition

hardcodedPhrases = {
    "go to bed": Action("sleep"),
    "look in mirror": Action("look", None, "mirror"),
    "look in the mirror": Action("look", None, "mirror"),
    "look out window": Action("look", None, "outside"),
    "look out the window": Action("look", None, "outside"),
    "see out window": Action("look", None, "outside"),
    "see out the window": Action("look", None, "outside"),
    "look out windows": Action("look", None, "outside"),
    "look out the windows": Action("look", None, "outside"),
    "see out the windows": Action("look", None, "outside"),
    "see out windows": Action("look", None, "outside"),
    "look through window": Action("look", None, "outside"),
    "look through the window": Action("look", None, "outside"),
    "look through the windows": Action("look", None, "outside"),
    "look through windows": Action("look", None, "outside"),
    "turn on flashlight": Action("activate", None, "flashlight"),
    "turn on the flashlight": Action("activate", None, "flashlight"),
    "light a match": Action("activate", None, "matchbook"),
    "light match": Action("activate", None, "matchbook"),
    "strike a match": Action("activate", None, "matchbook"),
    "strike match": Action("activate", None, "matchbook"),
    "ignite match": Action("activate", None, "matchbook"),
    "ignite a match": Action("activate", None, "matchbook"),
    "start fire": Action("activate", None, "matchbook"),
    "start a fire": Action("activate", None, "matchbook"),
    "pick nose": "That's gross."
}
