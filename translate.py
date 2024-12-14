
class Translator:

    def __init__(self, english):
        self.s = 0
        self.i = 0
        self.english = english
        self.greek = ''

    def t(self, a, b):
        self.i = self.english.find(a, self.s)
        if self.i == -1:
            raise Exception(f"`{a}' not found")
        self.greek += self.english[self.s:self.i]
        self.greek += b
        self.s = self.i + len(a)

    def finalize(self):
        self.greek += self.english[self.s:]

def translate_t(t):
    t.t('lang="en"', 'lang="el"')
    t.t('Theodoros Dimakopoulos', 'Θοδωρής Δημακόπουλος')
    t.t('content="Biography and portfolio overview, for employers"',
        'content="Βιογραφικό και χαρτοφυλάκιο για εργοδότες"')
    t.t('Theme', 'Θέμα')
    t.t('Light theme', 'Ανοιχτό θέμα')
    t.t('Dark theme', 'Σκούρο θέμα')
    t.t('High contrast dark', 'Έντονη αντίθεση')
    t.t('Portfolio', 'Χαρτοφυλάκιο')
    t.t('''href="index-el.html"''', '''href="index.html"''')
    t.t("Greek", "English")
    t.t("I'm", "<!-- στα Αγγλικά εδώ λέει I'm χωρίς strong -->")
    t.t('Theodore D.', 'Θοδωρής Δημακόπουλος')
    t.t('''Undergraduate programmer with a focus on
Linux and face to face interactions.''',
        '''Φοιτητής πληροφορικής, έχω κλίση στα Linux
και προτιμώ την άμεση επικοινωνία.''')
    t.t('''I'm looking for a 6 month part time internship,
or maybe a 3 month full time one,
so I can get my degree.''',
        '''Για πτυχίο θα χρειαστώ πρακτική άσκηση,
κατά προτίμηση μερικής απασχόλησης έξι μηνών
ή στην ανάγκη ολικής απασχόλησης τριών μηνών.''')
    t.t('alt="face of man, green eyes, long hair"',
        'alt="Πρόσωπο άντρα, πράσινα μάτια, μακρύ μαλλί"')
    t.t('About me', 'Γενικά')
    t.t('In July 2024 I interned full time',
        'Έκανα τρίμηνη πρακτική πλήρους απασχόλησης')
    t.t('at Helvia', 'στη Helvia')
    t.t('''one month on DevOps/operations and for two months
I learned NextJS, MongoDB and Python's FastAPI by''',
        '''τον Ιούλιο του 2024.
Τον πρώτο μήνα μάθαινα DevOps/operations και τους δύο επόμενους
εξοικειώθηκα με τα εργαλεία NextJS, MongoDB και FastAPI της Python''')
    t.t('making Key Mouth', 'φτιάχνοντας την εφαρμογή Key Mouth')
    t.t('''It's a chat app that shows each key instead of messages.
It was hard mainly because there's no point of reference to hold onto.''',
        '''Το Key Mouth είναι εφαρμογή ανταλλαγής μηνυμάτων που δείνχνει τα
πλήκτρα που πατάει ο άλλος χρήστης σε πραγματικό χρόνο.
Το δύσκολο ήταν ότι δεν υπήρχε σημείο αναφοράς.''')
    t.t('''Before joining Helvia, we had cources related to web development and
I tried PostGres SQL, MySQL and MongoDB,
I read some code in VueJS and Python's Jango and
I tried learning Spring in Java and Kotlin a few times.
I entered a few Docker containers in my free time to look around
and I played around with Jest and Typescript.''',
        '''Πριν την πρακτική στη Helvia, σε μαθήματα που αφορούσαν web development
στη σχολή, δοκίμασα PostGres SQL, MySQL και MongoDB,
είδα κώδικα άλλων σε VueJS και Jango της Python και
προσπάθησα να μάθω Spring σε Java και Kotlin πάνω από μία φορά.
Επίσης πειραματίστηκα στον ελεύθερό μου χρόνο με μερικά Docker containers
από περιέργεια και δοκίμασα λίγο Jest και Typescript.''')
    t.t('''I tried WSL in 2020, I believe,
then I went to Linux Mint and then,
because I couldn't figure out how to use minimal tools on Mint,
I installed Arch Linux with the manual installation.
I was''',
        '''Θυμάμαι το 2020 να δοκίμασα WSL πρώτη φορά, έπειτα χρησιμοποίησα
Linux Mint και έπειτα, επειδή δυσκολευόμουν να ρυθμίσω κάποια εργαλεία,
εγκατέστησα Arch Linux με το χειροκίνητο τρόπο.''')
    t.t("motivated mostly by the DistroTube channel",
        "Με ενέπνευσε πολύ το κανάλι DistroTube")
    t.t('''on YouTube
although I've changed my mindset since then.''',
        '''στο YouTube
αν και το κανάλι έχει ένα τρόπο σκέψης που πλέον δεν ακολουθώ.''')
    t.t('''I used the shell a lot and eventually I got good at
the POSIX subset, both for scripts and on the command line interactively.
One day I rented an Alpine Linux server
for backups and to use it to serve this site with NginX and certbot.
It's alright, though I wouldn't say I'm good at serving sites.
There's downtime sometimes and
the certificates are a little off,
but there's been progress.''',
        '''Χρησιμοποιούσα πολύ το shell και έμαθα αρκετά το υποσύνολο POSIX,
και για scripts και για γραμμή εντολών.
Κάποια στιγμή νοίκιασα έναν Alpine Linux server
για backups και για να σερβίρω αυτό τον ιστοχώρο με NginX και certbot.
Σε γενικές γραμμές πάει καλά, αν και δε θα έλεγα ότι ξέρω servers.
Άλλοτε πέφτει το σάιτ,
άλλοτε υπάρχει θέμα με τα πιστοποιητικά,
αλλά υπάρχει πρόοδος.''')
    t.t("Social experiences",
        "Κοινωνικές εμπειρίες")
    t.t('''I was a stereotypical programmer up to about 2021,
today I do have a few friends.''',
        '''Μέχρι το 2021 περίπου ήμουν στερεοτυπικός προγραμματιστής,
σήμερα έχω κάποιους φίλους.''')
    t.t('''In University projects
I gave emphasis on UX user tests,
I showed some teammates how we could do automated tests
and in two projects I demonstrated some draft prototypes.
None of this went well though and that's a topic that
I can talk about all day.
My favorite project was a simple research on the Rust compiler
with 3 firends where we were face to face
2 months, 4 hours a day, 4 days a week at least.''',
        '''Σε ομαδικά πρότζεκτ στη σχολή
έδωσα έμφαση στα UX user test,
έδειξα σε συνεργάτες πώς γίνονται τα αυτόματα τεστ
και σε δύο εργασίες χρησιμοποίησα πρωτότυπα για ιδέες.
Βέβαια, δεν πήγαν καλά αυτά.
Η αγαπημένη μου ομαδική εργασία ήταν μια σχετικά απλή έρευνα
γύρω από τη γλώσσα Rust και το μεταγλωττιστή της,
ήμασταν 4 φίλοι και συνεργαζόμασταν από κοντά
για δύο μήνες, 4 ώρες τη μέρα τουλάχιστον 4 μέρες την εβδομάδα.''')
    t.t('as PDF', 'σε PDF')
    t.t('''The CV complements this site.
It emphasizes the parts that are more measurable.''',
        '''Το CV δίνει πιο πολλή έμφαση σε μετρήσιμες έννοιες.''')
    t.t("Most educational projects",
        "Πρότζεκτ με μεγαλύτερη επηροή")
    t.t("The project that taught me the most, by far, is",
        "Το πρότζεκτ που με επηρέασε περισσότερο με διαφορά είναι")
    t.t("the Key Mouth web app",
        "η εφαρμογή Key Mouth")
    t.t("I won't go into details here though because there are",
        "δε θα αναφέρω όμως περισσότερα επειδή έχω αναφέρει όλες τις")
    t.t("details on the GitHub page",
        "λεπτομέρειες στο GitHub")
    t.t('''The most valuable lessons for me were rewritten projects
and ideas that I had to throw away, so that's what I'd like to focus on.''',
        '''Κατά τα άλλα, ό,τι έμαθα το έμαθα κυρίως από κώδικα που γράφτηκε δεύτερη φορά
ή που απλά πετάχτηκε, οπότε σε αυτά θα ήθελα να δώσω έμφαση εδώ.''')
    t.t("The 2 rewrites of this site",
        "Οι 3 εκδόσεις αυτού του ιστοχώρου")
    t.t("The site used to have a typical menu at the top.",
        "Υπήρχε ένα μενού στην κορυφή όπως σε άλλα σάιτ.")
    t.t("Identity buffee",
        "Συναρμολογούμενες συναρτήσεις")
    t.t('''Abstract PHP functions that compose HTML code.
It's still ''',
        '''PHP συναρτήσεις που επιστρέφουν strings HTML κώδικα.''')
    t.t("served",
        "Το σερβίρω")
    t.t("and it's on",
        "ακόμα και υπάρχει και στο")
    t.t("Fewest layers possible",
        "Λιγότερα επίπεδα αφαίρεσης")
    t.t('''Abstractions got replaced with abbreviations.
I serve an''',
        '''Ο κώδικας μοιάζει σα συντομεύσεις που παραπέμπουν σε περισσότερο κώδικα.
Σερβίρω μια''')
    t.t('older', 'παλιότερη')
    t.t('and a', 'και μια')
    t.t('newer', 'επόμενη')
    t.t('version', 'έκδοση')
    t.t("and it's on", "και υπάρχει ο κώδικας στο")
    t.t('''Least text possible''',
        '''Λιγότερο κείμενο''')
    t.t('''Kevin Powell's site''',
        '''Το σάιτ του Kevin Powell''')
    t.t('''inspired me to reduce the text,
to the point that I could serve hand written HTML.''',
        '''μου έδωσε την ιδέα να γράψω όσο λιγότερο κείμενο γίνεται
ώστε να μπορώ να γράψω την HTML με το χέρι.''')
    t.t('''Conclusion''', '''Τελικά''')
    t.t('''At first it looks like I lowered the requirements to get away with draft code
but I'd say the requirements overall went up.
It was a requirement to be laconic,
one could say there was a requirement to
make the browser tools reflect the source code better,
and it's fun to hand write HTML with no indentation.''',
        '''Μοιάζει σα να μειώθηκαν οι απαιτήσεις και να έγινε πιο πρόχειρος ο κώδικας.
Από μια άποψη όμως οι απαιτήσεις ανέβηκαν.
Πλέον πρέπει η σελίδα να είναι λακωνική,
πλέον αναμένεται ο browser να μπορεί να αναφέρει τον πηγαίο κώδικα
και αν δοκιμάσεις να γράψεις HTML χωρίς indentation δε ξεκολλάς.''')
    t.t("The 3 rewrites of my hotkey system",
        "Οι τέσσερις εκδόσεις συνδυασμών πλήκτρων")
    t.t('''I use an odd operating system which relies on key combinations
becuase there's no taskbar or bars on windows.
I had one real option, to use''',
        '''Το λειτουργικό μου σύστημα είναι λίγο στρυφνό και βασίζεται σε
συνδυασμούς πλήκτρων γιατί δεν έχει πολλά μενού και μπάρες.
Προφανώς θα χρησιμοποιούσα το πρόγραμμα''')
    t.t("but I wanted a pop-up guide too like",
        "αλλά ήθελα και ένα αναδυόμενο παράθυρο με συμβουλές σαν το")
    t.t("and I couldn't have one.", "που δε γίνεται.")
    t.t("Prompt for next key",
        "Εισαγωγή γράμματος")
    t.t('''3 bash scripts and the language shown below.
A terminal appeared to list keys and take input.''',
        '''3 bash script και η παρακάτω γλώσσα.
Εμφανίζεται ένα τερματικό, δείχνει μια λίστα από πλήκτρα και περιμένει για είσοδο.''')
    t.t('''The terminal messed with the notion of previous window
and the hotkeys for switching windows had bugs.''',
        '''Το τερματικό ανακατευόταν με τα υπόλοιπα παράθυρα
και οι συνδυασμοί πλήκτρων για να αλλάξεις παράθυρο χάλαγαν.''')
    t.t("Hotkey shell commands",
        "Ένα προς ένα εντολές Linux")
    t.t('''A new demand was that''',
        '''Μία νέα απαίτηση ήταν ότι το''')
    t.t('''should also be possible from the terminal as''',
        '''πρέπει να μπορεί να γίνει και από τη γραμμή εντολών πατώντας''')
    t.t('''Another new demand is that''',
        '''Επίσης, το''')
    t.t('''is bound to''',
        '''τρέχει την εντολή''')
    t.t('''and I'll be prompted to fill in the gap.
It's uploaded on''',
        '''αφού ρωτήσει το χρήστη πώς να συμπληρώσει το κενό.
Πλέον το ανέβασα και στο''')
    t.t(''' after the fact.''',
        '''.''')
    t.t('''The configuration code was verbose
and the commands couldn't be listed reliably.
It wasn't actually used it in the terminal either.''',
        '''Ρυθμίζεται λίγο δύσκολα και δεν υπήρχε καλός τρόπος να πάρεις μια λίστα
από πλήκτρα.
Φυσικά δεν το χρησιμοποιούσα από τη γραμμή εντολών σχεδόν ποτέ.''')
    t.t('''Code snippet composer''',
        '''Πρόγραμμα συνδυασμού κομματιών κώδικα''')
    t.t('''The demands went up
but they weren't based on real needs.
It's on''',
        '''Ανέβηκαν οι απαιτήσεις
αλλά χωρίς λόγο.
Είναι στο''')
    t.t('''There had to be a list of text snippets,
some of which are operating system commands,
some of which are bound to hotkeys.
Some can prompt for completion.
The completion gives hints,
a bar shows the final command that ran,
and each text snippet has an easily accessible description.
Other purposes for the text snippets were shell aliases,
copying ASCII art and
completing parts of a C for loop and copying it.
Below is part of the list that appeared on the screen.''',
        '''Δίνεται μια λίστα από κομμάτια κειμένου ή κώδικα,
κάποια εκ των οποίων είναι εντολές Linux,
κάποιες εκ των οποίων έχουν συνδυασμούς πλήκτρων.
Κάποιες ζητούν και συμπλήρωση.
Κατά τη συμπλήρωση το πρόγραμμα δίνει προτάσεις
και στο τέλος μια μπάρα γράφει ποια εντολή εκτελέστηκε.
Κάθε κομμάτι κειμένου έχει περιγραφή.
Τα κομμάτια εκτός από εντολές μπορεί να είναι shell aliases,
ASCII art για αντιγραφή στο πρόχειρο,
ένα C for loop που κάποια κομμάτια του λείπουν και θέλουν συμπλήρωση κλπ.
Στην οθόνη εμφανιζόταν μία λίστα που έμοιαζε κάπως έτσι:''')
    t.t('''The configuration was shell scripts that printed shell scripts.
It became so slow that I considered caching.''',
        '''Ρυθμιζόταν με shell scripts που παράγουν άλλα shell scripts.
Άρχισε να χρειάζεται caching κάποια στιγμή και είπα να δοκιμάσω άλλη προσέγγιση.''')
    t.t('''I got syntax highlighting in my configuration file,
I got a listing, a superset of the hotkey commands,
a bar saying what ran,
I could run the same actions from the terminal
and for the first time I could easily log the commands and their output.''',
        '''Αυτό το αρχείο χρωματίζεται από τον editor,
λειτουργεί σα λίστα, έχει ένα υπερσύνολο των εντολών που αντιστοιχούν σε πλήκτρα,
μια μπάρα αναφέρει τι εκτελέστηκε,
χρησιμοποιείται και από τη γραμμή εντολών
και για πρώτη φορά ήταν πρακτικό να φτιαχτεί logger.''')
    t.t('''It's on''',
        '''Είναι στο''')
    t.t('''among my dotfiles.''',
        '''ανάμεσα στα αρχεία ρυθμίσεών μου.''')
    t.t('''Conclusion''',
        '''Συμπέρασμα''')
    t.t('''This project made me think of code as a person going through phases.
It started relatable, then it became fancy and then almost grumpy.
Just like the website, I ended up with one file with flat hierarchies.
Maybe at scale a project can't go through phases in the same way
but I find this phenomenon to be fascinating.''',
        '''Αυτοί οι πειραματισμοί έκαναν τον κώδικα να μοιάζει με φάσεις ζωής.
Στην αρχή ήταν συμπαθητικός και οικείος,
έπειτα έγινε λίγο υπερβολικός και στο τέλος
έγινε βαρετός και περίεργος, σχεδόν κυνικός.
Μοιάζει λίγο με την ιστοσελίδα που έγινε ένα αρχείο με απλή δομή.
Ίσως σε μεγάλη κλίμακα να μη μπορεί ένα πρότζεκτ να περάσει από
τέτοιες φάσεις αλλά έχει ενδιαφέρον αυτό το φαινόμενο.''')
    t.t('''Other experiments at home''',
        '''Άλλοι πειραματισμοί''')
    t.t('''Some other stories are
the directory structure of my laptop
which was restructured 4 times alongside its remote backup,
the image tagging facilities which used python GUIs at first,
I was trying to decorate my operating system for some time,
I tried to &quot;clean-up&quot; the''',
        '''Είχε αλλάξει πολλές φορές επίσης η δομή των φακέλων στο λάπτοπ μου
και έπρεπε να αλλάζω αντίστοιχα το backup στον server,
προσπαθούσα για ένα μεγάλο διάστημα να ομαδοποιήσω κάποιες εικόνες
και χρησιμοποίησα αυτοσχέδια Python GUIs μεταξύ άλλων,
προσπαθούσα για ένα διάστημα να διακοσμίσω το λειτουργικό μου σύστημα,
προσπάθησα να κάνω &quot;πιο καθαρό&quot; τον κώδικα του''')
    t.t('''project but I had to accept I made it worse and I re-wrote a''',
        '''και χρειάστηκε να αποδεχτώ ότι απλά τον έκανα χειρότερο και, τέλος,
ξανάγραψα ένα''')
    t.t('''clock pop-up''',
        '''αναδυόμενο ρολόι''')
    t.t('''from Python to C and it ended up uglier.''',
        '''από Python σε C και έχασε σε εμφάνιση.''')
    t.t('''Thanks for reading''',
        '''Καλή συνέχεια!''')
    t.t('''Have a nice day, don't hesitate to hit me up!''',
        '''Μη διστάσετε να μου γράψετε για ο,τιδήποτε.''')

def translate(src='index.html', dest='index-el.html'):
    english = ""
    with open(src, 'r') as f:
        english = f.read()
    t = Translator(english)
    translate_t(t)
    t.finalize()

    with open(dest, 'w') as f:
        f.write(t.greek)

if __name__ == '__main__':
    translate()
