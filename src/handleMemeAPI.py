import requests


async def handleMemeGenerator(m):
    await m.channel.send("Ahi te cuento uno")
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "6bf5d3c645mshcbedf0c5a7f993fp1ea143jsn7edcc9d21eb5"
        }
    response = requests.request("GET", url, headers=headers)
    
    await m.channel.send(response.url)
    
