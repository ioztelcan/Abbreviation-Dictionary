from app import db, models
from app.models import Entry

def show_all_entries():
    entries = models.Entry.query.all()
    for e in entries:
        print "----------------"
        print e.id
        print e.name
        print e.description

def remove_all_entries():
    entries = models.Entry.query.all()
    for e in entries:
        print "Deleting %s..." % e.name
        db.session.delete(e)

    db.session.commit()
    print "All entries deleted!"

def add_entry(name, desc):
    e = models.Entry(name=name, description=desc)
    db.session.add(e)
    db.session.commit()
    print "Added %s," % name, "%s" % desc

def remove_entry(name):
    models.Entry.query. \
        filter(Entry.name == name). \
        delete()
    print "Deleting %s..." % name
    db.session.commit()

def add_test_entries():
    e = models.Entry(name='T1', description='Test 1')
    db.session.add(e)
    e = models.Entry(name='T2', description='Test 2')
    db.session.add(e)
    e = models.Entry(name='T3', description='Test 3')
    db.session.add(e)
    e = models.Entry(name='T4', description='Test 4')
    db.session.add(e)
    e = models.Entry(name='T5', description='Test 5')
    db.session.add(e)

    db.session.commit()
    print "Added T1, T2, T3, T4, T5"

def whoosh_search(term):
    term = str(term)
    return Entry.query.whoosh_search(term).all()

def db_query(term):
    return models.Entry.query.filter(models.Entry.name.like("%"+term+"%")).all()

def parse_n_add(filename):
    cnt = 0
    skip_cnt = 0
    f = open(filename, "r")
    for line in f:
        line = line.strip()
        n,d = line.split(",")
        if not db_query(n):
            print "Adding:", line
            e = models.Entry(name=n, description=d)
            db.session.add(e)
            cnt = cnt + 1
        else:
            print "Skipping:", line, "[Already in the database]"
            skip_cnt = skip_cnt + 1

    f.close()
    db.session.commit()
    print "Added %d entries successfully." %cnt
    print "Skipped %d entries." %skip_cnt

def db_dump(filename):
    cnt = 0
    entries = models.Entry.query.all()
    f = open(filename, "w")
    for e in entries:
        f.write(e.name + "," + e.description + "\n")
        cnt = cnt + 1

    f.close()
    print "Dumped %d entries successfully." % cnt

def change_name(name, new_name):
    models.Entry.query. \
        filter(Entry.name == name). \
        update({"name": new_name})
    db.session.commit()

def change_description(name, new_desc):
    models.Entry.query. \
        filter(Entry.name == name). \
        update({"description": new_desc})
    db.session.commit()

