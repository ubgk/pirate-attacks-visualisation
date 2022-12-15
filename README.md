# Global Maritime Pirate Attacks
This is a visualization of global maritime pirate attacks between 1993 and 2020 in the world's oceans.

The project was realized with `Plotly` and `Dash`.

Please find the visualisation deployed at [https://piracy.herokuapp.com](https://piracy.herokuapp.com)

## About
The app provides a simple and intuitive dashboard that allows users to visualize and interpret
 the data about global piracy attacks. It provides a valuable resource for users that wish
to understand patterns and trends in global maritime security.

## Local Deployments
### Running Locally
If you are given access, the pre-built app can be pulled from our private repository and run very easily locally with the following command:
```
$ docker run -p 8000:8000 ghcr.io/boragokbakan/pirate-attacks-visualisation:main 
```
For the permissions to pull the image, please contact me.

### Building Locally
In order to build the app locally, you will need a Mapbox token to access our custom map style. It can be obtained for 
free by registering at [https://studio.mapbox.com/](https://studio.mapbox.com/).

Once you have your token, you can build and run the app with the following steps:
```commandline
# Build the image and tag it as pirate-attacks-visualisation
$ docker build . -t pirate-attacks-visualisation 

# Run the app with your Mapbox token as an environment variable
$ docker run -p 8000:8000 -e MAPBOX_TOKEN={YOUR_TOKEN} pirate-attacks-visualisation
```

