from . import db_connect as db
import os

insert = db.Insert()
select = db.SelectAll()
select_by = db.SelectByKey()
show = db.MakeVisible()

def main():
    print('','-'*41,'\n|This is Lasses personal media collection!|\n','-'*41)
    while True:
        os.system('clear')
        print('Please make your choice to continue:')
        print("""
    Display:                  |Display all:               |Add:
        1 by genre            |   2 from main media       |   4 to main media
        1.1 by platform       |   2.1 from genre          |   4.1 to genre
        (1.2 by publisher)    |   2.2 from platform       |   4.2 to platform
        (1.3 by type of media)|   2.3 from type of media  |   4.3 to type of media
              
    To quit the programm just press ENTER
              """)
        
        choice = input('Enter your choice here: ')

        if choice == '1':
            os.system('clear')
            print('id\t| genre name\n','-'*25)
            for row in select.sel_from("genre;"):
                print(f'{row[0]}\t|{row[1]}')
            g_choice = int(input('Select the genre: '))
            print('name', '\t'*5,'|publisher\t',' |fsk ','|carrier|platform\n','-'*80)
            for row in select_by.genre_sel(g_choice):
                name = row[0] + ' '*(40 - len(row[0]))
                publisher = row[1] + ' '*(16 - len(row[1]))
                print(f'{name} |{publisher}|{row[2]}\t|{row[3]}\t|{row[4]}\t')
            input('\nEnter to continue')

        elif choice == '1.1':
            os.system('clear')
            print('Platform')
            for row in select.sel_from("platform;"):
                print(row[0])
            p_choice = input('Enter the selected platform here: ')
            os.system('clear')
            print('Input\t| Output\n','-'*25)
            for row in select_by.platform_def(p_choice):
                #print(f'{row[1]}\t|{row[2]}')
                print(row)
            print('name', '\t'*5,'|publisher\t',' |fsk ','|carrier|genre\n','-'*80)
            for row in select_by.platform_sel(p_choice):
                name = row[0] + ' '*(40 - len(row[0]))
                publisher = row[1] + ' '*(16 - len(row[1]))
                print(f'{name} |{publisher}|{row[2]}\t|{row[3]}\t|{row[4]}\t')
            input('\nEnter to continue')
            
        elif choice == '2':
            os.system('clear')
            print('id\t|name','\t'*5,'|type\t|genre\t|publisher','\t',' '*6,'|published_date\t|fsk\t|carrier|platform\n','-'*150)
            for row in select.sel_from("media;"):
                name = row[1] + ' '*(40 - len(row[1]))
                publisher = row[4] + ' '*(16 - len(row[4]))
                print(f'{row[0]}\t|{name}|{row[2]}\t|{row[3]}\t|{publisher}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
            input('Enter to continue')

        elif choice == '2.1':
            os.system('clear')
            print('id\t| genre name \t\t\t|\t describtion\n','-'*100)
            for row in select.sel_from("genre;"):
                g_name = row[1] + ' '*(15 - len(row[1]))
                print(f'{row[0]}\t|{g_name}\t\t|\t{row[2]},\n')
            input('Enter to continue')
        
        elif choice == '2.2':
            os.system('clear')
            print('platform|\tinput_hardware\t|\toutput_ardware\n','-'*100)
            for row in select.sel_from("platform;"):
                if len(row[1]) >= 16:
                    print(f'{row[0]}\t|{row[1]}\t| {row[2]}')
                    continue
                print(f'{row[0]}\t|{row[1]}\t\t| {row[2]}')
            input('Enter to continue')

        elif choice == '2.3':
            os.system('clear')
            print('type_id\t/\ttype_name\n')
            for row in select.sel_from("media_type;"):
                print(f'{row[0]}\t/\t{row[1]}')
            input('Enter to continue')

        elif choice == '3':
            os.system('clear')
            pass
        
        elif choice == '3.1':
            os.system('clear')
            pass
        
        elif choice == '3.2':
            os.system('clear')
            pass
        
        elif choice == '3.3':
            os.system('clear')
            pass
    
        elif choice == '4':
            os.system('clear')
            contend = ['name','type_id','genre_id','publisher(optional)','publishing_date YYYY/MM/DD(optional)','fsk','carrier_type','platform']
            data = []
            print('enter the required informations')

            for column in contend:

                if column == 'type_id':
                    for row in show.show_type():
                        print(row)
                    print('Take the related number!')
                elif column == 'genre_id':
                    for row in show.show_genre():
                        print(row)
                    print('Take the related number!')
                elif column == 'platform':
                    for row in show.show_platform():
                        print(row)
                    print('Take the matching platform!')

                n_d = input(f'Enter {column}: ')

                if column == 'type_id':
                    n_d = int(n_d)
                if column == 'genre_id':
                    n_d = int(n_d)
                if column == 'fsk':
                    n_d = int(n_d)

                data.append(n_d)
            insert.media_in(tuple(data))

        elif choice == '4.1':
            os.system('clear')
            contend = ['genre_name', 'describtion']
            data = []
            print('enter the required informations')
            
            for column in contend:
                n_d = input(f'Enter {column}: ')
                data.append(n_d)
            insert.genre_in(tuple(data))

        elif choice == '4.2':
            os.system('clear')
            contend = ['platform', 'input_hardware', 'output_hardware']
            data = []
            print('enter the required informations')

            for column in contend:
                n_d = input(f'Enter {column}: ')
                data.append(n_d)
            insert.platform_in(tuple(data))

        elif choice == '4.3':
            os.system('clear')
            n_d = input('Enter media type: ')
            insert.type_in((n_d,))
        
        elif choice == '':
            break

if __name__ == '__main__':
    main()