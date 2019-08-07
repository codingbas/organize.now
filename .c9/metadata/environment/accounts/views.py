{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["# Create your views here."],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":4,"column":41},"action":"insert","lines":["def index(request):","    \"\"\"Return the index.html file\"\"\"","    return render(request,  'index.html')"],"id":3}],[{"start":{"row":4,"column":41},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]},{"start":{"row":5,"column":4},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":6,"column":0},"end":{"row":9,"column":37},"action":"insert","lines":["def logout(request):","    \"\"\"Log the user out\"\"\"","    auth.logout(request)","    return redirect(reverse('index'))"],"id":6}],[{"start":{"row":0,"column":35},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":31},"action":"insert","lines":["from django.contrib import auth"],"id":8}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":52},"action":"insert","lines":["redirect, reverse"],"id":9}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","],"id":10}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":11}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":[","],"id":12}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":[" "],"id":13},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["m"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["e"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["s"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["s"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["a"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["g"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":24},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":11,"column":70},"action":"insert","lines":["","    messages.success(request, \"You have successfully been logged out\")"],"id":15}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":16},{"start":{"row":9,"column":24},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":37},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":18}],[{"start":{"row":13,"column":0},"end":{"row":15,"column":40},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    return render(request, 'login.html')"],"id":19}],[{"start":{"row":10,"column":68},"end":{"row":10,"column":69},"action":"insert","lines":["!"],"id":20}],[{"start":{"row":1,"column":41},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":40},"action":"insert","lines":["from accounts.forms import UserLoginForm"],"id":22}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":40},"action":"remove","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    return render(request, 'login.html')"],"id":23}],[{"start":{"row":14,"column":0},"end":{"row":17,"column":68},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"],"id":24}],[{"start":{"row":14,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})",""],"id":25}],[{"start":{"row":14,"column":0},"end":{"row":31,"column":68},"action":"insert","lines":["def login(request):","    \"\"\"Return a login page\"\"\"","    if request.method == \"POST\":","        login_form = UserLoginForm(request.POST)","","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","            ","","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully logged in!\")","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"],"id":26}],[{"start":{"row":0,"column":0},"end":{"row":31,"column":68},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse","from django.contrib import auth, messages","from accounts.forms import UserLoginForm","","def index(request):","    \"\"\"Return the index.html file\"\"\"","    return render(request,  'index.html')","    ","def logout(request):","    \"\"\"Log the user out\"\"\"","    auth.logout(request)","    messages.success(request, \"You have successfully been logged out!\")","    return redirect(reverse('index'))","    ","def login(request):","    \"\"\"Return a login page\"\"\"","    if request.method == \"POST\":","        login_form = UserLoginForm(request.POST)","","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","            ","","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully logged in!\")","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"],"id":27}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":68},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","from django.contrib import auth, messages","from accounts.forms import UserLoginForm","","def index(request):","    \"\"\"Return the index.html file\"\"\"","    return render(request,  'index.html')","","","def logout(request):","    \"\"\"Log the user out\"\"\"","    auth.logout(request)","    messages.success(request, \"You have successfully been logged out\")","    return redirect(reverse('index'))","","","def login(request):","    \"\"\"Return a login page\"\"\"","    if request.method == \"POST\":","        login_form = UserLoginForm(request.POST)","","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","            ","","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully logged in!\")","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})"],"id":28}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":33,"column":68},"end":{"row":33,"column":68},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565164961122,"hash":"23545a646e89c350fd6805ad3deee227bdba70b8"}