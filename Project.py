import re
def average_ratio(x):
    a = list() #list of lines starting with <ALIGNABLE_ANNOTATION
    b = list() #list of lines with time values
    c = list() #list of TIME_SLOT_REF2
    d = list() #list of TIME_SLOT_REF1
    e = list() #time value larger
    f = list() #time value smaller
    g = list() #time value larger as float 
    h = list() #time value smaller as float
    i = list() #input time
    j = list() #sum of input time
    m = list() #testser - list of lines starting with <ALIGNABLE_ANNOTATION
    n = list() #testser - list of lines with time values
    o = list() #testser - list of TIME_SLOT_REF2
    p = list() #testser - list of TIME_SLOT_REF1
    q = list() #testser - time value larger
    r = list() #testser - time value smaller
    s = list() #testser - time value larger as float 
    t = list() #testser - time value smaller as float
    u = list() #testser - input time
    v = list() #testser - sum of input time
    with open(x, 'r'):
        for line in x:
            if re.search(r'"<TIME_SLOT"', line):
                b.append(line)
            if re.search(r'"Vocal-child"', line):
                pass
            if re.search(r'"<ALIGN"', line):
                a.append(line)
            if re.search(r'</TIER>', line):
                break
        print (a)
        print (b)
        for line in x:
            if re.search(r'"Vocal-researcher"', line):
                pass
            if re.search(r'"<ALIGN"', line):
                m.append(line)
            if re.search(r'</TIER>', line):
                break
        for line in a:
            if re.search(r'TIME_SLOT_REF2="ts\d{2}"', line):
                ro = re.search(r'TIME_SLOT_REF2="(ts\d{2})"', line)
                so = ro.group(1)
                c.append(so)
            if re.search(r'TIME_SLOT_REF1="ts\d{2}"', line):
                ro = re.search(r'TIME_SLOT_REF1="(ts\d{2})"', line)
                so = ro.group(1)
                d.append(so)
        for line in c:
            if line in b:
                ro = re.search(r'TIME_VALUE="(\d{7})"', line) #
                so = ro.group(1)
                e.append(so)
        for line in d:
            if line in b:
                r = re.search(r'TIME_VALUE="(\d{7})"', line)
                s = r.group(1)
                f.append(s)
        for line in e:
            a = float(line)
            g.append(a)
        for line in f:
            a = float(line)
            h.append(a)
        for line in h:
            for line2 in g:
                if line2 > line:
                    a = line2 - line
                    i.append(a)
        j = sum(i)
        for line in m:
            if re.search(r'TIME_SLOT_REF2="ts\d{2}"', line):
                ro = re.search(r'TIME_SLOT_REF2="(ts\d{2})"', line)
                so = ro.group(1)
                o.append(so)
            if re.search(r'TIME_SLOT_REF1="ts\d{2}"', line):
                ro = re.search(r'TIME_SLOT_REF1="(ts\d{2})"', line)
                so = ro.group(1)
                p.append(so)
        for line in o:
            if line in n:
                ro = re.search(r'TIME_VALUE="(\d{7})"', line) #
                so = ro.group(1)
                q.append(so)
        for line in p:
            if line in n:
                ro = re.search(r'TIME_VALUE="(\d{7})"', line)
                so = ro.group(1)
                r.append(so)
        for line in q:
            a = float(line)
            s.append(a)
        for line in r:
            a = float(line)
            t.append(a)
        for line in t:
            for line2 in s:
                if line2 > line:
                    a = line2 - line
                    u.append(a)
        v = sum(u)
    print (c)
    
