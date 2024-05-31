
#ระบบเลือกหนัง

print('----------------------------------')
print('List of movie in this week\n 1.The Nun \n 2.A Haunting in Venice\n 3.Transformers\n 4.Supparor')
print('----------------------------------')
movies = ['The Nun','A Haunting in Venice','Transformers','Supparor']

def time_movie():
  while True:
    try:
      time = int(input('Which time of movie do you want? (1-3) : '))
      print('----------------------------------')
      if 1 <= time <= 3:
        return time
      else:
        print('Try again, you must type (1-3)')
        print('----------------------------------')
        continue
    except ValueError:
      print('Try again, you must type (1-3)')
      print('----------------------------------')
      continue

while True:
  try:
    movie = int(input('Which movie do you want to watch? (1-4) : '))
    if movie == 1:
      print('----------------------------------')
      print('Movie time\n 1.10:30 - 12:30 \n 2.13:00 - 15:00 \n 3.17:30 - 20:00')
      print('----------------------------------')
      movies_1 = ['10:30 - 12:30','13:00 - 15:00','17:30 - 20:00']
      time = time_movie()
      break
    elif movie == 2:
      print('----------------------------------')
      print('Movie time\n 1.10:30 - 12:00 \n 2.13:30 - 15:30 \n 3.18:30 - 20:30')
      print('----------------------------------')
      movies_2 = ['10:30 - 12:00','13:30 - 15:30','18:30 - 20:30']
      time = time_movie()
      break
    elif movie == 3:
      print('----------------------------------')
      print('Movie time\n 1.10:30 - 12:30 \n 2.13:00 - 15:00 \n 3.17:30 - 20:00')
      print('----------------------------------')
      movies_3 = ['10:30 - 12:30','13:00 - 15:00','17:30 - 20:00']
      time = time_movie()
      break
    elif movie == 4:
      print('----------------------------------')
      print('Movie time\n 1.10:30 - 12:00 \n 2.13:30 - 15:30 \n 3.18:30 - 20:30')
      print('----------------------------------')
      movies_4 = ['10:30 - 12:00','13:30 - 15:30','18:30 - 20:30']
      time = time_movie()
      break
    else:
      print('Try again, you must type (1-4)')
      print('----------------------------------')
      continue
  except ValueError:
    print('Try again, you must type (1-4)')
    print('----------------------------------')
    continue
while True:
  try:
    nseat = int(input('How many seats do you want? (1-6) : '))
    if 1 <= nseat <= 6:
      break
    else:
      print('Try again, you must type (1-6)')
      print('----------------------------------')
  except ValueError:
    print('Try again, you must type (1-6)')
    print('----------------------------------')

#ระบบเลือกที่นั่ง

print('----------------------------------')
seating = []
for i in  range(7):
    row = []
    for j in range(6):
        row.append(f'{chr(65 + i)}{j + 1}')#f'{chr(65 + i) 
    seating.append(row)
for row in seating:
    print(' '.join(row))
print('----------------------------------')
totalseat = 0
allseat = []
for _ in range(nseat):
  while True:
    seatrow = input('Which seatrow? (A - G) (A - B = 200 Baht) : ').upper().strip()
    if seatrow in ['A','B']:
      totalseat += 200
      break
    elif seatrow in ['C','D','E','F','G']:
      totalseat += 180
      break
    else:
      print('Try again, you must type (A-G)')
      print('----------------------------------')
  while True:
    try:
      seatnum = int(input('Which seatnum? (1 - 6) : '))
      if 1 <= seatnum <= 6:
        if seatrow + str(seatnum) in allseat:
          print('Try again, you already book this seat')
          print("----------------------------------")
          continue
        allseat.append(seatrow + str(seatnum))
        break
      else:
        print('Try again, you must type (1-6)')
        print('----------------------------------')
        continue
    except ValueError:
     print('Try again, you must type (1-6)')
     print('----------------------------------')
     continue
if nseat >= 3:
  totalseat -= totalseat*3/100

#ระบบบัตรสมาชิก

