import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # le os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # cria um dataframe com o nome x com os dados da coluna year
    x = df['Year']
    # cria um dataframe com o nome y com os dados da coluna CSIRO Adjusted Sea
    y = df['CSIRO Adjusted Sea Level']
    #modelo vai ser igual ao resultado da regressão linear entre x e y
    model = linregress(x, y)
    #plot o scatter plot
    plt.scatter(x, y)

    #cria uma variavel com os years prev porque a gente vai querer prever os dados de 1880 a 2050, por isso o range tmb
    years_prev = pd.Series(range(1880, 2051))
    #plota no eixo x o years prev, e no eixo y a equação da reta (y = mx + b) eu tive que pesquisar essa qeuacao ai
    plt.plot(years_prev, model.slope * years_prev + model.intercept)

    #pra segunda linha tem que fazer um filtro pra pegar os anos a partir de 2000
    x_train = df['Year'][df['Year'] >= 2000]
    #eixo y tbm
    y_train = df['CSIRO Adjusted Sea Level'][df['Year'] >=2000]
    #a regressao linar do segundo grafico vai usar o novo modelo que vai ser treinado com outros dados
    model2= linregress(x_train, y_train)
    #cria o range de anos que a gente quer prever pra segunda linha
    years_prev2 = pd.Series(range(2000, 2051))
    #plota a segunda linha
    plt.plot(years_prev2, model2.slope * years_prev2 + model2.intercept)
    
    #plota os labels e o titulo
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt.gca()