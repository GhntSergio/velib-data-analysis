import os
from setuptools import setup, find_packages

# Obtenir le chemin absolu du répertoire du script setup.py
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Définir le chemin relatif du README.md
README_PATH = os.path.join(BASE_DIR, "docs", "README.md")

# Lire le fichier README.md
with open(README_PATH, "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="velib_monitoring",  # Nom du package sur PyPI
    version="1.0.0",  # Version du package
    author="Serge Ganhounouto",
    author_email="serginhoganhounouto@gmail.com",
    description="Un package pour l'analyse des données Vélib en temps réel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GhntSergio/velib-data-analysis",
    packages=find_packages(include=["velib_data_analysis", "velib_data_analysis.*"]),
    install_requires=[
        "requests",
        "pandas",
        "matplotlib",
        "folium",
        "jupyter",
        "seaborn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "velib-monitor=velib_data_analysis.velib_monitoring:main"
        ]
    },
)
