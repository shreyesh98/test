bank = {
    'A': {'customer_name': 'Alice', 'balance': 5000.0},
    'B': {'customer_name': 'Bob', 'balance': 800.0},
    'C': {'customer_name': 'Charlie', 'balance': 12000.0},
}


def open():
  a = input('enter account initial ').upper()
  if a not in bank:
    print('account not found')
    b = input('do you want to open account ')
    while True:
      if b == 'yes':
        n = input('enter initial ').upper()
        name = input('enter name ').capitalize()
        amt = float(input('enter val '))
        bank[n] = {'customer_name':name,'balance': amt} 
        b = input('do you want to open another account ')
      elif b == 'no':
        print('thank you visit again')
        break

def operation():
  a = input('enter account initial ').upper()
  if a in bank:
    f = input('enter deposit/withdraw or exit ')
    while True:
      if f == 'deposit':
        g = float(input('enter amt to deposit '))
        o = bank[a]['balance'] + g
        p = round(o, 2)
        bank[a]['balance'] = p
        print(bank[a])
        f = input('enter another deposit/withdraw or exit ')
      elif f == 'withdraw':
        g = float(input('enter amt to withdraw '))
        if bank[a]['balance'] >= g:
          o = bank[a]['balance'] - g
          p = round(o, 2)
          bank[a]['balance'] = p
          print(bank[a])
          f = input('enter another deposit/withdraw or exit ')
        else:
          print(f'{bank[a]['balance']} not sufficient funds')
      elif f == 'exit':
        break
      else: 
        f = input('enter another deposit/withdraw or exit ')

def close():
  c = input('do you want to close account ')

  if c =='yes':
    d = input('enter account to close ').upper()
    bank.pop(d)
  else:
    print('its ok bud come again') 
 
    
def sbi():
  z = input('enter open/operation/close/exit ')
  while True: 
    if z == 'open':
      open()
      z = input('enter open/operation/close/exit ')
    elif z == 'operation':
      operation()
      z = input('enter open/operation/close/exit ')
    elif z == 'close':
      close()
      z = input('enter open/operation/close/exit ')
    elif z == 'exit':
      print(bank)
      break
    
sbi() 
