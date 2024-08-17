#Welcoming the User
print("Namaskar Deviyo aur Saajano ") 
print("Me Abhitabh Bacchan")
print("swagat karta hu aapka kaun banega crorepati me")

#Taking input of Name
hello = (input("Enter Your Name: "))
print("Kya aap taiyaar hai shuru karne ke liye...?")

#If user is ready or not
sambhav = (input("Enter Yes or No: "))

if (sambhav=='Yes'):
  print("Chaliye Shuru karte hain is khel ko Kaun Banega Crorepati")

#If user wants to know rules
sambhav2 = input("Kya Aap Prashan ke sahi jawab ke baad ke rupaye jaana chagenge..: ")

if (sambhav2=='Yes'):
  print("Dhyaan dei Phela Question 3500 rupaye ka hai")
  print("Dusara Question 10000 rupaye")
  print("Tisara Quesion 50000 rupaye ")
  print("Chautha Quesion 1 Lakh rupaye")
  print("Pachva Question 5 Lakh rupaye")
  print("Chata Quesion 20 Lakh rupaye")
  print("Satva Question 50 Lakh rupaye")
  print("Athwa Question 1 Crore rupaye")
  print("Nauwa Question 3.5 Crore rupaye")
  print("Aakhri Quesion 7 Crore rupaye")

else:
  print("Chaliye fhir Shuru karte hain...")

#Storage Area
Questions_List = ["Who wrote India's National Anthem? , Bharat ka Rastra Gaan kisne Likha ?" , "Which city is known as the Pink City of India ? , Konse Shahar ko Gulabi Shahar bola jata hai ?" , "How many major religions are there in India ? , Bharat me kul kitne dharm hain ? " , "When is the National Hindi Diwas celebrated ? , Rastriya Hindi Diwas kab manaya jata hai  ? " , "Who wrote Vande Mataram ? , Vande Matram kisne likha ? " , "Which one of the following places is famous for the Great Vishnu Temple ? , Inme se konsi jaga par mahan vishnu mandir stith hai ? " , "Which former Indian President died as a result of a road accident ? , Bharat ka konsa rastrapati ek sadak hadse me maare gaye ? " , "Who was the first Indian woman to win a medal in the Olympics ? , Olympics ke khel me kis mahila ne sabse phela sone ka medal jita ? " , "Taj Mahal was made of ? , Taj Mahal kis chig se bana hai ? " , "Who is the founder of the political party Dravida Munnetra Kazhagam (DMK) ? , Raajnitik dal dravid kadagam (DMK) ke sansthapak kaun hai ? "]

Answers_List = ["Rabindranath Tagore" , "Jaipur" , "6" , "14 September" , "Bankin Chandra Chaterjee" , "Ankorvat, Cambodia" , "Giani Zail Singh" , "Karnam Maleshwari" , "Marble" , "C.N. Annadurai"]

options = ["\n(A) Rabindranath Tagore \n(B) Lal Bahadur Shastri \n(C) Chetan Bhagat \n(D) RK Narayan " , "\n(A) Banglore \n(B) Maysore \n(C) Jaipur \n(D) Kochi" , "\n(A) 6 \n(B) 7 \n(C) 8 \n(D) 9" , "\n(A) 13 September \n(B) 14 September \n(C) 14 July \n(D) 15 August" , "\n(A) Sarat Chandra Chattopadhyay \n(B) Rabindranath Tagore \n(C) Bankim Chandra Chatterjee \n(D) Ishwar Chandra Vidyasagar" , "\n(A) Bordubar, Indonesia \n(B) Bamiya , Afganistan \n(C) Panja Sahib , Pakistan \n(D) Ankorvat , Cambodia" , "\n(A) Rajendra Prasad \n(B) Faqruddin Ali Ahmed \n(C) Giani Zail Singh  \n(D) R.Venkatraman" , "\n(A) P.T. Usha \n(B) Kunjarani Devi \n(C) Bachendri Pal \n(D) Karnam Maleshwari" , "\n(A) Brick \n(B) Marble \n(C) Granite \n(D) Sandstone" , "\n(A) C.N. Annadurai \n(B) M. Karunanidhi \n(C) M.G. Ramachandran \n(D) Jayalalitha" ]

