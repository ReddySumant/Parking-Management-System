import mysql.connector
import time
from datetime import date,datetime
import matplotlib.pyplot as plt


global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database=' parking_system', user='root', password='Mauli@123')
cursor = conn.cursor()


def clear():
  for _ in range(65):
     print()

def percentage(a,b):
    result = (a/b)*100
    return round(result,2)

#-----------------------------------------------------------------------------------------------------------------------------------------

def login():
    while True:
        clear()
        print('-'*100)
        print(' L o G I N    O P T I O N S  ')
        print('-'*100)
        print('1.  Administration Login \n')
        print('2.  Employee Login  \n')

        choice = int(input('Enter your choice :'))
        if choice == 1:
            while True:
                uname = input('Enter your administrator id :')
                upass = input('Enter your administrator Password :')
                cursor.execute('select * from adminlogin where name="{}" and pwd ="{}"'.format(uname,upass))
                cursor.fetchall()
                rows = cursor.rowcount
                if rows!=1:
                    print('Invalid Login details..... Try again')
                    clear()
                else:
                    print('You are eligible for operating this system............')
                    print('\n\n\n')
                    main_admin()
                    break

        if choice == 2:
            while True:
                uname = input('Enter your employee id :')
                upass = input('Enter your employee Password :')
                cursor.execute('select * from emplogin where name="{}" and pwd ="{}"'.format(uname,upass))
                cursor.fetchall()
                rows = cursor.rowcount
                if rows!=1:
                    print('Invalid Login details..... Try again')
                    clear()
                else:
                    print('You are eligible for operating this system............')
                    print('\n\n\n')
                    print('Press any key to continue...............')
                    main_employee()
                    break

#-----------------------------------------------------------------------------------------------------------------------------------------

def add_new_vehicle():
    clear()
    print('Vehicle Login Screen ')
    print('-'*100)
    vehicle_id = input('Enter Vehicle Number :' )
    parking_id = input('Enter parking ID :')
    entry_date = date.today()
    entry_time = datetime.now.strftime("%H:%M:%S")
    sql = 'insert into transaction(vehicle_id,parking_id,entry_date,entry_time) values \
           ("{}","{}","{}","{}");'.format(vehicle_id,parking_id,entry_date,entry_time)
    cursor.execute(sql)
    cursor.execute('update parking_space set status ="full" where id ={}'.format(parking_id))
    print('\n\n\n Record added successfully.................')
    wait= input('\n\n\nPress any key to continue.....')


def remove_vehicle():
    clear()
    print('Vehicle Logout Screen')
    print('-'*100)
    vehicle_id = input('Enter vehicle No :')
    exit_date = date.today()
    exit_time = datetime.now.strftime("%H:%M:%S")
    sql = 'select parking_id,price,entry_date from transaction tr,parking_space ps, parking_type pt \
           where tr.parking_id = ps.id and ps.type_id = pt.id and \
           vehicle_id ="'+vehicle_id+'" and exit_date is NULL;'
    cursor.execute(sql)
    record = cursor.fetchone()
    days = (exit_date-record[2]).days 
    if days ==0:
        days = days+1
    amount = record[1]*days
    clear()
    print('Logout Details ')
    print('-'*100)
    print('Parking ID : {}'.format(record[0]))
    print('Vehicle ID : {}'.format(vehicle_id))
    print('Login Date : {}'.format(record[2]))
    print('Login Time : {}'.format(record[3]))
    print('Logout Date : {}'.format(exit_date))
    print('Logout Date : {}'.format(exit_time))
    print('Amount Payable : {}'.format(amount))
    wait = input('press any key to continue......')
    # update transaction and parking space tables
    sql1 = 'update transaction set exit_date ="{}", exit_time ="{}", amount ={} where vehicle_id ="{}" \
            and exit_date is NULL;'.format(exit_date, exit_time, amount, vehicle_id)
    sql2 =  'update parking_space set status ="open" where id = {}'.format(record[0])
    cursor.execute(sql1)
    cursor.execute(sql2)
    wait = input('Vehicle Out from our System Successfully.......\n Press any key to continue....')

