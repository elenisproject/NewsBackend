#our database configuration
DB_CREDS = {
    'host':'localhost',
    'user':'root',
    'pass':'eleni123',
    'db':'NewsCrawler'
}

#list of words used in notebooks folder for the goodnews_badnews.ipynb, 20 words in each list
pos = ['καλυτερα','ενισχυση','ανοδο','μουσειο','στηριξη','δημιουργια','ευκαιρια','φεστιβαλ','μουσικη','τουρισμου','αναπτυξη',' ανακαμψης',' αισιοδοξα','καλος','χαρα','προσληψεις','εγκαινιαστηκε','ανακαλυψη','επιτυχια','καλη','συνεργασια']
neg = ['κριση','μετρων','προσπαθεια','προστασιας','ελεγχο','κινδυνο','χρειαζεται','ζητημα','αναγκη','μειωση','κρισης',' προβλημα',' ανησυχια','λυπη','συγχυση','επιθεση','πονο','υφεση','ακυρωση','προβληματα']

#list of countries used in notebooks folder for the most_common_countries.ipynb
countries_list = ['Κίνα',' Ινδία',' Αμερικη',' Ινδονησία',' Πακιστάν',' Βραζιλία',' Νιγηρία',' Μπανγκλαντές',' Ρωσία',' Μεξικό',' Ιαπωνία',' Αιθιοπία',' Φιλιππίνες',' Αίγυπτος',' Βιετνάμ',' Λαϊκή Δημοκρατία του Κονγκό ',' Ιράν',' Τουρκία',' Γερμανία',' Ηνωμένο Βασίλειο',' Ταϊλάνδη',' Γαλλία',' Ιταλία',' Νότια Αφρική',' Τανζανία',' Μιανμάρ',' Νότια Κορέα',' Κολομβία',' Κένυα',' Ισπανία',' Αργεντινή',' Αλγερία',' Σουδάν',' Ουκρανία',' Ουγκάντα',' Ιράκ',' Πολωνία',' Καναδάς',' Μαρόκο',' Σαουδική Αραβία',' Ουζμπεκιστάν',' Αφγανιστάν',' Μαλαισία',' Περού',' Βενεζουέλα',' Ανγκόλα',' Γκάνα',' Μοζαμβίκη',' Νεπάλ',' Υεμένη',' Καμερούν',' Ακτή Ελεφαντοστού ',' Μαδαγασκάρη',' Βόρεια Κορέα',' Αυστραλία',' Ταϊβάν ',' Νίγηρας',' Σρι Λάνκα',' Μπουρκίνα Φάσο',' Μάλι',' Χιλή',' Ρουμανία',' Καζακστάν',' Ζάμπια',' Μαλάουι',' Ισημερινός',' Συρία',' Ολλανδία',' Γουατεμάλα',' Καμπότζη',' Σενεγάλη',' Τσαντ',' Σομαλία',' Ζιμπάμπουε',' Ρουάντα',' Γουινέα',' Μπενίν',' Αϊτή',' Τυνησία',' Βολιβία',' Βέλγιο',' Μπουρούντι',' Νότιο Σουδάν',' Κούβα',' Τσεχία',' Ιορδανία',' Δομινικανή Δημοκρατία',' Σουηδία',' Πορτογαλία',' Αζερμπαϊτζάν',' Ηνωμένα Αραβικά Εμιράτα',' Ουγγαρία',' Λευκορωσία',' Τατζικιστάν',' Ονδούρα',' Ισραήλ',' Παπούα Νέα Γουινέα',' Αυστρία',' Ελβετία',' Σιέρα Λεόνε',' Τόγκο',' Χονγκ Κονγκ',' Λάος',' Παραγουάη',' Βουλγαρία',' Σερβία',' Λιβύη',' Λίβανος',' Νικαράγουα',' Κιργιζία',' Ελ Σαλβαδόρ',' Τουρκμενιστάν',' Δανία',' Σιγκαπούρη',' Φινλανδία',' Δημοκρατία του Κονγκό',' Σλοβακία',' Νορβηγία ',' Κόστα Ρίκα',' Λιβερία',' Κράτος της Παλαιστίνης',' Νέα Ζηλανδία',' Ιρλανδία',' Κεντροαφρικανική Δημοκρατία ',' Κουβέιτ',' Ομάν',' Παναμάς',' Μαυριτανία',' Κροατία',' Γεωργία',' Ερυθραία',' Ουρουγουάη',' Μογγολία',' Βοσνία και Ερζεγοβίνη',' Πουέρτο Ρίκο',' Αρμενία',' Αλβανία',' Λιθουανία',' Κατάρ',' Τζαμάικα',' Μολδαβία',' Ναμίμπια',' Γκάμπια',' Μποτσουάνα',' Γκαμπόν',' Λεσότο',' Σλοβενία',' Βόρεια Μακεδονία',' Λετονία',' Κόσοβο',' Μπαχρέιν',' Γουινέα-Μπισσάου',' Ισημερινή Γουινέα',' Τρινιντάντ και Τομπάγκο ',' Εσθονία',' Ανατολικό Τιμόρ',' Μαυρίκιος ',' Εσουατίνι',' Τζιμπουτί',' Κομόρες ',' Φίτζι',' Κύπρος',' Ρεϊνιόν',' Γουιάνα',' Μπουτάν',' Νήσοι Σολομώντα',' Μακάο',' Λουξεμβούργο',' Μαυροβούνιο',' Δυτική Σαχάρα',' Σουρινάμ',' Πράσινο Ακρωτήριο',' Μάλτα',' Υπερδνειστερία',' Μπρουνέι',' Μπελίζ',' Μπαχάμες',' Μαλδίβες',' Γουαδελούπη',' Ισλανδία',' Μαρτινίκα',' Γαλλική Γουιάνα',' Μαγιότ',' Γαλλική Πολυνησία',' Μπαρμπάντος',' Βανουάτου',' Νέα Καληδονία',' Αμπχαζία',' Σάο Τομέ και Πρίνσιπε',' Σαμόα',' Αγία Λουκία',' Γκουάμ',' Κουρασάο',' Αρούμπα',' Γρενάδα',' Άγιος Βικέντιος και Γρεναδίνες ',' Κιριμπάτι',' Τζέρσεϊ',' Αμερικανικές Παρθένοι Νήσοι',' Μικρονησία',' Τόνγκα',' Σεϋχέλλες',' Αντίγκουα και Μπαρμπούντα',' Νήσος του Μαν',' Ανδόρρα',' Δομινίκα',' Κέιμαν Νήσοι',' Βερμούδες',' Γκέρνσεϊ',' Γροιλανδία',' Αμερικανική Σαμόα',' Βόρειες Μαριάνες Νήσοι',' Νότια Οσσετία',' Νήσοι Μάρσαλ',' Άγιος Χριστόφορος και Νέβις',' Νήσοι Φερόες',' Τερκς και Κέικος',' Άγιος Μαρτίνος (Ολλανδία)',' Λίχτενσταϊν',' Μονακό',' Άγιος Μαρτίνος (Γαλλία)',' Γιβραλτάρ',' Άγιος Μαρίνος',' Βρετανικές Παρθένοι Νήσοι',' Παλάου',' Νήσοι Κουκ',' Ανγκουίλα',' Ουαλίς και Φουτουνά',' Τουβαλού',' Ναουρού',' Άγιος Βαρθολομαίος',' Σαιν Πιερ και Μικελόν',' Αγία Ελένη, Ασενσιόν και Τριστάν ντα Κούνια ',' Μοντσερράτ',' Νήσοι Φώκλαντ',' Νήσος των Χριστουγέννων',' Νησί Νόρφολκ',' Νιούε',' Τοκελάου',' Βατικανό',' Νησιά Κόκος']

