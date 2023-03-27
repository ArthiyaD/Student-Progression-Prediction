#I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1898903

#Date: 16/04/2022


#STUDENT VERSION 
def input_student(level):
   '''Takes an input and validates it.Checks if the value is an integer,and if the value is in the range 0,20,40,60,80,100,120
   and returns the integer value.If the conditions are not satisified appropriate messages are printed and the input is prompted for again'''
   while True:
    try:
        credit=int(input(f'Enter your credits at {level}: '))
        if credit in range(0,121,20):
           return credit
        else:
           print ('Out of range     ')
    except ValueError:
        print ('Integer Required')
      

def progression_student(Pass,Defer,Fail):
     '''Prints the progression outcome based on the user's inputs for Pass, Fail and Defer. Prints "Total incorrect" if total is not equal to 120.'''
     if Pass+Fail+Defer!= 120:
        return ('Total incorrect')
     else:
        if Pass== 120:
            return ('Progess')
        elif Pass== 100:
            return ('Progress (module trailer)')
        elif Fail<= 60:
            return ('Module retriever')
        else:
            return ('Exclude')

   
         
#STAFF VERSON WITH HORIZONTAL AND VERTICAL HISTOGRAMS,LIST AND FILE MANIPULATION 
def input_staff(level):
   '''Takes an input and validates it.Checks if the value is an integer,and if the value is in the range 0,20,40,60,80,100,120
   and returns the integer value.If the conditions are not satisified appropriate messages are printed and the input is prompted for again'''
   while True:
    try:
        credit=int(input(f'Enter your total {level} credits: '))
        if credit in range(0,121,20):
           return credit
        else:
           print ('Out of range') 
    except ValueError:
        print ('Integer Required')


def progression_staff(Pass,Defer,Fail):
     '''Prints the progression outcome based on user inputs. Prints "Total incorrect" if total is not equal to 120.'''
     global progress
     global trailer
     global retriever
     global exclude
     global outcomes
   
     if Pass+Fail+Defer!=120:
         return ('Total incorrect')
     else:
         outcomes+=1
         if Pass== 120:
             progress+=1
             return ('Progress')
         elif Pass== 100:
             trailer=trailer+1
             return ('Progress (module trailer)')
         elif Fail<= 60:
             retriever=retriever+1
             return ('Module retriever')
         elif Fail>= 80:
             exclude+=1
             return ('Exclude')
     

         

def listofcredits(Pass,Defer,Fail):
         '''Stores the input progression data into a list[datalist], and writes the input progress data into a file '''
         global inputlist
         global datalist
         
         inputlist.append(Pass) #appending input credits into a list 
         inputlist.append(Defer)
         inputlist.append(Fail)
         Strof_input_progression=result +' - '+str(inputlist)[1:-1] #source-stackoverflow ([1:-1] removes the brackets[] from the list)
                                                                    #Strof_input_progression is the string concatination of the input and progress data
         datalist.append(Strof_input_progression) #appending the input, progression data into a list
         f.write(Strof_input_progression+'\n') #writing the input, progression data into a text file
         inputlist=[] #resets the list for the next set of inputs 
         
def Horizontal_Histogram():
     '''Builder for the horizontal histogram'''
     global progress
     global trailer
     global retriever
     global exclude
     global outcomes
   
     print('------------------------------------------------------------')
     print('HORIZONTAL HISTOGRAM')
     print(f'Progress   {progress} :', '*'*progress) #string multiplication
     print(f'Trailer    {trailer} :','*'*trailer)
     print(f'Retriever  {retriever} :','*'*retriever)
     print(f'Excluded   {exclude} :','*'*exclude,'\n')
     print(f'{outcomes} outcomes in total.')
     print('------------------------------------------------------------')
     
          
def Vertical_Histogram():
    '''Builder for the vertical histogram'''
    global progress
    global trailer
    global retriever
    global exclude
    global outcomes
    a='*'
    b=' '
    print('VERTICAL HISTOGRAM')
    print (f' Progress {progress} | Trailer {trailer} | Retriever {retriever} | Excluded {exclude} |')
    for row in range(max(progress,trailer,retriever,exclude)):  #source-python documentation (max)       
            if progress>0:
                 print(f'{a:>6} {b:>5}',end='')  #end="" makes sure cursor doesnt go to a new line after printing string.
                 progress-=1                     #{_:>_}= left alignment of strings 
            else:
                 print(f'{b:>12}',end='')
            if trailer>0:
                 print(f'{a:>6} {b:>5}',end='')
                 trailer-=1
            else:
                 print(f'{b:>12}',end='')
            if retriever>0:
                 print(f'{a:>7} {b:>6}',end='')
                 retriever-=1
            else:
                 print(f'{b:>14}',end='')
            if exclude>0:              #The cursor moves to the next line after this condition is executed
                 print(f'{a:>6} ')
                 exclude-=1
            else:
                 print (' ')         
            
    print (f'\n{outcomes} outcomes in total.')
    print('------------------------------------------------------------')


#MAIN PROGRAM    
while True:
   mode=input('''Enter;      
1 - STUDENT VERSION
2 - STAFF VERSION
3 - QUIT the program: ''')  #menu   
   if mode=='1': #part 01- student version
      print("STUDENT VERSION")
      result="Total incorrect"
      while result=="Total incorrect":
         Pass=input_student('pass')
         Defer=input_student('defer')
         Fail=input_student('fail')
         result=progression_student(Pass,Defer,Fail)
         print (result)
         
   elif mode=='2':
      print("STAFF VERSION")#part 02- staff version
      inputlist=[] #list used to store the input credits 
      datalist=[]  #list used to store input progression data for part 03
                   #the lists are reset for every new staff version
      f=open("ProgressionResults.txt",'w') #file opening for part 04 in write mode (contents are deleted everytime it's opened)
      progress=0
      trailer=0
      retriever=0
      exclude=0
      outcomes=0
      result=''
      option="y"
      while option=="y":
         Pass=input_staff('PASS')
         Defer=input_staff('DEFER')
         Fail=input_staff('FAIL')
         result=progression_staff(Pass,Defer,Fail)
         print (result)
         if result!="Total incorrect":
            listofcredits(Pass,Defer,Fail)
         while True:
            option=input('Would you like to enter another set of data?\nEnter "y" to continue and "q" to quit and view results: ')
            if option=="y":
               break
            elif option=="q":
               break
            else:
               print('Invalid input. Try again with "q" or "y"')
      f.close()
      Horizontal_Histogram()
      Vertical_Histogram()
      
      print("DATA FROM LIST")  #part 03
      for line in datalist:
         print (line)
      print('------------------------------------------------------------')

      print ("DATA FROM TEXT FILE")  #part 04
      with open('ProgressionResults.txt', 'r') as f:
         print(f.read())
      print('------------------------------------------------------------')

   elif mode=='3':
      break
   else:
      print('Invaild input. Try again with "1","2" or "3".')


   
