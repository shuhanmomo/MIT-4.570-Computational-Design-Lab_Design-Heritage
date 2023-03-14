## MIT-4.570-Computational Design Lab: Design Heritage
This is the repository where I will update my ongoing projects in the course MIT 4.570
  
# Image Segmentation -- Decoding the Scene Atmosphere in Movies
  
### Project Statement
This study aims to examine the question how the physical spaces and environments in movies impact the narrative and emotional content of the scenes. Using semantic 
segmentation techniques, the study analyzes the proportion of architectural and natural elements in film sets and categorize the scenes into four emotional 
categories: Sad, Happy, Romantic, and Calm. By creating segmentation diagrams and decoding the design elements of movie sets, this study explores the influence of 
architecture and natural elements on scene atmosphere and storytelling,and contribute to our understanding of the role of these elements inshaping our emotional 
experiences of film.
  
This can be particularly useful for film makers and set designers, who can use this information to create specific atmospheres and moods in their scenes, and for 
film studies researchers, who can use this information to understand the impact of architectural design on the emotional content of films.

### Workflow
**Webscraping**  
- 'Selenium_login.py' is for scraping down corresponding movie shots under each category from an online tool  
![scraped images](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/cd693d93ce010c18932c2a4cf1fb75f1c038d96e/img/webscraping.jpg)
  
**Image Segmentation**:  
- 'DPT_Segmentation.zip' contains all the inputs and pretrained DPT model, needs to be uploaded to the google drive and copy corresponding path  
   Github link to DPT model https://github.com/isl-org/DPT
- 'Tracy_segmentation.ipynb' is a copy of google collab file which fits the input images into DPT model and out put segmented results and CSV file
![segmentation](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/cd693d93ce010c18932c2a4cf1fb75f1c038d96e/img/segmented.png)
  
**Data Visualization**:  
- 'pie chart.py' 'histo.py''distribution.py' uses Matplotlib to visualize the exported CSV data
![analysis](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/cd693d93ce010c18932c2a4cf1fb75f1c038d96e/img/data%20analysis.jpg)  
    
  
  
# Pix2pix --  Generating Pedestrian Path Patterns in Boston's Urban Parks (INCOMPLETE) 
 
### Project Statement
In this project, I prepare paired plan diagrams as training examples, with one diagram labeling the surrounding building programs, urban fabric and park boundaries, and the other diagram highlighting the pedestrian pathway inside the park. The goal is to train the model to take an urban plan with indication of park boundaries and surrounding urban fabric as input, and output the possible pedestrian pathway inside the park.

The research hopes to explore the relationship between pedestrian paths and other contextual  features. Current training faces a overfitting problem due to small-size dataset and less clear input diagrams, which will be modified in the next-round exploration. In the future, it will also compare pedestrian path patterns across different cities and regions.


### Workflow
**Color-coded Diagram**  
- 'Pedestrian_path.zip' contains prepared input diagrams
![coded images](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/49da4fd53152097c955dcb8fa5fc4c245c461a9d/img/pix2pix.png)
  
**Pix2pix Training**:  
- 'Ass2_Tracy_pix2pix.ipynb' is a copy from google collab which trains the pix2pix model with prepared diagrams  
link to original Pix2pix model:https://www.tensorflow.org/tutorials/generative/pix2pix
![training process](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/49da4fd53152097c955dcb8fa5fc4c245c461a9d/img/pix2pix-training%20process.png)  
Training Process of the Model
![loss value](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/49da4fd53152097c955dcb8fa5fc4c245c461a9d/img/pix2pix%20-loss.png)
Record of Loss Values during the Process  
  
  
  
# Video Analysis --  Public Spaces Through the Lens of TikTok (INCOMPLETE) 
 
### Project Statement
The aim of this research is to investigate cross-cultural differences in human activity patterns in public spaces, specifically Boston Common Park in the United States, Kowloon Park in Hong Kong, and Luxembourg Gardens in France. Using TikTok videos as the primary data source, I will analyze human activity patterns in each location and compare them across the three sites.

The project is inspired by The Street Life Project, conducted by William Whyte in the 1970s, aiming to understand the social dynamics of public spaces in urban areas by observing and analyzing people's behavior. Whyte's project focused on physical observations and interactions with people in public spaces
![streetlifeproject](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/5c49d8b0b44d9daf47ae6807a4de4e3d3a527090/img/street%20life%20project.png)

My expectation is a better understanding of the role of social media in shaping our experiences and perceptions of public spaces. such as how people behave in these spaces when they know they might be filmed or how TikTok trends influence the types of activities people engage in. Tiktok is a user-generated content which provides a unique and diverse perspective on public spaces that may not be captured by traditional data sources, such as surveillance cameras or sensor networks.

I download 100 TikTok videos for each location and use the Moments in Time model to classify the types of human activities observed in the TikTok videos and compare the frequency of each activity across the three locations.

Currently,the model fails in predicting these behavior most of the time. I think there may be some reasons due to data quality: 1. Change of scene happens too frequently in most Tiktok videos 2. it's hard to set a uniform second interval to analyze all Tiktok videos 3. Tiktok filters and captions may interfere the analysis.  In the future, I will try other video analysis model such as Yolo4 to detect objects in scene or pose prediction model and train the Moments in Time model with my own input.



### Workflow
**Webscraping**  
- 'scraping tiktok.py' contains python script to scrape down Tiktok videos
  
**Moments in Time Training**:  
- 'Moments_In_Time.zip' contains pretrained model and needs to be uploaded to google drive and copy the path to the collab file  
link to the original Moments in Time model :http://moments.csail.mit.edu/
- 'moments_in_time.ipynb' is a google collab file where I fit the pretrained model with my input videos and output corresponding CSV file
![training result](https://github.com/shuhanmomo/MIT-4.570-Design-Heritage/blob/5c49d8b0b44d9daf47ae6807a4de4e3d3a527090/img/moments%20in%20time.png)
  