while True:
  print('----------------------------------')
  member = input('Do you have member card? (Yes / No) : ').lower().strip()
  if member in ['yes','y']:
    totalseat -= totalseat*10/100
    break
  elif member in ['no','n']:
    break
  else:
    print('Try again, you must type (Yes / No)')
    print("----------------------------------")

#ระบบเลือกอาหาร

def popcorn_flavor():
  while True:
    try:
      flavor = int(input('Which flavor do you want? (1-5) : '))
      if 1 <= flavor <= 5:
        return flavor
      else:
        print('Try again, you must type (1-5)')
        print('----------------------------------')
        continue
    except ValueError:
      print('Try again, you must type (1-5)')
      print('----------------------------------')
      continue

totalfood = 0
allpopcorn = []
while True:
  print('----------------------------------')
  popcorn = input('Do you want popcorn? (Yes / No) : ').lower().strip()
  if popcorn in ['yes','y']:
    print('----------------------------------')
    print('1.set M (popcorn 46 Oz. + coke 22 Oz.) 150 baht\n2.set L (popcorn 64 Oz. + coke 32 Oz.) 200 baht \n3.set XL (popcorn 64 Oz. + coke(2) 32 Oz.) 300 baht')
    print('----------------------------------')
    while True:
      try:
        nset = int(input('How many set do you want? (1-4) : '))
        if 1 <= nset <= 4:
          break
        else:
          print('Try again, you must type (1-4)')
          print('----------------------------------')
          continue
      except ValueError:
        print('Try again, you must type (1-4)')
        print('----------------------------------')
        continue
    for _ in range(nset):
      while True:
        try:
          foodset = int(input('Which set do you want (1-3) : '))
          if 1 <= foodset <= 3:
            if foodset == 1:
              totalfood += 150
              popset = 'set M (popcorn 46 Oz. + coke 22 Oz.) 150 baht'
            elif foodset == 2:
              totalfood += 200
              popset = 'set L (popcorn 64 Oz. + coke 32 Oz.) 200 baht'
            elif foodset == 3:
              totalfood += 300
              popset = 'set XL (popcorn 64 Oz. + coke 32 Oz.) 300 baht'
            print('----------------------------------')
            print('Flavor of popcorn\n 1.Sweet \n 2.Salty\n 3.Cheese\n 4.Mala\n 5.Tomyum')
            print('----------------------------------')
            flavors = ['sweet', 'salty', 'cheese', 'mala', 'tomyum']
            flavor = popcorn_flavor()
            allpopcorn.append('{} and your flavor is {}.'.format(popset,flavors[flavor-1]))
            break
          else:
            print('Try again, you must type (1-3)')
            print('----------------------------------')
            continue
        except ValueError:
          print('Try again, you must type (1-3)')
          print('----------------------------------')
          continue
    break
  elif popcorn in ['no','n']:
    break
  else:
    print('Try again, you must type (Yes / No)')
    continue

#ระบบแสดงข้อมูล

print()
print("----------------------------------")
print()
print('Your movie is {}.'.format(movies[movie-1]))
if movie == 1:
  print(f'Your movie time is {movies_1[time-1]}.')
if movie == 2:
  print(f'Your movie time is {movies_2[time-1]}.')
if movie == 3:
  print(f'Your movie time is {movies_3[time-1]}.')
if movie == 4:
  print(f'Your movie time is {movies_4[time-1]}.')
if len(allseat) >= 2:
    seat_list = ' , '.join(allseat)
    print(f'Your seat = {seat_list}')
else:
    if len(allseat) == 1:
        print(f'Your seat = {allseat[0]}')
    else:
        print('No seat selected.')
print('Your total price is {} Baht.'.format('{:.2f}'.format(totalseat+totalfood)))
if popcorn in ['yes','y']:
  if len(allpopcorn) >= 2:
    print('Your popcorn set')
    for index,pops in enumerate(allpopcorn,1):
      print(f"{index}.{pops}")
  elif len(allpopcorn) == 1:
    for pop in allpopcorn:
      print(pop)
elif popcorn in ['no','n']:
  print("You didn't buy a popcorn set.")
print()
print("----------------------------------")