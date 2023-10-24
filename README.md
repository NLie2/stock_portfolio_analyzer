# stock_portfolio_analyzer
This is an application that allows users to analyse their stock portfolio. It is a project I have already been working on for quite some time in a google colab, and now turned into a full-stack application with django for the backend and react for the frontend. 

## Deployment link 
https://stock-portfolio-analyzer-cc275ea5067c.herokuapp.com/analyze/1/

## 🚀 Getting started
To run the backend: 
```pipenv install```

```pipenv shell```

```python manage.py runserver``` Or ```python3 manage.py runserver```

To run the frontend 
```cd client```

```npm i```

```npm start```

## 🕜 Timeframe
I created this project completely by myself, and took 14 days for it. 

## 👩‍💻 Technologies Used
- Django
- EOD historical data API
- React
- Bootstrap, scss
- Papaparse
- Chartjs for react

## 🧯 Challenges
- A challenge was definitely setting up the create function for the tradetable. The reason is that a trade model and a tradetable model to be created simultaneously. At first I tried it with a nested serializer, but soon found out that it was not the right approach. I ended up solving it by simply sending two objects when the request is made, and then creating the tradetable based on these two separate objects.
- Another challenge was visualizing the table that is returned from the EOD response, as it required me to use nested loops in react.
- Another challenge was bundling all the endpoints of the app. There are still a few ‘loose ends’, i.e.: requests that can be technically sent to the backend but are not handled at all by the frontend. The reason of that is that I am still working on a few functionalities of the app.
- The biggest challenge by far was understanding the specifics of the data analyses that need to be performed to determine the portfolio networth correctly. This is still a work in progress. 

## 💪 Wins
- I am quite happy with how simple this app is. It contributes to the kind of app-design that I love, where the actual technologies are 'transparent', and the user does not have to think about the technology behind the content that is provided to them. Most apps similar to mine are a lot more complicated for the user. 
- I am very happy with how little data actually needs to be stored in my database even though the app itself is rather data-intensive.
- I am also happy about the fact that I made it possible for a user to have multiple portfolios. It would have been easier to give one user one portfolio but I think it is a better user experience in case someone wants to analyse and keep track of multiple portfolios. 

## 💡 Key takeaways
Planning is everything when you work on a project entirely by yourself. I created a trello board, which helped me keep track of whether I was on time or not. 
Also, when you are working alone deciding which features are part of your MVP is quite crucial. It is easy to get lost in less important features. 
I did not know before how to implement a file reader, and also had not visualised graphs before. Researching and evaluating libraries was quite a nice learning experience, and something that I always used to struggle with in the past. In the end, I was quite happy with the two libraries I ended up finding for both of these (paparse, and chart.js for react). 

## 🐛 Bugs
Currently, the portfolio worth is simply determined based on seeded files. I still need to add the right calculations to determine the portfolio worth. 

## 🔮 Future improvements
1. Finalizing the portfolio networth calculation
2. Making it possible for a user to determine the networth of the portfolio without the trading data being saved. This can be somewhat easily done by bypassing the create request that I am using currently. However, this requires me to learn a bit more of about the specifics of the Django. 

## Wireframes
I am posting these wirefrmaes at the end because they are quite long ;) 

### Excalidraw 
I normally prefer making wireframes with excalidraw but since this was a rather big project I ended  up making additional wireframes in Figma 

![WOQIYzUa-m7WSKLNxxKbm3quZyhHtZx5QAaN-6q9mpHA3Vj6vR8-g6pm4m55saArnDj_4F7pTUj0mjTv9407BVtak4OF2NdPirZQOwTSKUWy_1u3EoaMJDW5j2sL](https://github.com/NLie2/stock_portfolio_analyzer/assets/99728936/770cb3fe-8b09-4470-9be2-43d8b1d4ff31)


### Figma
![image](https://github.com/NLie2/stock_portfolio_analyzer/assets/99728936/3fea6357-4371-480a-a7f2-f10f9630f0c2)
![image](https://github.com/NLie2/stock_portfolio_analyzer/assets/99728936/cf8bf899-4557-41ad-a2ea-f9a1e42e4890)
![image](https://github.com/NLie2/stock_portfolio_analyzer/assets/99728936/c6c23a75-cae9-47ed-8b2a-b00e6f14a74c)



