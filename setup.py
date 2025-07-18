from setuptools import setup, find_packages

setup(
    name='Akhil7205/Clone-Chatgpt',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'groq-chatbot=app:main',
        ],
    },
)
