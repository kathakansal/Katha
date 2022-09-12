while True:
    a = int(input('ENTER A NUMBER: '))
    try:
        print(100/a)
        break
    except:
        print('not divisible by 100')
    finally:
        print('end of program')
  
