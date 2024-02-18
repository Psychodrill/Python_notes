
from datetime import datetime
def WorkWithNotes():
    choice = ShowMenu()
    #phonebook = ReadFile('phonebook.csv')
    while(choice!=7):
        notes = ReadFile('notes.csv')
        if(choice==1):
            PrintResult(notes)
        elif(choice==2):
            id=input('Input id: ')
            print(FindById(notes,id))
            input()
        elif(choice==3):
            id=input('Input id: ')
            text=input('Input new note text: ')
            print(EditNote(notes,id,text))
            input()
        elif(choice==4):
            id=input('Input id: ')
            DeleteById(notes,id)
            input()
        elif(choice==5):
            date=input('Input date: ')
            print(FindByDate(notes,date))
            input()
        elif(choice==6):
            name = input('Input note name: ')
            text = input('Input note text: ')
            noteData=name+","+text
            AddNote(notes, noteData)

        choice = ShowMenu()
        
def ShowMenu():
    print('1. Show all notes\n'
          '2. Show note by id\n'
          '3. Edit note by id\n'
          '4. Delete note\n'
          '5. Show notes by date\n'
          '6. Add note\n'
          '7. Exit', sep='\n')
    choice= int(input())
    return choice

def ReadFile(filename):
    notes = []
    fields=['Id', 'Name', 'Text', 'Date']
    with open (filename, 'r', encoding='utf8') as fileData:
        for line in fileData:
            record = dict(zip(fields, line.split(',')))
            notes.append(record)
    return notes

def WriteFile(filename, notes, isAdding):
    with open (filename, 'w', encoding='utf8') as fileData:
        for i in range(len(notes)):
            s=''
            for v in notes[i].values():
                s+=v+','
            fileData.write(f'{s[:-1]}')
        if(isAdding):
            fileData.write('\n')

def PrintResult(notes):
    for rec in notes:
        row=[]
        for v in rec.values():
            row.append(v)
        print(row)


def FindById(notes, id):
    result=[]
    for record in notes:
        for key in record:
            if  key=='Id' and record[key] ==id:
                result.append(record)
    return result

def FindByDate(notes, date):
    result=[]
    for record in notes:
        for key in record:
            if  key=='Date' and date in record[key]:
                result.append(record)
    return result

def EditNote(notes, id, text):
    record = FindById(notes,id)
    if(len(record)==1):
        record[0]['Text']=text
    elif(len(record)==0):
        print("Not founded records!")
    elif(len(record)>1):
        print("More than one record founded!")
    WriteFile('notes.csv', notes, False)
    return record

def DeleteById(notes,id):
    record = FindById(notes,id)
    for item in record:
        notes.remove(item)
    WriteFile('notes.csv', notes, False)

def AddNote(notes, noteData):
    if(len(notes)==0):
        id = str(len(notes))
    else:
        id=str(int(notes[len(notes)-1]['Id'])+1)
    currentDate = datetime.now()
    date = currentDate.strftime("%m-%d-%Y")
    values =noteData.split(",")
    values.insert(0,id)
    values.append(date)
    keys = ['Id', 'Name', 'Text', 'Date']
    newRecord = dict(zip(keys,values))
    notes.append(newRecord)
    WriteFile('notes.csv', notes, True)

WorkWithNotes()