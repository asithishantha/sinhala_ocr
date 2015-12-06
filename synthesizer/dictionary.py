__author__ = 'Chin'

graphemes = {
         "\xe0\xb6\x85" : "a",      "\xe0\xb6\x86" : "aa",      "\xe0\xb6\x87" : "ae",      "\xe0\xb6\x88" : "aee",     "\xe0\xb6\x89" : "i",
         "\xe0\xb6\x8a" : "ii",     "\xe0\xb6\x8b" : "u",       "\xe0\xb6\x8c" : "uu",      "\xe0\xb6\x8d" : "iru",     "\xe0\xb6\x8e" : "iruu",
         "\xe0\xb6\x8f" : "ilu",    "\xe0\xb6\x90" : "iluu",    "\xe0\xb6\x91" : "e",       "\xe0\xb6\x92" : "ee",      "\xe0\xb6\x93" : "ai",
         "\xe0\xb6\x94" : "o",      "\xe0\xb6\x95" : "oo",      "\xe0\xb6\x96" : "au",

         "\xe0\xb6\x9a" : "ka",     "\xe0\xb6\x9b" : "ka",      "\xe0\xb6\x9c" : "ga",      "\xe0\xb6\x9d" : "ga",      "\xe0\xb6\x9e" : "M_Ang",
         "\xe0\xb6\x9f" : "nnga",   "\xe0\xb6\xa0" : "cha",     "\xe0\xb6\xa1" : "cha",     "\xe0\xb6\xa2" : "ja",      "\xe0\xb6\xa3" : "ja",
         "\xe0\xb6\xa4" : "nnya",   "\xe0\xb6\xa5" : "nnYa",    "\xe0\xb6\xa6" : "nnja",    "\xe0\xb6\xa7" : "ta",      "\xe0\xb6\xa8" : "ta",
         "\xe0\xb6\xa9" : "da",     "\xe0\xb6\xaa" : "da",      "\xe0\xb6\xab" : "na",      "\xe0\xb6\xac" : "nnda",    "\xe0\xb6\xad" : "tha",
         "\xe0\xb6\xae" : "tha",    "\xe0\xb6\xaf" : "dha",     "\xe0\xb6\xb0" : "dha",     "\xe0\xb6\xb1" : "na",      "\xe0\xb6\xb3" : "nndha",
         "\xe0\xb6\xb4" : "pa",     "\xe0\xb6\xb5" : "pa",      "\xe0\xb6\xb6" : "ba",      "\xe0\xb6\xb7" : "ba",      "\xe0\xb6\xb8" : "ma",
         "\xe0\xb6\xb9" : "mmba",   "\xe0\xb6\xba" : "ya",      "\xe0\xb6\xbb" : "ra",      "\xe0\xb6\xbd" : "la",      "\xe0\xb7\x80" : "wa",
         "\xe0\xb7\x81" : "sha",    "\xe0\xb7\x82" : "sha",     "\xe0\xb7\x83" : "sa",      "\xe0\xb7\x84" : "ha",      "\xe0\xb7\x85" : "la",
         "\xe0\xb7\x86" : "fa",     "\xe2\x80\x8d" : " ",

         "\xe0\xb7\x8a" : "M_Al",   "\xe0\xb7\x8f" : "M_Aa",    "\xe0\xb7\x90" : "M_Ae",    "\xe0\xb7\x91" : "M_Aee",   "\xe0\xb7\x92" : "M_I",
         "\xe0\xb7\x93" : "M_Ii",   "\xe0\xb7\x94" : "M_U",     "\xe0\xb7\x96" : "M_Uu",    "\xe0\xb7\x98" : "M_Iru",   "\xe0\xb7\x99" : "M_E",
         "\xe0\xb7\x9a" : "M_Ee",   "\xe0\xb7\x9b" : "M_Ai",    "\xe0\xb7\x9c" : "M_O",     "\xe0\xb7\x9d" : "M_Oo",    "\xe0\xb7\x9e" : "M_Au",
         "\xe0\xb7\x9f" : "M_gk",   "\xe0\xb7\xb2" : "M_Iruu",  "\xe0\xb7\xb3" : "M_Gk",    "\xe0\xb6\x82" : "M_Ang",  "\xe0\xb6\x83" : "M_Angg"
         }

