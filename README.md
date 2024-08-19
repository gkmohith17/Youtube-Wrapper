Introduction

The yt_wrapper package is a Python library that encapsulates the YouTube Data API and the YouTube Transcript API, providing a seamless interface for developers to retrieve video details, search for videos, list channel videos, and fetch video transcripts. This package is designed to simplify interactions with YouTube's data and transcript services, making it easier for developers to integrate YouTube content into their applications.



Installation

Prerequisites

Python Version: Python 3.6 or higher

YouTube Data API Key: You need to obtain an API key from the Google Developers Console.

Installation via Pip

To install the yt_wrapper package, run the following command in your terminal:

bash - Copy code

pip install yt_wrapper


Usage
1. Importing the Package

python

Copy code

from yt_wrapper import YouTubeAPIWrapper

2. Initializing the API Wrapper

Before using any functions, you need to initialize the YouTubeAPIWrapper class with your API key.

python
Copy code

api_key = 'YOUR_YOUTUBE_DATA_API_KEY'

yt = YouTubeAPIWrapper(api_key)



3. Retrieving Video Details
You can retrieve video details such as title, description, view count, and like count using the get_video_info_and_transcript method.

python - Copy code

video_info = yt.
get_video_info_and_transcript('VIDEO_ID')

print(video_info['video_details'])



4. Searching for Videos
Search for videos based on keywords using the search_videos method.

python

Copy code

search_results = yt.data_api.search_videos('Python Programming')
for video in search_results:
    print(video['snippet']['title'])


5. Listing Videos in a Channel

List all videos in a specific channel using the list_channel_videos method.

python

Copy code

channel_videos = yt.data_api.list_channel_videos('CHANNEL_ID')
for video in channel_videos:
    print(video['snippet']['title'])


6. Fetching Transcripts

Fetch the transcript for a given video in the specified language using the get_transcript method.

python

Copy code

transcript = yt.transcript_api.get_transcript('VIDEO_ID', languages=['en'])
print(transcript)


7. Fetching and Translating Transcripts
Fetch the transcript and translate it into another language.

python

Copy code

translated_transcript = yt.transcript_api.get_transcript_with_translation('VIDEO_ID', target_language='es')
print(translated_transcript)

Advanced Usage
Combining Video Details and Transcripts
The get_video_info_and_transcript method allows you to fetch both video details and its transcript in a single call.

python

Copy code

info_and_transcript = yt.get_video_info_and_transcript('VIDEO_ID')
print(info_and_transcript['video_details'])
print(info_and_transcript['transcript'])


Handling Errors

The package includes error handling for cases where transcripts are unavailable or when API limits are reached. Make sure to implement appropriate error handling in your application.


python

Copy code

try:
    transcript = yt.transcript_api.get_transcript('VIDEO_ID')
except Exception as e:
    print(f"An error occurred: {e}")


Testing

Running Unit Tests
Unit tests for the yt_wrapper package are included in the tests directory. The tests are written using the pytest framework.


Steps to Run Tests:

Navigate to the project directory:


bash

Copy code

cd /path/to/your/project

Install pytest:


bash

Copy code

pip install pytest

Run the tests:


bash

Copy code

pytest tests/

This will run all the test files in the tests directory.



Contribution Guide
We welcome contributions to the yt_wrapper package. If you'd like to contribute, please follow the guidelines below.


Steps to Contribute:

Fork the Repository:

Fork the repository to your GitHub account by clicking on the "Fork" button.

Clone Your Fork:

Clone your forked repository to your local machine.

bash

Copy code

git clone https://github.com/gkmohith17/Youtube-Wrapper.git

cd Youtube-Wrapper

Create a New Branch:

Create a new branch for your changes.


bash

Copy code

git checkout -b my-feature-branch

Make Your Changes:

Make the necessary changes in the code or documentation.

Commit Your Changes:

Commit your changes with a clear and concise commit message.

bash

Copy code

git commit -m "Description of the feature or fix"

Push to Your Fork:

Push your changes to your forked repository.

bash

Copy code

git push origin my-feature-branch

Create a Pull Request:


Go to the original repository and create a pull request from your forked branch. Provide a description of the changes you've made.

Contribution Guidelines:

Code Quality: Ensure that your code follows PEP 8 guidelines.

Testing: Write tests for any new features or bug fixes.

Documentation: Update the documentation to reflect any changes made.


License
This project is licensed under the MIT License - see the LICENSE file for details.


Acknowledgments
Special thanks to the Google API Python Client and YouTube Transcript API developers for providing the tools that made this package possible.
