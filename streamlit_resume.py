import streamlit as st

# Title of the app
st.title('Xia Jiun Lau\'s Resume')

# Contact Information
st.header('Contact Information')
st.write('Email: xiajiun21@gmail.com')
st.write('[LinkedIn Profile](https://linkedin.com/in/xiajiun)')

# Experience Section
st.header('Experience')

st.subheader('AI Researcher at GoQba Technology Corp. (Jun 2022 - Feb 2023)')
st.write('''
- Analyzed healthcare images with OpenCV
- Developed predictive models utilizing deep learning algorithms
- Successfully delivered two government-supported projects totaling 600 million won
- Published research findings at Rehabilitation Robotics & Medicine Conference 2022
- Published research paper at ICGHIT Conference 2023
''')

st.subheader('AI Research Engineer at nCyC (Jun 2021 - Feb 2023)')
st.write('''
- Experience in designing and developing machine learning models for government support projects related to AI.
- Experience in running AI projects using various knowledge and framework related to AI and computer science such as SQL data analysis, recommendation system, GANs, PyTorch, and so on.
- Participated in many AI projects from the planning stage with a limited resources
- Published and presented research paper at ICGHIT Conference 2022
''')

# Education Section
st.header('Education')
st.write('''
- Master's degree in Big Data Analysis, Ewha Womans University (2019 - 2020)
- Bachelor's degree in International/Global Studies, Ewha Womans University (2015 - 2018)
- Bachelor's degree in Business Administration and Management, General, Ewha Womans University (2015 - 2018)
- A-Levels, Taylor's College (2013 - 2014)
''')

# Skills Section
st.header('Skills')
st.write('Deep Convolutional Generative Adversarial Networks (DCGAN), Convolutional Neural Networks (CNN), Time Series Analysis, Django, ChatGPT, Generative AI, Quantum GIS, Recommender Systems, Scikit-Learn, Image Processing')

# Licenses & Certifications
st.header('Licenses & Certifications')
st.write('''
- TOPIK Level 6 - National Institute for International Education (Apr 2023 - May 2025)
- TOEIC 955/990
- Deep Learning Specialization - Coursera
- And others...
''')

# Honors & Awards
st.header('Honors & Awards')
st.write('''
- EGPP Full Scholarship, Ewha Womans University (2015, 2019)
- Global Ambassador Scholarship, LOTTE Mediheal Scholarship Foundation (Mar 2018)
''')


