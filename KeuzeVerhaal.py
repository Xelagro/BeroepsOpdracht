import time 

#how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A Or B\n") 

#starting with "intro"
def intro():
  print("""Dit is een verhaal over een man die woont in Syrië en homo
seksueel is, nu is het aan jou de keuze wat jij gaat doen in het leven van
deze man. Veel plezier!
-------------------------------------------------------------------------------""")
  time.sleep(3)
  print ("""Je bent weer een dag verder, je word wakker en het is maandag ochtend.
Je bent laat wakker maar, je moet naar werk toe.
Toch denk je erover na thuis te blijven, 
Je hebt de keuze nu om thuis te blijven of naar werk te gaan:
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""  A. Je blijft Thuis
  B. Je gaat naar werk""")
  choice = input(">>> ") 
  if choice in answer_A:
    verhaal02()
  elif choice in answer_B:
    verhaal03()

  else:
    print (required)
    intro()

#VERHAAL 2 MET EEN EINDE
  
def verhaal02():
  print ("""Je word opgebeld door je baas.
Hij vraagt of je toch nog komt werken anders word je ontslagen."
Wat kies jij?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""  A. Je blijft nog steeds thuis
  B. Je gaat toch naar werk""")
  choice = input(">>> ") 
  if choice in answer_A:
    einde01()
  elif choice in answer_B:
    verhaal03()
  else:
    print (required)
    intro()

#VERHAAL 3 

def verhaal03():
  print("""Je bent te laat gekomen op je werk en hebt ruzie gekregen met je baas
Je bent eindelijk vandaag klaar met werken, je kan kiezen tussen
Naar je vriend gaan of naar huis.
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""  A. Je gaat naar je Vriend.
  B. Je gaat naar huis""")
  choice = input(">>> ") 
  if choice in answer_A:
    verhaal04()
  elif choice in answer_B:
    verhaal09()
  else:
    print (required)
    intro()


#VERHAAL 4 MET EEN EINDE

def verhaal04():
  print("""Je bent onderweg naar je vriend.
Onderweg kom je een bekende tegen, hij vraagt waar je naartoe gaat.
Lieg je? Of ben je eerlijk.
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""A. Je bent eerlijk
  B. Je liegt""")
  choice = input(">>> ")
  if choice in answer_A:
    einde02()
  elif choice in answer_B:
    verhaal05()
  else:
    print (required)
    intro()
    

# VERHAAL 5 

def verhaal05():
  print("""Je hebt gelogen, hij vertrouwd het niet maar laat het gaan
Je loopt verder richting je vriend en hebt een fijne avond.
De volgende dag worden jullie wakker door een luide explosie,
er is een bom ontploft en mensen zitten onder het puin.
Nu aan jou de keuze help je de mensen of negeer je het
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Je helpt de mensen.
  B. Je negeert het""")
  choice = input(">>> ")
  if choice in answer_A:
    verhaal06()
  elif choice in answer_B:
    verhaal09()
  else:
    print (required)
    intro()


# VERHAAL 6 

def verhaal06():
  print("""Je red 3 mensen die onder het puin zitten en kan voor de rest niemand horen.
Je besluit hun te vertrouwen samen met je vriend omdat je hebt gehoord
dat hun ook willen vluchten uit Syrië.
Ze hebben met ze 3 al een plan van aanpak, ga je met hun mee?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Je gaat met hun mee.
  B. Je gaat niet mee.""")
  choice = input (">>> ")
  if choice in answer_A:
    verhaal07()
  elif choice in answer_B:
    verhaal10() 
  else:
    print (required)
    intro()


# VERHAAL 7 solo meer

def verhaal07():
  print("""Jullie vertekken 29 September.
Fast Forward...
Jullie ontmoeten op de afgesproken locatie daarna worden jullie opgehaald.
Eenmaal bij de volgende dag...
Jullie zitten in de kleine bestel bus.
Er word gevraagd of jullie met de boot willen of met het vliegtuig willen
Wat kies jij?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Het vliegtuig.
  B. De boot.""")
  choice = input (">>> ")
  if choice in answer_A:
    verhaal08()
  elif choice in answer_B:
    einde03()
  else:
    print (required)
    intro()


