# concentration-calculations

This is a project was done as a part of Master thesis. This soft calculates chemical reaction constants for a given chemical reactions, initial components concentrations,
experimental data (concentration vs time for each component), time period.

## installation

1. Download docker from [official resource](https://docs.docker.com/get-docker/)
2. Open command line in the root of the project and run `docker compose build`. This will build the images for a software components. Do it this action only once.
3. Run `docker compose up` from command line from the root folder.
4. Go to http://localhost:3050 and app should work now.

## run samples

1. Go to server\machineLearningModule\samples
2. This folder contains 3 sets of data. Each with a different purpose.From UI set configuration and experimantal values from `description.md` and `input.json` respectively.
3. Press "Calculate constants", after approximately 20 seconds app will return results to UI.
4. Compare results from the previous list item to the respective results in `description.md` under the "Example output" section. They should be almost the same.
  If that is true, the app works correctly.
  
  
For details refer to [Master thesis](https://drive.google.com/file/d/1OCu9oY4p88GcZwdZEF55ZjX6YaZYkVEp/view?usp=sharing) or contact me (ybatsiun@gmail.com).