phonemes = {"a" : "a",      "aa" : "aa",    "ae" : "ae",        "aee" : "aee",      "i" : "i",          "ii" : "ii",    "u" : "u",
            "uu" : "uu",     "iru" : "iru",  "iruu" : "iruu",    "ilu" : "ilu",      "iluu" : "iluu",    "e" : "e",      "ee" : "ee",
            "ai" : "ai",    "o" : "o",      "oo" : "oo",        "au" : "au",        "aM_Ang" : "ang",     "aM_Angg" : "a", "M_Ang" : "ng",

            "a_" : "a",      "aa_" : "aa",    "ae_" : "ae",        "aee_" : "aee",      "i_" : "i",          "ii_" : "ii",    "u_" : "u",
            "u_" : "uu",     "iru_" : "iru",  "iruu_" : "iruu",    "ilu_" : "ilu",      "iluu_" : "iluu",    "e_" : "e",      "ee_" : "ee",
            "ai_" : "ai",    "o_" : "o",      "oo_" : "oo",        "au_" : "au",        "aM_Ang" : "ang",     "aM_Angg" : "a",

            "ka" : "ka",        "ka_" : "ka_",      "kaM_Al" : "k",     "kaM_Aa" : "kaa",   "kaM_Ae" : "kae",   "kaM_Aee" : "kaee",
            "kaM_I" : "ki",     "kaM_Ii" : "kii",   "kaM_U" : "ku",     "kaM_Uu" : "kuu",   "kaM_Iru" : "kru",  "kaM_Iruu" : "kruu",
            "kaM_E" : "ke",     "kaM_Ee" : "kee",   "kaM_Ai" : "kai",   "kaM_O" : "ko",     "kaM_Oo" : "koo",   "kaM_Au" : "kau",
            "kaM_gk" : "ka",    "kaM_Gk" : "ka",    "kaM_Ang" : "kang", "kaM_Angg" : "ka",

            "ga" : "ga",        "ga_" : "ga_",      "gaM_Al" : "g",     "gaM_Aa" : "gaa",   "gaM_Ae" : "gae",   "gaM_Aee" : "gaee",
            "gaM_I" : "gi",     "gaM_Ii" : "gii",   "gaM_U" : "gu",     "gaM_Uu" : "guu",   "gaM_Iru" : "gru",  "gaM_Iruu" : "gruu",
            "gaM_E" : "ge",     "gaM_Ee" : "gee",   "gaM_Ai" : "gai",   "gaM_O" : "go",     "gaM_Oo" : "goo",   "gaM_Au" : "gau",
            "gaM_gk" : "ga",     "gaM_Gk" : "ga",     "gaM_Ang" : "gang", "gaM_Angg" : "ga",

            "cha" : "cha",        "cha_" : "cha_",      "chaM_Al" : "ch",     "chaM_Aa" : "chaa",   "chaM_Ae" : "chae",   "chaM_Aee" : "chaee",
            "chaM_I" : "chi",     "chaM_Ii" : "chii",   "chaM_U" : "chu",     "chaM_Uu" : "chuu",   "chaM_Iru" : "chru",  "chaM_Iruu" : "chruu",
            "chaM_E" : "che",     "chaM_Ee" : "chee",   "chaM_Ai" : "chai",   "chaM_O" : "cho",     "chaM_Oo" : "choo",   "chaM_Au" : "chau",
            "chaM_gk" : "cha",     "chaM_Gk" : "cha",     "chaM_Ang" : "chang", "chaM_Angg" : "cha",

            "ja" : "ja",        "ja_" : "ja_",      "jaM_Al" : "j",     "jaM_Aa" : "jaa",   "jaM_Ae" : "jae",   "jaM_Aee" : "jaee",
            "jaM_I" : "ji",     "jaM_Ii" : "jii",   "jaM_U" : "ju",     "jaM_Uu" : "juu",   "jaM_Iru" : "jru",  "jaM_Iruu" : "jruu",
            "jaM_E" : "je",     "jaM_Ee" : "jee",   "jaM_Ai" : "jai",   "jaM_O" : "jo",     "jaM_Oo" : "joo",   "jaM_Au" : "jau",
            "jaM_gk" : "ja",     "jaM_Gk" : "ja",     "jaM_Ang" : "jang", "jaM_Angg" : "ja",

            "ta" : "ta",        "ta_" : "ta_",      "taM_Al" : "t",     "taM_Aa" : "taa",   "taM_Ae" : "tae",   "taM_Aee" : "taee",
            "taM_I" : "ti",     "taM_Ii" : "tii",   "taM_U" : "tu",     "taM_Uu" : "tuu",   "taM_Iru" : "tru",  "taM_Iruu" : "truu",
            "taM_E" : "te",     "taM_Ee" : "tee",   "taM_Ai" : "tai",   "taM_O" : "to",     "taM_Oo" : "too",   "taM_Au" : "tau",
            "taM_gk" : "ta",     "taM_Gk" : "ta",     "taM_Ang" : "tang", "taM_Angg" : "ta",

            "da" : "da",        "da_" : "da_",      "daM_Al" : "d",     "daM_Aa" : "daa",   "daM_Ae" : "dae",   "daM_Aee" : "daee",
            "daM_I" : "di",     "daM_Ii" : "dii",   "daM_U" : "du",     "daM_Uu" : "duu",   "daM_Iru" : "dru",  "daM_Iruu" : "druu",
            "daM_E" : "de",     "daM_Ee" : "dee",   "daM_Ai" : "dai",   "daM_O" : "do",     "daM_Oo" : "doo",   "daM_Au" : "dau",
            "daM_gk" : "da",     "daM_Gk" : "da",     "daM_Ang" : "dang", "daM_Angg" : "da",

            "na" : "na",        "na_" : "na_",      "naM_Al" : "n",     "naM_Aa" : "naa",   "naM_Ae" : "nae",   "naM_Aee" : "naee",
            "naM_I" : "ni",     "naM_Ii" : "nii",   "naM_U" : "nu",     "naM_Uu" : "nuu",   "naM_Iru" : "nru",  "naM_Iruu" : "nruu",
            "naM_E" : "ne",     "naM_Ee" : "nee",   "naM_Ai" : "nai",   "naM_O" : "no",     "naM_Oo" : "noo",   "naM_Au" : "nau",
            "naM_gk" : "na",     "naM_Gk" : "na",     "naM_Ang" : "nang", "naM_Angg" : "na",

            "tha" : "tha",        "tha_" : "tha_",      "thaM_Al" : "th",     "thaM_Aa" : "thaa",   "thaM_Ae" : "thae",   "thaM_Aee" : "thaee",
            "thaM_I" : "thi",     "thaM_Ii" : "thii",   "thaM_U" : "thu",     "thaM_Uu" : "thuu",   "thaM_Iru" : "thru",  "thaM_Iruu" : "thruu",
            "thaM_E" : "the",     "thaM_Ee" : "thee",   "thaM_Ai" : "thai",   "thaM_O" : "tho",     "thaM_Oo" : "thoo",   "thaM_Au" : "thau",
            "thaM_gk" : "tha",     "thaM_Gk" : "tha",     "thaM_Ang" : "thang", "thaM_Angg" : "tha",

            "dha" : "dha",        "dha_" : "dha_",      "dhaM_Al" : "dh",     "dhaM_Aa" : "dhaa",   "dhaM_Ae" : "dhae",   "dhaM_Aee" : "dhaee",
            "dhaM_I" : "dhi",     "dhaM_Ii" : "dhii",   "dhaM_U" : "dhu",     "dhaM_Uu" : "dhuu",   "dhaM_Iru" : "dhru",  "dhaM_Iruu" : "dhruu",
            "dhaM_E" : "dhe",     "dhaM_Ee" : "dhee",   "dhaM_Ai" : "dhai",   "dhaM_O" : "dho",     "dhaM_Oo" : "dhoo",   "dhaM_Au" : "dhau",
            "dhaM_gk" : "dha",     "dhaM_Gk" : "dha",     "dhaM_Ang" : "dhang", "dhaM_Angg" : "dha",

            "pa" : "pa",        "pa_" : "pa_",      "paM_Al" : "p",     "paM_Aa" : "paa",   "paM_Ae" : "pae",   "paM_Aee" : "paee",
            "paM_I" : "pi",     "paM_Ii" : "pii",   "paM_U" : "pu",     "paM_Uu" : "puu",   "paM_Iru" : "pru",  "paM_Iruu" : "pruu",
            "paM_E" : "pe",     "paM_Ee" : "pee",   "paM_Ai" : "pai",   "paM_O" : "po",     "paM_Oo" : "poo",   "paM_Au" : "pau",
            "paM_gk" : "pa",     "paM_Gk" : "pa",     "paM_Ang" : "pang", "paM_Angg" : "pa",

            "ba" : "ba",        "ba_" : "ba_",      "baM_Al" : "b",     "baM_Aa" : "baa",   "baM_Ae" : "bae",   "baM_Aee" : "baee",
            "baM_I" : "bi",     "baM_Ii" : "bii",   "baM_U" : "bu",     "baM_Uu" : "buu",   "baM_Iru" : "bru",  "baM_Iruu" : "bruu",
            "baM_E" : "be",     "baM_Ee" : "bee",   "baM_Ai" : "bai",   "baM_O" : "bo",     "baM_Oo" : "boo",   "baM_Au" : "bau",
            "baM_gk" : "ba",     "baM_Gk" : "ba",     "baM_Ang" : "bang", "baM_Angg" : "ba",

            "ma" : "ma",        "ma_" : "ma_",      "maM_Al" : "m",     "maM_Aa" : "maa",   "maM_Ae" : "mae",   "maM_Aee" : "maee",
            "maM_I" : "mi",     "maM_Ii" : "mii",   "maM_U" : "mu",     "maM_Uu" : "muu",   "maM_Iru" : "mru",  "maM_Iruu" : "mruu",
            "maM_E" : "me",     "maM_Ee" : "mee",   "maM_Ai" : "mai",   "maM_O" : "mo",     "maM_Oo" : "moo",   "maM_Au" : "mau",
            "maM_gk" : "ma",     "maM_Gk" : "ma",     "maM_Ang" : "mang", "maM_Angg" : "ma",

            "ya" : "ya",        "ya_" : "ya_",      "yaM_Al" : "y",     "yaM_Aa" : "yaa",   "yaM_Ae" : "yae",   "yaM_Aee" : "yaee",
            "yaM_I" : "yi",     "yaM_Ii" : "yii",   "yaM_U" : "yu",     "yaM_Uu" : "yuu",   "yaM_Iru" : "yru",  "yaM_Iruu" : "yruu",
            "yaM_E" : "ye",     "yaM_Ee" : "yee",   "yaM_Ai" : "yai",   "yaM_O" : "yo",     "yaM_Oo" : "yoo",   "yaM_Au" : "yau",
            "yaM_gk" : "ya",     "yaM_Gk" : "ya",     "yaM_Ang" : "yang", "yaM_Angg" : "ya",

            "ra" : "ra",        "ra_" : "ra_",      "raM_Al" : "r",     "raM_Aa" : "raa",   "raM_Ae" : "rae",   "raM_Aee" : "raee",
            "raM_I" : "ri",     "raM_Ii" : "rii",   "raM_U" : "ru",     "raM_Uu" : "ruu",   "raM_Iru" : "rru",  "raM_Iruu" : "rruu",
            "raM_E" : "re",     "raM_Ee" : "ree",   "raM_Ai" : "rai",   "raM_O" : "ro",     "raM_Oo" : "roo",   "raM_Au" : "rau",
            "raM_gk" : "ra",     "raM_Gk" : "ra",     "raM_Ang" : "rang", "raM_Angg" : "ra",

            "la" : "la",        "la_" : "la_",      "laM_Al" : "l",     "laM_Aa" : "laa",   "laM_Ae" : "lae",   "laM_Aee" : "laee",
            "laM_I" : "li",     "laM_Ii" : "lii",   "laM_U" : "lu",     "laM_Uu" : "luu",   "laM_Iru" : "lru",  "laM_Iruu" : "lruu",
            "laM_E" : "le",     "laM_Ee" : "lee",   "laM_Ai" : "lai",   "laM_O" : "lo",     "laM_Oo" : "loo",   "laM_Au" : "lau",
            "laM_gk" : "la",     "laM_Gk" : "la",     "laM_Ang" : "lang", "laM_Angg" : "la",

            "wa" : "wa",        "wa_" : "wa_",      "waM_Al" : "w",     "waM_Aa" : "waa",   "waM_Ae" : "wae",   "waM_Aee" : "waee",
            "waM_I" : "wi",     "waM_Ii" : "wii",   "waM_U" : "wu",     "waM_Uu" : "wuu",   "waM_Iru" : "wru",  "waM_Iruu" : "wruu",
            "waM_E" : "we",     "waM_Ee" : "wee",   "waM_Ai" : "wai",   "waM_O" : "wo",     "waM_Oo" : "woo",   "waM_Au" : "wau",
            "waM_gk" : "wa",     "waM_Gk" : "wa",     "waM_Ang" : "wang", "waM_Angg" : "wa",

            "sha" : "sha",        "sha_" : "sha_",      "shaM_Al" : "sh",     "shaM_Aa" : "shaa",   "shaM_Ae" : "shae",   "shaM_Aee" : "shaee",
            "shaM_I" : "shi",     "shaM_Ii" : "shii",   "shaM_U" : "shu",     "shaM_Uu" : "shuu",   "shaM_Iru" : "shru",  "shaM_Iruu" : "shruu",
            "shaM_E" : "she",     "shaM_Ee" : "shee",   "shaM_Ai" : "shai",   "shaM_O" : "sho",     "shaM_Oo" : "shoo",   "shaM_Au" : "shau",
            "shaM_gk" : "sha",     "shaM_Gk" : "sha",     "shaM_Ang" : "shang", "shaM_Angg" : "sha",

            "sa" : "sa",        "sa_" : "sa_",      "saM_Al" : "s",     "saM_Aa" : "saa",   "saM_Ae" : "sae",   "saM_Aee" : "saee",
            "saM_I" : "si",     "saM_Ii" : "sii",   "saM_U" : "su",     "saM_Uu" : "suu",   "saM_Iru" : "sru",  "saM_Iruu" : "sruu",
            "saM_E" : "se",     "saM_Ee" : "see",   "saM_Ai" : "sai",   "saM_O" : "so",     "saM_Oo" : "soo",   "saM_Au" : "sau",
            "saM_gk" : "sa",     "saM_Gk" : "sa",     "saM_Ang" : "sang", "saM_Angg" : "sa",

            "ha" : "ha",        "ha_" : "ha_",      "haM_Al" : "h",     "haM_Aa" : "haa",   "haM_Ae" : "hae",   "haM_Aee" : "haee",
            "haM_I" : "hi",     "haM_Ii" : "hii",   "haM_U" : "hu",     "haM_Uu" : "huu",   "haM_Iru" : "hru",  "haM_Iruu" : "hruu",
            "haM_E" : "he",     "haM_Ee" : "hee",   "haM_Ai" : "hai",   "haM_O" : "ho",     "haM_Oo" : "hoo",   "haM_Au" : "hau",
            "haM_gk" : "ha",     "haM_Gk" : "ha",     "haM_Ang" : "hang", "haM_Angg" : "ha",

            "fa" : "fa",        "fa_" : "fa_",      "faM_Al" : "f",     "faM_Aa" : "faa",   "faM_Ae" : "fae",   "faM_Aee" : "faee",
            "faM_I" : "fi",     "faM_Ii" : "fii",   "faM_U" : "fu",     "faM_Uu" : "fuu",   "faM_Iru" : "fru",  "faM_Iruu" : "fruu",
            "faM_E" : "fe",     "faM_Ee" : "fee",   "faM_Ai" : "fai",   "faM_O" : "fo",     "faM_Oo" : "foo",   "faM_Au" : "fau",
            "faM_gk" : "fa",     "faM_Gk" : "fa",     "faM_Ang" : "fang", "faM_Angg" : "fa",

            "nnga" : "nnga",      "nnga_" : "nnga",    "nngaM_Al" : "g",     "nngaM_Aa" : "gaa",   "nngaM_Ae" : "gae",   "nngaM_Aee" : "gaee",
            "nngaM_I" : "gi",     "nngaM_Ii" : "gii",   "nngaM_U" : "gu",     "nngaM_Uu" : "guu",   "nngaM_Iru" : "gru",  "nngaM_Iruu" : "gruu",
            "nngaM_E" : "ge",     "nngaM_Ee" : "gee",   "nngaM_Ai" : "gai",   "nngaM_O" : "go",     "nngaM_Oo" : "goo",   "nngaM_Au" : "gau",
            "nngaM_gk" : "ga",     "nngaM_Gk" : "ga",     "nngaM_Ang" : "gang", "nngaM_Angg" : "nnga",

            "nnja" : "nnja",      "nnja_" : "nnja",    "nnjaM_Al" : "j",     "nnjaM_Aa" : "jaa",   "nnjaM_Ae" : "jae",   "nnjaM_Aee" : "jaee",
            "nnjaM_I" : "ji",     "nnjaM_Ii" : "jii",   "nnjaM_U" : "ju",     "nnjaM_Uu" : "juu",   "nnjaM_Iru" : "jru",  "nnjaM_Iruu" : "jruu",
            "nnjaM_E" : "je",     "nnjaM_Ee" : "jee",   "nnjaM_Ai" : "jai",   "nnjaM_O" : "jo",     "nnjaM_Oo" : "joo",   "nnjaM_Au" : "jau",
            "nnjaM_gk" : "ja",     "nnjaM_Gk" : "ja",     "nnjaM_Ang" : "jang", "nnjaM_Angg" : "nnja",

            "nnda" : "nnda",      "nnda_" : "nnda",    "nndaM_Al" : "d",     "nndaM_Aa" : "daa",   "nndaM_Ae" : "dae",   "nndaM_Aee" : "daee",
            "nndaM_I" : "di",     "nndaM_Ii" : "dii",   "nndaM_U" : "du",     "nndaM_Uu" : "duu",   "nndaM_Iru" : "dru",  "nndaM_Iruu" : "druu",
            "nndaM_E" : "de",     "nndaM_Ee" : "dee",   "nndaM_Ai" : "dai",   "nndaM_O" : "do",     "nndaM_Oo" : "doo",   "nndaM_Au" : "dau",
            "nndaM_gk" : "da",     "nndaM_Gk" : "da",     "nndaM_Ang" : "dang", "nndaM_Angg" : "nnda",

            "nndha" : "nndha",      "nndha_" : "nndha",    "nndhaM_Al" : "dh",     "nndhaM_Aa" : "dhaa",   "nndhaM_Ae" : "dhae",   "nndhaM_Aee" : "dhaee",
            "nndhaM_I" : "dhi",     "nndhaM_Ii" : "dhii",   "nndhaM_U" : "dhu",     "nndhaM_Uu" : "dhuu",   "nndhaM_Iru" : "dhru",  "nndhaM_Iruu" : "dhruu",
            "nndhaM_E" : "dhe",     "nndhaM_Ee" : "dhee",   "nndhaM_Ai" : "dhai",   "nndhaM_O" : "dho",     "nndhaM_Oo" : "dhoo",   "nndhaM_Au" : "dhau",
            "nndhaM_gk" : "dha",     "nndhaM_Gk" : "dha",     "nndhaM_Ang" : "dhang", "nndhaM_Angg" : "nndha",

            "mmba" : "mmba",      "mmba_" : "mmba",     "mmbaM_Al" : "b",     "mmbaM_Aa" : "baa",   "mmbaM_Ae" : "bae",   "mmbaM_Aee" : "baee",
            "mmbaM_I" : "bi",     "mmbaM_Ii" : "bii",   "mmbaM_U" : "bu",     "mmbaM_Uu" : "buu",   "mmbaM_Iru" : "bru",  "mmbaM_Iruu" : "bruu",
            "mmbaM_E" : "be",     "mmbaM_Ee" : "bee",   "mmbaM_Ai" : "bai",   "mmbaM_O" : "bo",     "mmbaM_Oo" : "boo",   "mmbaM_Au" : "bau",
            "mmbaM_gk" : "ba",     "mmbaM_Gk" : "ba",     "mmbaM_Ang" : "bang", "mmbaM_Angg" : "mmba",

            "nnya" : "nnya",      "nnya_" : "nnya",     "nnyaM_Al" : "y",     "nnyaM_Aa" : "yaa",   "nnyaM_Ae" : "yae",   "nnyaM_Aee" : "yaee",
            "nnyaM_I" : "yi",     "nnyaM_Ii" : "yii",   "nnyaM_U" : "yu",     "nnyaM_Uu" : "yuu",   "nnyaM_Iru" : "yru",  "nnyaM_Iruu" : "yruu",
            "nnyaM_E" : "ye",     "nnyaM_Ee" : "yee",   "nnyaM_Ai" : "yai",   "nnyaM_O" : "yo",     "nnyaM_Oo" : "yoo",   "nnyaM_Au" : "yau",
            "nnyaM_gk" : "ya",     "nnyaM_Gk" : "ya",     "nnyaM_Ang" : "yang", "nnyaM_Angg" : "nnya",
            }

