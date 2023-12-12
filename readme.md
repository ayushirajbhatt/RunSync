# Project Overview

## Objective
This project focuses on harnessing biometric signals, including Heart Rate (HR), Heart Rate Variability (HRV), and Electrodermal Activity (EDA), captured through consumer-grade wearable technology like smartwatches and wristbands. Our goal is to use these non-invasive bio signals as inputs for an innovative music recommendation algorithm. This algorithm is specifically tailored for medium-distance runners, aiming to enhance their running experience and potentially boost their performance.

## Repository Structure

- **Apple_health_export_2.zip**
  - Includes the raw Apple Watch data utilized in the project.

- **Applewatch Data Extraction.ipynb**
  - **Primary File**: Begin your journey here. This notebook is the heart of our project, processing Apple Watch data and developing the music recommendation model.

- **Spotify_recommender.py**
  - **Integration Script**: Leverages Spotify's recommendation API to assemble the final playlist.

- **Bio_Sensory_Zone_Model_test_1.csv**
  - **Output File**: Contains the results from our recommendation model.

- **[Intermediate] Songs from CSV.ipynb**
  - **Utility Notebook**: Aids in constructing the playlist from the model's output.

- **Playlist.csv**
  - **Final Output**: The complete playlist curated by our algorithm.

- **Playlist_Cover.png**
  - **Resource File**: The cover image for the final playlist.

## Results
This BioSensory Computing project marks an essential first step towards a comprehensive bio-signal-based music recommendation system. Our deliverable is a Python notebook that adeptly processes biometric data from wearable devices to create customized playlists. This algorithm considers age, heart rate and target heart rate zones (using Karvonen’s formula), and running pace to enhance the running experience. Check out our [Sample Playlist](https://open.spotify.com/playlist/3AI3A2vA2FJ0zLmkQQpjqB) generated from real workout data.

## Model Design
Our model seamlessly integrates data extraction from Apple Health XML files with Spotify's streaming service to generate user-specific playlists. 

1. **Initialization**: Users input their age and Apple Health data. The model uses this to calculate maximum heart rate and heart rate zones via Karvonen's method.
2. **Data Aggregation**: We average heart rates over 3-minute intervals, aligning with the average song length.
3. **Heart Rate Zones**: The model assigns each interval to a heart rate zone, ranging from Zone 1 (50%-60% intensity) to Zone 5 (90%-100% intensity), to tailor the music tempo and style.
4. **Spotify Integration**: Parameters like valence, popularity, tempo, and genre are adjusted based on the heart rate zone to influence the user's heart rate indirectly.
5. **Playlist Generation**: Finally, the model creates a Spotify playlist, directly accessible to the user.

*See Figure 1 for the BioSync model flowchart and Figure 2 for a 10k run heart rate visualization.*

### Future Work
This version sets a foundation, with risk management strategies and an extensive feature list in our roadmap. Future enhancements will be guided by user feedback and further research, particularly in fine-tuning the Spotify API parameters for optimal playlist generation.
