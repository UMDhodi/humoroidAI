import wolframalpha

app_id = "Wolframalpha api id"
client = wolframalpha.Client(app_id)
indx = query.lower().split().index('calculate')
query = query.split()[indx + 1:]
res = client.query(' '.join(query))
answer = next(res.results).text
print("The answer is " + answer)
speak("The answer is " + answer)    