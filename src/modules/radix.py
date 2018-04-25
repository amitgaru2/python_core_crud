'''
    Radix Sort
   	Best: Ω(nk)	Average:Θ(nk) Worst:O(nk)	Space:O(n+k)
'''   

class RadixSorting:

    # global bucket_ref
    # bucket_ref = {
    #                 '0':1, '1':2, '2':3, '3':4, '4':5, '5':6, '6':7, '7':8, '8':9, '9':10,
    #                 'a':11, 'b':12, 'c':13, 'd':14, 'e':15, 'f':16, 'g':17, 'h':18, 'i':19, 'j':20, 'k':21,
    #                 'l':22, 'm':23, 'n':24, 'o':25, 'p':26, 'q':27, 'r':28, 's':29, 't':30, 'u':31, 'v':32,
    #                 'w':33, 'x':34, 'y':35, 'z':36
    #              }   


    def __init__(self, result, sort_by):
        self.result = result
        self.sort_by = sort_by
        self.no_row = self.get_no_row()
        self.max_len = self.get_max_len()
        #print(self.max_len)
        

    def get_no_row(self):
        no_row = 0
        for row in self.result:
            no_row+=1
        return no_row
    

    def get_max_len(self):
        
        if self.sort_by == 0:
            max_id = 0
            for row in self.result:
                if max_id<row:
                    max_id = row
            return len(str(max_id))

        elif self.sort_by == 3:              # for phone no.xxxxxxxxxx
            return 13            # check the validator.py

        elif self.sort_by == 6:              # for gender
            return 1
        
        elif self.sort_by==5:       #dob
            return 8

        elif self.sort_by == 8:     # longitude latitude
            return 3
        
        elif self.sort_by == 9:
            return 2

        else:   
            max_len = 0
            for row in self.result:
                if (len(str(row[1]))>max_len):
                    max_len = len(str(row[1]))
            return max_len


    def sort_id(self,  **kwargs):
        bucket_ref = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[]
                      ]
            for n in range(self.no_row):
                number = str(self.result[n])
                if k>=len(number):                      # if the k preeceded the first digit of number then
                    buckets[0].append(self.result[n])        # append the tuple to 0 index 
                else:
                    indx = bucket_ref[number[len(number) - k - 1]]
                    buckets[indx].append(self.result[n])

            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)

    

    def sort_name(self):
        bucket_ref = {
                        'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10,
                        'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21,
                        'w':22, 'x':23, 'y':24, 'z':25
                     }
        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                        [],[],[],[],[],[],[],[],[],[],[],[]
                      ]
            for n in range(self.no_row):
                word = self.result[n][1].lower()
                if len(word)<(self.max_len - k):
                    buckets[0].append(self.result[n])
                else:
                    if word[self.max_len - k - 1] not in bucket_ref.keys():
                        indx = 26                     #same priority for all characters
                    else: indx = bucket_ref[word[self.max_len - k -1]]
                    buckets[indx].append(self.result[n])
            
            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)

    
    def sort_email_bio_address_media(self):
        bucket_ref = {
                        '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                        'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17, 'i':18, 'j':19, 'k':20,
                        'l':21, 'm':22, 'n':23, 'o':24, 'p':25, 'q':26, 'r':27, 's':28, 't':29, 'u':30, 'v':31,
                        'w':32, 'x':33, 'y':34, 'z':35
                     }

        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                        [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                        [],[],[],[],[],[],[]
                      ]
            for n in range(self.no_row):
                word = self.result[n][1].lower()
                if len(word)<(self.max_len - k):
                    buckets[0].append(self.result[n])
                else:
                    if word[self.max_len - k - 1] not in bucket_ref.keys():
                        indx = 36                     #same priority for all characters
                    else: indx = bucket_ref[word[self.max_len - k -1]]
                    buckets[indx].append(self.result[n])             # append the tuple of database row

            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)


    def sort_phone(self):
        bucket_ref = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[],[]
                      ]

            for n in range(self.no_row):
                number = str(self.result[n][1])
                if k>=len(number):                      # if the k preeceded the first digit of number then
                    buckets[0].append(self.result[n])        # append the tuple to 0 index 
                else:
                    if number[len(number)-k-1] not in bucket_ref.keys(): 
                        indx=10
                    else: 
                        indx = bucket_ref[number[len(number) - k - 1]]
                    buckets[indx].append(self.result[n])

            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)


    def sort_gender(self):
        bucket_ref = {'0':0,'1':1}

        for k in range(self.max_len):
            buckets = [ 
                        [],[],[]
                      ]

            for n in range(self.no_row):
                number = str(self.result[n][1])
                if k>=len(number):                      # if the k preeceded the first digit of number then
                    buckets[1].append(self.result[n])        # append the tuple to 0 index 
                else:
                   
                    if number[len(number)-k-1] not in bucket_ref.keys():
                        indx=2
                    else:
                        indx = bucket_ref[number[len(number) - k - 1]]
                    buckets[indx].append(self.result[n])

            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)
            


    def sort_long_lat(self):  #for id, phone, gender, longitude, latitude  
        bucket_ref = {
                        '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9  
                     }
        
        max_len_2 = 0
        for row in self.result:
            if '.' in row[1]:
                len_decimal_val = len(row[1].split('.')[1])
            else:
                len_decimal_val=0
            if(len_decimal_val>max_len_2):
                max_len_2 = len_decimal_val
        
        ### for decimal value
        for k in range(max_len_2):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[],[]
                      ]

            for n in range(self.no_row):
                if '.' in self.result[n][1]:
                    decimal = self.result[n][1].split('.')[1]
                else:
                    decimal = ''
                          
                if len(decimal)<(max_len_2 - k):
                    buckets[0].append(self.result[n])
                else:
                    if decimal[max_len_2 - k - 1] not in bucket_ref.keys():
                        indx = 10                     #same priority for all characters
                    else: 
                        indx = bucket_ref[decimal[max_len_2 - k -1]]
                    buckets[indx].append(self.result[n])             # append the tuple of database row

            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)
    

        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[],[]
                      ]

            for n in range(self.no_row):
                number = self.result[n][1].split('.')[0]
                if number.startswith('-'):
                    number = number[1:]
                if k>=len(number):                      # if the k preeceded the first digit of number then
                    buckets[0].append(self.result[n])        # append the tuple to 0 index 
                else:
                    if number[len(number)-k-1] not in bucket_ref.keys(): 
                        indx=11
                    else: 
                        indx = bucket_ref[number[len(number) - k - 1]]
                    buckets[indx].append(self.result[n])

            ## flat out the buckets back to new self.result list
            if k != (self.max_len - 1):     # dont loop at last
                self.result = []
                for buckt in buckets:
                    for row in buckt:
                        self.result.append(row)
        
        # rearrange all result such that -ve values are ahead of +ve values
        no_val_count = 0
        self.result = []
        for buckt in buckets:
            for row in buckt:
                if row[1] == '':
                    no_val_count+=1
                    self.result.append(row)
                elif row[1].startswith('-'):
                    self.result.insert(no_val_count, row)
                else:
                    self.result.append(row)

            
    def sort_dob(self):         # for dob
        bucket_ref = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        for k in range(self.max_len):
            buckets = [ 
                        [],[],[],[],[],[],[],[],[],[]
                      ]

            for n in range(self.no_row):
                date = str(self.result[n][1])
                
                if date=='':        # empty date
                    indx = 0
                else:
                    date = date.split('/')
                    number = date[2]+date[0]+date[1]     # mm/dd/yyyy -> yyyymmdd
                    #print(number, k)
                    indx = bucket_ref[number[len(number) - k - 1]]
                buckets[indx].append(self.result[n])
            
            ## flat out the buckets back to new self.result list
            self.result = []
            for buckt in buckets:
                for row in buckt:
                    self.result.append(row)
