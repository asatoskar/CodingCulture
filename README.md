# Coding Culture Hackathon
Project for coding culture hackathon.

## Trained Model Can Be Found At 

[google drive link](https://drive.google.com/open?id=18tzYWgoUXRSqt-iWVJfb4LhT_Xy6VPoz)


## Guide to Set Up And Use KHOJ

**Setting up repository**

Clone the entire repository (the *webapp* subfolder is not currently required and will be used for future front-end development after Hackathon results are out)

Create an *uploads* folder in the repository for the uploaded images.

Create a *model* subfolder in the repository and download the model from the Google Drive link and save it in this folder.

**Setting up Neo4J Server**

Download the Neo4J Community Edition tarball from the official Neo4j Website and extract it to any directory.

Navigate to the extracted folder and run the following command.

`./bin/neo4j console`

This will start the Neo4j Server

Navigate to the Neo4J browser at *http://localhost:7474/browser/* and change the passsword from default 'neo4j' to 'password'.

**Running the application**

Open a new terminal window and run the codingculture.py file using

`python3 codingculture.py`

CTRL+Click on the link in the terminal. Alternatively navigate to *http://127.0.0.1:5000/* to view the application in the Browser.

## Datasets

[Harvard Art Museum](https://www.harvardartmuseums.org/) - API key will be emailed to all.

[WikiArt](https://www.wikiart.org/) [WikiArt data retriever](https://github.com/lucasdavid/wikiart)

## Useful Links

[Artistic Style Transfer - Excellent Neural Network Explanation](https://harishnarayanan.org/writing/artistic-style-transfer/)

[pHash](https://www.phash.org/)

[DeepLearn.js](https://deeplearnjs.org/demos/mnist/mnist.html)

[Neo4j for Python Web App With Flask](https://neo4j.com/blog/building-python-web-application-using-flask-neo4j/)

[How Modification of Original Script Was Done](https://towardsdatascience.com/multi-label-image-classification-with-inception-net-cbb2ee538e30)

[Flask and Python tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
