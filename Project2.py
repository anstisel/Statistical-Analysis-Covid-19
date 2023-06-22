"""Project2.py
A program to conduct a statistical analysis on COVID-19 cases
by: Elisha Anstiss """
def main(csvfile):
    if type(csvfile) is not str: #terminate gracefully if invalid inputs given
        print("Invalid input")
        return None
    try:
        infile= open(csvfile, "r", encoding='latin-1')
    except FileNotFoundError: 
        print("The file", csvfile ,"was not found.") 
        return None
    except IOError: 
        print("The file", csvfile, "cannot be opened")
        return None
    
    fileread = infile.read()
    filelines = fileread.split("\n") 
    data = []  #create empty list to input the filelines
    
    for line in filelines[1:-1]: #-1 removes last index out of range
        values = line.split(",")
        data.append(values)
   
    headers = {} 
    for (key,value) in enumerate(filelines[0].split(',')): #goes through headers and keeps index
        headers[value] = key #make dictionary of header strings and their index point
    
    needlist= ["continent", "location", "date", "new_cases", "new_deaths"] #required columns
    for i in needlist:
        if i not in headers: 
            print("Needed column not found")
            return None
   
    countrylist = [] #create list of all countries
    continentlist = [] #create list of all continents
    for line in data:
        continentlist.append(line[headers["continent"]].lower()) #test cases keeps continent
        #uncomment  next section to ensure world country not included
        #if len(line[1]) < 1:
            #continue 
        countrylist.append(line[headers["location"]].lower())
        
    countrylist = set([i for i in (countrylist) if i != '']) #set removes duplicate countries
    continentlist = set((continentlist)) #remove duplicate continents, keep testing answer ''
    
    dict_country = {} #create dictionary with country as keys and value as answers
    for country in countrylist:
       sum_cases, death_cases, daysgt_case, daysgt_death = getnums(country, 'location' ,data, headers) 
       dict_country[country] = [sum_cases, death_cases, daysgt_case, daysgt_death] 
    
    dict_continent = {} #continent as keys and value as answers
    for continent in continentlist:
        sum_cases, death_cases, daysgt_case, daysgt_death = getnums(continent, 'continent', data, headers)
        dict_continent[continent] = [sum_cases, death_cases, daysgt_case, daysgt_death]
    
    return dict_country, dict_continent

def getnums(specificname, category, data, headers):
    """Gets the specific lines of data for each specific country or continent,
    does required calculations and appends them into a dictionary"""
    L = {} #dictionary of lines within data
    D = {} #months dictionary containing L's lines of (cases, deaths)
  
    for line in data:
        if line[headers[category]].lower() == specificname: #if header (line[index]) is input get data
            date = line[headers["date"]].split('/')#find month inside date
            if len(date) != 3: 
                continue #don't include row if not in date/month/year format
            
            month = int(date[1])
            case = line[headers["new_cases"]]
            death = line[headers["new_deaths"]]
            
            if str(case).isnumeric() == False or case == '': 
                L["case"] = 0 #all non-numeric data or no data should be considered as 0
            else:
                L["case"] = int(case)         
            if str(death).isnumeric()== False or death == '': 
                L["death"] = 0
            else:
                L["death"] = int(death)
                
            D.setdefault(month, {"case": [], "death": []}) #dictionary keys=months
            for k,v in L.items():
                D[month].setdefault(k, []).append(v)
    
    days_dict = {} #have dictionary of days in each month
    for i in range(1,13):
        if i in [1,3,5,7,8,10,12]:
            days_dict.setdefault(i, 31)
        if i in [4,6,9,11]:
            days_dict.setdefault(i, 30)
        days_dict[2] = 29
       
    for i in range(1,13):
            if i not in D.keys(): #if month doesn't exist in dictionary make it 0
                D[i] = [0]
            else:
                sumcase = sum(D[i]["case"])
                sumdeath = sum(D[i]["death"])
                D.setdefault("sum_case", []).append(sumcase)
                D.setdefault("sum_death", []).append(sumdeath)
                
                if category == 'continent': #continents assume data exists for all days
                    for days in range(days_dict[i]-len(D[i]["case"])):
                        D[i]["case"].append(0)
                    for days in range(days_dict[i]-len(D[i]["death"])):
                        D[i]["death"].append(0) #add zeros for missing days
                
                avgcases =  sumcase/len(D[i]['case'])
                avgdeaths = sumdeath/len(D[i]['death'])
                
                greatercases = len([x for x in D[i]["case"] if x > avgcases]) #for each month, for each day
                greaterdeaths = len([i for i in D[i]["death"] if i > avgdeaths])
                D.setdefault("daysgt_case", []).append(greatercases)
                D.setdefault("daysgt_death", []).append(greaterdeaths)
    return D["sum_case"], D["sum_death"], D["daysgt_case"], D["daysgt_death"]#return only required lists

if __name__ == "__main__":
    dict_country,dict_continent = main('Trying.csv')
    requested = input("Enter a country or continent name:")
    if requested in dict_country.keys():
        print(dict_country[requested],"\n")
    elif requested in dict_continent.keys():
        print(dict_continent[requested])
    else:
        print("Country/Continent could not be found!\n Please choose a country from this list:\n", dict_country.keys(), "\nOr try a Continent from this list:\n", dict_continent.keys())
