from flask import Blueprint

from counter.models import Counter

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
    #import pdb; pdb.set_trace() #console debug line by line
    counter = Counter.objects.all().first()
    if counter:
        counter.count += 1
        counter.two = counter.two * 2
        counter.save()
    else:
        counter = Counter()
        counter.count = 1
        counter.two = 2
        counter.save()
    return "<h1>Counter: " + str(counter.count) + "<h3>" + str(counter.two) + "</h3></h1>"