#list of sources used in notebooks folder for the most_news_source.ipynb
delete_source = ['. Ο Λ','. Ο Γ',' Η Γ','8Κ - HDMI 2.1',' LED ',' ΠΗΓΗ',' 13.660 ',' comfort food E','. Η 16',' Ο Κ',' Covid-19',' C. Ε','triple-double',' Android ',' Alpha Bank',' ΗΠΑ',' Ahval',' This picture was taken last w',' Η Ο',' https']

#list of different names for "ΑΠΕ-ΜΠΕ"
ape_mpe_names = [' ΑΠΕ ΜΠΕ',' ΑΠΕ ΜΠΕ Γ',' ΑΠΕ-ΜΠΕ Δ',' ΑΠΕ-ΜΠΕ',' ΑΠΕ ',' ΑΠΕ-ΜΠΕ ',' ΑΠΕ']

#list of colors used to plot barchars in notebook folder 
years_colors = ['brown','saddlebrown','darkorange', 'darkolivegreen','green','mediumturquoise','deepskyblue','royalblue', 'blueviolet','orchid']

#list of colors used to plot barchars in notebook folder 
category_colors = ['darkred','green','mediumblue', 'orange','cyan','palevioletred','darkgoldenrod','pink', 'darkmagenta','steelblue']
pie_colors = [['darkorange','maroon'],['darkviolet','dodgerblue'],['darkorange','forestgreen'],['chocolate','darkolivegreen'],['lightskyblue','pink'],['turquoise','rebeccapurple'],['navy','lavender'],['rebeccapurple','palegoldenrod'],['mediumvioletred','dodgerblue'],['aqua','crimson']]
wordpopularity_colors = ['red','blue','orange','green','purple','brown','pink','gray','olive','cyan']

cleaned_output = '/Users/elenikaranikola/Desktop/NewsBackend/output.csv'

categories = ['World','Sport','Culture','Society','Economics','Environment','Politics','Tech','Food','Style']