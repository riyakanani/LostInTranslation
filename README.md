# LostInTranslation

<p><a href="https://malayaheflin.github.io/LostInTransWeb/">Project Website:</a>.</p>

<p><a href="https://riyakanani.github.io/Selected%20Works%20Pages/lost_in_translation.html">My Website</a>.</p>


<h2> Project Overview:</h2>  
A physical art installation where the player enters a "phonebooth" to try to help out a "bot" lost and in trouble on the other line. This is a play on the frustrating human experience of trying to receive help from corporate AI phone systems, where our exhibition now flips the roles between robot and human. We hope to relay the confusion that miscommunication can bring, particularly in the space of technology, but also relating to the experiences of immigrants from foreign countries. By utilizing speech recognition, language translation, and the words from previous participants, each experience is unique and different from the last, offering an evolving narrative that changes with every person who engages with the installation. The project emphasizes how communication can become distorted, showcasing both the limitations of AI and the human struggle to connect across languages and systems.

<h2> My Contributions:</h2>  
In this project, I had contributions in many different areas. I worked a lot on assembling the physical installation, making purchasing and design choices. I made some contributions to creating the map in the physical installation. Our team worked on the storyline together throughout the development process. However, my main role was the tech lead, creating interactive audio-based scripts. The focus was on providing spoken instructions and processing user responses through speech recognition, text-to-speech conversion, and translation. Below is an outline of the key areas I worked on:

<h3> Speech-to-Text Integration:</h3>  
I integrated the speech_recognition library to allow the system to capture spoken input from the user in real-time. This enabled users to interact with the system by simply speaking, without requiring manual input.
Implemented a function speechToText() to handle voice input and convert it into text for processing.

<h3>Interactive Dialogue System:</h3>
I enhanced the interaction flow by adding dynamic user prompts and responses, which are controlled based on speech input. This creates a more natural conversation, where the system asks for confirmations and guides the user step by step.
I implemented an iterative process where the system asks the user for directions, confirms responses, and handles the transitions between various locations. The system is designed to adapt to user input, which is essential for real-time navigation guidance.

<h3>Text Translation:</h3>
I incorporated the googletrans library, developing the textTranslated function. This function translates parts of the user’s speech into random languages, creating a more diverse interaction.

<h3>Text-to-Speech (TTS) Implementation:</h3>
For output, I implemented a textToSpeech function using the gTTS library, which converts text into spoken words. This feature allowed the system to provide verbal feedback to users and facilitate interaction.

<h3>Error Handling and Robustness:</h3>
I built error-handling mechanisms to deal with speech recognition failures or incorrect responses. For example, if the system could not hear the user properly or if the input was unclear, it would play a prompt asking the user to repeat themselves. Furthermore, I implemented various fallback responses (e.g., "I'm having trouble. I'm just going to go up and left to Willow Creek Avenue") to handle scenarios where the system could not understand the user's direction.

<h3>Location-based Navigation Logic:</h3>
I developed the logic for location-based navigation, where the system tracks the user’s current location (e.g., "Serenity Circle") and provides specific instructions on how to reach the next location (e.g., "Tranquility Lane"). The directions are generated dynamically based on the user’s speech input, allowing the system to guide the user through multiple possible routes.

<h3>Optimization and Memory Management:</h3>
I implemented memory management techniques such as the gc.collect() function to optimize the system's memory usage, ensuring that the program runs smoothly over extended periods without performance degradation.
I also optimized the flow by handling multiple iterations of speech recognition and responses without overloading system resources.

