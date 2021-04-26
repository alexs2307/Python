import random
def main():
    geo_dict = {"Slovenia": "Ljubljana", "France": "Paris",
                "Germany": "Berlin", "Croatia": "Zagreb", "Lithuania": "Vilnius", "Russia": "Moscow",
                "Bosnia and Herzegovina": "Sarajevo", "The United Kingdom": "London", "Ireland": "Dublin",
                "Spain": "Madrid", "Portugal": "Lisbon", "Ukraine": "Kiev", "Belarus": "Minsk", "Serbia": "Belgrade",
                "Kosovo": "Pristina", "Macedonia": "Skopje", }
    name = input("Enter your name\n")
    print(f"Hello {name.upper()} and welcome to the Geography Quiz")
    countries = list(geo_dict.keys())
    for i in range(10):
        country = random.choice(countries)
        capital = geo_dict[country]
        capital_guess = input(f"What is the capital of {country} : ")
        if capital_guess == capital:
            print("Correct!! Nice job")
        else:
            print(f"Incorrect. The capital of {country} is {capital}.")
    print("End of the game")
main()