# VERHAAL 8 solo meer edit nodig 
def verhaal08():
  print("""Jullie zijn veilig met het vliegtuig aangekomen in Turkije.
Het is nu het moment voor jullie om uit te rusten in een hotel.
Er word gevraagd of jullie willen uitrusten of door willen reizen
willen wachten om even rustig te worden.
Wat is jouw keuze?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Jullie gaan morgen mee.
B. Jullie rusten nog een extra dagje uit.""")
  choice = input (">>> ")
  if choice in answer_A:
    verhaal11()
  elif choice in answer_B:
    verhaal11()
  else:
    print (required)
    intro()


# VERHAAL 9 SOLO


def verhaal09():
  print("""Je bent naar huis gegaan en belt met je vriend.
Jullie zijn van plan samen te vluchten. En zijn aan het denken voor een datum
De datum is geprikt 29 September gaan jullie
Hoe regel je het geld?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Je steelt het.
B. Je werkt voor de aankomende tijd door.""")
  choice = input (">>> ")
  if choice in answer_A:
    verhaal07()
  elif choice in answer_B:
    verhaal07()
  else:
    print (required)
    intro()


# VERHAAL 10 GROEP

def verhaal10():
  print("""Jullie hebben gekozen niet mee te gaan en gaan zelf weg,
Er zijn 2 routes die jullie kunnen nemen.
De lange of de korte.
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Lange route
B. Korte route""")
  choice = input (">>>" )
  if choice in answer_A:
    verhaal09()
  elif choice in answer_B:
    verhaal07()
  else:
    print (required)
    intro()


# VERHAAL 11

def verhaal11():
 print("""Jullie komen aan in Nederland - Nijmegen,
jullie krijgen 7 dagen de tijd om uit te rusten van de reis.
Na 7 dagen..
Jullie gaan in gesprek met de IND
Zij stellen jullie vragen over waarom jullie zijn gevlucht
Benje eerlijk? Of ga je liegen
-------------------------------------------------------------------------------""")
 time.sleep(1)
 print("""A. Je liegt
B. Je bent eerlijk""")
 choice = input (">>>" )
 if choice in answer_A:
   einde04()
 elif choice in answer_B:
    verhaal12()
 else:
    print (required)
    intro()


# VERHAAL 12

