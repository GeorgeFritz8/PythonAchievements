begin = "Hallo! Mijn naam is George Fritz en ik ga vandaag een quiz houden over mijzelf."
begin2 = "De vragen staan hier onder. Selecteer A, B of C door de gekozen letter of het antwoord zelf in te typen."

print(begin)

print(begin2)
score = 0

# QUESTION 1
answer1 = input("-Waar woon ik?- \nA. Rotterdam \nB. Amsterdam \nC. rond de Bijlmer \nAnswer: ")
if answer1 == "B" or answer1 == "Amsterdam":
    score += 1
    print("Correct! Ik leef in Amsterdam aan de Amstel.")
    print("Score: ", score)
    print("\n")
else:
    print("Fout! Het antwoord was B. Amsterdam.")
    print("Score: ", score)
    print("\n")


# QUESTION 2
answer2 = input("-Hoe oud ben ik?- \nA. 17 \nB. 19 \nC. 16 \nAnswer: ")
if answer2 == "A" or answer2 == "17":
    score += 1
    print("Correct! Ik ben inderdaad 17! Ik ben Geboren op 28 Augustus dus ik was recent 17 geworden toen ik voor het eerst naar het MA ging")
    print("Score: ", score)
    print("\n")
else:
    print("Fout! Het antwoord was A. 17")
    print("Score: ", score)
    print("\n")

if score <= 1:
# QUESTION 2.5
  answer25 = input("-Wat is de naam van mijn hond?- \nA. Biggie \nB. Cheppie \nC. Charley \nAnswer: ")
  if answer25 == "C" or answer25 == "Charley":
    score += 1
    print("Correct! De naam van mijn hond is Charley. Cheppie was de naam van mijn vaders hond en Biggie was Charley's kennel naam")
    print("Score: ", score)
    print("\n")
  else:
    print("Fout! Het antwoord was C. Charley")
    print("Score: ", score)
    print("\n")

if score >= 2:
# QUESTION 3
  answer3 = input("-Op welke sport zit ik?- \nA. Voetbal \nB. Roeien \nC. Hockey \nAnswer: ")
  if answer3 == "B" or answer3 == "Roeien":
    score += 1
    print("Correct! Ik zit op roeien voor minimaal 4 jaar al. Ik train op de Willem III roeivereniging en doe vaak mee aan wedstrijden.")
    print("Score: ", score)
    print("\n")
  else:
    print("Fout! Het antwoord was B. Roeien.")
    print("Score: ", score)
    print("\n")

# FINAL MESSAGE
if score <= 1:
    print("Jou totale score is:", score, "- Volgende keer gaat het misschien beter!     Bedankt voor het maken van mijn quiz!")
elif score == 2:
    print("Jou totale score is:", score, "- Bijna perfect! Heel goed!     Bedankt voor het maken van mijn quiz!")
else:
    print("Jou totale score is:", score, "- Helemaal perfect! Je hebt alles goed!      Bedankt voor het maken van mijn quiz!")
