import webscrapping

if __name__ == '__main__':

    currentTime = webscrapping.getCurrentTime()

    #TO TOWN

    busList = webscrapping.busWebScrape()

    
    #print("Current Time: " + currentTime + "\n\n" "(Vandyke North Bound Bus Stop) Next Bus Information:\nService: " + str(busList[0]) + "\nTime: " + str(busList[1]) + "\nArrival: "  + str(busList[2])  +  " Minutes" "\n" "\n(Vandyke South Bound Bus Stop) Next Bus Information:\nService: " + str(busList[3]) + "\nTime: " + str(busList[4]) + "\nArrival: "  + str(busList[5]) + " Minutes" "\n" "\n(Ullswater North Bound Bus Stop) Next Bus Information:\nService: " + str(busList[6]) + "\nTime: " + str(busList[7]) + "\nArrival: " + str(busList[8]) + " Minutes")

    #TO HOME
    busList = webscrapping.busHomeScrape()
    


    #print("Current Time: " + currentTime + "\n\n" "(Vandyke North Bound Bus Stop) Next Bus Information:\nService: " + str(busList[0]) + "\nTime: " + str(busList[1]) + "\nArrival: "  + str(busList[2])  +  " Minutes" "\n" "\n(Vandyke South Bound Bus Stop) Next Bus Information:\nService: " + str(busList[3]) + "\nTime: " + str(busList[4]) + "\nArrival: "  + str(busList[5]) + " Minutes" "\n" "\n(Ullswater North Bound Bus Stop) Next Bus Information:\nService: " + str(busList[6]) + "\nTime: " + str(busList[7]) + "\nArrival: " + str(busList[8]) + " Minutes")