def verhaal12():
  print("""Jullie hebben een verblijfs vergunning gekregen voor 5 jaar!
Nu mogen jullie samen een inburgerings examen hebben en dan mogen jullie
een huis hebben en trouwen!
Wat willen jullie eerst doen trouwen of een kind adopteren?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Trouwen
B. Een kind adopteren""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal14()
  elif choice in answer_B:
    verhaal13()
  else:
    print (required)
    intro()


#VERHAAL 13
    
def verhaal13():
  print("""Jullie hebben gekozen om als eerst een kind te adopteren,
Jullie mogen kiezen tussen een jongen of een meisje.
Wat willen jullie?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Meisje
B. Jongen""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal18()
  elif choice in answer_B:
    verhaal19()
  else:
    print (required)
    intro()


# VERHAAL 14

def verhaal14():
  print("""Jullie hebben gekozen om als eerst te trouwen!
Zouden jullie nog kinderen willen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Ja
B. Nee""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal15()
  elif choice in answer_B:
    goedEinde2()
  else:
    print (required)
    intro()


# VERHAAL 15

def verhaal15():
  print("""Jullie hebben gekozen om nog een kind bij het huwelijk te nemen!
Jullie kunnen nog kiezen tussen een meisje of een jongen!
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Meisje
B. Jongen""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal22()
  elif choice in answer_B:
    verhaal23()
  else:
    print (required)
    intro()

    


#VERHAAL 18 Non Married
def verhaal18():
  print("""Jullie hebben gekozen voor een meisje,
Hoe willen jullie haar noemen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Noor
B. Bibi""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal20()
  elif choice in answer_B:
      verhaal20()
  else:
    print (required)
    intro()


#VERHAAL 19 Non Married
def verhaal19():
  print("""Jullie hebben gekozen voor een jongen,
Hoe zouden jullie hem willen noemen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Rayan
B. Amir""")
  choice = input (">>>" )
  if choice in answer_A:
   verhaal20()
  elif choice in answer_B:
    verhaal20()
  else:
    print (required)
    intro()


#VERHAAL 23 Married
def verhaal23():
  print("""Jullie hebben gekozen voor een jongen,
Hoe zouden jullie hem willen noemen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Rayan
B. Amir""")
  choice = input (">>>" )
  if choice in answer_A:
     goedEinde1()
  elif choice in answer_B:
     goedEinde1()
  else:
    print (required)
    intro()



#VERHAAL 22 Married
def verhaal22():
  print("""Jullie hebben gekozen voor een meisje,
Hoe willen jullie haar noemen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Noor
B. Bibi""")
  choice = input (">>>" )
  if choice in answer_A:
      goedEinde1()
  elif choice in answer_B:
      goedEinde1()
  else:
    print (required)
    intro()


    
#VERHAAL 20
    
def verhaal20():
  print("""Jullie hebben nu een kind geadopteerd willen jullie nog trouwen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print("""A. Ja
B. Nee""")
  choice = input (">>>" )
  if choice in answer_A:
   goedEinde1()
  elif choice in answer_B:
    goedEinde3()
  else:
    print (required)
    intro()






#ALLE GOEDE EINDES

def goedEinde1():
  print("""Jullie zijn gelukkig getrouwd met een kind,
over 2 jaar zullen jullie weer opgeroepen te worden om te kijken
hoe de situatie is in jullie thuis land.
Dit was het einde van het verhaal ik hoop dat je hebt genoten!""")
  
def goedEinde2():
  print("""Jullie zijn gelukkig getrouwd maar hadden niet de behoefte om
een kind te adopteren. Over 2 jaar worden jullie opgeroepen om te kijken hoe
de situatie is in jullie thuis land.
Dit was het einde van het verhaal hoop dat je hebt genoten!""")

def goedEinde3():
  print("""Jullie hebben gekozen om niet te trouwen misschien later!
Maar hebben daarintegen wel een kind, over 2 jaar zullen jullie opgeroepen worden
om te kijken hoe de situatie in jullie thuis land is.
Dit was het einde van het verhaal ik hoop dat je hebt genoten!""")


  
#ALLE EINDES

def einde01():
  print("""Jammer genoeg ben je ontslagen van je baan en heb je
nu niet genoeg geld
voor verder te komen om te vluchten uit je land,
Dit is het einde.
Wilt u het opnieuw proberen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""A. Ja
B. Nee""")
  choice = input (">>> ")
  if choice in answer_A:
    intro()
  elif choice in answer_B:
    print ("""Dankjewel voor je deelname!""")
  else:
    print (required)
    intro()



def einde02():
  print("""Jammer genoeg is homo sexualiteit niet toegestaan in Syrië.
Je word verraden samen met je vriend en zitten nu samen in de gevangenis.
Wilt u het opnieuw proberen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""A. Ja
  B. Nee""")
  choice = input (">>> ")
  if choice in answer_A:
    intro()
  elif choice in answer_B:
    print ("""Dankjewel voor je deelname!""")
  else:
    print (required)
    intro()



def einde03():
  print("""Jammer genoeg is er een ongeluk gebeurt terwijl jullie aan het
varen waren en zijn jullie verdonken, degene die met het vliegtuig zijn gegaan
hebben het gered!
Wilje het opnieuw proberen??
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""A. Ja
  B. Nee""")
  choice = input (">>> ")
  if choice in answer_A:
    intro()
  elif choice in answer_B:
    print ("""Dankjewel voor je deelname!""")
  else:
    print (required)
    intro()



def einde04():
  print("""Jammer genoeg heeft u ervoor gekozen te liegen, hierdoor bent u terug gestuurd.
Nu bevind u zich weer in een gevaarlijke wereld waardoor u word gearresteerd en uw
vriend is verdwenen
Wil je het opnieuw proberen?
-------------------------------------------------------------------------------""")
  time.sleep(1)
  print ("""A. Ja
  B. Nee""")
  choice = input (">>> ")
  if choice in answer_A:
    intro
  elif choice in answer_B:
    print ("""Dankjewel voor je deelname!""")
  else:
    print (required)
    intro()


intro()