#-----------------------------------------------------------------------------------------------------------------------------------------

def display_parking_type_records():
    cursor.execute('select * from parking_type;')
    records = cursor.fetchall()
    for row in records:
        print(row)

def search_menu():
    clear()
    print(' S E A R C H  P A R K I N G  M E N U ')
    print('1.  Parking ID \n')
    print('2.  Vehicle Parked  \n')
    print('3.  Free Space \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'id'
    if choice == 2:
        field = 'vehicle No'
    if choice == 3:
        field = 'status'
    value = input('Enter value to search :')

    if choice == 1 or choice==3:
        sql = 'select ps.id,name,price, status \
          from parking_space ps , parking_type pt where ps.id = pt.id AND ps.id ={}'.format(value)
    else:
        sql = 'select id,vehicle_id,parking_id,entry_date from transaction where exit_date is NULL;'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    for row in results:
        print(row)
    if records < 1:
        print('Record not found \n\n\n ')
    wait = input('\n\n\nPress any key to continue......')

def parking_status(status):
    clear()
    print('Parking Status :',status)
    print('-'*100)
    sql ="select * from parking_space where status ='{}'".format(status)
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    wait =input('\n\n\nPress any key to continue.....')

def vehicle_status_report():
    clear()
    print('Vehicle Status - Currently Parked')
    print('-'*100)
    sql='select * from transaction where exit_date is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    wait =input('\n\n\nPress any key to continue.....')

#-----------------------------------------------------------------------------------------------------------------------------------------

def add_parking_type_record():
    clear()
    name = input('Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck 5. Trolly ) : ')
    price =  input('Enter Parking Price per day : ')
    sql = 'insert into parking_type(name,price) values("{}",{});'.format(name,price)
    cursor.execute(sql)
    print('\n\n New Parking Type added....')
    cursor.execute('select max(id) from parking_type')
    no = cursor.fetchone()
    print(' New Parking Type ID is : {} \n\n\n'.format(no[0]))
    wait= input('\n\n\nPress any key to continue............')


def add_parking_slot_record():
    clear()
    parking_type_id = input(
        'Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck 5. Trolly ) :')
    status = input('Enter current Status ( Open/Full ) :')
    sql = 'insert into parking_space(type_id,status) values \
            ("{}","{}");'.format(parking_type_id,status) 
    cursor.execute(sql)
    print('\n\n New Parking Space Record added....')

    cursor.execute('select max(id) from parking_space;')
    no = cursor.fetchone()
    print(' Your Parking ID is : {} \n\n\n'.format(no[0]))
    display_parking_type_records()
    wait = input('\n\n\nPress any key to continue............')


def modify_parking_type_record():
    clear()
    print(' M O D I F Y   P A R K I N G   T Y P E  S C R E E N ')
    print('-'*100)
    print('1.  Parking Type Name \n')
    print('2.  Parking Price  \n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice==1:
        field='name'
    if choice==2:
        field='price'
    
    park_id = input('Enter Parking Type ID :')
    value = input('Enter new values :')
    sql = 'update parking_type set '+ field +' = "' + value +'" where id ='+ park_id +';'
    cursor.execute(sql)
    print('Record updated successfully................')
    display_parking_type_records()
    wait = input('\n\n\nPress any key to continue............')


def modify_parking_space_record():
    clear()
    print(' M O D I F Y  P A R K I N G   S P A C E   R E C O R D ')
    print('-'*100)
    print('1.  Parking Type ID(1-Two Wheelar, 2: Car 3.Bus etc ):  ')
    print('2.  status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'type_id'
    if choice ==2:
        field = 'status'
    print('\n\n\n')
    crime_id = input('Enter Parking Space ID  :')
    value = input('Enter new values :')
    sql = 'update parking_space set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    cursor.execute(sql)
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')

#-----------------------------------------------------------------------------------------------------------------------------------------

def money_collected():
    clear()
    start_date = input('Enter start Date(yyyy-mm-dd): ')
    end_date = input('Enter End Date(yyyy-mm-dd): ')

    sql = "select sum(amount) from transaction where \
            exit_date between '{}' and '{}';".format(start_date,end_date)
    cursor.execute(sql)
    result = cursor.fetchone()

    print('Total money Collected from {} to {}'.format(start_date,end_date))
    print('-'*100)
    print(result[0])

    sql = "SELECT COUNT(*) FROM parking_type;"
    cursor.execute(sql)
    r = cursor.fetchone()
    count = int(r[0])

    percent = []
    Labels = []

    print('-'*100)
    print('\n\n\n')

    for i in range(1,count+1):
        sql = "SELECT sum(transaction.amount) FROM parking_space INNER JOIN transaction ON parking_space.id = transaction.parking_id where (exit_date between '{}' and '{}' ) and type_id = {}; ".format(start_date, end_date, i)
        cursor.execute(sql)
        result1 = cursor.fetchone()
        if result1[0] == None:
            resultf = 0
        else:
            resultf = result1[0]
        per = percentage(int(resultf),int(result[0]))
        percent.append(per)

        sql = "SELECT name FROM parking_type where id = {};".format(i)
        cursor.execute(sql)
        result2 = cursor.fetchone()
        name = result2[0]
        Labels.append(name)

        print('Total money Collected from {} to {} by {} is {}rs'.format(start_date,end_date,name,resultf))
        print('Percentage Revenue by {} is {}% of total'.format(name,per))
        print('-'*20)
    print('-'*100)

    labels = Labels
    colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred','gold','pink','brown']
    patches, texts = plt.pie(percent, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Total Revenue in %')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------
        
def report_menu():
    while True:
        clear()
        print(' P A R K I N G    R E P O R T S  ')
        print('-'*100)
        print('1.  Parking Types \n')
        print('2.  Free Space  \n')
        print('3.  Ocupied Space  \n')
        print('4.  Vehicle Status  \n')
        print('5.  Money Collected  \n')
        print('6.  Exit  \n')
        choice = int(input('Enter your choice :'))
        field = ''
        if choice == 1:
            display_parking_type_records()
        if choice == 2:
            parking_status("open")
        if choice == 3:
            parking_status("full")
        if choice == 4:
            vehicle_status_report()
        if choice == 5:
            money_collected()
        if choice ==6: 
            break
        

def main_admin():  
    while True:
      clear()
      print(' P A R K I N G   M A N A G E M E N T    S Y S T E M  ( A D M I N )')
      print('*'*100)
      print("\n1.  Add New Parking Type")
      print("\n2.  Add New Parking Slot")
      print('\n3.  Modify Parking Type Record')
      print('\n4.  Modify Parking Slot Record')
      print('\n5.  Report menu')
      print('\n6.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_parking_type_record()

      if choice == 2:
        add_parking_slot_record()

      if choice == 3:
        modify_parking_type_record()
      
      if choice == 4:
        modify_parking_space_record()
      
      if choice == 5:
        report_menu()
      
      if choice == 6:
        break

def main_employee():
    while True:
        clear()
        print(' P A R K I N G   M A N A G E M E N T    S Y S T E M  ( E M P L O Y E E )')
        print('*'*100)
        print('\n1.  Vehicle Login ')
        print('\n2.  Vehicle Logout')
        print('\n3.  Free Space  \n')
        print('\n4.  Ocupied Space  \n')
        print('\n5.  Search menu')
        print('\n6.  Close application')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))

        if choice == 1:
            add_new_vehicle()
      
        if choice == 2:
            remove_vehicle()

        if choice == 3:
            parking_status("open")
      
        if choice == 4:
            parking_status("full")

        if choice == 5:
            search_menu()

        if choice == 6:
            break

#-----------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    clear()
    msg = '''
    W E L C O M E  T O  P A R K I N G  M A N A G E M E N T  S Y S T E M

    
    P L E A S E  L O G I N  T O  C O N T I N U E :
    '''
    for x in msg:
        print(x, end='')
        time.sleep(0.0001)

    login()
