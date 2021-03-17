def ExtractDataFromFile():

    movie_numbers = []
    movie_titles = []
    movie_distributors = []
    box_office = []
    movie_ratings = []

    FileHandler = open("moviesData.txt", "r")
    MovieData = FileHandler.readlines()
    FileHandler.close()

    for line in MovieData:
         line.split("#")
         movie_numbers.append(line[0])
         movie_titles.append(line[1])
         movie_distributors.append(line[2])
         box_office.append(line[3])
         movie_ratings.append(line[4])

    for amount in box_office:
        amount = int(amount)

    return movie_numbers, movie_titles, movie_distributors, box_office, movie_ratings

def MoviesAbove200(movie_names, box_office_sales):

    movies_above_200 = []
    for item in box_office:
        if item > 200:
            index = box_office.index(item)
    movies_above_200.append(movie_names[index])

    return movies_above_200

def RestrictedMovies(distributors, ratings_list):

    restricted_distributors = []
    for rating in ratings_list:
        if rating == "R":
            index = ratings_list.index(rating)
    restricted_movie_distributor = distributor[index]
    restricted_distributors.append(restricted_movie_distributor)

    return restricted_distributors    


def DistributorTotalSales(distributors, box_office_sales, distributor_name):
    total_sales = 0
    for item in distributors:
        if item == distributor_name:
            index = distributors.index(item)
            total_sales += box_office_sales[index]
   
    return total_sales

def main():
   
  ExtractDataFromFile()
  MoviesAbove200(movie_titles, box_office)
  RestrictedMovies(movie_distributors, movie_ratings)
  DistributorTotalSales(movie_distributors, box_office, "Disney")

main()   
