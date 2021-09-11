#conexoes entre pontos
conexoes = {}

conexoes["Casa"] = {"Santo Amaro"}
conexoes["Santo Amaro"] = {"Casa", "Socorro"}
conexoes["Socorro"] = {"Santo Amaro", "Pinheiros"}

conexoes["Pinheiros"] = {"Socorro", "República", "Luz"}
conexoes["República"] = {"Pinheiros", "Barra Funda"}
conexoes["Luz"] = {"Pinheiros", "Sé"}

conexoes["Sé"] = {"Luz", "Barra Funda"}
conexoes["Barra Funda"] = {"República", "Sé", "Impacta"}
conexoes["Impacta"] = {"Barra Funda"}

#localização de todos os lugares 

localizacao = {}
localizacao["Casa"] = [3,20]
localizacao["Santo Amaro"] = [2,16]
localizacao["Socorro"] = [2,14]

localizacao["Pinheiros"] = [3,9]
localizacao["República"] = [4,6]

localizacao["Luz"] = [1,3]

localizacao["Sé"] = [1,1]
localizacao["Barra Funda"] = [4,1]
localizacao["Impacta"] = [6,1]