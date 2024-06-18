print(len('Science Fiction'))

# elif choice == '2':
#             os.system('clear')
#             print('id\t|name\t|type_id|genre_id|publisher\t|publishing_date\t|fsk\t|carrier_type\t|platform\n','-'*100)
#             for row in select.sel_from("media;"):
#                 if len(row[1]) < 16:
#                     print(f'{row[0]}\t|{row[1]}\t\t\t\t|{row[2]}\t|{row[3]}\t|{row[4]}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
#                 elif len(row[1]) < 24:
#                     print(f'{row[0]}\t|{row[1]}\t\t\t|{row[2]}\t|{row[3]}\t|{row[4]}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
#                 elif len(row[1]) < 30:
#                     print(f'{row[0]}\t|{row[1]}\t\t|{row[2]}\t|{row[3]}\t|{row[4]}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
#                 elif len(row[1]) < 36:
#                     print(f'{row[0]}\t|{row[1]}\t|{row[2]}\t|{row[3]}\t|{row[4]}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
#                 else:
#                     print(f'{row[0]}\t|{row[1]}|{row[2]}\t|{row[3]}\t|{row[4]}\t|{row[5]}\t|{row[6]}\t|{row[7]}\t|{row[8]}')
#             input('Enter to continue')