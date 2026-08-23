from cryptocode import encrypt,decrypt
import pickle
import secrets
import pwinput

pwd = '''


 ______   __     __     _____    
/\  == \ /\ \  _ \ \   /\  __-.  
\ \  _-/ \ \ \/ ".\ \  \ \ \/\ \ 
 \ \_\    \ \__/".~\_\  \ \____- 
  \/_/     \/_/   \/_/   \/____/ 


                                 
'''

#pwd = pwd.replace('@','*')

#functions
def write_dict(dict , file = 'password'):
    file = open(file,'wb')
    pickle.dump(dict,file)
    file.close()

def load_file(file = 'password'):
    file = open(file,'rb')
    loaded_file = pickle.load(file)
    file.close()
    return loaded_file

#write_dict({})
file_dict = load_file()

#PWD
help_dict = {'USERS':'See Users[No access]','REMOVE':'Remove Users[No access]','LOGIN':'Create Users or Login in to Existing User[No access]','STATUS':'Displays Access permission[No access]','EXIT':'Exit terminal[No access]','NEW':'Adds new value[access Required]','DELETE':'Delete value[access Required]','MODIFY':'Modify value[access Required]','ADDCOLUMN':'Add new column to value[acess Required]','TOKEN':'Generate a key/password[access Required]','VIEWPW':'View Password for specified column[access Required]'}
keys = {'no access':['HELP','USERS','REMOVE','LOGIN','EXIT','STATUS'],'access':['ADDCOLUMN','NEW','VIEW','MODIFY','DELETE','TOKEN','VIEWPW']}
status = {'access':False}
access = False
user = '?'
user_no = 1
encrypt_list = ['Password']
print(pwd)
key = 'pwd'
while True:

    print('#========================================#')
    key = input( '[ ' + user + ' ]~~>').strip().upper()
    print()
    if access == False:
        if key not in keys['no access']:
            print('    Invalid Command')
    else:
        if key not in keys['no access'] and key not in keys['access']:
            print('    Invalid Command')
        
    #print(load_file())

    if key == 'HELP':
        for help_key in help_dict.keys():
            print(help_key + ':' + help_dict[help_key])
    
    user_no = 1
    if key == 'USERS':
        for dict_key in file_dict.keys():
            print('    ' + str(user_no) + '. ' + dict_key)
            user_no += 1
        if user_no == 1:
            print('     No Users Found')

    if key == 'REMOVE':
        user_temp = input('    Enter Username: ')
        master_pwd_temp = pwinput.pwinput('    Enter Master Password: ')
        if user_temp in file_dict.keys():
            if not(decrypt(file_dict[user_temp]['User'],master_pwd_temp)):
                print('        Unsuccessful Attempt - Password Incorrect')
                continue
            else:
                access = False
                status['access'] = False
                del file_dict[user_temp]
                print('        Deleted ' + user_temp)
                user = '?'
                del user_temp
                master_pwd = ''
                del master_pwd_temp
                write_dict(file_dict)
        else:
            print('        ' + user_temp +' Does not exist')
        
    if key=='LOGIN':
        user_temp = input('    Enter Username: ')
        master_pwd_temp = pwinput.pwinput('    Enter Master Password: ')
        if user_temp in file_dict.keys():
            if not(decrypt(file_dict[user_temp]['User'],master_pwd_temp)):
                print('        Unsuccessful Attempt - Password Incorrect')
                access = False
                continue
            else:
                user = user_temp
                del user_temp
                master_pwd = master_pwd_temp
                del master_pwd_temp
                print('        Logged in ' + user)
                
        else:
            user = user_temp
            del user_temp
            master_pwd = master_pwd_temp
            del master_pwd_temp
            file_dict.update({user:{'User':encrypt(user,master_pwd),'Application':[],'Account':[],'Password':[]}})
            write_dict(file_dict)
            print('        Created user ' + user)

    if key == 'EXIT':
        break

    if key == 'STATUS':
        for stat in status.keys():
            print(stat,':',status[stat])
        
    if user in file_dict.keys():
        access = True
        status['access'] = True
        
    if access == True:
        
        if key == 'ADDCOLUMN':
            column = input('    Enter Column Name: ')
            file_dict[user].update({column:[]})
            for i in  range(len(file_dict[user]['Application'])):
                file_dict[user][column].append('NONE')
            write_dict(file_dict)

        if key=='NEW':
            for key in file_dict[user].keys():
                if key != 'User':
                    if key in encrypt_list:
                        file_dict[user][key].append(encrypt(pwinput.pwinput('    Enter ' + key + ': '),master_pwd))
                    else:
                        file_dict[user][key].append(input('    Enter ' + key + ': '))
                write_dict(file_dict)
            print('        Successfully created New Record')

        if key == 'VIEW':
            print('    ',end='')
            for key in file_dict[user].keys():
                if key == 'User':
                    key = 'Sl NO.'
                print(key,end = 10*' ')
            print()
            for i in range(len(file_dict[user]['Application'])):
                for key in file_dict[user].keys():
                    if key == 'User':
                        print('    ',i + 1,end = (10-len(str(i+1)))*' ')
                    elif decrypt(file_dict[user][key][i],master_pwd):
                        print('    ',end = '  ')
                    else:
                        print('    ',file_dict[user][key][i],end = (16-len(str(file_dict[user][key][i])))*' ')
                print()

        if key == 'VIEWPW':
            modify_no = input('    Enter the Sl NO. to view Password: ')
            try:
                modify_no = int(modify_no) - 1
            except:
                print('        Enter Integer Only!')
                continue
            if modify_no < len(file_dict[user]['Application']):
                key_element = 'Password'
                if key_element in file_dict[user].keys():
                    if key_element in encrypt_list:
                        print('Password: ',decrypt(file_dict[user][key_element][modify_no],master_pwd))


        if key == 'DELETE':
            delete_no = input('    Enter the Sl NO. to be Deleted: ')
            try:
                delete_no = int(delete_no) - 1
            except:
                print('        Enter Integer Only!')
                continue
            if delete_no < len(file_dict[user]['Application']):
                for key in file_dict[user].keys():
                    if key != 'User':
                        del file_dict[user][key][delete_no]
                write_dict(file_dict)
                print('        Deleted Successfully')
            else:
                print('        Given Sl NO. is greater than the NO. of Elements contained')

        if key == 'MODIFY':
            modify_no = input('    Enter the Sl NO. to be Modified: ')
            try:
                modify_no = int(modify_no) - 1
            except:
                print('        Enter Integer Only!')
                continue
            if modify_no < len(file_dict[user]['Application']):
                key_element = input('    Enter the Column Name: ')
                if key_element in file_dict[user].keys():
                    if key_element in encrypt_list:
                        file_dict[user][key_element][modify_no] = encrypt(pwinput.pwinput('    Modify '+decrypt(file_dict[user][key_element][modify_no],master_pwd)+' to: '),master_pwd)
                    else:
                        file_dict[user][key_element][modify_no] = input('    Modify '+str(file_dict[user][key_element][modify_no])+' to: ')
                    write_dict(file_dict)
                    print('        Modified Successfully')
                else:
                    print('        Given Column does not Exist')
            else:
                print('        Given Sl NO. is greater than the NO. of Elements contained')

        if key=="TOKEN":
            length = input('    Enter length of generating Password: ')
            try:
                print('Password: ',secrets.token_urlsafe(int(length)))                
            except:
                print('        Enter Integer Only!')