sounds = {"a" : "sounds/characters/00 - vowels/01 - a.wav",         "aa" : "sounds/characters/00 - vowels/02 - aa.wav",
          "ae" : "sounds/characters/00 - vowels/03 - ae.wav",       "aee" : "sounds/characters/00 - vowels/04 - aee.wav",
          "i" : "sounds/characters/00 - vowels/05 - i.wav",         "ii" : "sounds/characters/00 - vowels/06 - ii.wav",
          "u" : "sounds/characters/00 - vowels/07 - u.wav",         "uu" : "sounds/characters/00 - vowels/08 - uu.wav",
          "e" : "sounds/characters/00 - vowels/09 - e.wav",         "ee" : "sounds/characters/00 - vowels/10 - ee.wav",
          "ai" : "sounds/characters/00 - vowels/11 - ai.wav",       "o" : "sounds/characters/00 - vowels/12 - o.wav",
          "oo" : "sounds/characters/00 - vowels/13 - oo.wav",       "au" : "sounds/characters/00 - vowels/14 - au.wav",
          "ang" : "sounds/characters/00 - vowels/15 - ang.wav",     "iru" : "sounds/characters/00 - vowels/16 - hri.wav",
          "iruu" : "sounds/characters/00 - vowels/17 - hrii.wav",

          "k" : "sounds/characters/01 - k/00 - k.wav",          "ka" : "sounds/characters/01 - k/01 - ka.wav",
          "ka_" : "sounds/characters/01 - k/01 - ka2.wav",      "kaa" : "sounds/characters/01 - k/02 - kaa.wav",
          "kae" : "sounds/characters/01 - k/03 - kae.wav",      "kaee" : "sounds/characters/01 - k/04 - kaee.wav",
          "ki" : "sounds/characters/01 - k/05 - ki.wav",        "kii" : "sounds/characters/01 - k/06 - kii.wav",
          "ku" : "sounds/characters/01 - k/07 - ku.wav",        "kuu" : "sounds/characters/01 - k/08 - kuu.wav",
          "ke" : "sounds/characters/01 - k/09 - ke.wav",        "kee" : "sounds/characters/01 - k/10 - kee.wav",
          "kai" : "sounds/characters/01 - k/11 - kai.wav",      "ko" : "sounds/characters/01 - k/12 - ko.wav",
          "koo" : "sounds/characters/01 - k/13 - koo.wav",      "kau" : "sounds/characters/01 - k/14 - kau.wav",
          "kang" : "sounds/characters/01 - k/15 - kang.wav",    "kru" : "sounds/characters/01 - k/16 - kru.wav",
          "kruu" : "sounds/characters/01 - k/17 - kruu.wav",

          "g" : "sounds/characters/02 - g/00 - g.wav",          "ga" : "sounds/characters/02 - g/01 - ga.wav",
          "ga_" : "sounds/characters/02 - g/01 - ga2.wav",      "gaa" : "sounds/characters/02 - g/02 - gaa.wav",
          "gae" : "sounds/characters/02 - g/03 - gae.wav",      "gaee" : "sounds/characters/02 - g/04 - gaee.wav",
          "gi" : "sounds/characters/02 - g/05 - gi.wav",        "gii" : "sounds/characters/02 - g/06 - gii.wav",
          "gu" : "sounds/characters/02 - g/07 - gu.wav",        "guu" : "sounds/characters/02 - g/08 - guu.wav",
          "ge" : "sounds/characters/02 - g/09 - ge.wav",        "gee" : "sounds/characters/02 - g/10 - gee.wav",
          "gai" : "sounds/characters/02 - g/11 - gai.wav",      "go" : "sounds/characters/02 - g/12 - go.wav",
          "goo" : "sounds/characters/02 - g/13 - goo.wav",      "gau" : "sounds/characters/02 - g/14 - gau.wav",
          "gang" : "sounds/characters/02 - g/15 - gang.wav",    "gru" : "sounds/characters/02 - g/16 - gru.wav",
          "gruu" : "sounds/characters/02 - g/17 - gruu.wav",

          "ch" : "sounds/characters/03 - ch/00 - ch.wav",          "cha" : "sounds/characters/03 - ch/01 - cha.wav",
          "cha_" : "sounds/characters/03 - ch/01 - cha2.wav",      "chaa" : "sounds/characters/03 - ch/02 - chaa.wav",
          "chae" : "sounds/characters/03 - ch/03 - chae.wav",      "chaee" : "sounds/characters/03 - ch/04 - chaee.wav",
          "chi" : "sounds/characters/03 - ch/05 - chi.wav",        "chii" : "sounds/characters/03 - ch/06 - chii.wav",
          "chu" : "sounds/characters/03 - ch/07 - chu.wav",        "chuu" : "sounds/characters/03 - ch/08 - chuu.wav",
          "che" : "sounds/characters/03 - ch/09 - che.wav",        "chee" : "sounds/characters/03 - ch/10 - chee.wav",
          "chai" : "sounds/characters/03 - ch/11 - chai.wav",      "cho" : "sounds/characters/03 - ch/12 - cho.wav",
          "choo" : "sounds/characters/03 - ch/13 - choo.wav",      "chau" : "sounds/characters/03 - ch/14 - chau.wav",
          "chang" : "sounds/characters/03 - ch/15 - chang.wav",    "chru" : "sounds/characters/03 - ch/16 - chru.wav",
          "chruu" : "sounds/characters/03 - ch/17 - chruu.wav",

          "j" : "sounds/characters/04 - j/00 - j.wav",          "ja" : "sounds/characters/04 - j/01 - ja.wav",
          "ja_" : "sounds/characters/04 - j/01 - ja2.wav",      "jaa" : "sounds/characters/04 - j/02 - jaa.wav",
          "jae" : "sounds/characters/04 - j/03 - jae.wav",      "jaee" : "sounds/characters/04 - j/04 - jaee.wav",
          "ji" : "sounds/characters/04 - j/05 - ji.wav",        "jii" : "sounds/characters/04 - j/06 - jii.wav",
          "ju" : "sounds/characters/04 - j/07 - ju.wav",        "juu" : "sounds/characters/04 - j/08 - juu.wav",
          "je" : "sounds/characters/04 - j/09 - je.wav",        "jee" : "sounds/characters/04 - j/10 - jee.wav",
          "jai" : "sounds/characters/04 - j/11 - jai.wav",      "jo" : "sounds/characters/04 - j/12 - jo.wav",
          "joo" : "sounds/characters/04 - j/13 - joo.wav",      "jau" : "sounds/characters/04 - j/14 - jau.wav",
          "jang" : "sounds/characters/04 - j/15 - jang.wav",    "jru" : "sounds/characters/04 - j/16 - jru.wav",
          "jruu" : "sounds/characters/04 - j/17 - jruu.wav",

          "t" : "sounds/characters/05 - t/00 - t.wav",          "ta" : "sounds/characters/05 - t/01 - ta.wav",
          "ta_" : "sounds/characters/05 - t/01 - ta2.wav",      "taa" : "sounds/characters/05 - t/02 - taa.wav",
          "tae" : "sounds/characters/05 - t/03 - tae.wav",      "taee" : "sounds/characters/05 - t/04 - taee.wav",
          "ti" : "sounds/characters/05 - t/05 - ti.wav",        "tii" : "sounds/characters/05 - t/06 - tii.wav",
          "tu" : "sounds/characters/05 - t/07 - tu.wav",        "tuu" : "sounds/characters/05 - t/08 - tuu.wav",
          "te" : "sounds/characters/05 - t/09 - te.wav",        "tee" : "sounds/characters/05 - t/10 - tee.wav",
          "tai" : "sounds/characters/05 - t/11 - tai.wav",      "to" : "sounds/characters/05 - t/12 - to.wav",
          "too" : "sounds/characters/05 - t/13 - too.wav",      "tau" : "sounds/characters/05 - t/14 - tau.wav",
          "tang" : "sounds/characters/05 - t/15 - tang.wav",    "tru" : "sounds/characters/05 - t/16 - tru.wav",
          "truu" : "sounds/characters/05 - t/17 - truu.wav",

          "d" : "sounds/characters/06 - d/00 - d.wav",          "da" : "sounds/characters/06 - d/01 - da.wav",
          "da_" : "sounds/characters/06 - d/01 - da2.wav",      "daa" : "sounds/characters/06 - d/02 - daa.wav",
          "dae" : "sounds/characters/06 - d/03 - dae.wav",      "daee" : "sounds/characters/06 - d/04 - daee.wav",
          "di" : "sounds/characters/06 - d/05 - di.wav",        "dii" : "sounds/characters/06 - d/06 - dii.wav",
          "du" : "sounds/characters/06 - d/07 - du.wav",        "duu" : "sounds/characters/06 - d/08 - duu.wav",
          "de" : "sounds/characters/06 - d/09 - de.wav",        "dee" : "sounds/characters/06 - d/10 - dee.wav",
          "dai" : "sounds/characters/06 - d/11 - dai.wav",      "do" : "sounds/characters/06 - d/12 - do.wav",
          "doo" : "sounds/characters/06 - d/13 - doo.wav",      "dau" : "sounds/characters/06 - d/14 - dau.wav",
          "dang" : "sounds/characters/06 - d/15 - dang.wav",    "dru" : "sounds/characters/06 - d/16 - dru.wav",
          "druu" : "sounds/characters/06 - d/17 - druu.wav",

          "n" : "sounds/characters/07 - n/00 - n.wav",          "na" : "sounds/characters/07 - n/01 - na.wav",
          "na_" : "sounds/characters/07 - n/01 - na2.wav",      "naa" : "sounds/characters/07 - n/02 - naa.wav",
          "nae" : "sounds/characters/07 - n/03 - nae.wav",      "naee" : "sounds/characters/07 - n/04 - naee.wav",
          "ni" : "sounds/characters/07 - n/05 - ni.wav",        "nii" : "sounds/characters/07 - n/06 - nii.wav",
          "nu" : "sounds/characters/07 - n/07 - nu.wav",        "nuu" : "sounds/characters/07 - n/08 - nuu.wav",
          "ne" : "sounds/characters/07 - n/09 - ne.wav",        "nee" : "sounds/characters/07 - n/10 - nee.wav",
          "nai" : "sounds/characters/07 - n/11 - nai.wav",      "no" : "sounds/characters/07 - n/12 - no.wav",
          "noo" : "sounds/characters/07 - n/13 - noo.wav",      "nau" : "sounds/characters/07 - n/14 - nau.wav",
          "nang" : "sounds/characters/07 - n/15 - nang.wav",    "nru" : "sounds/characters/07 - n/16 - nru.wav",
          "nruu" : "sounds/characters/07 - n/17 - nruu.wav",

          "th" : "sounds/characters/08 - th/00 - th.wav",          "tha" : "sounds/characters/08 - th/01 - tha.wav",
          "tha_" : "sounds/characters/08 - th/01 - tha2.wav",      "thaa" : "sounds/characters/08 - th/02 - thaa.wav",
          "thae" : "sounds/characters/08 - th/03 - thae.wav",      "thaee" : "sounds/characters/08 - th/04 - thaee.wav",
          "thi" : "sounds/characters/08 - th/05 - thi.wav",        "thii" : "sounds/characters/08 - th/06 - thii.wav",
          "thu" : "sounds/characters/08 - th/07 - thu.wav",        "thuu" : "sounds/characters/08 - th/08 - thuu.wav",
          "the" : "sounds/characters/08 - th/09 - the.wav",        "thee" : "sounds/characters/08 - th/10 - thee.wav",
          "thai" : "sounds/characters/08 - th/11 - thai.wav",      "tho" : "sounds/characters/08 - th/12 - tho.wav",
          "thoo" : "sounds/characters/08 - th/13 - thoo.wav",      "thau" : "sounds/characters/08 - th/14 - thau.wav",
          "thang" : "sounds/characters/08 - th/15 - thang.wav",    "thru" : "sounds/characters/08 - th/16 - thru.wav",
          "thruu" : "sounds/characters/08 - th/17 - thruu.wav",

          "dh" : "sounds/characters/09 - dh/00 - dh.wav",          "dha" : "sounds/characters/09 - dh/01 - dha.wav",
          "dha_" : "sounds/characters/09 - dh/01 - dha2.wav",      "dhaa" : "sounds/characters/09 - dh/02 - dhaa.wav",
          "dhae" : "sounds/characters/09 - dh/03 - dhae.wav",      "dhaee" : "sounds/characters/09 - dh/04 - dhaee.wav",
          "dhi" : "sounds/characters/09 - dh/05 - dhi.wav",        "dhii" : "sounds/characters/09 - dh/06 - dhii.wav",
          "dhu" : "sounds/characters/09 - dh/07 - dhu.wav",        "dhuu" : "sounds/characters/09 - dh/08 - dhuu.wav",
          "dhe" : "sounds/characters/09 - dh/09 - dhe.wav",        "dhee" : "sounds/characters/09 - dh/10 - dhee.wav",
          "dhai" : "sounds/characters/09 - dh/11 - dhai.wav",      "dho" : "sounds/characters/09 - dh/12 - dho.wav",
          "dhoo" : "sounds/characters/09 - dh/13 - dhoo.wav",      "dhau" : "sounds/characters/09 - dh/14 - dhau.wav",
          "dhang" : "sounds/characters/09 - dh/15 - dhang.wav",    "dhru" : "sounds/characters/09 - dh/16 - dhru.wav",
          "dhruu" : "sounds/characters/09 - dh/17 - dhruu.wav",

          "p" : "sounds/characters/10 - p/00 - p.wav",          "pa" : "sounds/characters/10 - p/01 - pa.wav",
          "pa_" : "sounds/characters/10 - p/01 - pa2.wav",      "paa" : "sounds/characters/10 - p/02 - paa.wav",
          "pae" : "sounds/characters/10 - p/03 - pae.wav",      "paee" : "sounds/characters/10 - p/04 - paee.wav",
          "pi" : "sounds/characters/10 - p/05 - pi.wav",        "pii" : "sounds/characters/10 - p/06 - pii.wav",
          "pu" : "sounds/characters/10 - p/07 - pu.wav",        "puu" : "sounds/characters/10 - p/08 - puu.wav",
          "pe" : "sounds/characters/10 - p/09 - pe.wav",        "pee" : "sounds/characters/10 - p/10 - pee.wav",
          "pai" : "sounds/characters/10 - p/11 - pai.wav",      "po" : "sounds/characters/10 - p/12 - po.wav",
          "poo" : "sounds/characters/10 - p/13 - poo.wav",      "pau" : "sounds/characters/10 - p/14 - pau.wav",
          "pang" : "sounds/characters/10 - p/15 - pang.wav",    "pru" : "sounds/characters/10 - p/16 - pru.wav",
          "pruu" : "sounds/characters/10 - p/17 - pruu.wav",

          "b" : "sounds/characters/11 - b/00 - b.wav",          "ba" : "sounds/characters/11 - b/01 - ba.wav",
          "ba_" : "sounds/characters/11 - b/01 - ba2.wav",      "baa" : "sounds/characters/11 - b/02 - baa.wav",
          "bae" : "sounds/characters/11 - b/03 - bae.wav",      "baee" : "sounds/characters/11 - b/04 - baee.wav",
          "bi" : "sounds/characters/11 - b/05 - bi.wav",        "bii" : "sounds/characters/11 - b/06 - bii.wav",
          "bu" : "sounds/characters/11 - b/07 - bu.wav",        "buu" : "sounds/characters/11 - b/08 - buu.wav",
          "be" : "sounds/characters/11 - b/09 - be.wav",        "bee" : "sounds/characters/11 - b/10 - bee.wav",
          "bai" : "sounds/characters/11 - b/11 - bai.wav",      "bo" : "sounds/characters/11 - b/12 - bo.wav",
          "boo" : "sounds/characters/11 - b/13 - boo.wav",      "bau" : "sounds/characters/11 - b/14 - bau.wav",
          "bang" : "sounds/characters/11 - b/15 - bang.wav",    "bru" : "sounds/characters/11 - b/16 - bru.wav",
          "bruu" : "sounds/characters/11 - b/17 - bruu.wav",

          "m" : "sounds/characters/12 - m/00 - m.wav",          "ma" : "sounds/characters/12 - m/01 - ma.wav",
          "ma_" : "sounds/characters/12 - m/01 - ma2.wav",      "maa" : "sounds/characters/12 - m/02 - maa.wav",
          "mae" : "sounds/characters/12 - m/03 - mae.wav",      "maee" : "sounds/characters/12 - m/04 - maee.wav",
          "mi" : "sounds/characters/12 - m/05 - mi.wav",        "mii" : "sounds/characters/12 - m/06 - mii.wav",
          "mu" : "sounds/characters/12 - m/07 - mu.wav",        "muu" : "sounds/characters/12 - m/08 - muu.wav",
          "me" : "sounds/characters/12 - m/09 - me.wav",        "mee" : "sounds/characters/12 - m/10 - mee.wav",
          "mai" : "sounds/characters/12 - m/11 - mai.wav",      "mo" : "sounds/characters/12 - m/12 - mo.wav",
          "moo" : "sounds/characters/12 - m/13 - moo.wav",      "mau" : "sounds/characters/12 - m/14 - mau.wav",
          "mang" : "sounds/characters/12 - m/15 - mang.wav",    "mru" : "sounds/characters/12 - m/16 - mru.wav",
          "mruu" : "sounds/characters/12 - m/17 - mruu.wav",

          "y" : "sounds/characters/13 - y/00 - y.wav",          "ya" : "sounds/characters/13 - y/01 - ya.wav",
          "ya_" : "sounds/characters/13 - y/01 - ya2.wav",      "yaa" : "sounds/characters/13 - y/02 - yaa.wav",
          "yae" : "sounds/characters/13 - y/03 - yae.wav",      "yaee" : "sounds/characters/13 - y/04 - yaee.wav",
          "yi" : "sounds/characters/13 - y/05 - yi.wav",        "yii" : "sounds/characters/13 - y/06 - yii.wav",
          "yu" : "sounds/characters/13 - y/07 - yu.wav",        "yuu" : "sounds/characters/13 - y/08 - yuu.wav",
          "ye" : "sounds/characters/13 - y/09 - ye.wav",        "yee" : "sounds/characters/13 - y/10 - yee.wav",
          "yai" : "sounds/characters/13 - y/11 - yai.wav",      "yo" : "sounds/characters/13 - y/12 - yo.wav",
          "yoo" : "sounds/characters/13 - y/13 - yoo.wav",      "yau" : "sounds/characters/13 - y/14 - yau.wav",
          "yang" : "sounds/characters/13 - y/15 - yang.wav",    "yru" : "sounds/characters/13 - y/16 - yru.wav",
          "yruu" : "sounds/characters/13 - y/17 - yruu.wav",

          "r" : "sounds/characters/14 - r/00 - r.wav",          "ra" : "sounds/characters/14 - r/01 - ra.wav",
          "ra_" : "sounds/characters/14 - r/01 - ra2.wav",      "raa" : "sounds/characters/14 - r/02 - raa.wav",
          "rae" : "sounds/characters/14 - r/03 - rae.wav",      "raee" : "sounds/characters/14 - r/04 - raee.wav",
          "ri" : "sounds/characters/14 - r/05 - ri.wav",        "rii" : "sounds/characters/14 - r/06 - rii.wav",
          "ru" : "sounds/characters/14 - r/07 - ru.wav",        "ruu" : "sounds/characters/14 - r/08 - ruu.wav",
          "re" : "sounds/characters/14 - r/09 - re.wav",        "ree" : "sounds/characters/14 - r/10 - ree.wav",
          "rai" : "sounds/characters/14 - r/11 - rai.wav",      "ro" : "sounds/characters/14 - r/12 - ro.wav",
          "roo" : "sounds/characters/14 - r/13 - roo.wav",      "rau" : "sounds/characters/14 - r/14 - rau.wav",
          "rang" : "sounds/characters/14 - r/15 - rang.wav",

          "l" : "sounds/characters/15 - l/00 - l.wav",          "la" : "sounds/characters/15 - l/01 - la.wav",
          "la_" : "sounds/characters/15 - l/01 - la2.wav",      "laa" : "sounds/characters/15 - l/02 - laa.wav",
          "lae" : "sounds/characters/15 - l/03 - lae.wav",      "laee" : "sounds/characters/15 - l/04 - laee.wav",
          "li" : "sounds/characters/15 - l/05 - li.wav",        "lii" : "sounds/characters/15 - l/06 - lii.wav",
          "lu" : "sounds/characters/15 - l/07 - lu.wav",        "luu" : "sounds/characters/15 - l/08 - luu.wav",
          "le" : "sounds/characters/15 - l/09 - le.wav",        "lee" : "sounds/characters/15 - l/10 - lee.wav",
          "lai" : "sounds/characters/15 - l/11 - lai.wav",      "lo" : "sounds/characters/15 - l/12 - lo.wav",
          "loo" : "sounds/characters/15 - l/13 - loo.wav",      "lau" : "sounds/characters/15 - l/14 - lau.wav",
          "lang" : "sounds/characters/15 - l/15 - lang.wav",    "lru" : "sounds/characters/15 - l/16 - lru.wav",
          "lruu" : "sounds/characters/15 - l/17 - lruu.wav",

          "w" : "sounds/characters/16 - w/00 - w.wav",          "wa" : "sounds/characters/16 - w/01 - wa.wav",
          "wa_" : "sounds/characters/16 - w/01 - wa2.wav",      "waa" : "sounds/characters/16 - w/02 - waa.wav",
          "wae" : "sounds/characters/16 - w/03 - wae.wav",      "waee" : "sounds/characters/16 - w/04 - waee.wav",
          "wi" : "sounds/characters/16 - w/05 - wi.wav",        "wii" : "sounds/characters/16 - w/06 - wii.wav",
          "wu" : "sounds/characters/16 - w/07 - wu.wav",        "wuu" : "sounds/characters/16 - w/08 - wuu.wav",
          "we" : "sounds/characters/16 - w/09 - we.wav",        "wee" : "sounds/characters/16 - w/10 - wee.wav",
          "wai" : "sounds/characters/16 - w/11 - wai.wav",      "wo" : "sounds/characters/16 - w/12 - wo.wav",
          "woo" : "sounds/characters/16 - w/13 - woo.wav",      "wau" : "sounds/characters/16 - w/14 - wau.wav",
          "wang" : "sounds/characters/16 - w/15 - wang.wav",    "wru" : "sounds/characters/16 - w/16 - wru.wav",
          "wruu" : "sounds/characters/16 - w/17 - wruu.wav",

          "sh" : "sounds/characters/17 - sh/00 - sh.wav",          "sha" : "sounds/characters/17 - sh/01 - sha.wav",
          "sha_" : "sounds/characters/17 - sh/01 - sha2.wav",      "shaa" : "sounds/characters/17 - sh/02 - shaa.wav",
          "shae" : "sounds/characters/17 - sh/03 - shae.wav",      "shaee" : "sounds/characters/17 - sh/04 - shaee.wav",
          "shi" : "sounds/characters/17 - sh/05 - shi.wav",        "shii" : "sounds/characters/17 - sh/06 - shii.wav",
          "shu" : "sounds/characters/17 - sh/07 - shu.wav",        "shuu" : "sounds/characters/17 - sh/08 - shuu.wav",
          "she" : "sounds/characters/17 - sh/09 - she.wav",        "shee" : "sounds/characters/17 - sh/10 - shee.wav",
          "shai" : "sounds/characters/17 - sh/11 - shai.wav",      "sho" : "sounds/characters/17 - sh/12 - sho.wav",
          "shoo" : "sounds/characters/17 - sh/13 - shoo.wav",      "shau" : "sounds/characters/17 - sh/14 - shau.wav",
          "shang" : "sounds/characters/17 - sh/15 - shang.wav",    "shru" : "sounds/characters/17 - sh/16 - shru.wav",
          "shruu" : "sounds/characters/17 - sh/17 - shruu.wav",

          "s" : "sounds/characters/18 - s/00 - s.wav",          "sa" : "sounds/characters/18 - s/01 - sa.wav",
          "sa_" : "sounds/characters/18 - s/01 - sa2.wav",      "saa" : "sounds/characters/18 - s/02 - saa.wav",
          "sae" : "sounds/characters/18 - s/03 - sae.wav",      "saee" : "sounds/characters/18 - s/04 - saee.wav",
          "si" : "sounds/characters/18 - s/05 - si.wav",        "sii" : "sounds/characters/18 - s/06 - sii.wav",
          "su" : "sounds/characters/18 - s/07 - su.wav",        "suu" : "sounds/characters/18 - s/08 - suu.wav",
          "se" : "sounds/characters/18 - s/09 - se.wav",        "see" : "sounds/characters/18 - s/10 - see.wav",
          "sai" : "sounds/characters/18 - s/11 - sai.wav",      "so" : "sounds/characters/18 - s/12 - so.wav",
          "soo" : "sounds/characters/18 - s/13 - soo.wav",      "sau" : "sounds/characters/18 - s/14 - sau.wav",
          "sang" : "sounds/characters/18 - s/15 - sang.wav",    "sru" : "sounds/characters/18 - s/16 - sru.wav",
          "sruu" : "sounds/characters/18 - s/17 - sruu.wav",

          "h" : "sounds/characters/19 - h/00 - h.wav",          "ha" : "sounds/characters/19 - h/01 - ha.wav",
          "ha_" : "sounds/characters/19 - h/01 - ha.wav",      "haa" : "sounds/characters/19 - h/02 - haa.wav",
          "hae" : "sounds/characters/19 - h/03 - hae.wav",      "haee" : "sounds/characters/19 - h/04 - haee.wav",
          "hi" : "sounds/characters/19 - h/05 - hi.wav",        "hii" : "sounds/characters/19 - h/06 - hii.wav",
          "hu" : "sounds/characters/19 - h/07 - hu.wav",        "huu" : "sounds/characters/19 - h/08 - huu.wav",
          "he" : "sounds/characters/19 - h/09 - he.wav",        "hee" : "sounds/characters/19 - h/10 - hee.wav",
          "hai" : "sounds/characters/19 - h/11 - hai.wav",      "ho" : "sounds/characters/19 - h/12 - ho.wav",
          "hoo" : "sounds/characters/19 - h/13 - hoo.wav",      "hau" : "sounds/characters/19 - h/14 - hau.wav",
          "hang" : "sounds/characters/19 - h/15 - hang.wav",    "hru" : "sounds/characters/19 - h/16 - hru.wav",
          "hruu" : "sounds/characters/19 - h/17 - hruu.wav",

          "f" : "sounds/characters/20 - f/00 - f.wav",          "fa" : "sounds/characters/20 - f/01 - fa.wav",
          "fa_" : "sounds/characters/20 - f/01 - fa2.wav",      "faa" : "sounds/characters/20 - f/02 - faa.wav",
          "fae" : "sounds/characters/20 - f/03 - fae.wav",      "faee" : "sounds/characters/20 - f/04 - faee.wav",
          "fi" : "sounds/characters/20 - f/05 - fi.wav",        "fii" : "sounds/characters/20 - f/06 - fii.wav",
          "fu" : "sounds/characters/20 - f/07 - fu.wav",        "fuu" : "sounds/characters/20 - f/08 - fuu.wav",
          "fe" : "sounds/characters/20 - f/09 - fe.wav",        "fee" : "sounds/characters/20 - f/10 - fee.wav",
          "fai" : "sounds/characters/20 - f/11 - fai.wav",      "fo" : "sounds/characters/20 - f/12 - fo.wav",
          "foo" : "sounds/characters/20 - f/13 - foo.wav",      "fau" : "sounds/characters/20 - f/14 - fau.wav",
          "fang" : "sounds/characters/20 - f/15 - fang.wav",    "fru" : "sounds/characters/20 - f/16 - fru.wav",
          "fruu" : "sounds/characters/20 - f/17 - fruu.wav",

          "nnga" : "sounds/characters/nnga.wav",        "nnda" : "sounds/characters/nnda.wav",
          "nndha" : "sounds/characters/nndha.wav",      "nnja" : "sounds/characters/nnja.wav",
          "mmba" : "sounds/characters/mmba.wav",        "nnya" : "sounds/characters/nnya.wav",
          "ng" : "sounds/characters/ng.wav",

          " " : "sounds/characters/null.wav",       "." : "sounds/characters/null2.wav",
          "?" : "sounds/characters/null2.wav",      "," : "sounds/characters/null.wav",

          }