reward = ["0", "3,500" , "10,000" , "50,000" , "1,00,000" , "5,00,000" , "20,00,000" , "50,00,000" , "1,00,00,000" , "3,50,00,000" , "7,00,00,000" ]

#start of KBC
print("Phela Prashan Aapki Screen par")

def Question_0():
  
  print(Questions_List[0])
  print(options[0])

  sambhav3 = (input("Enter Your Answer: "))
  
  if sambhav3=='Rabindranath Tagore':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[1], "ruyape")

  else:
    print("\nAapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[0] ,"rupaye")
    quit()
Question_0()
  
def Question_1():

  print(Questions_List[1])
  print(options[1])

  sambhav4 = (input("Enter Your Answer: "))

  if sambhav4=='Jaipur':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[1] ,"rupaye")
    quit()
Question_1()

def Question_2():

  print(Questions_List[2])
  print(options[2])

  sambhav5 = (input("Enter Your Answer: "))

  if sambhav5=='Jaipur':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[2] ,"rupaye")
    quit()
Question_2()

def Question_3():

  print(Questions_List[3])
  print(options[3])

  sambhav6 = (input("Enter Your Answer: "))

  if sambhav6==6:
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[2] ,"rupaye")
    quit()
Question_3()

def Question_4():

  print(Questions_List[4])
  print(options[4])

  sambhav7 = (input("Enter Your Answer: "))

  if sambhav7=='14 September':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[3] ,"rupaye")
    quit()
Question_4()

def Question_5():

  print(Questions_List[5])
  print(options[5])

  sambhav8 = (input("Enter Your Answer: "))

  if sambhav8=='Bankin Chandra Chaterjee':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[4] ,"rupaye")
    quit()
Question_5()

def Question_6():

  print(Questions_List[6])
  print(options[6])

  sambhav9 = (input("Enter Your Answer: "))

  if sambhav9=='Ankorvat,Cambodia' or sambhav9=='Ankorvat , Cambodia':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5]+reward[6], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[5] ,"rupaye")
    quit()
Question_6()

def Question_7():

  print(Questions_List[7])
  print(options[7])

  sambhav10 = (input("Enter Your Answer: "))

  if sambhav10=='Giani Zail Singh':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5]+reward[6]+reward[7], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[6] ,"rupaye")
    quit()
Question_7()

def Question_8():

  print(Questions_List[8])
  print(options[8])

  sambhav11 = (input("Enter Your Answer: "))

  if sambhav11=='Karnam Maleshwari':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5]+reward[6]+reward[7]+reward[8], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[7] ,"rupaye")
    quit()
Question_8()

def Question_9():

  print(Questions_List[9])
  print(options[9])

  sambhav12 = (input("Enter Your Answer: "))

  if sambhav12=='Marble':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5]+reward[6]+reward[7]+reward[8]+reward[9], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[8] ,"rupaye")
    quit()
Question_9()

def Question_10():

  print(Questions_List[10])
  print(options[10])

  sambhav13 = (input("Enter Your Answer: "))

  if sambhav13=='C.N. Annadurai' or sambhav13=='C.N Annadurai':
    print("Mubarak aapka jawab sahi hai aap jit te hain", reward[0]+reward[1]+reward[2]+reward[3]+reward[4]+reward[5]+reward[6]+reward[7]+reward[8]+reward[9]+reward[10], "ruyape")

  else:
    print("Aapka jawab galat hai aapka safar yahi khatam hota hai")
    print("Aap Total jit te hain", reward[9] ,"rupaye")
    quit()
Question_10()



  




