{"filter":false,"title":"settings.py","tooltip":"/finalmilestone/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":[","],"id":71}],[{"start":{"row":72,"column":70},"end":{"row":73,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":73,"column":0},"end":{"row":73,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":73,"column":16},"end":{"row":73,"column":58},"action":"insert","lines":["'django.template.context_processors.media'"],"id":73}],[{"start":{"row":147,"column":1},"end":{"row":148,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":148,"column":0},"end":{"row":149,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":149,"column":0},"end":{"row":150,"column":21},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"],"id":75}],[{"start":{"row":73,"column":58},"end":{"row":73,"column":59},"action":"insert","lines":[","],"id":76}],[{"start":{"row":73,"column":59},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":74,"column":0},"end":{"row":74,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":74,"column":16},"end":{"row":74,"column":45},"action":"insert","lines":["'cart.contexts.cart_contents'"],"id":78}],[{"start":{"row":151,"column":21},"end":{"row":152,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":152,"column":0},"end":{"row":153,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":153,"column":0},"end":{"row":155,"column":0},"action":"insert","lines":["STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')","STRIPE_SECRET = os.getenv('STRIPE_SECRET')",""],"id":80}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":82},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["e"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["n"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"remove","lines":["s"],"id":83}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["l"],"id":84},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["i"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["s"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":65},"action":"remove","lines":["SECRET_KEY = '1t)vhcb@-da@*u(4w9$0meq#x7y=s5oa9jp%3g5iq%-*x@%g_2'"],"id":85}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":41},"action":"insert","lines":["SECRET_KEY = os.environ.get('SECRET_KEY')"],"id":86}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":87}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":22},"action":"insert","lines":["import dj_database_url"],"id":88}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"insert","lines":["    "],"id":89},{"start":{"row":89,"column":0},"end":{"row":89,"column":4},"action":"insert","lines":["    "]},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":88,"column":4},"end":{"row":93,"column":5},"action":"remove","lines":["DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":90}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"remove","lines":["    "],"id":91}],[{"start":{"row":88,"column":0},"end":{"row":94,"column":0},"action":"insert","lines":["DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}",""],"id":92}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"insert","lines":["#"],"id":93}],[{"start":{"row":88,"column":1},"end":{"row":88,"column":2},"action":"insert","lines":[" "],"id":94}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"insert","lines":["#"],"id":95}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"insert","lines":["#"],"id":96}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"remove","lines":[" "],"id":97}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["#"],"id":98}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":[" "],"id":99}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["#"],"id":100}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"insert","lines":["#"],"id":101}],[{"start":{"row":93,"column":2},"end":{"row":94,"column":0},"action":"insert","lines":["",""],"id":102},{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":95,"column":0},"end":{"row":104,"column":5},"action":"insert","lines":["if host == onlineurl:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","    ","else:","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":103}],[{"start":{"row":95,"column":20},"end":{"row":95,"column":21},"action":"remove","lines":[":"],"id":104}],[{"start":{"row":95,"column":19},"end":{"row":95,"column":20},"action":"remove","lines":["l"],"id":105},{"start":{"row":95,"column":18},"end":{"row":95,"column":19},"action":"remove","lines":["r"]},{"start":{"row":95,"column":17},"end":{"row":95,"column":18},"action":"remove","lines":["u"]},{"start":{"row":95,"column":16},"end":{"row":95,"column":17},"action":"remove","lines":["e"]},{"start":{"row":95,"column":15},"end":{"row":95,"column":16},"action":"remove","lines":["n"]},{"start":{"row":95,"column":14},"end":{"row":95,"column":15},"action":"remove","lines":["i"]},{"start":{"row":95,"column":13},"end":{"row":95,"column":14},"action":"remove","lines":["l"]},{"start":{"row":95,"column":12},"end":{"row":95,"column":13},"action":"remove","lines":["n"]},{"start":{"row":95,"column":11},"end":{"row":95,"column":12},"action":"remove","lines":["o"]},{"start":{"row":95,"column":10},"end":{"row":95,"column":11},"action":"remove","lines":[" "]},{"start":{"row":95,"column":9},"end":{"row":95,"column":10},"action":"remove","lines":["="]},{"start":{"row":95,"column":8},"end":{"row":95,"column":9},"action":"remove","lines":["="]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"remove","lines":[" "]}],[{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"remove","lines":["t"],"id":106},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"remove","lines":["s"]},{"start":{"row":95,"column":4},"end":{"row":95,"column":5},"action":"remove","lines":["o"]},{"start":{"row":95,"column":3},"end":{"row":95,"column":4},"action":"remove","lines":["h"]},{"start":{"row":95,"column":2},"end":{"row":95,"column":3},"action":"remove","lines":[" "]},{"start":{"row":95,"column":1},"end":{"row":95,"column":2},"action":"remove","lines":["f"]},{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"remove","lines":["i"]},{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":97,"column":0},"end":{"row":103,"column":5},"action":"remove","lines":["else:","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":107},{"start":{"row":96,"column":4},"end":{"row":97,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":95,"column":79},"end":{"row":95,"column":80},"action":"remove","lines":[")"],"id":108},{"start":{"row":95,"column":78},"end":{"row":95,"column":79},"action":"remove","lines":["'"]},{"start":{"row":95,"column":77},"end":{"row":95,"column":78},"action":"remove","lines":["L"]},{"start":{"row":95,"column":76},"end":{"row":95,"column":77},"action":"remove","lines":["R"]},{"start":{"row":95,"column":75},"end":{"row":95,"column":76},"action":"remove","lines":["U"]},{"start":{"row":95,"column":74},"end":{"row":95,"column":75},"action":"remove","lines":["_"]},{"start":{"row":95,"column":73},"end":{"row":95,"column":74},"action":"remove","lines":["E"]},{"start":{"row":95,"column":72},"end":{"row":95,"column":73},"action":"remove","lines":["S"]},{"start":{"row":95,"column":71},"end":{"row":95,"column":72},"action":"remove","lines":["A"]},{"start":{"row":95,"column":70},"end":{"row":95,"column":71},"action":"remove","lines":["B"]},{"start":{"row":95,"column":69},"end":{"row":95,"column":70},"action":"remove","lines":["A"]},{"start":{"row":95,"column":68},"end":{"row":95,"column":69},"action":"remove","lines":["T"]},{"start":{"row":95,"column":67},"end":{"row":95,"column":68},"action":"remove","lines":["A"]},{"start":{"row":95,"column":66},"end":{"row":95,"column":67},"action":"remove","lines":["D"]},{"start":{"row":95,"column":65},"end":{"row":95,"column":66},"action":"remove","lines":["'"]},{"start":{"row":95,"column":64},"end":{"row":95,"column":66},"action":"remove","lines":["()"]},{"start":{"row":95,"column":63},"end":{"row":95,"column":64},"action":"remove","lines":["t"]},{"start":{"row":95,"column":62},"end":{"row":95,"column":63},"action":"remove","lines":["e"]}],[{"start":{"row":95,"column":61},"end":{"row":95,"column":62},"action":"remove","lines":["g"],"id":109},{"start":{"row":95,"column":60},"end":{"row":95,"column":61},"action":"remove","lines":["."]},{"start":{"row":95,"column":59},"end":{"row":95,"column":60},"action":"remove","lines":["n"]},{"start":{"row":95,"column":58},"end":{"row":95,"column":59},"action":"remove","lines":["o"]},{"start":{"row":95,"column":57},"end":{"row":95,"column":58},"action":"remove","lines":["r"]},{"start":{"row":95,"column":56},"end":{"row":95,"column":57},"action":"remove","lines":["i"]},{"start":{"row":95,"column":55},"end":{"row":95,"column":56},"action":"remove","lines":["v"]},{"start":{"row":95,"column":54},"end":{"row":95,"column":55},"action":"remove","lines":["n"]},{"start":{"row":95,"column":53},"end":{"row":95,"column":54},"action":"remove","lines":["e"]},{"start":{"row":95,"column":52},"end":{"row":95,"column":53},"action":"remove","lines":["."]},{"start":{"row":95,"column":51},"end":{"row":95,"column":52},"action":"remove","lines":["s"]}],[{"start":{"row":95,"column":50},"end":{"row":95,"column":51},"action":"remove","lines":["o"],"id":110}],[{"start":{"row":95,"column":50},"end":{"row":95,"column":51},"action":"insert","lines":[")"],"id":111}],[{"start":{"row":95,"column":50},"end":{"row":95,"column":52},"action":"insert","lines":["\"\""],"id":112}],[{"start":{"row":95,"column":51},"end":{"row":95,"column":212},"action":"insert","lines":["postgres://plzrykbcetfdyb:b694113d8a9ccede9fbf5cbfc711b7617f7c0f6dde1c72c9eebceb161f424627@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/d5gfgu88sto9sj"],"id":113}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"remove","lines":["    "],"id":114}],[{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"remove","lines":["",""],"id":115},{"start":{"row":93,"column":2},"end":{"row":94,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":93,"column":2},"end":{"row":94,"column":0},"action":"insert","lines":["",""],"id":116},{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["",""],"id":117},{"start":{"row":95,"column":0},"end":{"row":96,"column":0},"action":"insert","lines":["",""]},{"start":{"row":96,"column":0},"end":{"row":97,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":95,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","    }","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }",""],"id":118}],[{"start":{"row":97,"column":66},"end":{"row":97,"column":67},"action":"remove","lines":[")"],"id":119},{"start":{"row":97,"column":65},"end":{"row":97,"column":66},"action":"remove","lines":["'"]},{"start":{"row":97,"column":64},"end":{"row":97,"column":65},"action":"remove","lines":["L"]},{"start":{"row":97,"column":63},"end":{"row":97,"column":64},"action":"remove","lines":["R"]},{"start":{"row":97,"column":62},"end":{"row":97,"column":63},"action":"remove","lines":["U"]},{"start":{"row":97,"column":61},"end":{"row":97,"column":62},"action":"remove","lines":["_"]},{"start":{"row":97,"column":60},"end":{"row":97,"column":61},"action":"remove","lines":["E"]},{"start":{"row":97,"column":59},"end":{"row":97,"column":60},"action":"remove","lines":["S"]},{"start":{"row":97,"column":58},"end":{"row":97,"column":59},"action":"remove","lines":["A"]},{"start":{"row":97,"column":57},"end":{"row":97,"column":58},"action":"remove","lines":["B"]},{"start":{"row":97,"column":56},"end":{"row":97,"column":57},"action":"remove","lines":["A"]},{"start":{"row":97,"column":55},"end":{"row":97,"column":56},"action":"remove","lines":["T"]},{"start":{"row":97,"column":54},"end":{"row":97,"column":55},"action":"remove","lines":["A"]}],[{"start":{"row":97,"column":53},"end":{"row":97,"column":54},"action":"remove","lines":["D"],"id":120},{"start":{"row":97,"column":52},"end":{"row":97,"column":53},"action":"remove","lines":["'"]},{"start":{"row":97,"column":51},"end":{"row":97,"column":53},"action":"remove","lines":["()"]},{"start":{"row":97,"column":50},"end":{"row":97,"column":51},"action":"remove","lines":["t"]},{"start":{"row":97,"column":49},"end":{"row":97,"column":50},"action":"remove","lines":["e"]},{"start":{"row":97,"column":48},"end":{"row":97,"column":49},"action":"remove","lines":["g"]},{"start":{"row":97,"column":47},"end":{"row":97,"column":48},"action":"remove","lines":["."]},{"start":{"row":97,"column":46},"end":{"row":97,"column":47},"action":"remove","lines":["n"]},{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"remove","lines":["o"]},{"start":{"row":97,"column":44},"end":{"row":97,"column":45},"action":"remove","lines":["r"]},{"start":{"row":97,"column":43},"end":{"row":97,"column":44},"action":"remove","lines":["i"]},{"start":{"row":97,"column":42},"end":{"row":97,"column":43},"action":"remove","lines":["v"]},{"start":{"row":97,"column":41},"end":{"row":97,"column":42},"action":"remove","lines":["n"]}],[{"start":{"row":97,"column":40},"end":{"row":97,"column":41},"action":"remove","lines":["e"],"id":121},{"start":{"row":97,"column":39},"end":{"row":97,"column":40},"action":"remove","lines":["."]},{"start":{"row":97,"column":38},"end":{"row":97,"column":39},"action":"remove","lines":["s"]},{"start":{"row":97,"column":37},"end":{"row":97,"column":38},"action":"remove","lines":["o"]}],[{"start":{"row":97,"column":37},"end":{"row":97,"column":38},"action":"insert","lines":[")"],"id":122}],[{"start":{"row":97,"column":37},"end":{"row":97,"column":39},"action":"insert","lines":["\"\""],"id":123}],[{"start":{"row":97,"column":38},"end":{"row":97,"column":199},"action":"insert","lines":["postgres://plzrykbcetfdyb:b694113d8a9ccede9fbf5cbfc711b7617f7c0f6dde1c72c9eebceb161f424627@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/d5gfgu88sto9sj"],"id":124}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":211},"action":"remove","lines":["DATABASES = {'default': dj_database_url.parse(\"postgres://plzrykbcetfdyb:b694113d8a9ccede9fbf5cbfc711b7617f7c0f6dde1c72c9eebceb161f424627@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/d5gfgu88sto9sj\")}"],"id":125},{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"remove","lines":["",""]},{"start":{"row":108,"column":0},"end":{"row":109,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":111,"column":0},"end":{"row":112,"column":0},"action":"remove","lines":["",""],"id":126},{"start":{"row":110,"column":0},"end":{"row":111,"column":0},"action":"remove","lines":["",""]},{"start":{"row":109,"column":4},"end":{"row":110,"column":0},"action":"remove","lines":["",""]},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"remove","lines":["    "]},{"start":{"row":108,"column":0},"end":{"row":109,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"remove","lines":["",""],"id":127}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["#"],"id":128}],[{"start":{"row":29,"column":86},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":129}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["\"\""],"id":130}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"remove","lines":["\"\""],"id":131}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["]"],"id":132},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["\"\""]}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["\""],"id":133},{"start":{"row":30,"column":1},"end":{"row":30,"column":35},"action":"insert","lines":["https://organizenow.herokuapp.com/"]}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["}"],"id":134}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["}"],"id":135}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["]"],"id":136}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["]"],"id":137},{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":[" "]}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":[" "],"id":138},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"remove","lines":["/"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["m"]}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["o"],"id":139},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["c"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"remove","lines":["."]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"remove","lines":["p"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"remove","lines":["p"]},{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"remove","lines":["a"]},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["u"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["k"]},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"remove","lines":["o"]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"remove","lines":["r"]},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"remove","lines":["e"]},{"start":{"row":30,"column":21},"end":{"row":30,"column":22},"action":"remove","lines":["h"]},{"start":{"row":30,"column":20},"end":{"row":30,"column":21},"action":"remove","lines":["."]},{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"remove","lines":["w"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"remove","lines":["o"]},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"remove","lines":["n"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["e"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"remove","lines":["z"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"remove","lines":["i"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"remove","lines":["n"]}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":["a"],"id":140},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"remove","lines":["g"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"remove","lines":["r"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"remove","lines":["o"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["/"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["/"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":[":"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["s"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["p"]},{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"remove","lines":["t"]},{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["t"]},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["h"]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["\""],"id":141},{"start":{"row":29,"column":86},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":86},"end":{"row":29,"column":87},"action":"insert","lines":["]"],"id":142}],[{"start":{"row":29,"column":86},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":143}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["]"],"id":144},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":[","]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":[","],"id":145}],[{"start":{"row":29,"column":86},"end":{"row":29,"column":87},"action":"insert","lines":["]"],"id":146}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":34},"action":"insert","lines":["https://organizenow.herokuapp.com/"],"id":147}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["/"],"id":148},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["/"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":[":"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["s"]},{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"remove","lines":["p"]},{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["t"]},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["t"]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["h"]}],[{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["/"],"id":149}],[{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"insert","lines":["'"],"id":150},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"insert","lines":["]"]}],[{"start":{"row":29,"column":86},"end":{"row":29,"column":87},"action":"remove","lines":["]"],"id":151}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["o"],"id":152},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["'"]}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["r"],"id":153},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"insert","lines":["o"]}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["g"],"id":154},{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"insert","lines":["r"]},{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"remove","lines":["a"]},{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"insert","lines":["g"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["n"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["a"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["i"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["n"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["z"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["i"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["e"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["z"]}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["n"],"id":155},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["e"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"remove","lines":["o"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["n"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"remove","lines":["w"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["o"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"remove","lines":["."]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["w"]}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":["h"],"id":156},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["."]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"remove","lines":["e"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["h"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"remove","lines":["r"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["e"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"remove","lines":["o"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["r"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["k"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"remove","lines":["u"],"id":157},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"insert","lines":["k"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"remove","lines":["a"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"insert","lines":["u"]}],[{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"remove","lines":["p"],"id":158},{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"insert","lines":["a"]},{"start":{"row":30,"column":20},"end":{"row":30,"column":21},"action":"remove","lines":["p"]},{"start":{"row":30,"column":20},"end":{"row":30,"column":21},"action":"insert","lines":["p"]},{"start":{"row":30,"column":21},"end":{"row":30,"column":22},"action":"remove","lines":["."]},{"start":{"row":30,"column":21},"end":{"row":30,"column":22},"action":"insert","lines":["p"]},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"remove","lines":["c"]},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"insert","lines":["."]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"remove","lines":["o"]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"insert","lines":["c"]}],[{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"remove","lines":["m"],"id":159},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"insert","lines":["o"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["'"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"insert","lines":["m"]},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["]"]},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"insert","lines":["'"]}],[{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"insert","lines":["]"],"id":160}],[{"start":{"row":29,"column":86},"end":{"row":29,"column":87},"action":"insert","lines":[","],"id":161}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["#"],"id":162}],[{"start":{"row":29,"column":87},"end":{"row":30,"column":0},"action":"remove","lines":["",""],"id":163}],[{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"remove","lines":["e"],"id":164},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"remove","lines":["u"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"remove","lines":["r"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["T"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["F"],"id":165},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["a"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["l"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["s"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["#"],"id":166}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["#"],"id":167}],[{"start":{"row":97,"column":37},"end":{"row":97,"column":200},"action":"remove","lines":["\"postgres://plzrykbcetfdyb:b694113d8a9ccede9fbf5cbfc711b7617f7c0f6dde1c72c9eebceb161f424627@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/d5gfgu88sto9sj\""],"id":168},{"start":{"row":97,"column":37},"end":{"row":97,"column":55},"action":"insert","lines":["os.environ['HOME']"]}],[{"start":{"row":97,"column":49},"end":{"row":97,"column":53},"action":"remove","lines":["HOME"],"id":169},{"start":{"row":97,"column":49},"end":{"row":97,"column":63},"action":"insert","lines":["\"DATABASE_URL\""]}],[{"start":{"row":97,"column":62},"end":{"row":97,"column":63},"action":"remove","lines":["\""],"id":170}],[{"start":{"row":97,"column":49},"end":{"row":97,"column":50},"action":"remove","lines":["\""],"id":171}]]},"ace":{"folds":[],"scrolltop":79.5,"scrollleft":0,"selection":{"start":{"row":99,"column":5},"end":{"row":99,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1566398393846,"hash":"fb7895c205d8ab6adc0d8fe7390cdc7962f4b206"}