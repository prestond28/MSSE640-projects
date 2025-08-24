# Project 2 - Integration Testing

## Introduction

## Part 1 - APIs and Integration Testing with Postman

### HTTP Basics

HTTP stands for HyperText Transfer Protocol, and the name is pretty good at explaining what it is. HTTP is a protocol for transferring (sending or receiving) data across the internet. The sending and received of data using HTTP is stateless, meaning the transactions of sending and receive data are not remembered or stored anywhere after they have been completed. Normally, this transferring of data happens between clients and servers. A client is usually a web browser/application and a server is a computer or collection of computers that holds data. Clients request the data from the server, and the server sends a response which contains the requested data. When these requests happen, there are "headers" that are sent with the request that include info like what data is needed or any authorization that is needed in order to receive the data. A server usually sends a "body" as the response, which includes the actual data. The way I think about it is the headers have the info needed to access the data, and the body contains the data itself.

Another piece of info that comes with the response is a status code. This indicates the result of the request, whether it was successful or failed. There could be a few reasons the request failed, the most common ones being the resource (data) couldn't be found, authorization failed, or an internal server error occurred.

The four main types of HTTP request that can be sent to a server from a client are described with these four verbs:

- GET: Retrieve some data from the server
- POST: Send some new data to the server
- PUT: Update some existing data on the server
- DELETE: Remove some data from the server

These four types of request cover pretty much everything you would need to do, and it's best practice to only use these four types of requests.

### Role of APIs in Modern Applications

APIs are heavily used in modern applications. If you have a front-end web application, you pretty much use APIs to retrieve all your data. Imagine storing all the data you would ever need in one application, your application would be huge and probably not perform as well! With APIs, you can request only the data you need at that moment and have servers work asynchronously to store any data your application needs to save, making your application more efficient.

One application of a modern use of open APIs that I thought was interesting is weather apps! Turns out that most apps that display the weather are actually accessing an open API to get that weather data. Which makes total sense, because you wouldn't expect every business to start their own weather monitoring operation just to display the weather.

Source: https://nordicapis.com/5-examples-of-apis-we-use-in-our-everyday-lives/

### Cross-Origin Resource Sharing (CORS)

CORS (Cross-Origin Resource Sharing) is implemented as a security feature by web browsers. It controls who can access resources from one domain to another, and by default it is blocked. This is another level of security to ensure only the right people are accessing the requested resources. In order to get through CORS, the server would need to send specific HTTP headers with the response so that the web browser allows the response.

### 5 Public APIs You Can Get Data From

#### OpenWeatherMap API -> https://openweathermap.org/api

- You can get historical, current, and future weather forecast data for any location in the world.

#### The Cat API -> https://thecatapi.com/

- On the free version, you can get a bunch of random pictures of cats.

#### Random Useless Facts -> https://uselessfacts.jsph.pl/

- You can get the daily useless fact or a random useless fact.

#### Spotify Web API -> https://developer.spotify.com/documentation/web-api

- I actually used this API for my last class project, you can get a bunch of music data and even set up a music player.

#### Google Maps API -> https://developers.google.com/maps

- You can get a ton of information on maps and navigation.

## Part 2 - Postman Video Demonstration

![Postman Demo](./videos/postman_demo.mp4)

<video width="600" controls>
  <source src="./videos/postman_demo.mp4" type="video/mp4">
</video>


## Conclusion

I had a lot of fun setting up different API requests and getting them to actually work! It's amazing to see how much information is just public and readily available for you to use in your own applications. I didn't know about Postman's collections or environments, so I'm glad I was able to learn about that aspect of Postman, it's going to save me so much time in the future!

One recommendation I had for this assignment: I liked how some of the other assignments had you research and talk about things in part one that you then implemented in part two. While this assignment did that a little bit, I think it would be useful to talk more about postman in part 1 so that you feel more prepared to use it in part 2.

