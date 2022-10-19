# Follow the instructions in the tab to the right
# Write your mad libs program here

# friend citation 
yourName= input("Please enter your name: ")
friendName= input ("Please enter your friend's name: ")
adjective1= input("please enter an adjective: ")
adjective2= input("please enter an adjective: ")
height= input("please enter a float between 5-6.5: ")
weight= input("please enter a weight between 40-100: ")
appearance= input("Enter an apperance e.g ugly, fine etc: ")
status= input("Enter any financial status: ")
school= input("Enter a school name: ")
country= input("Enter a country name: ")
company= input("Enter a company name: ")
role= input("Enter a job title: ")
motivational_quote= input("Enter your favorite motivational quote: ")
marital_staus= input("Enter a marital status: ")
kids= input("Enter a number: ")



about= f"{yourName} has a friend named {friendName}. {friendName} happens to be {adjective1} and {adjective2}. {friendName} has so many awards for being {adjective1}."
qualities= f"{friendName} is about {height}ft tall, with a weight of about {weight}kg. {friendName} is {appearance} and as well {status}."
academics= f"{friendName} recently graduated from {school} after bagging a first class degree honour."
milestone= f"{friendName} currently lives in {country} and works with {company} as the {role}."
favorite_quote= f"In the face of adversity {friendName} says {motivational_quote}."
marraige=f"{friendName} is {marital_staus} with {kids} children."


print(about + qualities + academics + milestone + favorite_quote + marraige)
